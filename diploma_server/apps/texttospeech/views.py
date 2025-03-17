from django.http import HttpResponse, HttpResponseBadRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from transformers import AutoTokenizer, VitsModel
import torch
from scipy.io import wavfile
import io

LANGUAGE_MODEL_MAPPING = {
    'che': 'facebook/mms-tts-che', # Чеченский
    'ava': 'facebook/mms-tts-ava', # Аварский
    'tat': 'facebook/mms-tts-tat', # Татарский
    'bak': 'facebook/mms-tts-bak', # Башкирский
    'chv': 'facebook/mms-tts-chv', # Чувашский
    'sah': 'facebook/mms-tts-sah', # Якутский
    'kum': 'facebook/mms-tts-kum', # Кумыкский
    'dar': 'facebook/mms-tts-dar', # Даргинский
    'krc': 'facebook/mms-tts-krc', # Карачаево-Балкарский
    'nog': 'facebook/mms-tts-nog', # Ногайский
    'oss': 'facebook/mms-tts-oss', # Осетинский
    'udm': 'facebook/mms-tts-udm', # Удмуртский
    'myv': 'facebook/mms-tts-myv', # Эрзянский
    'kpv': 'facebook/mms-tts-kpv', # Коми-Зыранский
    'tkr': 'facebook/mms-tts-tkr', # Цахурский
    'agx': 'facebook/mms-tts-agx', # Агульский
    'xal': 'facebook/mms-tts-xal', # Калмыцкий
}

loaded_models = {}


class GenerateAudioView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
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

            response = HttpResponse(buffer.read(), content_type='audio/wav')
            response['Content-Disposition'] = f'attachment; filename="tts_{language_code}.wav"'
            return response

        except Exception as e:
            return HttpResponseBadRequest(f"Error: {str(e)}")