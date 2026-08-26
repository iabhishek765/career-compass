"use client";

const testimonials = [
  {
    name: "Rahul Sharma",
    role: "Computer Science Student",
    review:
      "Career Compass helped me identify Data Science as the right career path and gave me a clear roadmap.",
  },
  {
    name: "Priya Singh",
    role: "AI/ML Student",
    review:
      "The personalized recommendations and skill analysis were extremely helpful.",
  },
  {
    name: "Aman Verma",
    role: "Software Engineering Student",
    review:
      "A beautiful platform with accurate AI-based career guidance.",
  },
];

export default function Testimonials() {
  return (
    <section id="testimonials" className="py-24 bg-background">
      <div className="max-w-6xl mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-12">
          What Students Say
        </h2>

        <div className="grid md:grid-cols-3 gap-8">
          {testimonials.map((item) => (
            <div
              key={item.name}
              className="rounded-xl border bg-card p-6"
            >
              <p className="text-muted-foreground mb-5">
                "{item.review}"
              </p>

              <h3 className="font-semibold">
                {item.name}
              </h3>

              <p className="text-sm text-muted-foreground">
                {item.role}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}