"use client";

export default function CTA() {
  return (
    <section
      id="get-started"
      className="relative overflow-hidden py-28 bg-background text-foreground"
    >
      {/* Background grid */}
      <div
        className="absolute inset-0 pointer-events-none opacity-60"
        style={{
          backgroundImage: `
            linear-gradient(rgba(255,255,255,0.035) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.035) 1px, transparent 1px)
          `,
          backgroundSize: "48px 48px",
        }}
      />

      {/* Ambient glow */}
      <div className="absolute left-1/2 top-1/2 h-[500px] w-[800px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-cyan-500/10 blur-3xl pointer-events-none" />

      <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
        {/* Label */}
        <p className="text-sm font-medium uppercase tracking-[0.2em] text-cyan-400 mb-5">
          Your Next Step
        </p>

        {/* Heading */}
        <h2 className="text-4xl md:text-6xl font-bold tracking-tight leading-tight mb-6">
          Build a clearer path
          <br />
          toward your{" "}
          <span className="text-cyan-400">career</span>
        </h2>

        {/* Description */}
        <p className="max-w-2xl mx-auto text-base md:text-lg text-muted-foreground leading-relaxed mb-10">
          Complete your assessment to understand your current profile,
          identify areas to improve, and get personalized career guidance.
        </p>

        {/* CTA */}
        <a
          href="/assessment"
          className="inline-flex items-center gap-3 rounded-lg bg-cyan-400 px-7 py-3.5 text-base font-semibold text-slate-950 transition-all duration-300 hover:bg-cyan-300 hover:-translate-y-0.5"
        >
          Start Your Assessment
          <span aria-hidden="true">→</span>
        </a>

        {/* Supporting line */}
        <p className="mt-5 text-sm text-muted-foreground">
          Assess your profile. Understand your strengths. Plan your next step.
        </p>
      </div>
    </section>
  );
}