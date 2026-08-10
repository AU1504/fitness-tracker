'use client'

import { useState, useEffect, use } from 'react'
import { useRouter } from 'next/navigation'
import { getSession, submitSet } from '@/lib/api'
import type { SessionStartResponse, SetResponse } from '@/lib/api'

export default function SessionPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params)
  const sessionId = parseInt(id)
  const router = useRouter()
  const [session, setSession] = useState<SessionStartResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [currentExerciseIndex, setCurrentExerciseIndex] = useState(0)
  const [currentWeight, setCurrentWeight] = useState('')
  const [currentReps, setCurrentReps] = useState('')
  const [loggedSets, setLoggedSets] = useState<Record<number, SetResponse[]>>({})
  const [lastSetWasPR, setLastSetWasPR] = useState(false)

  useEffect(() => {
    getSession(sessionId)
      .then((data) => {
        setSession(data)
        setLoading(false)
      })
  }, [sessionId])

  if (loading) return <div>Loading...</div>
  if (!session) return null

  const currentExercise = session.exercises[currentExerciseIndex]
  const currentLoggedSets = loggedSets[currentExercise.session_exercise_id] || []

  const handleLogSet = async () => {
  const weight = currentWeight === '' ? 0 : parseFloat(currentWeight)

  const result = await submitSet(
    sessionId,
    currentExercise.session_exercise_id,
    parseInt(currentReps),
    weight
  )

  const newLoggedSets = [...(loggedSets[currentExercise.session_exercise_id] || []), result]

  setLoggedSets(prev => ({
    ...prev,
    [currentExercise.session_exercise_id]: newLoggedSets
  }))

  setLastSetWasPR(result.is_pr)
  setCurrentWeight('')
  setCurrentReps('')

  if (newLoggedSets.length >= currentExercise.planned_sets) {
    setTimeout(() => {
      setLastSetWasPR(false)
      if (currentExerciseIndex < session.exercises.length - 1) {
        setCurrentExerciseIndex(prev => prev + 1)
      }
    }, 1500)
  }
}

const handleNextExercise = () => {
  setLastSetWasPR(false)
  setCurrentExerciseIndex(prev => prev + 1)
}

return (
  <div className="space-y-4">
    <p className="text-sm text-muted-foreground">
      Exercise {currentExerciseIndex + 1} of {session.exercises.length}
    </p>

    <h2 className="text-2xl font-bold">{currentExercise.name}</h2>
    <p className="text-sm text-muted-foreground">
      Planned: {currentExercise.planned_sets} sets × {currentExercise.planned_reps} reps
    </p>

    {lastSetWasPR && (
      <div className="rounded-xl bg-green-500/20 p-3 text-green-400 font-semibold">
        🏆 New PR!
      </div>
    )}

    <p className="text-sm">Sets logged: {currentLoggedSets.length} / {currentExercise.planned_sets}</p>

    <input
      type="number"
      placeholder="Weight (lbs) - Leave empty for bodyweight"
      value={currentWeight}
      onChange={(e) => setCurrentWeight(e.target.value)}
      className="w-full rounded-xl border border-border bg-muted p-3 text-foreground"
    />
    <input
      type="number"
      placeholder="Reps"
      value={currentReps}
      onChange={(e) => setCurrentReps(e.target.value)}
      className="w-full rounded-xl border border-border bg-muted p-3 text-foreground"
    />

    <button
      onClick={handleLogSet}
      className="w-full rounded-xl bg-primary p-3 font-semibold text-primary-foreground"
    >
      Log Set
    </button>

    {currentExerciseIndex < session.exercises.length - 1 && (
      <button
        onClick={handleNextExercise}
        className="w-full rounded-xl border border-border p-3 font-semibold"
      >
        Next Exercise
      </button>
    )}
  </div>
)
}