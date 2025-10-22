# LifeOS Frontmatter Schemas

**Last Updated:** 2025-10-16

This directory contains frontmatter schema definitions for all structured data in LifeOS. These schemas enable Dataview queries and transform markdown into a queryable database.

---

## Available Schemas

### 📋 [Idea Schema](idea-schema.md)
For tracking ideas in `projects/_ideas.md` or individual idea files.

**Key fields:** `status`, `priority`, `effort`, `category`

**Use for:**
- Ideas backlog management
- Filtering by status (new, considering, ready, completed)
- Prioritization and effort estimation

---

### 🎯 [Project Schema](project-schema.md)
For tracking projects in `projects/INDEX.md` or PRD files in `projects/prds/`.

**Key fields:** `status`, `health`, `priority`, `velocity`, `blockers`

**Use for:**
- Project health monitoring
- Velocity tracking
- Blocker identification
- Time allocation (effort_hours)

---

### 📝 [Review Schema](review-schema.md)
For daily, weekly, and monthly reviews in `reviews/` directory.

**Key fields:** `review_type`, `energy_level`, `focus_time_hours`, `domains_active`, `wins`, `learnings`

**Use for:**
- Energy and productivity trend analysis
- Domain balance tracking (career, wealth, art, etc.)
- Historical wins and learnings
- Weekly/monthly velocity

---

## How to Use These Schemas

### 1. Add Frontmatter to Files

At the top of any markdown file, add YAML frontmatter between `---` delimiters:

```markdown
---
idea_id: "voice-interface"
title: "Voice Interface for LifeOS"
status: "considering"
priority: "high"
effort: "M"
category: "lifeos-infra"
created: 2025-10-16
updated: 2025-10-16
---

# Voice Interface for LifeOS

Rest of your markdown content...
```

### 2. Query with Dataview

In any markdown file, create a Dataview query code block:

````markdown
```dataview
TABLE status, priority, effort
FROM "projects"
WHERE category = "lifeos-infra"
AND status != "completed"
SORT priority DESC
```
````

This renders as a live-updating table.

### 3. Create Dashboard Pages

Create files in `dashboards/` directory with multiple Dataview queries:

```markdown
# Ideas Dashboard

## 🔴 High Priority - Ready to Start

\```dataview
LIST
FROM "projects"
WHERE idea_id
AND status = "ready"
AND priority = "high"
\```

## 🤔 Currently Considering

\```dataview
TABLE effort, value_proposition
FROM "projects"
WHERE idea_id
AND status = "considering"
SORT updated DESC
\```
```

---

## Schema Design Principles

### Required vs Optional Fields

**Always required:**
- ID fields (`idea_id`, `project_id`)
- Title
- Status
- Dates (created, updated)

**Optional but recommended:**
- Priority (only when status = "ready")
- Effort estimates
- Tags

**Truly optional:**
- Descriptive fields (value_proposition, notes)
- Relationship fields (blockers, dependencies)

### Date Format

All dates use **ISO 8601** format: `YYYY-MM-DD`

Examples:
- `2025-10-16`
- `2025-12-31`

### Enum Values

Always use exact enum values (case-sensitive):

✅ Correct:
```yaml
status: "active"
priority: "high"
```

❌ Wrong:
```yaml
status: "Active"  # Wrong case
priority: "HIGH"  # Wrong case
```

### Array Format

Use YAML array syntax:

```yaml
tags:
  - automation
  - email
blockers:
  - "Waiting on API access"
  - "Design feedback needed"
```

---

## Validation

### Manual Validation
Before committing, check:
1. YAML syntax is valid (no unclosed quotes, proper indentation)
2. Enum values match schema exactly
3. Dates are in YYYY-MM-DD format
4. Required fields are present

### Automated Validation (coming soon)
- Obsidian Linter plugin (YAML validation on save)
- Pre-commit hook (validate all frontmatter before commit)
- Dataview query test suite (ensure queries don't break)

---

## Migration Strategy

### Phase 1: New Files Only
- Use templates (Templater plugin) to auto-populate frontmatter for new files
- Don't worry about backfilling old files yet

### Phase 2: Backfill High-Value Files
- Add frontmatter to active projects in `INDEX.md`
- Add frontmatter to ideas in `_ideas.md`
- Add frontmatter to recent reviews (last 4 weeks)

### Phase 3: Complete Backfill
- Add frontmatter to all historical reviews
- Add frontmatter to all completed projects
- Add frontmatter to context files (for versioning)

---

## Querying Tips

### Basic Query Structure

```dataview
TABLE field1, field2, field3
FROM "folder"
WHERE condition
SORT field DESC
LIMIT 10
```

### Common Filters

**Active projects:**
```
WHERE status = "active"
```

**High priority items:**
```
WHERE priority = "high"
```

**Blocked projects:**
```
WHERE health = "blocked"
```

**Last 7 days:**
```
WHERE date >= date(today) - dur(7 days)
```

**Multiple conditions:**
```
WHERE status = "active"
AND priority = "primary"
AND health != "healthy"
```

### Useful Functions

**Count items:**
```dataview
TABLE length(rows) as "Count"
FROM "projects"
WHERE status = "active"
GROUP BY priority
```

**Sum hours:**
```dataview
TABLE sum(rows.effort_hours) as "Total Hours"
FROM "projects"
WHERE status = "active"
```

**Calculate average:**
```dataview
TABLE round(average(rows.energy_level), 1) as "Avg Energy"
FROM "reviews/weekly"
WHERE review_type = "weekly"
```

---

## Schema Versioning

Schemas will evolve over time. When making breaking changes:

1. **Document the change** in schema file
2. **Add migration notes** to this README
3. **Update existing frontmatter** (bulk find/replace or script)
4. **Test all queries** in dashboards

### Version History

**v1.0 (2025-10-16):** Initial schema definitions
- Idea schema
- Project schema
- Review schema (daily, weekly, monthly)

---

## Resources

**Dataview Documentation:**
- Official docs: https://blacksmithgu.github.io/obsidian-dataview/
- Query reference: https://blacksmithgu.github.io/obsidian-dataview/queries/structure/
- Functions: https://blacksmithgu.github.io/obsidian-dataview/reference/functions/

**YAML Syntax:**
- YAML spec: https://yaml.org/spec/1.2/spec.html
- Quick reference: https://quickref.me/yaml

**Obsidian:**
- Frontmatter guide: https://help.obsidian.md/Editing+and+formatting/Properties
- Dataview plugin: https://github.com/blacksmithgu/obsidian-dataview

---

## Questions?

When uncertain about schema design:
- **Keep it simple** - Add fields only when you'll query them
- **Be consistent** - Use the same field names across similar entities
- **Stay portable** - Standard YAML that works outside Obsidian too
- **Document it** - If you add a custom field, document it in the schema file

---

*These schemas are living documents. Update as LifeOS evolves.*
