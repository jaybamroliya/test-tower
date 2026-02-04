## Architecture Diagram

User
  ↓
CLI (agentctl)
  ↓
Archestra Control Plane
  ├─ Security Agent (policy enforcement)
  ├─ Task Agent (execution)
  └─ Observer Agent (logging & metrics)

Agents never communicate directly.
All execution flows through Archestra.
