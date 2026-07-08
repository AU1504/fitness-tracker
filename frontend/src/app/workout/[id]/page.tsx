'use client'

import { useState, useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { getWorkoutDetails, startSession } from '@/lib/api'
import type { WorkoutDetailResponse } from '@/lib/api'
import { use } from 'react'

const DAY_LABELS: Record<number, string> = {
  1: 'Push Day',
  2: 'Pull Day',
  3: 'Leg Day'
}

export default function WorkoutPreviewPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params)
  const workoutId = parseInt(id)
  const router = useRouter()
  const [workout, setWorkout] = useState<WorkoutDetailResponse | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getWorkoutDetails(workoutId)
      .then((data) => {
        setWorkout(data)
        setLoading(false)
      })
  }, [workoutId])

  if (loading) return <div>Loading...</div>
  if (!workout) return null

  return(
    <section
      aria-labelledby="workout-preview-heading"
      className="rounded-3xl border border-border bg-card p-5 shadow-sm"
    >
        <Button size="lg" className="mt-5 h-12 w-full rounded-2xl text-base font-semibold shadow-sm"
          onClick={() => router.push('/')}>
          Back to Dashboard
        </Button>
      <div className="flex items-center justify-between">
        <span className="inline-flex items-center rounded-full bg-accent px-3 py-1 text-xs font-semibold text-accent-foreground">
          Workout Preview
        </span>
        <span className="text-sm font-medium text-muted-foreground">{DAY_LABELS[workout.program_day]}</span>
      </div>
        <h2 id="workout-preview-heading" className="mt-4 text-2xl font-bold tracking-tight text-foreground text-balance">
            {workout.program_name}
        </h2>
        <p className="mt-1 text-sm text-muted-foreground">{workout.comments}</p>
        <ul className="mt-4 divide-y divide-border rounded-2xl bg-muted/60">
            {workout.exercises.map((exercise) => (
              <li key={exercise.name} className="flex items-center justify-between px-4 py-2.5">
                <span className="text-sm font-medium text-foreground">{exercise.name}</span>
                <span className="text-sm text-muted-foreground">{`${exercise.planned_sets} x ${exercise.planned_reps}`}</span>
              </li>
            ))}
        </ul>
        <Button size="lg" className="mt-5 h-12 w-full rounded-2xl text-base font-semibold shadow-sm"
          onClick={() => {
            startSession(workoutId)
              .then((session) => {
                router.push(`/session/${session.session_id}`)
              })
          }}>
          Start Workout
        </Button>
    </section>
  )
}