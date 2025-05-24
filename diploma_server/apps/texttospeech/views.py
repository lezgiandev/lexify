from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from transformers import AutoTokenizer, VitsModel
import torch
from scipy.io import wavfile
import io
from gradio_client import Client
import os
import shutil
import tempfile

LANGUAGE_MODEL_MAPPING = {
    'che': 'facebook/mms-tts-che',  # Чеченский
    'ava': 'facebook/mms-tts-ava',  # Аварский
    'tat': 'facebook/mms-tts-tat',  # Татарский
    'bak': 'facebook/mms-tts-bak',  # Башкирский
    'chv': 'facebook/mms-tts-chv',  # Чувашский
    'sah': 'facebook/mms-tts-sah',  # Якутский
    'oss': 'facebook/mms-tts-oss',  # Осетинский
    'lek': 'gradio_client'  # Лезгинский
}

loaded_models = {}


class GenerateAudioView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Генерация аудио из текста на языке пользователя",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['text'],
            properties={
                'text': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Текст для синтеза речи",
                    example="Салам! Мени язум Марут язум"
                )
            }
        ),
        responses={
            200: openapi.Response(
                description="Аудио файл в формате WAV",
                content={'audio/wav': {}}
            ),
            400: openapi.Response(
                description="Некорректный запрос",
                examples={
                    "application/json": {
                        "error": "Text is required"
                    }
                }
            ),
            401: openapi.Response(
                description="Не авторизован"
            )
        }
    )
    def post(self, request):
        """
        Генерирует аудио из текста на языке, указанном в профиле пользователя.
        Поддерживаемые языки: чеченский, аварский, татарский, башкирский,
        чувашский, якутский, осетинский, лезгинский.
        """
        text = request.data.get('text')
        user = request.user

        if not text:
            return HttpResponseBadRequest("Text is required")

        if not user.language:
            return HttpResponseBadRequest("User language is not set")

        language_code = user.language.code.lower()

        if language_code not in LANGUAGE_MODEL_MAPPING:
            return HttpResponseBadRequest(f"Language {language_code} is not supported")

        try:
            if language_code == 'lek':
                return self._handle_lezgin(text)
            return self._handle_other_languages(text, language_code)
        except Exception as e:
            return HttpResponseBadRequest(f"Processing Error: {str(e)}")

    def _handle_lezgin(self, text):
        """Обработка лезгинского языка через Gradio"""
        try:
            client = Client("https://leks-forever-lez-tts.hf.space/")
            with tempfile.TemporaryDirectory() as temp_dir:
                result_path = client.predict(text, 1, 0, True, fn_index=0)
                temp_file = os.path.join(temp_dir, "temp_audio.wav")
                shutil.copy(result_path, temp_file)
                with open(temp_file, 'rb') as f:
                    audio_data = f.read()
            response = HttpResponse(audio_data, content_type='audio/wav')
            response['Content-Disposition'] = 'attachment; filename="tts_lez.wav"'
            return response
        except Exception as e:
            return HttpResponseBadRequest(f"Gradio Error: {str(e)}")

    def _handle_other_languages(self, text, language_code):
        """Обработка других языков через локальные модели"""
        if language_code not in loaded_models:
            model_name = LANGUAGE_MODEL_MAPPING[language_code]
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = VitsModel.from_pretrained(model_name)
            loaded_models[language_code] = (tokenizer, model)

        tokenizer, model = loaded_models[language_code]
        inputs = tokenizer(text, return_tensors="pt")

        with torch.no_grad():
            audio = model(**inputs).waveform.squeeze().cpu().numpy()

        buffer = io.BytesIO()
        wavfile.write(buffer, model.config.sampling_rate, audio)
        buffer.seek(0)

        return HttpResponse(buffer.read(), content_type='audio/wav')