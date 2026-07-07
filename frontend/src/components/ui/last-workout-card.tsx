import { CheckCircle2 } from 'lucide-react'

export function LastWorkoutCard() {
  return (
    <section
      aria-labelledby="last-workout-heading"
      className="rounded-3xl border border-border bg-card p-5 shadow-sm"
    >
      <div className="flex items-center justify-between">
        <h2 id="last-workout-heading" className="text-base font-semibold text-foreground">
          Last Workout
        </h2>
      </div>
      <p className="mt-3 text-sm text-muted-foreground">
        No recent workouts yet. Complete a session to see your history here.
      </p>
    </section>
  )
}