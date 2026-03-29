# CODEX PLUGINS

The plugin workspace for Codex.

Built for humans, AI agents, and CI/CD pipelines.

```text
 ██████╗ ██████╗ ██████╗ ███████╗██╗  ██╗    ██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝    ██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██║     ██║   ██║██║  ██║█████╗   ╚███╔╝     ██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██║     ██║   ██║██║  ██║██╔══╝   ██╔██╗     ██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
╚██████╗╚██████╔╝██████╔╝███████╗██╔╝ ██╗    ██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

## What Codex can already do with plugins

This is the real, current capability surface from plugins in this repo today.

### Create web apps quickly
- Build and refine Next.js-style product UIs with `build-web-apps` (`frontend-skill`, `react-best-practices`, `shadcn-best-practices`).
- Turn Figma designs into implementation tasks and component mappings with `figma` (`figma-implement-design`, `figma-code-connect-components`, `figma-create-design-system-rules`).
- Convert code changes into GitHub branches and PRs with `github` (`yeet`, `github`, `gh-address-comments`).
- Add payments and database architecture safely with `stripe` (`stripe-best-practices`) and `supabase` (`setup`, `supabase-usage`, `cli`).

### Design and visual iteration workflows
- Run design-to-code loops using `figma` plus UI refinement in `build-web-apps`.
- Test and verify web output in browser flows with `vercel` (`agent-browser`, `agent-browser-verify`, `verification`).
- Structure storefront/admin UX work for commerce projects with `medusa` and `saleor` skills.
- Iterate safely with branching and review workflows via `github` and `superpowers`.

### Development tools you can run now
- Use structured implementation workflows from `superpowers` (planning, debugging, TDD, verification, code review).
- Run plugin-specific CLI workflows with `supabase` (`cli`) and `resend` (`resend-cli`).
- Use integration-focused workflows for cloud/platform ops with `aws`, `cloudflare`, `vercel`, and `netlify`.
- Triage production signals with `sentry` and feed fixes into repo workflows with `github`.

### Deploy and ship faster
- Deploy and operate web apps with `vercel` (`deployments-cicd`, `vercel-cli`, `env-vars`, `observability`).
- Deploy to Netlify with `netlify` (`netlify-deploy`).
- Manage production-ready delivery flows from implementation to PR using `github` + `superpowers`.
- Support links/domains/env management through deployment and platform skills in `vercel` and `netlify`.

### Collaboration and coordination
- Summarize channels, draft replies, and build digests with `slack` skills.
- Triage inboxes and draft email responses with `gmail`.
- Schedule and coordinate team calendars with `google-calendar`.
- Capture planning/research/meeting knowledge with `notion`.
- Add annotation-driven developer feedback loops in React apps with `agentation`.

### Advanced AI and platform capabilities
- Build AI-enabled app flows with `vercel` (`ai-sdk`, `ai-elements`, `ai-gateway`, `chat-sdk`).
- Configure and use MCP-backed workflows in supported plugins (`vercel`, `supabase`, `cloudflare`, `aws`, `medusa`, `resend`, `hugging-face`, `agentation`, `build-web-apps`).
- Explore models, datasets, eval, and inference workflows with `hugging-face`.
- Build agent/runtime systems on edge/cloud with `cloudflare`, `aws`, and `vercel` skills.

### Broad project support
- Web frameworks/platforms: strong support via `vercel`, `netlify`, `build-web-apps`, `cloudflare`.
- Mobile: `build-ios-apps` (SwiftUI) and `test-android-apps` (emulator QA).
- Commerce: `medusa` and `saleor`.
- Productivity/workspace automation: `google-drive`, `gmail`, `google-calendar`, `slack`, `notion`, `box`, `linear`.

TODO: auto-generate top-skill and expandable hidden-skill blocks from plugin metadata/scripts.

## 2-minute setup

Clone and open the repo (any location is fine):

```bash
git clone https://github.com/openwebu/codex-plugins.git
cd codex-plugins
```

### Linux

```bash
bash scripts/install_linux.sh
```

### Windows (Git Bash)

```bash
bash scripts/install_windows.sh
```

## Check it worked

```bash
ls -l "$HOME/plugins"
ls -l "$HOME/.agents/plugins/marketplace.json"
scripts/sync_plugins_to_marketplace.py --dry-run
```

Expected:

- `~/plugins` points to this repo `plugins/`
- `~/.agents/plugins/marketplace.json` points to this repo marketplace

## Add your first plugin

```bash
bash scripts/new-plugin.sh my-plugin
```

This creates the plugin scaffold, syncs marketplace, and prints the exact `git add`, `git commit`, and `git push` commands.

## Need advanced options?

See [docs/setup-reference.md](docs/setup-reference.md) for:

- manual setup commands
- manual plugin creation flow
- repo structure and optional plugin surfaces
- troubleshooting notes

## Current plugin lineup

Live in this repo today, grouped by use case so you can find the right plugin and skills quickly.

TODO: auto-generate top-skill and expandable hidden-skill blocks from plugin metadata/scripts.

### Productivity

#### [`linear`](./plugins/linear)
Turn product requests into shipped work with issue triage and delivery workflows.
- Top skills: `linear`
- Skill count: `1`

#### [`google-calendar`](./plugins/google-calendar)
Plan smarter schedules, automate prep, and keep team calendars conflict-free.
- Top skills: `google-calendar`, `google-calendar-daily-brief`, `google-calendar-free-up-time`, `google-calendar-group-scheduler`
  <details>
  <summary>Show 1 more skills</summary>
  More skills: `google-calendar-meeting-prep`
  </details>
- Skill count: `5`

#### [`gmail`](./plugins/gmail)
Triage inboxes fast and draft high-quality replies with context-aware workflows.
- Top skills: `gmail`, `gmail-inbox-triage`
- Skill count: `2`

#### [`slack`](./plugins/slack)
Summarize channels, triage notifications, and ship clear outbound updates in seconds.
- Top skills: `slack`, `slack-channel-summarization`, `slack-daily-digest`, `slack-notification-triage`
  <details>
  <summary>Show 2 more skills</summary>
  More skills: `slack-outgoing-message`, `slack-reply-drafting`
  </details>
- Skill count: `6`

#### [`canva`](./plugins/canva)
Generate polished visual assets and social-ready variants without leaving the terminal.
- Top skills: `canva-branded-presentation`, `canva-resize-for-all-social-media`, `canva-translate-design`
- Skill count: `3`

#### [`figma`](./plugins/figma)
Bridge design and code with component generation, system rules, and rapid design ops.
- Top skills: `figma-code-connect-components`, `figma-create-design-system-rules`, `figma-create-new-file`, `figma-generate-design`
  <details>
  <summary>Show 3 more skills</summary>
  More skills: `figma-generate-library`, `figma-implement-design`, `figma-use`
  </details>
- Skill count: `7`

#### [`jam`](./plugins/jam)
Capture and structure bug feedback loops to accelerate debugging and product quality.
- Top skills: `coming soon`
- Skill count: `0` (plugin scaffold present, skill pack in progress)

#### [`box`](./plugins/box)
Automate secure file workflows and enterprise document operations at scale.
- Top skills: `box`
- Skill count: `1`

#### [`google-drive`](./plugins/google-drive)
Work across Docs, Sheets, and Drive assets with high-speed workspace automation.
- Top skills: `google-docs`, `google-drive`, `google-sheets`, `google-sheets-chart-builder`
  <details>
  <summary>Show 6 more skills</summary>
  More skills: `google-sheets-formula-builder`, `google-slides`, `google-slides-import-presentation`, `google-slides-template-migration`, `google-slides-template-surgery`, `google-slides-visual-iteration`
  </details>
- Skill count: `10`

#### [`notion`](./plugins/notion)
Capture knowledge, transform notes into specs, and operationalize docs workflows.
- Top skills: `notion-knowledge-capture`, `notion-meeting-intelligence`, `notion-research-documentation`, `notion-spec-to-implementation`
- Skill count: `4`

### Developer Workflows

#### [`github`](./plugins/github)
Run end-to-end repo operations: triage, CI fixes, review workflows, and PR publishing.
- Top skills: `gh-address-comments`, `gh-fix-ci`, `github`, `yeet`
- Skill count: `4`

#### [`build-ios-apps`](./plugins/build-ios-apps)
Design, refactor, and debug SwiftUI apps with simulator-aware engineering workflows.
- Top skills: `ios-debugger-agent`, `swiftui-liquid-glass`, `swiftui-performance-audit`, `swiftui-ui-patterns`
  <details>
  <summary>Show 1 more skills</summary>
  More skills: `swiftui-view-refactor`
  </details>
- Skill count: `5`

#### [`build-web-apps`](./plugins/build-web-apps)
Create high-impact web products with deployment, UI, data, and payments best practices.
- Top skills: `deploy-to-vercel`, `frontend-skill`, `react-best-practices`, `shadcn-best-practices`
  <details>
  <summary>Show 3 more skills</summary>
  More skills: `stripe-best-practices`, `supabase-best-practices`, `web-design-guidelines`
  </details>
- Skill count: `7`

#### [`test-android-apps`](./plugins/test-android-apps)
Automate Android app QA and emulator-driven validation for release confidence.
- Top skills: `android-emulator-qa`
- Skill count: `1`

#### [`superpowers`](./plugins/superpowers)
Advanced engineering execution skills for planning, debugging, reviews, and delivery.
- Top skills: `brainstorming`, `dispatching-parallel-agents`, `executing-plans`, `finishing-a-development-branch`
  <details>
  <summary>Show 10 more skills</summary>
  More skills: `receiving-code-review`, `requesting-code-review`, `subagent-driven-development`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `using-superpowers`, `verification-before-completion`, `writing-plans`, `writing-skills`
  </details>
- Skill count: `14`

#### [`game-studio`](./plugins/game-studio)
Prototype, playtest, and ship engaging game experiences across 2D/3D web stacks.
- Top skills: `game-playtest`, `game-studio`, `game-ui-frontend`, `phaser-2d-game`
  <details>
  <summary>Show 5 more skills</summary>
  More skills: `react-three-fiber-game`, `sprite-pipeline`, `three-webgl-game`, `web-3d-asset-pipeline`, `web-game-foundations`
  </details>
- Skill count: `9`

#### [`saleor`](./plugins/saleor)
Accelerate Saleor storefront architecture with practical, implementation-ready guidance.
- Top skills: `saleor-paper-storefront`
- Skill count: `1`

#### [`medusa`](./plugins/medusa)
Build and extend commerce backends, storefronts, and admin customizations with speed.
- Top skills: `building-admin-dashboard-customizations`, `building-storefronts`, `building-with-medusa`, `db-generate`
  <details>
  <summary>Show 4 more skills</summary>
  More skills: `db-migrate`, `learning-medusa`, `new-user`, `storefront-best-practices`
  </details>
- Skill count: `8`

#### [`agentation`](./plugins/agentation)
Add annotation-driven agent feedback loops directly into React product workflows.
- Top skills: `agentation`
- Skill count: `1`

### Platform & Infrastructure

#### [`vercel`](./plugins/vercel)
Ship full-stack apps faster with deep support for deploys, AI, observability, and infra.
- Top skills: `agent-browser`, `agent-browser-verify`, `ai-elements`, `ai-gateway`
  <details>
  <summary>Show 43 more skills</summary>
  More skills: `ai-generation-persistence`, `ai-sdk`, `auth`, `bootstrap`, `chat-sdk`, `cms`, `cron-jobs`, `deployments-cicd`, `email`, `env-vars`, `geist`, `geistdocs`, `investigation-mode`, `json-render`, `marketplace`, `micro`, `ncc`, `next-forge`, `nextjs`, `observability`, `payments`, `react-best-practices`, `routing-middleware`, `runtime-cache`, `satori`, `shadcn`, `sign-in-with-vercel`, `swr`, `turbopack`, `turborepo`, `v0-dev`, `vercel-agent`, `vercel-api`, `vercel-cli`, `vercel-firewall`, `vercel-flags`, `vercel-functions`, `vercel-queues`, `vercel-sandbox`, `vercel-services`, `vercel-storage`, `verification`, `workflow`
  </details>
- Skill count: `47`

#### [`netlify`](./plugins/netlify)
Deploy and operate modern web projects with streamlined Netlify-focused automation.
- Top skills: `netlify-deploy`
- Skill count: `1`

#### [`stripe`](./plugins/stripe)
Build safer payment flows, upgrades, and integration decisions with battle-tested patterns.
- Top skills: `stripe-best-practices`, `upgrade-stripe`
- Skill count: `2`

#### [`cloudflare`](./plugins/cloudflare)
Build edge-native apps, agents, workers, and durable systems on Cloudflare.
- Top skills: `agents-sdk`, `building-ai-agent-on-cloudflare`, `building-mcp-server-on-cloudflare`, `cloudflare`
  <details>
  <summary>Show 5 more skills</summary>
  More skills: `durable-objects`, `sandbox-sdk`, `web-perf`, `workers-best-practices`, `wrangler`
  </details>
- Skill count: `9`

#### [`sentry`](./plugins/sentry)
Inspect real production issues and prioritize fixes with error-first operational visibility.
- Top skills: `sentry`
- Skill count: `1`

#### [`aws`](./plugins/aws)
Design and operate secure AWS architectures, including OpenAI-powered workloads.
- Top skills: `aws-openai-workflow`, `aws-workflow`
- Skill count: `2`

#### [`supabase`](./plugins/supabase)
Stand up and run Supabase projects with CLI-first setup and usage workflows.
- Top skills: `cli`, `setup`, `supabase-usage`
- Skill count: `3`

#### [`resend`](./plugins/resend)
Operationalize email delivery from local dev to CI pipelines with Resend-native tooling.
- Top skills: `resend-cli`
- Skill count: `1`

#### [`hugging-face`](./plugins/hugging-face)
Production toolkit for model discovery, datasets, evals, Spaces, and inference flows.
- Top skills: `cli`, `community-evals`, `datasets`, `gradio`
  <details>
  <summary>Show 7 more skills</summary>
  More skills: `jobs`, `llm-trainer`, `paper-publisher`, `papers`, `trackio`, `transformers.js`, `vision-trainer`
  </details>
- Skill count: `11`

## License

MIT
