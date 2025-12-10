# Implementation Plan: Embodied Intelligence: A Guide to Physical AI & Humanoid Robotics

**Branch**: `001-physical-ai-book` | **Date**: 2025-12-08 | **Spec**: [specs/001-physical-ai-book/spec.md](specs/001-physical-ai-book/spec.md)
**Input**: Feature specification from `/specs/001-physical-ai-book/spec.md`

## Summary

This plan outlines the development of a Docusaurus-based book on Physical AI and Humanoid Robotics. The project encompasses generating technical content across 11 chapters, deploying the book to GitHub Pages, and augmenting it with an integrated RAG chatbot, personalization features, and Urdu translation capabilities. The implementation will leverage FastAPI for backend services, Neon for database, Qdrant for vector storage, and Better-Auth for user authentication.

## Technical Context



**Language/Version**: Python 3.10+ (for FastAPI, Agents), JavaScript/TypeScript (for Docusaurus, React components).  

**Primary Dependencies**: Docusaurus, Spec-Kit Plus, FastAPI, Neon (PostgreSQL), Qdrant (Vector DB), OpenAI Agents/ChatKit SDKs, Better-Auth.  

**Storage**: Neon Serverless Postgres (user data, metadata), Qdrant Cloud Free Tier (vector embeddings for RAG).  

**Testing**: (NEEDS CLARIFICATION: Frameworks for Docusaurus, FastAPI, and agent logic testing)  

**Target Platform**: Web (Docusaurus book deployed to GitHub Pages), Cloud (FastAPI backend, Neon, Qdrant).  

**Project Type**: Hybrid (Static site generation with Docusaurus, dynamic backend services with FastAPI).  

**Performance Goals**: RAG chatbot response under 5 seconds (SC-002), FastAPI RAG backend p95 latency under 500ms (SC-007).  

**Constraints**: Book content must be the sole source for RAG answers. Docusaurus content (MDX) compatibility. No plagiarism. Citations must follow IEEE style.  

**Scale/Scope**: 11 chapters of content. Multiple concurrent users for personalization and translation.



## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Project Title Alignment**: Does the plan align with "Embodied Intelligence: Physical AI & Humanoid Robotics"? (Yes, this is the core project)
- [X] **Core Goal Adherence**: Does the plan aim to "Write, deploy, and augment a Docusaurus-based book on Physical AI and Humanoid Robotics, including an integrated RAG chatbot."? (Yes, the plan directly supports this goal)
- [X] **Deliverables Covered**: Does the plan include the Docusaurus Book, Integrated RAG Chatbot, and Personalization/Translation Features? (Yes, these are broken down into phases)
- [X] **Required Tools Utilization**: Does the plan leverage Docusaurus, Spec-Kit Plus, FastAPI, Neon, Qdrant, OpenAI Agents/ChatKit SDKs, and Better-Auth? (Yes, these are explicitly mentioned in technical context and plan phases)
- [X] **Agent Roles Defined**: Does the plan align with the defined Agent Roles? (Yes, the phases are structured around agent responsibilities)

## Project Structure

### Documentation (this feature)

```text
specs/001-physical-ai-book/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Hybrid: Docusaurus Frontend + FastAPI Backend

physical-ai-textbook/  # Docusaurus project
├── src/                # React components, pages
│   ├── components/     # Custom UI components (e.g., chatbot, personalization buttons)
│   └── pages/          # Docusaurus pages
├── docs/               # Markdown/MDX content for chapters
├── docusaurus.config.js # Docusaurus configuration
├── package.json        # Frontend dependencies
└── ...

backend/                # FastAPI project
├── app/
│   ├── api/            # FastAPI endpoints (e.g., RAG, Auth, Translation)
│   ├── core/           # Core logic (e.g., RAG processing, personalization)
│   ├── db/             # Database interactions (Neon, Qdrant)
│   └── models/         # Data models
├── tests/              # Backend tests
├── requirements.txt    # Python dependencies
└── ...

agents/                 # Agent definitions and reusable skills
├── translator_agent/   # Translator_Agent implementation
└── personalizer_agent/ # Background_Personalizer_Agent implementation

```

**Structure Decision**: A hybrid project structure is chosen to clearly separate the static Docusaurus frontend, the dynamic FastAPI backend, and dedicated directories for reusable AI agents. This promotes modularity and maintainability.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
