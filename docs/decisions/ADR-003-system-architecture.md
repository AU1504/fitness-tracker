# ADR-003: System Architecture, Project Structure, and Deployment Strategy

## Date
2026-05-25

## Status

Accepted

---

## Context

The project will use a separate frontend and backend architecture. The frontend will be built with Next.js, while the backend will be built with FastAPI. The application will also use a PostgreSQL database and a separate PR service.

Because the project has multiple entities, backend rules, and future growth planned, the structure needs to be organized enough to support maintainability without being overengineered for the MVP.

---

## Decision

We will use a layered FastAPI backend architecture.

The backend will be organized around the following responsibilities:

- Routes: define the API endpoints the frontend can call
- Schemas: define request and response shapes
- Models: define database tables and relationships
- Services: contain business logic and application behavior
- Database/migrations: manage persistence and schema changes over time

The general backend flow will be:

Request from Next.js
→ FastAPI route
→ service/business logic
→ database model
→ response schema
→ JSON response to Next.js

We will also use an API client layer in the Next.js frontend.

Instead of calling the backend directly from many different components, frontend API calls will be centralized in a dedicated client layer. This keeps backend URLs, request formatting, JSON handling, and error handling in one place.

The frontend flow will be:

React component/page
→ API client function
→ shared client.ts fetch wrapper
→ FastAPI backend


Next.js and FastAPI will communicate through RESTful HTTP endpoints using JSON request and response bodies.

Example endpoint style:

GET    /programs
GET    /programs/{id}
POST   /sessions
GET    /sessions/{id}
PATCH  /sessions/{id}
POST   /sessions/{id}/complete


The project will use the following deployment strategy:

Next.js frontend → Vercel
FastAPI backend → Railway
PostgreSQL database → Railway PostgreSQL


---

## Consequences

This architecture creates a clear separation of responsibilities.

Next.js will focus on UI, routing, frontend state, and user interaction. FastAPI will focus on API endpoints, validation, business logic, database access, and application rules. PostgreSQL will store persistent application data.

Using REST and JSON keeps frontend/backend communication simple, predictable, and easy to test.

Using a frontend API client layer prevents backend calls from being scattered across the Next.js application. This will make the frontend easier to refactor when backend routes, environment variables, auth, or error handling change.

Using Railway for both the backend and PostgreSQL keeps the initial deployment simple. Vercel is used for the Next.js frontend because it is well suited for Next.js deployment.

The tradeoff is that this introduces more moving parts than a single full-stack Next.js app. However, the separation better matches the long-term direction of the project and supports cleaner backend logic, future auth, migrations, and possible service expansion.