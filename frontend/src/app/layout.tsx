import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";
import { DashboardHeader } from "@/components/ui/dashboard-header";
import { BottomNav } from "@/components/ui/bottom-nav";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "LiftLog",
  description: "Your personal strength training tracker",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${geistSans.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col bg-background">
        <div className="mx-auto flex min-h-screen w-full max-w-md flex-col">
          <DashboardHeader />
          <main className="flex-1 px-4 pt-4 pb-28">
            {children}
          </main>
          <BottomNav />
        </div>
      </body>
    </html>
  );
}