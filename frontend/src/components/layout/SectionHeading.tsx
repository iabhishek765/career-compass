interface SectionHeadingProps {
  badge?: string;
  title: string;
  description?: string;
  center?: boolean;
}

export default function SectionHeading({
  badge,
  title,
  description,
  center = true,
}: SectionHeadingProps) {
  return (
    <div
      className={`mb-16 ${
        center ? "text-center" : "text-left"
      }`}
    >
      {badge && (
        <span className="inline-flex rounded-full border border-cyan-500/30 bg-cyan-500/10 px-4 py-1 text-sm font-medium text-cyan-400">
          {badge}
        </span>
      )}

      <h2 className="mt-4 text-4xl font-bold tracking-tight text-white md:text-5xl">
        {title}
      </h2>

      {description && (
        <p className="mx-auto mt-5 max-w-3xl text-lg leading-8 text-slate-400">
          {description}
        </p>
      )}
    </div>
  );
}