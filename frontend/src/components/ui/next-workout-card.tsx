'use client'

import { Play } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { useState, useEffect } from 'react'
import { getNextWorkout, getWorkoutDetails } from '@/lib/api'
import type { NextWorkoutResponse, WorkoutDetailResponse } from '@/lib/api'

const DAY_LABELS: Record<number, string> = {
  1: 'Push Day',
  2: 'Pull Day',
  3: 'Leg Day'
}

export function NextWorkoutCard() {
  const [nextWorkout, setNextWorkout] = useState<NextWorkoutResponse | null>(null)
  const [workoutDetail, setWorkoutDetail] = useState<WorkoutDetailResponse | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getNextWorkout()
      .then((data) => {
        setNextWorkout(data)
        return getWorkoutDetails(data.workout_id)
      })
      .then((detail) => {
        setWorkoutDetail(detail)
        setLoading(false)
      })
    }, [])

    if (loading) return <div>Loading...</div>
    if (!nextWorkout) return null
   
  return (
    <section
      aria-labelledby="next-workout-heading"
      className="rounded-3xl border border-border bg-card p-5 shadow-sm"
    >
      <div className="flex items-center justify-between">
        <span className="inline-flex items-center rounded-full bg-accent px-3 py-1 text-xs font-semibold text-accent-foreground">
          Next Workout
        </span>
        <span className="text-sm font-medium text-muted-foreground">{DAY_LABELS[nextWorkout.program_day]}</span>
      </div>

      <h2 id="next-workout-heading" className="mt-4 text-2xl font-bold tracking-tight text-foreground text-balance">
        {nextWorkout.program_name}
      </h2>
      <p className="mt-1 text-sm text-muted-foreground">{nextWorkout.comments}</p>

      <ul className="mt-4 divide-y divide-border rounded-2xl bg-muted/60">
        {workoutDetail?.exercises.map((exercise) => (
          <li key={exercise.name} className="flex items-center justify-between px-4 py-2.5">
            <span className="text-sm font-medium text-foreground">{exercise.name}</span>
            <span className="text-sm text-muted-foreground">{`${exercise.planned_sets} x ${exercise.planned_reps}`}</span>
          </li>
        ))}
      </ul>

      <Button size="lg" className="mt-5 h-12 w-full rounded-2xl text-base font-semibold shadow-sm">
        <Play className="size-5 fill-current" aria-hidden="true" />
        Start Workout
      </Button>
    </section>
  )
}
