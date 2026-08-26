"use client";

interface StepIndicatorProps {
  current: number;
  total: number;
}

export default function StepIndicator({
  current,
  total,
}: StepIndicatorProps) {

  return (

    <div className="flex justify-center gap-3 mb-8">

      {Array.from({ length: total }).map((_, index) => (

        <div
          key={index}
          className={`h-3 w-3 rounded-full transition-all
          ${
            index + 1 <= current
              ? "bg-cyan-500"
              : "bg-zinc-700"
          }`}
        />

      ))}

    </div>

  );
}