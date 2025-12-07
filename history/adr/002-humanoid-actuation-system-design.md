# ADR-002: Humanoid Actuation System Design

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Proposed
- **Date:** 2025-12-06
- **Feature:** 003-humanoid-robotics-capstone
- **Context:** The choice of actuation technology for the humanoid robot's joints significantly impacts its performance, robustness, cost, safety, and physical interaction capabilities. This decision is closely tied to the robot's morphology and power requirements. A thorough research phase is required before a definitive choice can be made.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The decision is to conduct a thorough research and evaluation phase to select the optimal actuation technology (electric, hydraulic, or series elastic actuators) for the humanoid robot's joints. This decision will be based on a detailed analysis of the following factors:

-   **Power density**: Required force/torque output relative to actuator size and weight.
-   **Precision and accuracy**: Ability to achieve and maintain desired joint positions and velocities.
-   **Compliance and physical interaction safety**: Inherent or controlled ability to absorb impacts and safely interact with the environment.
-   **Cost**: Budgetary constraints for procurement or manufacturing.
-   **Integration complexity**: Ease of integrating actuators with existing control systems and mechanical designs.
-   **Morphological impact**: Influence on the overall robot design, weight distribution, and limb dimensions.
-   **Power consumption**: Energy efficiency and heat generation, crucial for battery-operated systems.

## Consequences

### Positive

-   Ensures a deliberate, research-backed decision that aligns the chosen actuation technology with the specific performance, safety, and cost goals of the capstone project.
-   Mitigates risks associated with selecting an unsuitable actuation technology by understanding the tradeoffs upfront.
-   Provides a solid foundation for subsequent hardware design, control system development, and mechanical integration.

### Negative

-   Requires dedicated research time and resources, which could potentially delay downstream development if the research phase is not effectively managed and prioritized.
-   The eventual choice of actuation technology will introduce specific hardware and software constraints (e.g., driver requirements, control algorithms) that must be integrated and managed.
-   Limitations of the chosen technology could impact the range of tasks the humanoid robot can realistically perform.

## Alternatives Considered

The primary alternatives are the actuation types themselves, which are the subject of ongoing research for this project:

-   **Electric Actuators (e.g., Brushless DC motors with gearboxes)**:
    -   *Pros*: Generally precise, easy to control with mature electronic drivers, relatively clean operation, good for force control when combined with appropriate sensing.
    -   *Cons*: Can have lower power density compared to hydraulics for very high force applications, can be rigid if not designed with compliance, potential for overheating in high-load, continuous operation.
-   **Hydraulic Actuators**:
    -   *Pros*: Very high power density, capable of robust and high-force tasks, can be very stiff when needed.
    -   *Cons*: Require complex plumbing (pumps, valves, reservoirs), potential for leaks, generally less precise than electric, high maintenance, typically higher cost and noise.
-   **Series Elastic Actuators (SEAs)**:
    -   *Pros*: Inherently compliant, excellent for safe physical interaction with the environment and humans, good for force control and energy storage.
    -   *Cons*: Can be bulkier and heavier due to integrated springs, more complex mechanical design, may have dynamic limitations in high-frequency movements.

## References

- Feature Spec: `specs/003-humanoid-robotics-capstone/spec.md`
- Implementation Plan: `specs/003-humanoid-robotics-capstone/plan.md`
- Research Topics: `specs/003-humanoid-robotics-capstone/research.md` (specifically Section 1: Actuation Type)
- Related ADRs: N/A
