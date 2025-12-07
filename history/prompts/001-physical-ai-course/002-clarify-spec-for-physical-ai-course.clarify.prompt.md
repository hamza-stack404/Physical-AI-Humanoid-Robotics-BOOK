---
id: 002
title: Clarify Spec for Physical AI Course
stage: clarify
date: 2025-12-06
surface: agent
model: gemini-2.5-flash
feature: physical-ai-course
branch: 001-physical-ai-course
user: unknown
command: /sp.clarify Context for prioritization: My course book specification is stored in specs/001-physical-ai-course/spec.md Analyze it for the following: Ambiguous terms What does “complete course book” mean — is it a textbook, a curriculum, or a hybrid? "High-level hardware requirements"—how detailed should pricing, benchmarks, and compatibility be? “Humanoid interaction design”—what depth is expected (theoretical or implementation-level)? "Embodied intelligence"—what exact definitions or frameworks should be used? Missing assumptions Required baseline knowledge for students (Python? Linear algebra? ROS 2 experience?). Expected depth of physics topics (kinematics, dynamics, locomotion control). Citation style and technical sourcing expectations for robotics papers. Whether diagrams/figures will be text-only placeholders or full rendered images. Whether the book is self-contained or assumes external ROS/Isaac documentation. Incomplete or unclear requirements How detailed each module must be: ROS 2: Are code examples required or only conceptual descriptions? Gazebo/Unity: Include installation steps or high-level simulation theory? Isaac Sim: Depth of coverage for SLAM, navigation, RL pipeline, and synthetic data? VLA: Should it include prompt engineering or only robotics-side logic? Hardware sections: Do we include full purchasing guides or only technical minimum specs? Cloud architecture: Should cost modeling be approximate or precise? Capstone project: How detailed should the evaluation rubric and deliverables be? Scope conflicts Is the book primarily an academic explanation of Physical AI OR a practical hands-on training course? Should the focus be humanoid robots specifically, or also quadrupeds/arms (proxy systems)? Simulation-first approach vs. physical robot-first learning — which is prioritized? Should the book be strictly educational or also serve as a lab setup guide for institutions? What gaps need to be clarified before planning the book structure? Required student prerequisite knowledge Expected coding depth (minimal vs. fully instructional) Level of mathematical rigor Extent of hardware guidance (basic overview vs. full lab manual) Whether real robot deployment is mandatory or optional Specific grading/assessment guidelines for the capstone Whether the book should include full lesson plans or only conceptual chapters How deep VLA, GPT integration, and SLAM pipelines should go
labels: ["clarification", "spec"]
links:
  spec: specs/001-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-course/spec.md
tests:
---

## Prompt

/sp.clarify Context for prioritization: My course book specification is stored in specs/001-physical-ai-course/spec.md Analyze it for the following: Ambiguous terms What does “complete course book” mean — is it a textbook, a curriculum, or a hybrid? "High-level hardware requirements"—how detailed should pricing, benchmarks, and compatibility be? “Humanoid interaction design”—what depth is expected (theoretical or implementation-level)? "Embodied intelligence"—what exact definitions or frameworks should be used? Missing assumptions Required baseline knowledge for students (Python? Linear algebra? ROS 2 experience?). Expected depth of physics topics (kinematics, dynamics, locomotion control). Citation style and technical sourcing expectations for robotics papers. Whether diagrams/figures will be text-only placeholders or full rendered images. Whether the book is self-contained or assumes external ROS/Isaac documentation. Incomplete or unclear requirements How detailed each module must be: ROS 2: Are code examples required or only conceptual descriptions? Gazebo/Unity: Include installation steps or high-level simulation theory? Isaac Sim: Depth of coverage for SLAM, navigation, RL pipeline, and synthetic data? VLA: Should it include prompt engineering or only robotics-side logic? Hardware sections: Do we include full purchasing guides or only technical minimum specs? Cloud architecture: Should cost modeling be approximate or precise? Capstone project: How detailed should the evaluation rubric and deliverables be? Scope conflicts Is the book primarily an academic explanation of Physical AI OR a practical hands-on training course? Should the focus be humanoid robots specifically, or also quadrupeds/arms (proxy systems)? Simulation-first approach vs. physical robot-first learning — which is prioritized? Should the book be strictly educational or also serve as a lab setup guide for institutions? What gaps need to be clarified before planning the book structure? Required student prerequisite knowledge Expected coding depth (minimal vs. fully instructional) Level of mathematical rigor Extent of hardware guidance (basic overview vs. full lab manual) Whether real robot deployment is mandatory or optional Specific grading/assessment guidelines for the capstone Whether the book should include full lesson plans or only conceptual chapters How deep VLA, GPT integration, and SLAM pipelines should go

## Response snapshot

The specification for the "Physical AI and Humanoid Robotics Course" has been clarified through 5 targeted questions. The `spec.md` file has been updated, and the clarifications are recorded in a new section. All critical ambiguities have been addressed.

## Outcome

- ✅ Impact: The feature specification is now more precise, with key ambiguities resolved and requirements refined based on user input. This reduces downstream rework risk.
- 🧪 Tests: No explicit tests were run; the process involved interactive clarification and direct spec modification.
- 📁 Files: The `specs/001-physical-ai-course/spec.md` file was modified to include the clarifications.
- 🔁 Next prompts: The user is now ready to proceed with planning the feature.
- 🧠 Reflection: The interactive clarification process was effective in refining the specification. The ability to dynamically update the spec after each question ensures that the document remains accurate and up-to-date.

## Evaluation notes (flywheel)

- Failure modes observed: None during the clarification process itself after initial setup was resolved.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Automate the addition of `## Clarifications` section if not present, and handle the numbering of `FR-` more dynamically.
