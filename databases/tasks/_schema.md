# Task Schema Template

Use this frontmatter structure for all task files in `databases/tasks/`.

```yaml
---
title: "Task title goes here"
status: backlog              # backlog | todo | in-progress | blocked | done
priority: medium             # high | medium | low
project: null                # [[Project Name]] or null
due_date: null               # YYYY-MM-DD or null
effort: M                    # S | M | L | XL
assigned_to: User
dependencies: []             # Links to blocking tasks: [[task-name]]
tags: []
created: 2025-10-19
updated: 2025-10-19
---

# Task Description

Brief description of what needs to be done.

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Notes

Any additional context, links, or information.
```

## Field Definitions

### Required Fields

**title** (string)
- Clear, action-oriented description
- Examples: "Fix login bug", "Implement user dashboard", "Review pull request #123"

**status** (enum)
- `backlog` - Not yet started, in backlog
- `todo` - Ready to start, prioritized
- `in-progress` - Currently working on
- `blocked` - Waiting on dependency or blocker
- `done` - Completed

**created** (date)
- Auto-filled by template: YYYY-MM-DD
- Used for sorting and metrics

### Optional Fields

**priority** (enum)
- `high` - Must ship today/this week, blocking others
- `medium` - Important but not urgent (default)
- `low` - Nice to have, background work

**project** (link or null)
- Link to parent project: `[[Project Name]]`
- Can link to PRD: `[[projects/prds/yourproject]]`
- Or null if standalone task

**due_date** (date or null)
- Target completion date: YYYY-MM-DD
- Null if no specific deadline

**effort** (enum)
- `S` (Small): < 2 hours
- `M` (Medium): 2-4 hours (default)
- `L` (Large): 1-2 days
- `XL` (Extra Large): 3+ days (consider breaking down)

**assigned_to** (string)
- Person responsible
- Default: User
- For team tasks, specify team member

**dependencies** (array)
- Links to tasks that must complete first
- Format: `["[[task-1]]", "[[task-2]]"]`
- Empty array `[]` if no dependencies

**tags** (array)
- Free-form categorization
- Examples: `[bug, frontend, urgent]`
- Empty array `[]` if no tags

**updated** (date)
- Last modified date: YYYY-MM-DD
- Update when status changes or significant edits

## Example Task

```yaml
---
title: "Implement newsletter automation"
status: in-progress
priority: high
project: [[projects/prds/newsletter-system]]
due_date: 2025-10-20
effort: L
assigned_to: User
dependencies: []
tags: [automation, email, productivity]
created: 2025-10-19
updated: 2025-10-19
---

# Implement Newsletter Automation

Create automated system to send morning brief via email, reducing time spent checking apps.

## Acceptance Criteria

- [ ] Python script sends email with morning brief content
- [ ] Email formatted correctly (HTML + plain text)
- [ ] Scheduled to run at 6:00 AM daily
- [ ] Error handling and logging implemented
- [ ] Tested with real data

## Notes

- Use SendGrid API for email delivery
- Pull content from morning brief generation script
- Consider adding unsubscribe link (even though it's just for me)
```

---

**See:** `databases/tasks/README.md` for usage guide and workflow
