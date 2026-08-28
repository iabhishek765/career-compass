"use client";


import { apiRequest } from "@/services/api";


import { useState } from "react";
import { useRouter } from "next/navigation";

import { assessmentSections } from "../data/sections";
import { questions } from "../data/questions";

import ProgressBar from "./ProgressBar";
import StepIndicator from "./StepIndicator";
import QuestionCard from "./QuestionCard";
import NavigationButtons from "./NavigationButtons";
import LoadingOverlay from "./LoadingOverlay";

import { Answers } from "../types";

export default function AssessmentForm() {
  const router = useRouter();
const [isSubmitting, setIsSubmitting] = useState(false);
const [submitError, setSubmitError] = useState("");
  const [currentSection, setCurrentSection] = useState(1);
  const [answers, setAnswers] = useState<Answers>({});

  // Total number of assessment sections
  const totalSections = assessmentSections.length;

  // Current section information
  const section = assessmentSections.find(
    (section) => section.id === currentSection
  );

  // Questions belonging only to the current section
  const sectionQuestions = questions.filter(
    (question) => question.section === currentSection
  );

  // Save/update an answer
  const handleAnswer = (
    field: string,
    value: string | number
  ) => {
    setAnswers((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  // Validate every question on the current section
  const isCurrentSectionValid = sectionQuestions.every(
    (question) => {
      const answer = answers[question.field];

      // Required-field validation
      if (
        question.required &&
        (answer === undefined || answer === "")
      ) {
        return false;
      }

      // Number validation
      if (
        question.type === "number" &&
        answer !== undefined &&
        answer !== ""
      ) {
        const numericValue = Number(answer);

        if (Number.isNaN(numericValue)) {
          return false;
        }

        if (
          question.min !== undefined &&
          numericValue < question.min
        ) {
          return false;
        }

        if (
          question.max !== undefined &&
          numericValue > question.max
        ) {
          return false;
        }
      }

      return true;
    }
  );

  async function handleSubmit() {
  try {
    setIsSubmitting(true);
    setSubmitError("");

    const payload = {
      ...answers,

      Age: Number(answers.Age),
      Graduation_Year: Number(answers.Graduation_Year),
      CGPA: Number(answers.CGPA),
      LeetCode_Problems: Number(answers.LeetCode_Problems),
      Total_Projects: Number(answers.Total_Projects),
      AI_ML_Projects: Number(answers.AI_ML_Projects),
      GitHub_Repositories: Number(answers.GitHub_Repositories),
      Internship_Count: Number(answers.Internship_Count),
      Industry_Certifications: Number(answers.Industry_Certifications),
    };

    console.log("Sending payload:", payload);

    const response = await fetch(
  `${process.env.NEXT_PUBLIC_API_URL}/predict/`,
  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  }
);

    if (!response.ok) {
      const errorData = await response.json();
      console.error("Backend error:", errorData);
      throw new Error("Prediction request failed.");
    }

    const result = await response.json();

    console.log("Prediction result:", result);

    sessionStorage.setItem(
      "careerCompassResult",
      JSON.stringify(result)
    );

    router.push("/results");
  } catch (error) {
    console.error("Submission error:", error);

    setSubmitError(
      "Unable to generate your career assessment. Please try again."
    );
  } finally {
    setIsSubmitting(false);
  }
}

  // Move to the next assessment section
  function nextSection() {
    if (!isCurrentSectionValid) {
      return;
    }

    if (currentSection < totalSections) {
      setCurrentSection((prev) => prev + 1);

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    } else {
      handleSubmit();
    }
  }

  // Move to the previous assessment section
  function previousSection() {
    if (currentSection > 1) {
      setCurrentSection((prev) => prev - 1);

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    }
  }

  if (isSubmitting) {
  return <LoadingOverlay />;
}

  return (
    <div className="max-w-4xl mx-auto">
      {/* Section-based progress */}
      <ProgressBar
        current={currentSection}
        total={totalSections}
      />

      {/* Five assessment section indicators */}
      <StepIndicator
        current={currentSection}
        total={totalSections}
      />

      {/* Current section heading */}
      <div className="mt-10 mb-8">
        <p className="text-sm text-cyan-400">
          Section {currentSection} of {totalSections}
        </p>

        <h2 className="mt-2 text-3xl font-bold">
          {section?.title}
        </h2>

        <p className="mt-2 text-zinc-400">
          {section?.description}
        </p>
      </div>

      {/* All questions belonging to the current section */}
      <div className="space-y-6">
        {sectionQuestions.map((question) => (
          <QuestionCard
            key={question.id}
            question={question}
            value={answers[question.field]}
            onChange={(value) =>
              handleAnswer(question.field, value)
            }
          />
        ))}
      </div>

      {/* Section navigation */}
      <div className="mt-8">
        <NavigationButtons
          current={currentSection}
          total={totalSections}
          onNext={nextSection}
          onPrevious={previousSection}
          disabled={!isCurrentSectionValid}
        />
      </div>
    </div>
  );
}