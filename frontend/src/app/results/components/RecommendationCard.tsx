interface RecommendationCardProps {
  title: string;
  items: string[];
}

export default function RecommendationCard({
  title,
  items,
}: RecommendationCardProps) {
  if (!items || items.length === 0) {
    return null;
  }

  return (
    <section className="border border-slate-700 rounded-xl p-6">
      <h2 className="text-xl font-semibold">
        {title}
      </h2>

      <ul className="mt-4 space-y-2">
        {items.map((item, index) => (
          <li
            key={`${item}-${index}`}
            className="text-slate-200"
          >
            • {item}
          </li>
        ))}
      </ul>
    </section>
  );
}