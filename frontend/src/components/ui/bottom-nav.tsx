'use client'

import { useRouter, usePathname } from 'next/navigation'
import { Home, History, Trophy, Settings } from 'lucide-react'
import { cn } from '@/lib/utils'

const navItems = [
    { id: 'home', label: 'Home', icon: Home, path: '/' },
    { id: 'history', label: 'History', icon: History, path: '/history' },
    { id: 'prs', label: 'PRs', icon: Trophy, path: '/prs' },
    { id: 'settings', label: 'Settings', icon: Settings, path: '/settings' },
  ]


export function BottomNav() {
  
  const router = useRouter()
  const pathname = usePathname()

  return (
    <nav
      aria-label="Primary"
      className="fixed inset-x-0 bottom-0 z-10 border-t border-border bg-background/90 backdrop-blur-md"
    >
      <ul className="mx-auto flex max-w-md items-stretch justify-around px-2 pb-[env(safe-area-inset-bottom)]">
        {navItems.map((item) => {
          const Icon = item.icon
          const isActive = pathname === item.path
          return (
            <li key={item.id} className="flex-1">
              <button
                type="button"
                onClick={() => router.push(item.path)}
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
