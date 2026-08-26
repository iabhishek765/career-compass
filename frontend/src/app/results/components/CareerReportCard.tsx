type CareerReportCardProps = {
  report: string;
};

export default function CareerReportCard({
  report,
}: CareerReportCardProps) {
  return (
    <section className="rounded-2xl border border-slate-700 bg-slate-950 p-6">
      <div className="mb-4">
        <p className="text-sm font-medium uppercase tracking-wider text-slate-400">
          AI Career Insights
        </p>

        <h2 className="mt-1 text-xl font-semibold text-white">
          Personalized Career Report
        </h2>
      </div>

      <p className="leading-7 text-slate-300">
        {report}
      </p>
    </section>
  );
}