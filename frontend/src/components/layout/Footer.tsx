"use client";

export default function Footer() {
  return (
    <footer className="border-t py-8 bg-background">
      <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center">

        <div>
          <h3 className="font-bold text-lg">
            Career Compass
          </h3>

          <p className="text-muted-foreground">
            AI Powered Career Guidance
          </p>
        </div>

        <p className="text-sm text-muted-foreground mt-4 md:mt-0">
          © 2026 Career Compass. All rights reserved.
        </p>

      </div>
    </footer>
  );
}