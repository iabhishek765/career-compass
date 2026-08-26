"use client";

const faqs = [
  {
    question: "How does Career Compass work?",
    answer:
      "It uses AI and Machine Learning to analyze your profile and recommend suitable career paths.",
  },
  {
    question: "Is it free?",
    answer:
      "Yes. Students can use the platform free of cost.",
  },
  {
    question: "Is my data secure?",
    answer:
      "Yes. Your information is securely processed and never shared without permission.",
  },
];

export default function FAQ() {
  return (
    <section id="faq" className="py-24 bg-muted/20">
      <div className="max-w-4xl mx-auto px-6">

        <h2 className="text-4xl font-bold text-center mb-12">
          Frequently Asked Questions
        </h2>

        <div className="space-y-6">
          {faqs.map((faq) => (
            <div
              key={faq.question}
              className="rounded-lg border p-6 bg-card"
            >
              <h3 className="font-semibold mb-2">
                {faq.question}
              </h3>

              <p className="text-muted-foreground">
                {faq.answer}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}