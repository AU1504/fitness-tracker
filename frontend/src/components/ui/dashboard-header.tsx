import { Dumbbell, Settings } from 'lucide-react'

export function DashboardHeader() {
  return (
    <header className="sticky top-0 z-10 flex items-center justify-between border-b border-border bg-background/85 px-5 py-4 backdrop-blur-md">
      <div className="flex items-center gap-2">
        <span className="flex size-8 items-center justify-center rounded-lg bg-primary text-primary-foreground">
          <Dumbbell className="size-5" aria-hidden="true" />
        </span>
        <h1 className="text-xl font-bold tracking-tight text-foreground">LiftLog</h1>
      </div>
      <button
        type="button"
        aria-label="Open settings"
        className="flex size-9 items-center justify-center rounded-full text-muted-foreground transition-colors hover:bg-muted hover:text-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
      >
        <Settings className="size-5" aria-hidden="true" />
      </button>
    </header>
  )
}
