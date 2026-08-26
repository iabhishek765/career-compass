"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { Menu, X, Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";

import Logo from "@/components/common/Logo";
import Container from "./Container";
import { NAV_LINKS } from "@/constants/navigation";
import { Button } from "@/components/ui/button";

export default function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

useEffect(() => {
    setMounted(true);
}, []);

if (!mounted) return null;

  return (
    <header className="fixed top-0 left-0 right-0 z-50 border-b border-white/10 bg-slate-950/70 backdrop-blur-xl">
      <Container>
        <div className="flex h-20 items-center justify-between">
          <Logo />

          {/* Desktop Navigation */}

          <nav className="hidden items-center gap-8 md:flex">
            {NAV_LINKS.map((item) => (
              <Link
                key={item.label}
                href={item.href}
                className="text-sm font-medium text-slate-300 transition hover:text-cyan-400"
              >
                {item.label}
              </Link>
            ))}
          </nav>

          {/* Right Side */}

          <div className="hidden items-center gap-3 md:flex">
            <Button
              variant="ghost"
              size="icon"
              onClick={() =>
                setTheme(theme === "dark" ? "light" : "dark")
              }
            >
              {theme === "dark" ? (
                <Sun size={18} />
              ) : (
                <Moon size={18} />
              )}
            </Button>

            
            <div className="flex items-center gap-2">
  <Link href="/history">
    <Button variant="outline">
      History
    </Button>
  </Link>

  <Link href="/assessment">
    <Button>
      Get Started
    </Button>
  </Link>
</div>
          </div>

          {/* Mobile Button */}

          <button
            className="md:hidden"
            onClick={() => setMobileOpen(!mobileOpen)}
          >
            {mobileOpen ? <X /> : <Menu />}
          </button>
        </div>

        {mobileOpen && (
          <div className="space-y-4 border-t border-white/10 py-6 md:hidden">
            {NAV_LINKS.map((item) => (
              <Link
                key={item.label}
                href={item.href}
                className="block text-slate-300 hover:text-cyan-400"
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
              </Link>
            ))}

            <Button className="w-full">
              Get Started
            </Button>
          </div>
        )}
      </Container>
    </header>
  );
}