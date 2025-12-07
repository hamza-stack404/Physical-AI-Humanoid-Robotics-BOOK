# ADR-001: Humanoid Robotics Core Technologies

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-12-06
- **Feature:** 003-humanoid-robotics-capstone
- **Context:** The foundational choices for the programming languages, primary dependencies (ROS 2, simulation platforms, AI frameworks), and target deployment environments for the humanoid robotics project. These decisions dictate the entire development ecosystem and future extensibility.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

-   **Languages**: Python 3.10+, C++ (for ROS 2)
-   **Robotics Framework**: ROS 2 Humble/Iron
-   **Simulation Platforms**: Gazebo/Unity, NVIDIA Isaac Sim
-   **AI/ML Frameworks**: Whisper (for ASR), LLM (for task planning)
-   **Edge Inference Hardware**: Jetson (Orin Nano/NX)
-   **Development/Cloud Platforms**: Linux server, workstation/cloud

<!-- For technology stacks, list all components:
     - Framework: Next.js 14, App Router
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

-   Leverage established robotics ecosystem (ROS 2), providing a robust communication and control backbone.
-   Access to advanced simulation capabilities (NVIDIA Isaac Sim) for synthetic data generation and AI training.
-   Enable embodied AI with a Vision-Language-Action (VLA) pipeline through Whisper and LLMs, facilitating natural language interaction.
-   Support for edge deployment on Jetson platforms, allowing for real-world application of trained models.
-   Benefit from large, active communities and extensive documentation for chosen technologies.

### Negative

-   Steep learning curve for integrating and managing multiple complex technologies (ROS 2, Isaac Sim, LLMs, Jetson).
-   Potential integration challenges and compatibility issues between different simulation platforms (e.g., Gazebo/Unity vs. Isaac Sim workflows).
-   Significant hardware requirements, particularly an RTX GPU for NVIDIA Isaac Sim.
-   Dependency on specific operating system (Ubuntu 22.04) for ROS 2 compatibility.

## Alternatives Considered

-   **Alternative 1 (Robotics Framework)**: `MoveIt` as a primary motion planning framework. *Rejected for simplicity for a capstone project; the initial focus is on building core ROS 2 components and direct control to understand fundamentals, rather than abstracting with higher-level planning libraries immediately.*
-   **Alternative 2 (Simulation Platforms)**: `MuJoCo` or `PyBullet`. *Rejected due to potentially higher setup complexity or less comprehensive tooling compared to Isaac Sim for AI-driven robotics tasks, especially concerning synthetic data generation and integrated physics simulation capabilities.*
-   **Alternative 3 (AI/ML Language Models)**: Custom speech recognition models or smaller, specialized Natural Language Understanding (NLU) models. *Rejected to leverage the state-of-the-art capabilities of Whisper for robust ASR and powerful LLMs for advanced task planning and natural language understanding, which are critical for the capstone's objectives.*

## References

- Feature Spec: `specs/003-humanoid-robotics-capstone/spec.md`
- Implementation Plan: `specs/003-humanoid-robotics-capstone/plan.md`
- Related ADRs: N/A
