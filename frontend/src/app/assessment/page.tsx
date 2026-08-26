import Link from "next/link";
import { Button } from "@/components/ui/button";
import AssessmentForm from "./components/AssessmentForm";
export default function AssessmentPage() {
  return (
    <main className="min-h-screen bg-background py-20 px-6">

     <div className="max-w-5xl mx-auto">

         <h1 className="text-5xl font-bold text-center mb-4">
          Career Assessment
          </h1>

          <p className="text-center text-muted-foreground mb-16">
          Answer a few questions to receive your AI-powered career prediction.
           </p>

           <div className="mb-10">
            <Link href="/">
             <Button variant="outline">
              ← Back to Home
              </Button>
            </Link>
           </div>

           

         <AssessmentForm />

  </div>

</main>
  );
}