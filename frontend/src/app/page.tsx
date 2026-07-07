import { DashboardHeader } from '@/components/ui/dashboard-header'
import { NextWorkoutCard } from '@/components/ui/next-workout-card'
import { LastWorkoutCard } from '@/components/ui/last-workout-card'
import { PrHighlightsCard } from '@/components/ui/pr-highlights-card'
import { BottomNav } from '@/components/ui/bottom-nav'

export default function Page() {
  return (
    <div className="mx-auto flex min-h-screen max-w-md flex-col bg-background">
      <DashboardHeader />
      <main className="flex-1 space-y-4 px-5 pb-28 pt-5">
        <NextWorkoutCard />
        <LastWorkoutCard />
        <PrHighlightsCard />
      </main>
      <BottomNav />
    </div>
  )
}
