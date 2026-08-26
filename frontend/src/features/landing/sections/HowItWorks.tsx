"use client";

const steps = [
  {
    number: "01",
    title: "Complete Your Assessment",
    description:
      "Share your academic background, skills, experience, interests, and other profile details through the assessment.",
  },
  {
    number: "02",
    title: "ML-Based Analysis",
    description:
      "The system analyzes your assessment profile and uses the trained machine learning model to generate a placement prediction.",
  },
  {
    number: "03",
    title: "Get Personalized Guidance",
    description:
      "Receive a personalized career report with suitable career directions, skill gaps, and practical recommendations for your next steps.",
  },
];

export default function HowItWorks() {
  return (
    <section
      id="how-it-works"
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
            How Career Compass Works
          </p>

          <h2 className="text-4xl md:text-5xl font-bold tracking-tight mb-5">
            From your profile to your{" "}
            <span className="text-cyan-400">next step</span>
          </h2>

          <p className="text-base md:text-lg text-muted-foreground leading-relaxed">
            A simple three-step process turns your profile into a clearer
            understanding of your career direction and areas to improve.
          </p>
        </div>

        {/* Steps */}
        <div className="grid md:grid-cols-3 gap-6">
          {steps.map((step, index) => (
            <div key={step.number} className="relative">
              {/* Connection line */}
              {index < steps.length - 1 && (
                <div className="hidden md:block absolute top-8 left-[calc(100%+0.75rem)] w-3 h-px bg-cyan-400/30 z-20" />
              )}

              <div className="group relative h-full rounded-2xl border border-border bg-card p-7 transition-all duration-300 hover:-translate-y-1 hover:border-cyan-400/50">
                {/* Step number */}
                <div className="flex items-center justify-between mb-8">
                  <span className="text-sm font-semibold tracking-widest text-cyan-400">
                    {step.number}
                  </span>

                  <div className="h-px flex-1 mx-4 bg-border group-hover:bg-cyan-400/30 transition-colors duration-300" />
                </div>

                {/* Step title */}
                <h3 className="text-2xl font-semibold leading-tight mb-4">
                  {step.title}
                </h3>

                {/* Step description */}
                <p className="text-muted-foreground leading-relaxed">
                  {step.description}
                </p>

                {/* Bottom accent */}
                <div className="mt-8 h-1 w-10 rounded-full bg-cyan-400/70 transition-all duration-300 group-hover:w-16" />
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}