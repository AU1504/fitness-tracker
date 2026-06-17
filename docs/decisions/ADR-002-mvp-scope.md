# ADR-002: MVP Scope and Versioning Strategy

## Date
2026-05-22

## Status
Accepted

## Context
The fitness tracker project includes workout logging, progression tracking, authentication, AI-generated routines, analytics, and live workout features. Building all of these at once would create unnecessary complexity early in development.

We need a phased rollout plan that keeps the MVP focused while still designing the system for future expansion.

## Decision
The project will be developed in five version tiers.

### MVP
Focus: Core workout tracking
Features:

* Pre-seeded workout templates (PPL, Upper/Lower, 5/3/1, etc.)
* Log workout sessions
* Track sets, reps, and weight
* Show previous session performance
* Automatic PR detection
* Weekly volume tracking
* PR history
* Basic exercise library

  * Name
  * Muscle groups
  * Movement pattern

The MVP will use a single hardcoded user, but will be built with authentication in mind.

---

### V2

Focus: Progression systems and analytics

Features:

* Suggested target weights
* Stall detection
* Manual program creation
* Estimated 1RM tracking
* Charts and progress visualization

---

### V3

Focus: Multi-user support and authentication

Features:

* User registration/login
* OAuth with NextAuth.js
* User profiles

  * Goals
  * Experience level
  * Equipment access

---

### V4

Focus: AI-assisted coaching features

Features:

* AI-generated programs/routines
* Variable progression systems
* Exercise reference material

  * Videos
  * Images
  * AI-recommended resources

---

### V5

Focus: Live workout experience

Features:

* Live workout tracker
* Rest timer
* Geofence workout prompts
* Possible wearable/health integrations

## Consequences

This approach makes it easier to:

* Keep the MVP achievable
* Build foundational systems first
* Avoid premature complexity
* Expand features incrementally

Tradeoffs:

* V2 features like weight suggestions and stall detection depend on having enough logged data to be meaningful, which is why logging comes first
* Authentication is postponed until V3, this is not ignoring auth, it simply allows for setting up the bones of the application first
* Certain features may require schema expansion later

## Additional Decisions

### Hardcoded User in MVP

The MVP uses a single hardcoded user to reduce early complexity and focus on validating the workout tracking experience before implementing authentication.

### Auth-Aware Data Model

Even without login functionality, the database schema will still include `user_id` relationships from the beginning to avoid major rewrites later.

### Seeded Templates

Workout templates in MVP are treated as pre-seeded data rather than user-created programs. Manual program creation is delayed until V2.

### Exercise Library Scope

The MVP exercise library is functional only:

* Names
* Muscle groups
* Movement patterns

Reference content like videos and AI-recommended resources is intentionally delayed until V4.
