### Status: Proposed
### Date: 2025-07-11
### Deciders:
- #### Hubert Kwiatek
### Consulted:
- #### -
### Informed:
- #### -

---

# ADR-0001: Technology Stack Selection

## Context and Problem Statement

What technology stack should we choose to build the ToDo Web Application?

## Decision Drivers

1. The stack should be easily testable and maintainable in a small team.
2. The backend must support asynchronous processing for integration with Celery and a message broker.
3. The frontend and backend stacks should have mature ecosystems and available boilerplate templates to allow rapid development.
4. We aim to use a single relational database for simplicity, consistency, and faster development.

## Considered Options

### 1. Frontend
- Framework: React / Angular / Vue
- CSS: Tailwind / Bootstrap / custom
- Build tools: Vite / Webpack / CRA
- Language: TypeScript / JavaScript

### 2. Backend
- Framework: Django / Express / FastAPI / Spring Boot
- Language: Python / Node.js / Java / Go
- API style: REST / GraphQL / gRPC
- Auth: JWT / OAuth2 / Sessions

### 3. Database
- Relational: PostgreSQL / MySQL / SQLite
- NoSQL: MongoDB / Redis / DynamoDB
- ORM: SQLAlchemy / Prisma / Django ORM

### 4. Queues / Messaging
- Message broker: RabbitMQ / Kafka / Redis 
- Task Runners: Celery (Python) / BullMQ (Node.js) / Spring Batch

### 5. DevOps & Deployment
- Containerization: Docker / Podman
- Orchestration: Kubernetes / Docker Compose 
- CI/CD: GitHub Actions / GitLab CI / Azure DevOps / Jenkins

### 6. Testing
- Frontend: Jest / React Testing Library / Vue Testing Library / Cypress
- Backend: Pytest / Postman / Supertest

## Decision Outcome

We have chosen:
- Frontend: Vue 3 + Tailwind CSS + Vite + TypeScript
- Backend: Django + DRF with JWT authentication (ASGI-compatible) and build API with REST metodology
- Database: PostgreSQL
- Message Queue: Redis + Celery
- DevOps: Docker, Docker Compose for local development; GitHub Actions for CI/CD
- Testing: Jest & Vue Testing Library (frontend), Pytest (backend)

## Consequences

* Good, because fast and efficient implementation thanks to the chosen technology stack, which we are already familiar with.
* Good, because rapid development due to the availability of mature ecosystems and ready-to-use packages in both Django and Vue.
* Bad, because potential limitations if we later decide to scale or replace parts of the stack with technologies outside the ecosystems.

## Validation

This decision was driven by the team’s deep expertise with these technologies.

## Options  - Pros and Cons

1. **Frontend: Vue 3 + Tailwind CSS + Vite + TypeScript**  

    **Pros:** 
     - Large ecosystem of Vue plugins
     - Easy integration with component libraries (e.g. Headless UI, Vuetify)
     - Lightning and fast local development 
     - Strong typing and autocomplete from TypeScript

    **Cons:**
     - Initial learning curve if team isn’t yet fluent in TypeScript.
     - Potential bundle‑size bloat if unused Tailwind utilities aren’t purged.

2. **Backend: Django + DRF**

    **Pros:**
     - Team already has deep expertise with Python/Django
     - Well‑documented ecosystem with thousands of reusable packages.
     - DRF provides serializers, viewsets and browsable API out of the box
     - Included: auth, admin UI, ORM, migrations.

    **Cons:**
     - Generally slower raw performance compared to Go or Node.js

3. **Database: PostgreSQL**

    **Pros:**
     - Support in Django ORM
     - Excellent community and commercial tooling
     - The database our team knows best

4. **Message Queue: Redis + Celery**

    **Pros:**
     - Simple setup for background jobs and rate‑limited tasks.
     - Great for small to medium traffic
     - Easy to monitor and scale
     - Includes built‑in caching support

    **Cons:**
     - Redis isn’t a true Message Queue, lacks features like message persistence and complex routing
     - Migrating to RabbitMQ or Kafka may be required in future

5. **DevOps & Deployment**

    **Pros:**
     - GitHub Actions makes it trivial to define CI/CD workflows in YAML
     - Docker containers isolate dependencies — identical local, staging, and production environments.
     - Docker Compose simplifies multi‑container setups for local development.

    **Cons:**
     - Need platform that manage containers (ECS, App Platform ...)

6. **Testing**

    **Pros:**
     - Pytest and Django’s test framework provide robust unit‑ and integration‑testing
     - Jest + Vue Testing Library for reliable component and end‑to‑end tests.
    **Cons:**
     - Writing and maintaining tests adds upfront time to feature development.

## More Information

This ADR should be implemented as soon as we start developing our ToDo Web Application.

- [Vue](https://vuejs.org/guide/introduction.html)  
- [Vite](https://vitejs.dev/guide/)
- [Tailwind CSS](https://tailwindcss.com/docs/installation)  
- [TypeScript](https://www.typescriptlang.org/docs/)  
- [Django](https://www.djangoproject.com/) 
- [Django Rest Framework](https://www.django-rest-framework.org/)  
- [PostgreSQL](https://www.postgresql.org/docs/)  
- [Celery](https://docs.celeryproject.org/) 
- [Redis](https://redis.io/documentation)  
- [Docker](https://docs.docker.com/get-started/)  
- [Docker Compose](https://docs.docker.com/compose/)  
- [GitHub Actions](https://docs.github.com/actions)  
- [Pytest](https://docs.pytest.org/)  
- [Jest](https://jestjs.io/docs/getting-started) 
- [Vue Testing Library](https://testing-library.com/docs/vue-testing-library/overview/)

