"use client";

interface ProgressBarProps {
  current: number;
  total: number;
}

export default function ProgressBar({
  current,
  total,
}: ProgressBarProps) {

  const percentage = (current / total) * 100;

  return (
    <div className="mb-8">

      <div className="flex justify-between mb-2 text-sm">

        <span>
          Page {current} of {total}
        </span>

        <span>
          {Math.round(percentage)}%
        </span>

      </div>

      <div className="h-2 rounded-full bg-zinc-800">

        <div
          className="h-2 rounded-full bg-cyan-500 transition-all duration-300"
          style={{
            width: `${percentage}%`,
          }}
        />

      </div>

    </div>
  );
}