import { NextWorkoutCard } from '@/components/ui/next-workout-card'
import { LastWorkoutCard } from '@/components/ui/last-workout-card'
import { PrHighlightsCard } from '@/components/ui/pr-highlights-card'

export default function Page() {
  return (
    <div className="space-y-4">
      <NextWorkoutCard />
      <LastWorkoutCard />
      <PrHighlightsCard />
    </div>
  )
}