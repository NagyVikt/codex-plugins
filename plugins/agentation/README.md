# agentation

```
 █████╗  ██████╗ ███████╗███╗   ██╗████████╗ █████╗ ████████╗██╗ ██████╗ 
██╔══██╗██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██║██╔═══██╗
███████║██║  ███╗█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   ██║██║   ██║
██╔══██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██║██║   ██║
██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ 
                                                                         
███╗   ██╗
████╗  ██║
██╔██╗ ██║
██║╚██╗██║
██║ ╚████║
╚═╝  ╚═══╝
          
```

Agentation adds in-app annotations and MCP-synced feedback loops for React teams and coding agents.

## What It Can Do
- Adds in-app annotations to React apps so bugs, questions, and TODOs are captured in context.
- Synchronizes annotation threads with MCP-enabled coding agents for round-trip updates.
- Supports acknowledgment, replies, and resolution workflows directly from agent tooling.

## Why Use It
- Keeps implementation feedback attached to the exact UI state where it happened.
- Reduces handoff friction between product/design/dev and coding agents.
- Makes review loops faster by turning comments into actionable, trackable items.

## How It Works
1. Install Agentation in your React app and enable local annotation capture.
2. Connect the Agentation MCP server so the agent can read and act on annotation threads.
3. Use the built-in annotation lifecycle (reply/acknowledge/resolve) while iterating on code.

## Quick Examples

```
Set up Agentation in my React app and wire MCP sync for my coding agent
```

## Requirements
- A React application where Agentation can be installed.
- Node.js tooling to run the MCP server (`npx -y agentation-mcp server`).
