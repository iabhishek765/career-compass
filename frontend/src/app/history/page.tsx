"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

import {
  getHistoryReports,
  deleteHistoryReport,
} from "../../services/historyService";

import type { HistoryReport } from "../../types/history";

export default function HistoryPage() {
  const [reports, setReports] = useState<HistoryReport[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  useEffect(() => {
    loadReports();
  }, []);

  async function loadReports() {
    try {
      setLoading(true);
      setError(null);

      const data = await getHistoryReports();

      setReports(data);
    } catch (err) {
      console.error("Failed to load history:", err);

      setError(
        err instanceof Error
          ? err.message
          : "Failed to load report history."
      );
    } finally {
      setLoading(false);
    }
  }

  async function handleDelete(reportId: number) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this report?"
    );

    if (!confirmed) {
      return;
    }

    try {
      setDeletingId(reportId);

      await deleteHistoryReport(reportId);

      setReports((currentReports) =>
        currentReports.filter((report) => report.id !== reportId)
      );
    } catch (err) {
      console.error("Failed to delete report:", err);

      alert(
        err instanceof Error
          ? err.message
          : "Failed to delete the report."
      );
    } finally {
      setDeletingId(null);
    }
  }

  if (loading) {
    return (
      <main className="min-h-screen bg-background px-6 py-12">
        <div className="mx-auto max-w-6xl">
          <h1 className="mb-2 text-4xl font-bold">
            Assessment History
          </h1>

          <p className="text-muted-foreground">
            Loading your previous career assessments...
          </p>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="min-h-screen bg-background px-6 py-12">
        <div className="mx-auto max-w-6xl">
          <h1 className="mb-2 text-4xl font-bold">
            Assessment History
          </h1>

          <div className="mt-8 rounded-xl border p-6">
            <p className="font-medium">
              Unable to load your assessment history.
            </p>

            <p className="mt-2 text-sm text-muted-foreground">
              {error}
            </p>

            <button
              onClick={loadReports}
              className="mt-5 rounded-lg border px-4 py-2 text-sm font-medium hover:bg-muted"
            >
              Try Again
            </button>
          </div>
        </div>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-background px-6 py-12">
      <div className="mx-auto max-w-6xl">

        {/* Header */}
        <div className="mb-10 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <h1 className="text-4xl font-bold">
              Assessment History
            </h1>

            <p className="mt-2 text-muted-foreground">
              View your previous career predictions and recommendations.
            </p>
          </div>

          <Link
            href="/assessment"
            className="inline-flex w-fit rounded-lg border px-4 py-2 text-sm font-medium transition hover:bg-muted"
          >
            New Assessment
          </Link>
        </div>

        {/* Empty state */}
        {reports.length === 0 ? (
          <div className="rounded-2xl border p-10 text-center">
            <h2 className="text-xl font-semibold">
              No assessments yet
            </h2>

            <p className="mt-2 text-muted-foreground">
              Complete your first career assessment to see it here.
            </p>

            <Link
              href="/assessment"
              className="mt-6 inline-flex rounded-lg border px-5 py-2.5 text-sm font-medium hover:bg-muted"
            >
              Start Assessment
            </Link>
          </div>
        ) : (
          <>
            {/* Summary */}
            <div className="mb-6">
              <p className="text-sm text-muted-foreground">
                {reports.length}{" "}
                {reports.length === 1
                  ? "assessment"
                  : "assessments"}{" "}
                found
              </p>
            </div>

            {/* Report cards */}
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {reports.map((report, index) => (
                <div
                  key={report.id}
                  className="rounded-2xl border p-6 transition hover:shadow-md"
                >
                  <div className="mb-5 flex items-start justify-between gap-4">
                    <div>
                      <p className="text-sm text-muted-foreground">
                      Assessment {index + 1}
                      </p>

                      <h2 className="mt-1 text-xl font-semibold">
                        Career Prediction
                      </h2>
                    </div>

                    <span
                      className="rounded-full border px-3 py-1 text-xs font-medium"
                    >
                      {report.prediction}
                    </span>
                  </div>

                  <div className="space-y-3">
                    <div>
                      <p className="text-xs text-muted-foreground">
                        Confidence
                      </p>

                      <p className="text-lg font-semibold">
                        {Number(report.confidence).toFixed(2)}%
                      </p>
                    </div>

                    <div>
                      <p className="text-xs text-muted-foreground">
                        Created
                      </p>

                      <p className="text-sm">
                        {new Date(
    `${report.created_at.replace(" ", "T")}Z`
  ).toLocaleString("en-IN", {
    timeZone: "Asia/Kolkata",
})}
                      </p>
                    </div>
                  </div>

                  <div className="mt-6 flex gap-3">
                    <Link
                      href={`/history/${report.id}`}
                      className="flex-1 rounded-lg border px-4 py-2 text-center text-sm font-medium hover:bg-muted"
                    >
                      View Report
                    </Link>

                    <button
                      onClick={() =>
                        handleDelete(report.id)
                      }
                      disabled={deletingId === report.id}
                      className="rounded-lg border px-4 py-2 text-sm font-medium hover:bg-muted disabled:cursor-not-allowed disabled:opacity-50"
                    >
                      {deletingId === report.id
                        ? "Deleting..."
                        : "Delete"}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </main>
  );
}