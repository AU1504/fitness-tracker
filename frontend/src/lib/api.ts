const BASE_URL = process.env.NEXT_PUBLIC_API_URL

async function apiFetch<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
    },
    ...options,
  })

  if (!response.ok) {
    throw new Error(`API error: ${response.status}`)
  }

  return response.json()
}

export type WorkoutExerciseInfo = {
    name: string
    planned_sets: number
    planned_reps: number
}

export type WorkoutDetailResponse = {
    program_name: string
    program_day: number
    comments: string | null
    exercises: WorkoutExerciseInfo[]
}

export type NextWorkoutResponse = {
    workout_id: number
    program_name: string
    program_day: number
    comments: string | null
}

export type SetResponse = {
    set_id: number
    reps: number
    weight: number
    comments: string | null
    is_pr: boolean
}

export type SessionExerciseInfo = {
    session_exercise_id: number
    name: string
    planned_sets: number
    planned_reps: number
}

export type SessionStartResponse = {
    session_id: number
    date: string
    program_name: string
    program_day: number
    comments: string | null
    exercises: SessionExerciseInfo[]
}

export type PreviousSetInfo = {
    set_number: number
    reps: number
    weight: number
    is_pr: boolean
}

export type PreviousExerciseInfo = {
    name: string
    sets: PreviousSetInfo[]
}

export type PreviousSessionResponse = {
    session_date: string
    program_name: string
    program_day: number
    comments: string | null
    exercises: PreviousExerciseInfo[]
}

export type PRResponse = {
    exercise_name: string
    pr_date: string
    pr_weight: number
}

export async function getNextWorkout(): Promise<NextWorkoutResponse> {
    return apiFetch<NextWorkoutResponse>('/workouts/next')
}

export async function getWorkoutDetails(workoutId: number): Promise<WorkoutDetailResponse> {
    return apiFetch<WorkoutDetailResponse>(`/workouts/${workoutId}`)
}

export async function startSession(workoutId: number): Promise<SessionStartResponse> {
    return apiFetch<SessionStartResponse>(`/workouts/${workoutId}/start`, {
        method: 'POST',
    })
}

export async function getPreviousSession(sessionId: number): Promise<PreviousSessionResponse> {
    return apiFetch<PreviousSessionResponse>(`/sessions/${sessionId}/previous`)
}

export async function getPRs(userId: number): Promise<PRResponse[]> {
    return apiFetch<PRResponse[]>(`/users/${userId}/prs`)
}   

export async function submitSet(sessionId: number, session_exercise_id: number, reps: number, weight: number, comments?: string): Promise<SetResponse> {
    return apiFetch<SetResponse>(`/sessions/${sessionId}/sets`, {
        method: 'POST',
        body: JSON.stringify({
            session_exercise_id,
            reps,
            weight,
            comments, 
        }),
    })
}

export async function getSession(sessionId: number): Promise<SessionStartResponse> {
  return apiFetch<SessionStartResponse>(`/sessions/${sessionId}`)
}