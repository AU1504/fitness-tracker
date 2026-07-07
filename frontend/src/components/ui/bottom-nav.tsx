'use client'

import { useState } from 'react'
import { Home, History, Trophy, Settings } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
  { id: 'home', label: 'Home', icon: Home },
  { id: 'history', label: 'History', icon: History },
  { id: 'prs', label: 'PRs', icon: Trophy },
  { id: 'settings', label: 'Settings', icon: Settings },
]

export function BottomNav() {
  const [active, setActive] = useState('home')

  return (
    <nav
      aria-label="Primary"
      className="fixed inset-x-0 bottom-0 z-10 border-t border-border bg-background/90 backdrop-blur-md"
    >
      <ul className="mx-auto flex max-w-md items-stretch justify-around px-2 pb-[env(safe-area-inset-bottom)]">
        {navItems.map((item) => {
          const Icon = item.icon
          const isActive = active === item.id
          return (
            <li key={item.id} className="flex-1">
              <button
                type="button"
                onClick={() => setActive(item.id)}
                aria-current={isActive ? 'page' : undefined}
                className={cn(
                  'flex w-full flex-col items-center gap-1 py-2.5 text-xs font-medium transition-colors',
                  isActive ? 'text-primary' : 'text-muted-foreground hover:text-foreground',
                )}
              >
                <Icon className={cn('size-5', isActive && 'fill-primary/15')} aria-hidden="true" />
                {item.label}
              </button>
            </li>
          )
        })}
      </ul>
    </nav>
  )
}
