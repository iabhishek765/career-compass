"use client";

import { ArrowRight, BrainCircuit, Sparkles } from "lucide-react";

export default function Hero() {
  return (
    <section
      id="home"
      className="relative min-h-[calc(100vh-80px)] overflow-hidden bg-background text-foreground"
    >
      {/* Background glow */}
      <div className="pointer-events-none absolute inset-0">
        <div className="absolute left-1/2 top-1/4 h-80 w-80 -translate-x-1/2 rounded-full bg-cyan-500/10 blur-3xl" />
        <div className="absolute -left-20 bottom-0 h-72 w-72 rounded-full bg-blue-500/10 blur-3xl" />
        <div className="absolute -right-20 top-20 h-72 w-72 rounded-full bg-cyan-400/10 blur-3xl" />

        <div
          className="absolute inset-0 opacity-[0.04]"
          style={{
            backgroundImage:
              "linear-gradient(rgba(255,255,255,0.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.5) 1px, transparent 1px)",
            backgroundSize: "48px 48px",
          }}
        />
      </div>

      {/* Hero content */}
      <div className="relative mx-auto flex min-h-[calc(100vh-80px)] max-w-6xl items-center justify-center px-6 py-24">
        <div className="max-w-4xl text-center">
          {/* Small badge */}
          <div className="mb-7 inline-flex items-center gap-2 rounded-full border border-border bg-card/60 px-4 py-2 text-sm text-muted-foreground backdrop-blur-sm">
            <Sparkles className="h-4 w-4 text-cyan-400" />
            <span>AI-powered career intelligence</span>
          </div>

          {/* Main heading */}
          <h1 className="text-5xl font-bold leading-tight tracking-tight sm:text-6xl lg:text-7xl">
            Find the Career Path
            <span className="block text-cyan-400">That Fits You</span>
          </h1>

          {/* Description */}
          <p className="mx-auto mt-7 max-w-2xl text-lg leading-8 text-muted-foreground sm:text-xl">
            Career Compass analyzes your academic profile, skills, interests,
            and experience to provide an ML-based placement prediction and
            personalized career recommendations. Turn your assessment profile 
            into a clearer view of your placement outlook, skill gaps, and
            next career steps.
            
          </p>

          {/* Supporting statement */}
          <p className="mt-5 text-sm text-muted-foreground/80">
            Assess your profile. Understand your strengths. Build your next step.
          </p>

          {/* CTA */}
          <div className="mt-9 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <a
              href="/assessment"
              className="inline-flex items-center gap-2 rounded-lg bg-cyan-500 px-6 py-3 font-medium text-slate-950 transition hover:bg-cyan-400"
            >
              Start Your Assessment
              <ArrowRight className="h-4 w-4" />
            </a>

            <a
              href="#features"
              className="inline-flex items-center gap-2 rounded-lg border border-border px-6 py-3 font-medium transition hover:bg-card"
            >
              Explore Career Compass
            </a>
          </div>

          {/* Capability indicators */}
          <div className="mt-12 flex flex-wrap items-center justify-center gap-x-7 gap-y-3 text-sm text-muted-foreground">
            <span className="inline-flex items-center gap-2">
              <BrainCircuit className="h-4 w-4 text-cyan-400" />
              ML-based prediction
            </span>

            <span className="hidden h-1 w-1 rounded-full bg-muted-foreground/50 sm:block" />

            <span>🔍Skill gap analysis</span>

            <span className="hidden h-1 w-1 rounded-full bg-muted-foreground/50 sm:block" />

            <span>🎯Personalized recommendations</span>
          </div>
        </div>
      </div>
    </section>
  );
}