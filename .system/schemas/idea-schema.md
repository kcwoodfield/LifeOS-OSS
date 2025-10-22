# Idea Schema

Template for idea frontmatter in `projects/_ideas.md` or individual idea files.

```yaml
---
idea_id: "unique-slug-or-uuid"
title: "Descriptive title"
status: "new"  # new | considering | ready | paused | completed | rejected
priority: "medium"  # high | medium | low
effort: "M"  # S | M | L | XL
category: "lifeos-infra"  # lifeos-infra | side-project | learning
created: 2025-10-16
updated: 2025-10-16
value_proposition: "What value does this create?"
tags:
  - tag1
  - tag2
---
```

## Field Definitions

**idea_id** (required, string)
- Unique identifier (kebab-case slug or UUID)
- Example: `voice-interface-lifeos`, `calendar-integration`

**title** (required, string)
- Human-readable title
- Example: "Voice Interface for LifeOS"

**status** (required, enum)
- `new` - Just captured, needs evaluation
- `considering` - Evaluating feasibility and value
- `ready` - Scoped and ready to start
- `paused` - Started but on hold
- `completed` - Shipped/built
- `rejected` - Decided not to pursue

**priority** (optional, enum)
- `high` - Significant impact, aligned with goals
- `medium` - Good idea, not urgent
- `low` - Nice to have, low priority
- Only set when status is `ready`

**effort** (optional, enum)
- `S` - Small (few hours)
- `M` - Medium (few days)
- `L` - Large (few weeks)
- `XL` - Extra Large (months)

**category** (required, enum)
- `lifeos-infra` - LifeOS infrastructure and automation
- `side-project` - Revenue-generating projects or tools
- `learning` - Learning experiments and skill development

**created** (required, date)
- Date idea was first captured (YYYY-MM-DD)

**updated** (required, date)
- Date frontmatter was last updated (YYYY-MM-DD)

**value_proposition** (optional, string)
- Brief description of value this idea creates
- Example: "Reduces friction in morning routine"

**tags** (optional, array)
- Free-form tags for categorization
- Example: `[automation, email, morning-routine]`

## Example

```yaml
---
idea_id: "morning-brief-email"
title: "Morning Brief Email Delivery"
status: "considering"
priority: "medium"
effort: "M"
category: "lifeos-infra"
created: 2025-10-16
updated: 2025-10-16
value_proposition: "Frictionless delivery of daily brief to inbox"
tags:
  - automation
  - email
  - morning-routine
---
```
