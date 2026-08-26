"use client";

export default function Features() {
  const features = [
    {
      number: "01",
      title: "ML-Based Career Prediction",
      description:
        "Analyze your academic profile, skills, experience, and assessment inputs to generate an ML-based placement prediction.",
    },
    {
      number: "02",
      title: "Skill Gap Analysis",
      description:
        "Identify the skills that need improvement and understand which areas can strengthen your career readiness.",
    },
    {
      number: "03",
      title: "Personalized Recommendations",
      description:
        "Receive career paths, learning suggestions, and actionable recommendations tailored to your assessment profile.",
    },
  ];

  return (
    <section
      id="features"
      className="relative overflow-hidden py-24 bg-background text-foreground"
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

      {/* Subtle blue ambient glow */}
      <div className="absolute -top-40 left-1/2 h-[500px] w-[700px] -translate-x-1/2 rounded-full bg-cyan-500/10 blur-3xl pointer-events-none" />

      <div className="relative z-10 max-w-6xl mx-auto px-6">

        {/* Section heading */}
        <div className="max-w-2xl mx-auto text-center mb-14">
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-cyan-400 mb-4">
            What Career Compass Offers
          </p>

          <h2 className="text-4xl md:text-5xl font-bold tracking-tight mb-5">
            Built around your{" "}
            <span className="text-cyan-400">career profile</span>
          </h2>

          <p className="text-base md:text-lg text-muted-foreground leading-relaxed">
            Turn your academic background, skills, and experience into
            clearer career direction and practical next steps.
          </p>
        </div>

        {/* Feature cards */}
        <div className="grid md:grid-cols-3 gap-6">
          {features.map((feature) => (
            <div
              key={feature.number}
              className="group relative rounded-2xl border border-border bg-card p-7 transition-all duration-300 hover:-translate-y-1 hover:border-cyan-400/50"
            >
              <div className="flex items-center justify-between mb-8">
                <span className="text-sm font-semibold tracking-widest text-cyan-400">
                  {feature.number}
                </span>

                <div className="h-px flex-1 mx-4 bg-border group-hover:bg-cyan-400/30 transition-colors duration-300" />
              </div>

              <h3 className="text-2xl font-semibold leading-tight mb-4">
                {feature.title}
              </h3>

              <p className="text-muted-foreground leading-relaxed">
                {feature.description}
              </p>

              <div className="mt-8 h-1 w-10 rounded-full bg-cyan-400/70 transition-all duration-300 group-hover:w-16" />
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}