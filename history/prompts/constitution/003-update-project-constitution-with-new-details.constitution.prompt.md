---
id: 003
title: Update project constitution with new details
stage: constitution
date: 2025-12-08
surface: agent
model: (unknown)
feature: none
branch: (unknown)
user: (unknown)
command: /sp.constitution replace the old constitution with this 
TITLE: Embodied Intelligence: Physical AI & Humanoid Robotics
CORE_GOAL: Write, deploy, and augment a Docusaurus-based book on Physical AI and Humanoid Robotics, including an integrated RAG chatbot.
DELIVERABLES:
1. Docusaurus Book (Deployed to GitHub Pages).
2. Integrated RAG Chatbot (FastAPI, Neon, Qdrant).
3. Personalization/Translation Features (Better-Auth integration, Chapter personalization button, Urdu translation button).

REQUIRED_TOOLS:
- Docusaurus (Static Site Generator for the book).
- Spec-Kit Plus (For driving the book content generation).
- FastAPI (Backend for the RAG Chatbot and Auth).
- Neon Serverless Postgres (Chatbot user/metadata storage).
- Qdrant Cloud Free Tier (Vector Database for RAG).
- OpenAI Agents/ChatKit SDKs (For RAG Chatbot logic).
- Better-Auth (For Signup/Signin and user personalization).

AGENT_ROLES:
1. **Book_Author_Agent (Primary):** Responsible for generating the technical content for the 11 chapters based on the course details.
2. **Docusaurus_Engineer_Agent:** Responsible for setting up the Docusaurus project structure and integrating custom React components (chatbot, personalization buttons).
3. **RAG_Engineer_Agent:** Responsible for the FastAPI RAG backend, data ingestion logic, and Qdrant/Neon setup.
4. **Auth_Engineer_Agent:** Responsible for integrating Better-Auth signup/signin flows and storing user background for personalization.
5. **Translator_Agent (Subagent):** A dedicated, reusable skill to translate specified text content into Urdu.
labels: ["constitution", "update"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
tests:

---

## Prompt

/sp.constitution replace the old constitution with this 
TITLE: Embodied Intelligence: Physical AI & Humanoid Robotics
CORE_GOAL: Write, deploy, and augment a Docusaurus-based book on Physical AI and Humanoid Robotics, including an integrated RAG chatbot.
DELIVERABLES:
1. Docusaurus Book (Deployed to GitHub Pages).
2. Integrated RAG Chatbot (FastAPI, Neon, Qdrant).
3. Personalization/Translation Features (Better-Auth integration, Chapter personalization button, Urdu translation button).

REQUIRED_TOOLS:
- Docusaurus (Static Site Generator for the book).
- Spec-Kit Plus (For driving the book content generation).
- FastAPI (Backend for the RAG Chatbot and Auth).
- Neon Serverless Postgres (Chatbot user/metadata storage).
- Qdrant Cloud Free Tier (Vector Database for RAG).
- OpenAI Agents/ChatKit SDKs (For RAG Chatbot logic).
- Better-Auth (For Signup/Signin and user personalization).

AGENT_ROLES:
1. **Book_Author_Agent (Primary):** Responsible for generating the technical content for the 11 chapters based on the course details.
2. **Docusaurus_Engineer_Agent:** Responsible for setting up the Docusaurus project structure and integrating custom React components (chatbot, personalization buttons).
3. **RAG_Engineer_Agent:** Responsible for the FastAPI RAG backend, data ingestion logic, and Qdrant/Neon setup.
4. **Auth_Engineer_Agent:** Responsible for integrating Better-Auth signup/signin flows and storing user background for personalization.
5. **Translator_Agent (Subagent):** A dedicated, reusable skill to translate specified text content into Urdu.

## Response snapshot

The project constitution file `.specify/memory/constitution.md` has been updated to version 1.2.0.
The update includes new project overview details, required tools, and agent roles, based on the provided input.
The "Core Principles" section has been generalized to indicate future definition.

Summary for user:
- New version: 1.2.0 (minor bump due to significant updates in project overview, tools, and agent roles).
- Files flagged for manual follow-up:
    - .specify/templates/plan-template.md
    - .specify/templates/spec-template.md
    - .specify/templates/tasks-template.md
- Suggested commit message: docs: amend constitution to v1.2.0 (project overview, tools, and agent roles update)

## Outcome

- ✅ Impact: The project constitution was successfully updated with new project overview, tools, and agent roles.
- 🧪 Tests: No new tests were added or run for this constitution update.
- 📁 Files: 1 file was modified: .specify/memory/constitution.md
- 🔁 Next prompts: User will review the updated constitution and provide further instructions.
- 🧠 Reflection: The process involved parsing user input, updating the constitution template, and generating a sync impact report. Templates for plan, spec, and tasks require manual update.

## Evaluation notes (flywheel)

- Failure modes observed: 
- Graders run and results (PASS/FAIL): 
- Prompt variant (if applicable): 
- Next experiment (smallest change to try): 
