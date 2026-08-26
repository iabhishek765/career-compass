import Link from "next/link";
import { Compass } from "lucide-react";

export default function Logo() {
  return (
    <Link href="/" className="flex items-center gap-3">
      <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-cyan-500 text-white">
        <Compass className="h-5 w-5" />
      </div>

      <div>
        <h1 className="text-lg font-bold">Career Compass</h1>
        <p className="text-xs text-slate-400">
          AI Career Guidance
        </p>
      </div>
    </Link>
  );
}