"use client";

import PredictionCard from "./components/PredictionCard";
import CareerReportCard from "./components/CareerReportCard";
import CareerPathCard from "./components/CareerPathCard";
import RecommendationCard from "./components/RecommendationCard";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

interface Recommendations {
  career_path: string[];
  missing_skills: string[];
  recommended_certifications: string[];
  recommended_courses: string[];
  recommended_projects: string[];
}

interface CareerCompassResult {
  prediction: string;
  probability: number;
  recommendations: Recommendations;
  report: string;
}

export default function ResultsPage() {
  const router = useRouter();

  const [result, setResult] = useState<CareerCompassResult | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    try {
      const storedResult = sessionStorage.getItem("careerCompassResult");

      if (!storedResult) {
        setLoading(false);
        return;
      }

      const parsedResult: CareerCompassResult = JSON.parse(storedResult);

      setResult(parsedResult);
    } catch (error) {
      console.error("Failed to load assessment result:", error);
    } finally {
      setLoading(false);
    }
  }, []);

  if (loading) {
    return (
      <main className="min-h-screen flex items-center justify-center">
        <p>Loading your career analysis...</p>
      </main>
    );
  }

  if (!result) {
    return (
      <main className="min-h-screen flex flex-col items-center justify-center gap-4">
        <h1 className="text-2xl font-bold">
          No assessment result found
        </h1>

        <p>
          Complete the career assessment first to generate your result.
        </p>

        <button
          onClick={() => router.push("/assessment")}
          className="border px-5 py-2 rounded-lg"
        >
          Take Assessment
        </button>
      </main>
    );
  }

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-5xl mx-auto space-y-8">

        <div>
          <p className="text-sm uppercase tracking-wider">
            Career Compass
          </p>

          <h1 className="text-4xl font-bold mt-2">
            Your Career Analysis
          </h1>

          <p className="mt-2">
            Personalized insights based on your assessment.
          </p>
        </div>

        <PredictionCard
          prediction={result.prediction}
          probability={result.probability}
        />

        <CareerReportCard report={result.report} />

        <CareerPathCard
          careerPath={result.recommendations.career_path}
        />

        <RecommendationCard
          title="Recommended Courses"
          items={result.recommendations.recommended_courses}
        />

        <RecommendationCard
          title="Recommended Projects"
          items={result.recommendations.recommended_projects}
        />

        <RecommendationCard
          title="Recommended Certifications"
          items={result.recommendations.recommended_certifications}
        />

        {result.recommendations.missing_skills.length > 0 ? (
          <RecommendationCard
            title="Skills to Improve"
            items={result.recommendations.missing_skills}
          />
        ) : (
          <section className="border rounded-xl p-6">
            <h2 className="text-xl font-semibold">
              Skills to Improve
            </h2>

            <p className="mt-4">
              No major skill gaps identified from your current profile.
            </p>
          </section>
        )}

        <div className="flex gap-4">
          <button
            onClick={() => router.push("/assessment")}
            className="border px-5 py-2 rounded-lg"
          >
            Retake Assessment
          </button>

          <button
  onClick={() => router.push("/history")}
  className="border px-5 py-2 rounded-lg"
>
  Result history
</button>

          <button
            onClick={() => router.push("/")}
            className="border px-5 py-2 rounded-lg"
          >
            Back to Home
          </button>
        </div>

      </div>
    </main>
  );
}