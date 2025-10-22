# Task Schema

**Purpose:** Frontmatter schema for individual task files in `tasks/` directory.

**Last Updated:** 2025-10-17

---

## Frontmatter Template

```yaml
---
# Core Fields (Required)
task_id: "TASK-001"              # Unique ID (TASK-XXX format)
title: "Task title"              # Brief description
status: "backlog"                # backlog|todo|in-progress|blocked|review|done|cancelled
project: "minerva"               # Project tag (lowercase)

# Priority & Sizing
priority: "medium"               # critical|high|medium|low
effort: "medium"                 # small|medium|large|xlarge
impact: "high"                   # high|medium|low

# Dates
created: 2025-10-17             # Creation date (auto)
updated: 2025-10-17             # Last modified (auto)
due_date: 2025-10-25            # Target completion
completed_date:                 # Completion date (when done)

# Assignment
assignee: "User"               # Who's responsible
team:                           # Team/domain (optional)

# Relationships (Jira-like)
parent_task:                    # Parent task ID (for sub-tasks)
blocked_by: []                  # Array of blocking task IDs
blocks: []                      # Array of tasks this blocks
related_tasks: []               # Related task IDs

# Kanban Integration
kanban_lane: "backlog"          # Which column: backlog|todo|in-progress|done
kanban_board: "master"          # Which board: master|minerva|blog|voice

# Metadata
domain: "wealth"                # career|wealth|art|operations|personal|health|social
tags: [research, interviews]    # Category tags
sprint:                         # Sprint/milestone name
epic:                           # Epic/theme

# Custom Fields
acceptance_criteria: []         # List of done criteria
notes:                          # Additional context
---
```

---

## Field Descriptions

### Required Fields

**task_id** (string)
- Unique identifier for the task
- Use kebab-case: "write-blog-post-minerva"
- Should match filename

**status** (enum)
- `todo` - Not started
- `in-progress` - Currently working on
- `done` - Completed
- `blocked` - Can't proceed (waiting on something)

**priority** (enum)
- `high` - Important and urgent
- `medium` - Important but not urgent
- `low` - Nice to have

**domain** (enum)
- `career` - Work-related tasks
- `wealth` - Side projects, financial tasks
- `art` - Art practice tasks
- `operations` - Life admin, systems work
- `personal` - Personal errands, life tasks
- `health` - Health, fitness, wellness
- `social` - Relationships, social connection

**created** (date: YYYY-MM-DD)
- Date task was created

**updated** (date: YYYY-MM-DD)
- Last time task was modified

---

### Optional Fields

**project** (wiki-link)
- Link to related project: `[[minerva]]`
- Leave blank if not project-specific

**due_date** (date: YYYY-MM-DD)
- When task must be completed
- Only use for actual deadlines (not aspirational)

**effort** (string)
- Estimated time to complete
- Options: `15m`, `30m`, `1h`, `2h`, `4h`, `8h`, `1d`, `1w`
- Helps with capacity planning

**blocked_by** (string)
- What's preventing this task from progressing
- Example: "Waiting on design feedback", "Need to research options first"

**tags** (array)
- Additional categorization
- Examples: `[coding, writing, research, meeting, decision]`

---

## File Naming Convention

**Pattern:** `task-name.md`

**Examples:**
- `write-minerva-blog-post.md`
- `quarterly-review-2025-q4.md`
- `fix-project-health-dashboard.md`
- `research-blog-platforms.md`

**Guidelines:**
- Use kebab-case (lowercase, hyphens)
- Be specific but concise
- Task name should be clear action

---

## Task File Structure

```markdown
---
task_id: "example-task"
status: "todo"
priority: "medium"
project: "[[minerva]]"
domain: "wealth"
due_date: 2025-11-01
effort: "2h"
created: 2025-10-17
updated: 2025-10-17
tags: [coding, research]
---

# Task: Example Task Name

## Description

[What needs to be done? Be specific.]

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Context

[Any additional context, links, notes]

## Blockers

[What's preventing this? Leave blank if none]

## Notes

[Work log, decisions made, etc.]

---

**Created:** 2025-10-17
**Status:** Todo
**Next Action:** [Specific next step]
```

