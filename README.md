# MCP Agent Control Tower

## Problem
As AI agents move into production, teams lack a centralized way to run, secure,
and observe MCP-based agents safely at scale.

## Solution
MCP Agent Control Tower is a production-style control plane built on Archestra
that orchestrates, secures, and observes MCP agents through a single governed
execution path.

## Architecture
User interacts via CLI. All agent execution is routed through Archestra,
which enforces security, orchestration, and observability.

User → CLI → Archestra → MCP Agents

Agents:
- Task Agent: Executes approved tasks
- Security Agent: Validates permissions
- Observer Agent: Logs activity and metrics

## Execution Flow
1. User submits a task via CLI
2. Archestra validates the request using the Security Agent
3. Approved tasks are executed by the Task Agent
4. All actions are logged by the Observer Agent

Agents never communicate directly.
All execution is governed through Archestra.

## Permission Scopes

The Security Agent enforces scoped permissions before any task is executed.

| Scope   | Allowed Actions |
| ------- | --------------- |
| read    | hello, status   |
| execute | run, deploy     |

Requests that do not match a defined permission scope are explicitly denied, ensuring safe and predictable agent behavior.

## Failure Handling

The system demonstrates controlled failure scenarios:
1. Unauthorized tasks are denied by policy
2. Unknown tasks without a permission scope are rejected
3. Explicitly forbidden actions are blocked

This proves that MCP agents cannot bypass security controls.

## Architecture Diagram

User
  ↓
CLI (agentctl)
  ↓
Archestra Control Plane
  ├─ Security Agent (policy enforcement)
  ├─ Task Agent (execution)
  └─ Observer Agent (logging & metrics)


## Why Archestra

Archestra provides:
1. Centralized orchestration of MCP agents
2. Policy-based security enforcement
3. Built-in observability and execution tracing
4. A production-ready control plane for AI agents'
observability for MCP agents—capabilities that are impossible to achieve
when agents run independently.
