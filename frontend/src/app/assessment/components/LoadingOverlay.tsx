"use client";

import { useEffect, useState } from "react";

const messages = [
  "Analyzing your academic profile...",
  "Evaluating technical skills...",
  "Running placement prediction model...",
  "Generating AI career insights...",
  "Preparing personalized recommendations..."
];

export default function LoadingOverlay() {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prev) =>
        prev < messages.length - 1 ? prev + 1 : prev
      );
    }, 1800);

    return () => clearInterval(timer);
  }, []);

  return (
    <div className="fixed inset-0 z-50 bg-[#050816] flex flex-col items-center justify-center">

      <div className="w-20 h-20 rounded-full border-4 border-cyan-500 border-t-transparent animate-spin mb-10"></div>

      <h2 className="text-3xl font-bold text-white">
        Processing Your Career Report
      </h2>

      <p className="text-cyan-400 mt-6 text-lg">
        {messages[index]}
      </p>

      <p className="mt-10 text-gray-400">
        Please wait...
      </p>

    </div>
  );
}