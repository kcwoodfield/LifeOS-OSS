# Project Schema

Template for project frontmatter in `projects/INDEX.md` or individual project PRD files.

```yaml
---
project_id: "project-slug"
title: "Project Title"
status: "active"  # ideation | planning | active | maintenance | paused | completed
health: "healthy"  # healthy | at-risk | blocked
priority: "primary"  # primary | secondary | maintenance
velocity: "medium"  # high | medium | low | stalled
effort_hours: 5  # Weekly hours allocated
started: 2025-10-16
target_completion: 2025-12-31
blockers: []
tags:
  - tag1
  - tag2
---
```

## Field Definitions

**project_id** (required, string)
- Unique identifier (kebab-case slug)
- Example: `yourproject-ai-assistant`, `project-b-viz`, `personal-blog`

**title** (required, string)
- Human-readable project name
- Example: "Project Alpha - AI Research Assistant"

**status** (required, enum)
- `ideation` - Exploring the idea, not committed yet
- `planning` - Committed, planning architecture/scope
- `active` - Actively building and shipping
- `maintenance` - Shipped, ongoing improvements
- `paused` - Temporarily on hold
- `completed` - Shipped and no longer actively developed

**health** (required, enum)
- `healthy` - 🟢 On track, no blockers, making progress
- `at-risk` - 🟡 Minor issues, slower progress, needs attention
- `blocked` - 🔴 Critical blocker preventing progress

**priority** (required, enum)
- `primary` - Top priority, primary focus project (limit 1-2)
- `secondary` - Active but not primary focus (limit 2-3)
- `maintenance` - Keeping alive, minimal time investment

**velocity** (optional, enum)
- `high` - Shipping multiple times per week
- `medium` - Steady progress, shipping weekly
- `low` - Slow progress, shipping monthly
- `stalled` - No recent progress

**effort_hours** (optional, number)
- Weekly hours allocated to this project
- Example: `5` for primary project, `2` for secondary

**started** (required, date)
- Date project work began (YYYY-MM-DD)

**target_completion** (optional, date)
- Target launch/completion date (YYYY-MM-DD)
- Can be null for ongoing projects

**blockers** (optional, array)
- List of current blockers preventing progress
- Example: `["Waiting on API access", "Design feedback needed"]`
- Empty array if no blockers

**tags** (optional, array)
- Free-form tags for categorization
- Example: `[ai, side-project, revenue]`

## Example

```yaml
---
project_id: "yourproject-ai-assistant"
title: "Project Alpha - AI Research Assistant"
status: "active"
health: "at-risk"
priority: "primary"
velocity: "low"
effort_hours: 8
started: 2025-09-15
target_completion: 2025-11-30
blockers:
  - "RAG implementation needs optimization"
  - "UI/UX design not finalized"
tags:
  - ai
  - side-project
  - revenue
  - python
---
```

## PRD File Frontmatter

For PRD files in `projects/prds/`, use the same schema but add:

```yaml
prd_version: "1.0"
last_reviewed: 2025-10-16
stakeholders:
  - User
  - Atlas
  - Engineer
```