---

## Status Workflow

```
todo → in-progress → done
   ↓
blocked → (resolve blocker) → in-progress → done
```

**Transitions:**
- **todo → in-progress:** When you start working
- **in-progress → done:** When complete
- **any → blocked:** When you can't proceed
- **blocked → todo:** When blocker is resolved but not yet restarted
- **blocked → in-progress:** When blocker is resolved and work resumes

---

## Priority Guidelines

### High Priority
- Time-sensitive deadlines
- Blocks other work
- High impact on goals
- **Limit:** Max 3-5 high-priority tasks at once

### Medium Priority
- Important but not urgent
- Supports goals but not critical
- Can be scheduled flexibly
- **Most tasks should be here**

### Low Priority
- Nice to have
- Low impact
- Can be deferred indefinitely
- **Consider:** Is this actually worth doing?

---

## Effort Estimates

**15m:** Quick tasks (send email, schedule meeting)
**30m:** Small tasks (review document, quick research)
**1h:** Standard tasks (draft outline, initial implementation)
**2h:** Larger tasks (write blog post, design mockup)
**4h:** Half-day tasks (deep work session, comprehensive research)
**8h:** Full-day tasks (ship feature, write comprehensive guide)
**1d+:** Multi-day tasks (consider breaking down into smaller tasks)

**Rule:** If task is >4 hours, consider breaking into subtasks

---

## Task Lifecycle

### Daily
- Review `status = "in-progress"` tasks
- Pick 1-3 tasks for today (Top 3 priorities)
- Update status as you work
- Mark tasks `done` when complete

### Weekly
- Review all `todo` tasks
- Prioritize for coming week
- Resolve or document `blocked` tasks
- Archive completed tasks (move to archive/ or delete)

### Monthly
- Review task velocity (how many done?)
- Assess priority accuracy (were high-priority tasks actually important?)
- Clean up stale tasks (delete or convert to ideas)

---

## Integration with Projects

**Project Tasks:**
- Link to project via `project: [[project-name]]`
- Project-specific tasks support project milestones
- Query by project in dashboards

**Standalone Tasks:**
- Not tied to specific project
- Still categorized by domain
- Examples: "Schedule dentist", "Review quarterly goals", "Update weekly review"

---

## Integration with Daily Reviews

**Daily Top 3:**
- Daily review template references top tasks
- Tasks with `due_date = today` auto-surface
- High-priority in-progress tasks are visible

**Completion Tracking:**
- Daily review can query `done` tasks for wins
- Track task completion rate over time

---

## Tips for Effective Task Management

1. **Be Specific:** "Write blog post" → "Draft outline for Project Alpha blog post"
2. **Actionable:** Start with verb (Write, Research, Fix, Review, Schedule)
3. **Right-Sized:** Tasks should be completable in one session
4. **Don't Overload:** If >20 active tasks, you're overcommitted
5. **Review Regularly:** Weekly task review keeps system clean
6. **Archive Completed:** Don't let done tasks clutter active list

---

## Common Patterns

### Recurring Tasks
- Create new task file each time (e.g., `weekly-review-2025-W42.md`)
- Or use single task file, update `updated` date when done
- Decide: One-time vs. recurring pattern

### Task Dependencies
- Use `blocked_by` field to note dependencies
- Link to blocking task if it exists: `blocked_by: "[[setup-development-environment]]"`

### Research Tasks
- When research is needed before action
- `status: in-progress`, tag: `[research]`
- Document findings in task file
- Convert to action task when research complete

---

**See Also:**
- [[schemas/idea-schema]] - Ideas backlog
- [[schemas/project-schema]] - Project tracking
- [[schemas/review-schema]] - Daily/weekly/monthly reviews

---

*Tasks are captured work. Ideas are potential work. Projects are structured work. Know which is which.*
