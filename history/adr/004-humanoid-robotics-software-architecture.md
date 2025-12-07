# ADR-004: Humanoid Robotics Software Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-12-06
- **Feature:** 003-humanoid-robotics-capstone
- **Context:** The overall organization and interaction patterns of software components are crucial for managing complexity, enabling collaboration, ensuring maintainability, and facilitating the integration of diverse robotics and AI functionalities within the Humanoid Robotics AI Capstone project. This decision outlines the project's folder structure, module responsibilities, and comprehensive testing strategy.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The project will adopt a single-repository, robotics-adapted software architecture. This structure emphasizes modularity through ROS 2 packages while keeping all related assets and documentation within a cohesive project.

-   **Project Structure**:
    -   `ros_packages/`: Central directory for all ROS 2 workspaces and individual packages. This includes:
        -   `<robot_description_pkg>/`: Contains Universal Robot Description Format (URDF), meshes, and other robot model assets.
        -   `<controller_pkg>/`: ROS 2 packages implementing robot controllers and interfaces (e.g., joint controllers, inverse kinematics).
        -   `<perception_pkg>/`: ROS 2 packages for vision (VSLAM, object detection) and other sensor processing nodes.
        -   `<vla_pipeline_pkg>/`: ROS 2 packages integrating Whisper, LLM, and action servers for the Vision-Language-Action pipeline.
    -   `ai_models/`: Dedicated storage for trained AI models, including object detection weights, LLM fine-tunes, and other machine learning artifacts.
    -   `simulation_assets/`: Contains assets for simulation environments, such as Gazebo/Unity worlds, 3D models, and textures.
    -   `scripts/`: General utility scripts for tasks like data processing, hardware setup, and custom tool development.
    -   `docs/`: The root directory for the Docusaurus project, housing all research paper chapters, tutorials, and project documentation.
    -   `static/`: Stores static assets (images, diagrams) used within the Docusaurus documentation.
    -   `tests/`: Comprehensive testing suite for the entire project, categorized into:
        -   `unit/`: Unit tests for individual code modules and algorithms.
        -   `integration/`: Integration tests for verifying the interaction between ROS 2 nodes and the VLA pipeline.
        -   `simulation/`: Simulation-based tests to validate robot behaviors, task completion, and system robustness in various virtual environments.

-   **Module Responsibilities**:
    -   Clear separation of concerns: ROS 2 packages handle real-time robotics tasks; `ai_models` are for learned intelligence; `simulation_assets` define the digital twin; and `docs` ensures knowledge transfer.
    -   Each ROS 2 package will have a single, well-defined responsibility.

-   **Testing Strategy**:
    -   Adoption of a multi-layered testing strategy (unit, integration, simulation) to ensure the reliability and correctness of both software components and robot behaviors.
    -   Emphasis on simulation-based testing for validation of complex, real-world robot interactions before deployment.

## Consequences

### Positive

-   **Clear Separation of Concerns**: Promotes modularity, making the codebase easier to understand, maintain, and allowing for parallel development efforts.
-   **ROS 2 Ecosystem Integration**: Standardized ROS 2 package structure facilitates leveraging community tools, components, and best practices, as well as potential future contribution.
-   **Robust Development Workflow**: Dedicated testing directories and a multi-layered testing strategy encourage a test-driven approach, improving code quality and robot reliability.
-   **Comprehensive Documentation**: Integration with Docusaurus provides a structured framework for the research paper, tutorials, and project documentation, enhancing knowledge transfer and onboarding.

### Negative

-   **Initial Setup Complexity**: The number of specialized directories and ROS 2 conventions might introduce a steeper learning curve for newcomers to the project.
-   **Management Overhead**: Requires careful adherence to naming conventions, module boundaries, and inter-package dependencies to prevent architectural erosion and maintain clarity.
-   **Integration Test Challenges**: Designing and maintaining robust integration tests for complex hardware/software systems can be challenging and time-consuming, particularly for validating physical robot behaviors.
-   **Redundancy Concerns**: Potential for redundancy if assets or configurations are duplicated across simulation platforms (e.g., Gazebo and Isaac Sim).

## Alternatives Considered

-   **Alternative 1 (Monolithic Structure)**:
    -   *Description*: All code placed in a single `src/` directory without distinct ROS package separation or specialized directories for AI models and simulation assets.
    -   *Rejected*: Would lead to significantly reduced modularity, increased complexity for a large robotics and AI project, and hinder code reuse and independent development of components.
-   **Alternative 2 (Distributed Microservices/Multiple Repositories)**:
    -   *Description*: Each major component (e.g., control, perception, VLA pipeline) is managed in its own separate Git repository, interacting via well-defined APIs.
    -   *Rejected*: Overkill for a capstone research project of this scale; significantly increases overhead for deployment, inter-service communication management, versioning, and local development setup. Introduces unnecessary complexity for coordination.
-   **Alternative 3 (Minimal Testing)**:
    -   *Description*: Rely primarily on manual testing and high-level simulation-only validation, with limited unit or integration tests.
    -   *Rejected*: Greatly increases the risk of undetected bugs, reduces confidence in robot behavior, makes debugging more difficult, and hinders continuous integration and deployment efforts, which are critical for an AI-driven robotics project.

## References

- Feature Spec: `specs/003-humanoid-robotics-capstone/spec.md`
- Implementation Plan: `specs/003-humanoid-robotics-capstone/plan.md`
- Related ADRs: N/A
