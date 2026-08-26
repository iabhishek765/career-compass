import Navbar from "@/components/layout/Navbar";
import Hero from "@/features/landing/sections/Hero";
import Features from "@/features/landing/sections/Features";
import HowItWorks from "@/features/landing/sections/HowItWorks";
import Statistics from "@/features/landing/sections/Statistics";
import CTA from "@/features/landing/sections/CTA";
import Footer from "@/components/layout/Footer";

export default function Home() {
  return (
    <main className="min-h-screen bg-background">
      <Navbar />

      <Hero />

      <Features />

      <HowItWorks />

      <Statistics />

      <CTA />

      <Footer />
    </main>
  );
}