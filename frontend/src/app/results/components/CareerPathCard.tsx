type CareerPathCardProps = {
  careerPath: string[];
};

export default function CareerPathCard({
  careerPath,
}: CareerPathCardProps) {
  if (!careerPath || careerPath.length === 0) {
    return null;
  }

  return (
    <section className="rounded-2xl border border-slate-700 bg-slate-950 p-6">
      <div className="mb-6">
        <p className="text-sm font-medium uppercase tracking-wider text-slate-400">
          Career Progression
        </p>

        <h2 className="mt-1 text-xl font-semibold text-white">
          Recommended Career Path
        </h2>
      </div>

      <div className="flex flex-wrap items-center gap-3">
        {careerPath.map((role, index) => (
          <div key={`${role}-${index}`} className="flex items-center gap-3">
            <div className="rounded-lg border border-slate-700 bg-slate-900 px-4 py-3">
              <p className="text-sm text-slate-400">
                Stage {index + 1}
              </p>

              <p className="mt-1 font-medium text-white">
                {role}
              </p>
            </div>

            {index < careerPath.length - 1 && (
              <span className="text-xl text-cyan-400">
                →
              </span>
            )}
          </div>
        ))}
      </div>
    </section>
  );
}