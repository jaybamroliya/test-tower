# MCP Agent Control Tower

## Problem
As AI agents move into production, teams lack a centralized way to run, secure, and observe MCP-based agents safely at scale.

When agents run independently, enforcing permissions, auditing behavior, and maintaining operational control becomes difficult.

---

## Solution
**MCP Agent Control Tower** is a production-style control plane built on **Archestra** that orchestrates, secures, and observes MCP-based AI agents through a single governed execution path.

This project demonstrates how AI agents can be deployed in a **controlled, secure, and observable** environment ready for real-world use.

---

## Architecture
Users interact with the system via a CLI.  
All agent execution is routed through **Archestra**, which enforces security, orchestration, and observability.

User → CLI → Archestra → MCP Agents


### Agents
- **Task Agent:** Executes approved tasks  
- **Security Agent:** Validates permissions and scopes  
- **Observer Agent:** Logs activity and metrics

Agents never communicate directly; all execution is governed by Archestra.

---

## Execution Flow
1. User submits a task via CLI  
2. Archestra validates the request using the Security Agent  
3. Approved tasks are executed by the Task Agent  
4. All actions are logged by the Observer Agent

All execution is governed through Archestra.

---

## Permission Scopes
The Security Agent enforces scoped permissions before any task is executed.

| Scope    | Allowed Actions |
|----------|-----------------|
| read     | hello, status   |
| execute  | run, deploy     |

Requests without a defined permission scope are **explicitly denied**, ensuring safe and predictable agent behavior.

---

## Failure Handling
This system demonstrates controlled failure scenarios:
1. Unauthorized tasks are denied by policy  
2. Unknown tasks without a permission scope are rejected  
3. Explicitly forbidden actions are blocked

This proves MCP agents cannot bypass security controls.

---

## Architecture Diagram

User
↓
CLI (agentctl)
↓
Archestra Control Plane
├─ Security Agent (policy enforcement)
├─ Task Agent (execution)
└─ Observer Agent (logging & metrics)


All execution flows through Archestra.

---

## Why Archestra
Archestra provides:

1. Centralized orchestration of MCP agents  
2. Policy-based security enforcement  
3. Built-in observability and execution tracing  
4. A production-ready control plane for safe MCP agent deployment

These capabilities are difficult or impossible to achieve when agents run independently.

---

## Demo
```bash
# Allowed task
python cli/agentctl.py hello

# Unauthorized (denied) task
python cli/agentctl.py forbidden

# Unknown task (no scope)
python cli/agentctl.py unknown

Summary

MCP Agent Control Tower demonstrates how to operate MCP-based AI agents responsibly, safely, and at scale — emphasizing security, governance, and observability over mere agent capabilities.
