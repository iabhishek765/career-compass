"use client";


import { Question } from "../types";


interface QuestionCardProps {
    question: Question;
    value?: string | number;
    onChange: (value: string | number) => void;
}


export default function QuestionCard({
    question,
    value,
    onChange,
}: QuestionCardProps) {

  return (
  <div className="rounded-xl border border-zinc-800 p-8">

    <h2 className="text-2xl font-semibold mb-6">
      {question.question}
    </h2>

    {/* SELECT / RADIO QUESTIONS */}
    {(question.type === "select" || question.type === "radio") && (
      <div className="space-y-3">
        {question.options?.map((option) => (
          <button
            key={option}
            type="button"
            onClick={() => onChange(option)}
            className={`w-full rounded-lg border p-4 text-left transition ${
              value === option
                ? "border-cyan-500 bg-cyan-500/20"
                : "border-zinc-700 hover:border-cyan-500"
            }`}
          >
            {option}
          </button>
        ))}
      </div>
    )}

    {/* NUMBER QUESTIONS */}
    {question.type === "number" && (
  <input
    type="number"
    value={value ?? ""}
    min={question.min}
    max={question.max}
    step={question.step}
    onChange={(e) => {
      const rawValue = e.target.value;

      if (rawValue === "") {
        onChange("");
        return;
      }

      onChange(rawValue);
    }}
    placeholder={question.placeholder ?? "Enter your answer"}
    className="mt-4 w-full rounded-lg border border-zinc-700 bg-transparent p-4 outline-none focus:border-cyan-500"
  />
)}
  </div>
);
}