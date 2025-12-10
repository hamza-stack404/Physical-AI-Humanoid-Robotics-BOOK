<!--
Sync Impact Report:
- Version change: 1.1.0 -> 1.2.0
- Modified principles: Replaced existing detailed principles with a placeholder for future definition.
- Added sections: None (existing sections were populated with new content).
- Removed sections: None (existing sections were populated with new content).
- Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
- Follow-up TODOs: None
-->

# Project Constitution

## 1. Project Overview

### 1.1. Title
Embodied Intelligence: Physical AI & Humanoid Robotics

### 1.2. Core Goal
Write, deploy, and augment a Docusaurus-based book on Physical AI and Humanoid Robotics, including an integrated RAG chatbot.

### 1.3. Deliverables
1. Docusaurus Book (Deployed to GitHub Pages).
2. Integrated RAG Chatbot (FastAPI, Neon, Qdrant).
3. Personalization/Translation Features (Better-Auth integration, Chapter personalization button, Urdu translation button).

## 2. Core Principles
(To be defined later based on project progression and specific content guidelines. For now, principles are implicitly derived from the Core Goal and Deliverables.)

## 3. Technology & Tools

### 3.1. Required Tools
- Docusaurus (Static Site Generator for the book).
- Spec-Kit Plus (For driving the book content generation).
- FastAPI (Backend for the RAG Chatbot and Auth).
- Neon Serverless Postgres (Chatbot user/metadata storage).
- Qdrant Cloud Free Tier (Vector Database for RAG).
- OpenAI Agents/ChatKit SDKs (For RAG Chatbot logic).
- Better-Auth (For Signup/Signin and user personalization).

### 3.2. Agent Roles
1. **Book_Author_Agent (Primary):** Responsible for generating the technical content for the 11 chapters based on the course details.
2. **Docusaurus_Engineer_Agent:** Responsible for setting up the Docusaurus project structure and integrating custom React components (chatbot, personalization buttons).
3. **RAG_Engineer_Agent:** Responsible for the FastAPI RAG backend, data ingestion logic, and Qdrant/Neon setup.
4. **Auth_Engineer_Agent:** Responsible for integrating Better-Auth signup/signin flows and storing user background for personalization.
5. **Translator_Agent (Subagent):** A dedicated, reusable skill to translate specified text content into Urdu.

## 4. Governance

### 4.1. Version
1.2.0

### 4.2. Ratification Date
2025-12-08

### 4.3. Last Amended Date
2025-12-08

### 4.4. Amendment Procedure
This constitution can be amended by a supermajority vote (2/3) of the project's core contributors. Proposed amendments must be circulated to all core contributors at least one week prior to a vote.

### 4.5. Compliance Review
Compliance with these principles will be reviewed quarterly by the project lead and documented in a publicly accessible report.
