---
id: 1
title: Establish Project Constitution for AI Robotics Course
stage: constitution
date: 2025-12-05
surface: agent
model: gemini
feature: none
branch: 001-physical-ai-robotics-book
user: TALHAdevelops
command: /sp.constitution
labels: [constitution, project-setup, robotics, ai-course]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .gemini/commands/sp.constitution.toml
tests:
  - none
---

## Prompt

/sp.constitution Project: Physical AI & Humanoid Robotics Course — A complete Docusaurus-based educational book covering modern physical AI systems, humanoid robotics, embodied intelligence, and practical development workflows.

Core Principles

Scientific accuracy: All robotics and AI concepts must reference primary sources (research papers, manufacturer docs, IEEE, arXiv, MIT Press).

Engineering clarity: Content must be understandable to students and developers with foundational programming and hardware knowledge.

Hands-on orientation: Every chapter must include practical examples, code, simulations, or hardware workflows.

Traceability: Each concept must cite its origin—paper, academic source, robotics standard, or official documentation.

AI-native workflow: Book creation must demonstrate Spec-Kit Plus + Claude Code usage for structured writing, automated generation, and refinement.

Modular learning: Chapters must progress from basics to advanced humanoid robotics systems (mechanics → sensing → control → AI).

Key Standards

Citation style: Short-form academic style with research-backed references.

Source quality: Minimum 50% peer-reviewed sources (IEEE, ACM, Springer, arXiv with credibility).

Technical accuracy:

Mechanical concepts (kinematics, dynamics) must use correct formulas.

AI/ML content must reflect state-of-the-art reasoning techniques.

Robotics frameworks (ROS2, Gazebo, MuJoCo, Isaac) must follow official documentation.

Code validity: All code examples must run in modern environments (ROS2 Humble+, Python 3.10+, C++).

Writing clarity: Target readability for advanced students and early-career robotics engineers.

Content consistency: Each chapter must use the same structure: concept → technical depth → practical example → reference links.

Constraints

Chapters: 10–14 chapters, each 800–1500 words.

Format: MDX/Markdown optimized for Docusaurus v3.

Graphics: Diagrams, robot architectures, and flowcharts rendered via Mermaid or embedded images.

Deployment: Must deploy to GitHub Pages with CI/CD (GitHub Actions).

Folder structure:

specs/ — All Spec-Kit Plus specification files

docs/ — All book chapters

static/ — Assets and diagrams

Tooling: Mandatory use of Spec-Kit Plus for spec generation + Claude Code for iterative writing.

Success Criteria

Spec-traceable: Every chapter must link back to at least one sp.specification file.

Build verification: Docusaurus must build with zero warnings or errors.

Technical correctness:

Kinematics/dynamics formulas correct

Sensor explanations accurate

AI control laws valid

Code examples executable

Deployment-ready: Book must be live on GitHub Pages.

Reader outcome: A learner should be able to:

Understand humanoid robot structure

Work with ROS2

Simulate robots

Implement AI/ML pipelines for physical agents

Build basic humanoid robotics applications

## Response snapshot

Updated the project constitution and verified consistency across all project templates and command definitions.

## Outcome

- ✅ Impact: Established a new project constitution and ensured all related templates and command definitions are consistent with it.
- 🧪 Tests: none
- 📁 Files: 
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .gemini/commands/sp.constitution.toml
- 🔁 Next prompts: none
- 🧠 Reflection: The process of updating the constitution and then propagating those changes through the project's templates and command definitions is a good example of maintaining project consistency.

## Evaluation notes (flywheel)

- Failure modes observed: The initial prompt for `sp.constitution` had an incorrect path for checking command files.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
