#ADR-001: Tech Stack Decision Making. Frontend, Backend, Database, Auth.

##Date
2026-05-22

##Status
Accepted

##Context
We are building a fitness tracker application that will evolve through multiple phases:
	• MVP workout logging and progression tracking 
	• Expanded analytics and overload logic 
	• Multi-user authentication and profiles 
	• AI-generated programs and recommendations 
	• Live workout tracking and possible wearable integrations 
The project needs a stack that supports:
	• A modern reactive frontend 
	• A scalable API backend 
	• Future AI-related features 
	• Clear separation of frontend and backend responsibilities 
	• Easy iteration during development 
	• A clean path from MVP to production 
Although the MVP will initially use a single hardcoded user, the architecture should still be designed as if multi-user support already exists so authentication can be added later without major rewrites.

##Decision
We will use the following architecture:
	• Frontend: Next.js with the App Router 
	• Backend: Python/FastAPI 
	• Database: PostgreSQL 
	• Authentication: NextAuth.js on the frontend with backend token validation added during V3
	• Backend ORM/Data Layer: Python ORM (SQLModel)

##Options Considered
	• Option A: Next.js frontend + FastAPI backend
This was chosen because it provides a clean separation between frontend and backend responsibilities while allowing the backend to use Python for analytics, progression logic, and future AI features. FastAPI also provides strong typing, validation through Pydantic, automatic API documentation, and a structure better suited for API-first development.
	• Option B: Full-stack Next.js with Prisma
This was considered because it simplifies deployment and allows everything to exist in one TypeScript application. However, it tightly couples frontend and backend concerns and pushes all backend logic into the JavaScript ecosystem. Since this project is expected to grow into AI-assisted programming and more advanced progression logic, a Python backend was considered a better long-term fit.
	• Option C: React/Next.js frontend + Express backend
This was considered because Express is lightweight and widely used. However, FastAPI provides stronger validation, cleaner API structure, built-in OpenAPI documentation, and better developer ergonomics for typed APIs. FastAPI is also better aligned with future machine learning or AI-related integrations.
	• Option D: Django full-stack backend
This was considered because Django includes many built-in features like authentication and administration tooling. However, the project does not need a monolithic backend-rendered architecture. Django was considered heavier than necessary for an API-first application and less aligned with the intended frontend/backend separation.

##Consequences
This decision makes it easier to:
	• Keep frontend and backend responsibilities clearly separated 
	• Build APIs cleanly and consistently 
	• Use Python for progression algorithms and future AI integrations 
	• Scale frontend and backend independently 
	• Maintain a modern React frontend experience 
	• Add AI-generated workout planning later without changing backend ecosystems 
	• Create reusable backend APIs for possible future mobile apps 
The tradeoffs are:
	• More deployment complexity because frontend and backend are separate services 
	• Additional work for authentication flows between Next.js and FastAPI 
	• More initial setup compared to a monolithic application 
	• Requires managing two runtimes and development environments 
	• API contracts between frontend and backend must remain synchronized
	• FastAPI is being chose partly to gain Python experience which might slow initial development velocity while ramping up
