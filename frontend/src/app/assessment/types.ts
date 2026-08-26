export type QuestionType =
  | "select"
  | "radio"
  | "number";

export interface Question {
  id: number;

  field: string;

  question: string;

  type: QuestionType;

  section: number;
  required?: boolean;

  options?: string[];

  min?: number;

  max?: number;

  step?: number;

  placeholder?: string;
  
}

export type Answers = Record<
  string,
  string | number | undefined
>;