export interface DictionaryCategory {
  id: number;
  name: string;
}

export interface PartOfSpeech {
  id: number;
  name: string;
}

export interface Word {
  id: number;
  text: string;
  category: DictionaryCategory;
  part_of_speech: PartOfSpeech;
}

export interface Translation {
  id: number;
  text: string;
  audio: string;
  language: string;
  word: Word;
}

export interface Language {
  id: number;
  name: string;
  code: string;
  flag: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  password: string;
  language: Language;
}

export interface FavoriteWord {
  id: number;
  user: User;
  translation: Translation;
}

export interface DictionaryResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Translation[];
}

export interface Book {
  id: number;
  title: string;
  author: string;
  language: Language;
  logo: string;
}

export interface BookResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Book[];
}

export interface Sentence {
  id: number;
  text: string;
  audio: string;
  translate: string;
  book: Book;
}

export interface CompletedBook {
  id: number;
  user: User;
  book: Book;
}

export interface Letter {
  id: number;
  letter: string;
  audio: string;
  language: Language;
}

export interface SourceCategory {
  id: number;
  name: string;
}

export interface Source {
  id: number;
  text: string;
  link: string;
  category: SourceCategory;
  language: Language;
}

export interface SourceResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Source[];
}

export interface MarkedSource {
  id: number;
  user: User;
  source: Source;
}
