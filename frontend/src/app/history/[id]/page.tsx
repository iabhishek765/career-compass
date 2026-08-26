"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useParams } from "next/navigation";

import { getHistoryReport } from "../../../services/historyService";
import type { HistoryReportDetail } from "../../../types/history";

export default function HistoryReportPage() {
  const params = useParams();

  const reportId = Number(params.id);

  const [report, setReport] = useState<HistoryReportDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!reportId || Number.isNaN(reportId)) {
      setError("Invalid report ID.");
      setLoading(false);
      return;
    }

    loadReport(reportId);
  }, [reportId]);

  async function loadReport(id: number) {
    try {
      setLoading(true);
      setError(null);

      const data = await getHistoryReport(id);

      setReport(data);
    } catch (err) {
      console.error("Failed to load report:", err);

      setError(
        err instanceof Error
          ? err.message
          : "Failed to load the report."
      );
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-background px-6 py-12">
        <div className="mx-auto max-w-5xl">
          <p className="text-muted-foreground">
            Loading assessment report...
          </p>
        </div>
      </main>
    );
  }

  if (error || !report) {
    return (
      <main className="min-h-screen bg-background px-6 py-12">
        <div className="mx-auto max-w-5xl">
          <Link
            href="/history"
            className="text-sm text-muted-foreground hover:underline"
          >
            ← Back to History
          </Link>

          <div className="mt-8 rounded-2xl border p-8">
            <h1 className="text-2xl font-bold">
              Report Not Found
            </h1>

            <p className="mt-2 text-muted-foreground">
              {error || "The requested assessment could not be found."}
            </p>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-background px-6 py-12">
      <div className="mx-auto max-w-5xl">

        {/* Header */}
        <div className="mb-8">
          <Link
            href="/history"
            className="text-sm text-muted-foreground hover:underline"
          >
            ← Back to History
          </Link>

          <div className="mt-6">
            <p className="text-sm text-muted-foreground">
              Assessment #{report.id}
            </p>

            <h1 className="mt-1 text-4xl font-bold">
              Career Assessment Report
            </h1>

            <p className="mt-2 text-muted-foreground">
              {new Date(report.created_at).toLocaleString()}
            </p>
          </div>
        </div>

        {/* Prediction */}
        <section className="rounded-2xl border p-6">
          <p className="text-sm text-muted-foreground">
            PLACEMENT PREDICTION
          </p>

          <div className="mt-2 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div>
              <h2 className="text-3xl font-bold">
                {report.prediction}
              </h2>
            </div>

            <div>
              <p className="text-sm text-muted-foreground">
                Model Confidence
              </p>

              <p className="text-3xl font-bold">
                {Number(report.confidence).toFixed(2)}%
              </p>
            </div>
          </div>
        </section>

        {/* Career Report */}
        <section className="mt-6 rounded-2xl border p-6">
          <p className="text-sm text-muted-foreground">
            AI CAREER INSIGHTS
          </p>

          <h2 className="mt-1 text-2xl font-semibold">
            Personalized Career Report
          </h2>

          <p className="mt-5 leading-7 text-muted-foreground">
            {report.career_report}
          </p>
        </section>

        {/* Career Path */}
        <section className="mt-6 rounded-2xl border p-6">
          <p className="text-sm text-muted-foreground">
            CAREER PROGRESSION
          </p>

          <h2 className="mt-1 text-2xl font-semibold">
            Recommended Career Path
          </h2>

          <div className="mt-5 space-y-3">
            {report.career_path.map((stage, index) => (
              <div
                key={index}
                className="rounded-xl border p-4"
              >
                <p className="text-xs text-muted-foreground">
                  Stage {index + 1}
                </p>

                <p className="mt-1 font-medium">
                  {stage}
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* Recommendations */}
        <section className="mt-6 grid gap-6 md:grid-cols-2">

          {/* Courses */}
          <div className="rounded-2xl border p-6">
            <h2 className="text-xl font-semibold">
              Recommended Courses
            </h2>

            <ul className="mt-4 space-y-3">
              {report.recommended_courses.map(
                (course, index) => (
                  <li
                    key={index}
                    className="rounded-lg border p-3 text-sm"
                  >
                    {course}
                  </li>
                )
              )}
            </ul>
          </div>

          {/* Projects */}
          <div className="rounded-2xl border p-6">
            <h2 className="text-xl font-semibold">
              Recommended Projects
            </h2>

            <ul className="mt-4 space-y-3">
              {report.recommended_projects.map(
                (project, index) => (
                  <li
                    key={index}
                    className="rounded-lg border p-3 text-sm"
                  >
                    {project}
                  </li>
                )
              )}
            </ul>
          </div>

          {/* Certifications */}
          <div className="rounded-2xl border p-6">
            <h2 className="text-xl font-semibold">
              Recommended Certifications
            </h2>

            <ul className="mt-4 space-y-3">
              {report.recommended_certifications.map(
                (certification, index) => (
                  <li
                    key={index}
                    className="rounded-lg border p-3 text-sm"
                  >
                    {certification}
                  </li>
                )
              )}
            </ul>
          </div>

          {/* Skills */}
          <div className="rounded-2xl border p-6">
            <h2 className="text-xl font-semibold">
              Skills to Improve
            </h2>

            <ul className="mt-4 space-y-3">
              {report.skills_to_improve.map(
                (skill, index) => (
                  <li
                    key={index}
                    className="rounded-lg border p-3 text-sm"
                  >
                    {skill}
                  </li>
                )
              )}
            </ul>
          </div>
        </section>

        {/* Bottom navigation */}
        <div className="mt-8">
          <Link
            href="/history"
            className="inline-flex rounded-lg border px-5 py-2.5 text-sm font-medium hover:bg-muted"
          >
            ← Back to Assessment History
          </Link>
        </div>
      </div>
    </main>
  );
}