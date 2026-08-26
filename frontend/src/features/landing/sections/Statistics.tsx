"use client";

const reportItems = [
  {
    number: "01",
    title: "Career Prediction",
    description:
      "See the career outcome predicted from your assessment profile, along with the confidence associated with the prediction.",
  },
  {
    number: "02",
    title: "Profile Insights",
    description:
      "Understand the strengths and areas of your academic background, skills, experience, and assessment profile.",
  },
  {
    number: "03",
    title: "Skill Gap Analysis",
    description:
      "Identify the skills and areas that need improvement to strengthen your readiness for your target career direction.",
  },
  {
    number: "04",
    title: "Personalized Recommendations",
    description:
      "Get practical recommendations and learning directions based on the results of your assessment.",
  },
];

export default function Statistics() {
  return (
    <section
      id="report"
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

      {/* Subtle ambient glow */}
      <div className="absolute top-0 left-1/2 h-[500px] w-[700px] -translate-x-1/2 rounded-full bg-cyan-500/10 blur-3xl pointer-events-none" />

      <div className="relative z-10 max-w-6xl mx-auto px-6">
        {/* Section heading */}
        <div className="max-w-3xl mx-auto text-center mb-14">
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-cyan-400 mb-4">
            Your Career Report
          </p>

          <h2 className="text-4xl md:text-5xl font-bold tracking-tight mb-5">
            Understand your{" "}
            <span className="text-cyan-400">career direction</span>
          </h2>

          <p className="text-base md:text-lg text-muted-foreground leading-relaxed">
            Your assessment results are brought together into a clear report
            that helps you understand your current profile, identify gaps, and
            decide what to focus on next.
          </p>
        </div>

        {/* Report preview */}
        <div className="relative max-w-5xl mx-auto">
          {/* Main report panel */}
          <div className="rounded-2xl border border-border bg-card/70 backdrop-blur-sm overflow-hidden">
            {/* Report header */}
            <div className="flex items-center justify-between px-6 py-5 border-b border-border">
              <div>
                <p className="text-sm text-muted-foreground mb-1">
                  Assessment Result
                </p>

                <h3 className="text-xl font-semibold">
                  Personalized Career Report
                </h3>
              </div>

              <div className="hidden sm:flex items-center gap-2 rounded-full border border-cyan-400/30 bg-cyan-400/5 px-4 py-2">
                <span className="h-2 w-2 rounded-full bg-cyan-400" />
                <span className="text-sm text-cyan-300">
                  AI-assisted analysis
                </span>
              </div>
            </div>

            {/* Report content */}
            <div className="grid md:grid-cols-2">
              {reportItems.map((item, index) => (
                <div
                  key={item.number}
                  className={`p-7 ${
                    index < 2 ? "md:border-b border-border" : ""
                  } ${
                    index % 2 === 0 ? "md:border-r border-border" : ""
                  }`}
                >
                  <div className="flex items-center gap-4 mb-5">
                    <span className="text-sm font-semibold tracking-widest text-cyan-400">
                      {item.number}
                    </span>

                    <div className="h-px flex-1 bg-border" />
                  </div>

                  <h3 className="text-xl font-semibold mb-3">
                    {item.title}
                  </h3>

                  <p className="text-muted-foreground leading-relaxed">
                    {item.description}
                  </p>
                </div>
              ))}
            </div>
          </div>

          {/* Bottom note */}
          <div className="mt-8 text-center">
            <p className="text-sm text-muted-foreground">
              One assessment and you get a clearer picture of where you are 
              and what to work on next.
              
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}