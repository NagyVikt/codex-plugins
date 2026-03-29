---
name: agentation
description: Use when setting up Agentation in a React app, configuring annotation workflows, or connecting an MCP-enabled coding agent for real-time annotation sync.
---

# Agentation Setup

Use this workflow to integrate Agentation quickly and safely.

## 1) Install package

```bash
npm install agentation -D
```

Equivalent options:

- `yarn add -D agentation`
- `pnpm add -D agentation`
- `bun add -d agentation`

## 2) Add component (development-only)

Render `Agentation` near app root so annotation UI is available across screens.

```tsx
import { Agentation } from "agentation"

function App() {
  return (
    <>
      <YourApp />
      {process.env.NODE_ENV === "development" && <Agentation />}
    </>
  )
}
```

## 3) Connect MCP server (recommended)

Preferred universal setup command:

```bash
npx add-mcp "npx -y agentation-mcp server"
```

Claude Code specific interactive setup:

```bash
npx agentation-mcp init
```

Health check:

```bash
npx agentation-mcp doctor
```

Default server port is `4747`.

## 4) Wire endpoint in React

```tsx
<Agentation
  endpoint="http://localhost:4747"
  onSessionCreated={(sessionId) => {
    console.log("Session started:", sessionId)
  }}
/>
```

## 5) Expected behavior

- local-first annotations work offline
- same session is reused across refreshes
- only new annotations are uploaded
- server-side resolves/dismissals win on rejoin

## 6) Security and environment guardrails

- keep Agentation dev-only (`NODE_ENV === "development"`)
- default mode is local-only (no external requests)
- when endpoint is used, data should stay on localhost

## 7) Troubleshooting checklist

- verify React 18+ and client-side rendering context
- confirm MCP server is reachable on expected port
- rerun `npx agentation-mcp doctor`
- ensure only one active server process is bound to the chosen port
