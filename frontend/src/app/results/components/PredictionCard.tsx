type PredictionCardProps = {
  prediction: string;
  probability: number;
};

export default function PredictionCard({
  prediction,
  probability,
}: PredictionCardProps) {
  const isPlaced = prediction.toLowerCase() === "placed";

  return (
    <div className="rounded-2xl border border-slate-700 bg-slate-950 p-6">
      <p className="mb-2 text-sm font-medium uppercase tracking-wider text-slate-400">
        Placement Prediction
      </p>

      <div className="flex items-end justify-between gap-4">
        <div>
          <h2 className="text-3xl font-bold text-white">
            {prediction}
          </h2>

          <p className="mt-2 text-sm text-slate-400">
            Model Confidence
          </p>
        </div>

        <div className="text-right">
          <span className="text-3xl font-bold text-cyan-400">
            {probability.toFixed(2)}%
          </span>
        </div>
      </div>

      <div className="mt-6 h-2 w-full overflow-hidden rounded-full bg-slate-800">
        <div
          className={`h-full rounded-full ${
            isPlaced ? "bg-emerald-500" : "bg-amber-500"
          }`}
          style={{
            width: `${Math.min(Math.max(probability, 0), 100)}%`,
          }}
        />
      </div>

      <p className="mt-4 text-sm text-slate-400">
        {isPlaced
          ? "Your profile currently shows a strong placement readiness."
          : "Your profile has improvement opportunities that can strengthen your placement readiness."}
      </p>
    </div>
  );
}