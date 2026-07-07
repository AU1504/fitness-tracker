'use client'

import { Trophy } from 'lucide-react'
import { useState, useEffect } from 'react'
import type { PRResponse } from '@/lib/api'
import { getPRs } from '@/lib/api'

export function PrHighlightsCard() {

  const [personalRecords, setPersonalRecords] = useState<PRResponse[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchPersonalRecords = async () => {
      setLoading(true)
      try {
        const data = await getPRs(1) // Replace 1 with the actual user ID
        setPersonalRecords(data)
      } catch (error) {
        console.error('Error fetching personal records:', error)
      } finally {
        setLoading(false)
      }
    }

    fetchPersonalRecords()
  }, [])

  return (
    <section
      aria-labelledby="pr-highlights-heading"
      className="rounded-3xl border border-border bg-card p-5 shadow-sm"
    >
      <div className="flex items-center gap-2">
        <Trophy className="size-5 text-primary" aria-hidden="true" />
        <h2 id="pr-highlights-heading" className="text-base font-semibold text-foreground">
          PR Highlights
        </h2>
      </div>

      <ul className="mt-4 space-y-3">
        {personalRecords.map((pr) => (
          <li
            key={pr.exercise_name}
            className="flex items-center justify-between rounded-2xl bg-muted/60 px-4 py-3"
          >
            <div>
              <p className="text-sm font-semibold text-foreground">{pr.exercise_name}</p>
              <p className="text-xs text-muted-foreground">{new Date(pr.pr_date).toLocaleDateString()}</p>
            </div>
            <div className="text-right">
              <p className="text-base font-bold text-foreground">{`${pr.pr_weight} lbs`}</p>
            </div>
          </li>
        ))}
      </ul>
    </section>
  )
}
