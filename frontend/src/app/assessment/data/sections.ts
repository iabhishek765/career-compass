export interface AssessmentSection {
  id: number;
  title: string;
  description: string;
}

export const assessmentSections: AssessmentSection[] = [
  {
    id: 1,
    title: "Academic Profile",
    description: "Tell us about your academic background.",
  },
  {
    id: 2,
    title: "Coding & Technical Skills",
    description: "Help us understand your programming and technical skills.",
  },
  {
    id: 3,
    title: "AI/ML & Projects",
    description: "Tell us about your AI, machine learning, and project experience.",
  },
  {
    id: 4,
    title: "Experience & Professional Profile",
    description: "Share your practical experience and professional presence.",
  },
  {
    id: 5,
    title: "Career Preferences",
    description: "Tell us about your career goals and preferred domain.",
  },
];