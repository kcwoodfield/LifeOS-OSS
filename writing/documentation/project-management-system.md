# LifeOS Project Management System

**A hybrid approach combining Bases, Kanban, and Tasks**

---

## Overview

LifeOS uses a three-tier project management system:

1. **Bases** - Structured project tracking with properties and views
2. **Kanban** - Visual workflow management for sprints and phases
3. **Tasks** - Daily task management with due dates and priorities

This combines the best of database-driven project tracking (Bases), visual workflow (Kanban), and GTD-style task management (Tasks).

---

## Architecture

```
Projects (High-Level Strategy)
    ↓
  Bases: projects.base
  - Track all projects
  - Properties: status, health, priority, velocity
  - Views: Active, Blocked, All
    ↓
Kanban Boards (Tactical Execution)
    ↓
  Master Kanban: projects/master-kanban.md
  - Backlog → To Do → In Progress → Done
  - Cross-project view
    ↓
  Project Kanbans (per-project):
  - minerva-kanban.md (Primary focus)
  - blog-kanban.md
  - voice-assistant-kanban.md
    ↓
Daily Tasks (Operational)
    ↓
  Tasks Plugin: reviews/daily/YYYY-MM-DD.md
  - Top 3 priorities
  - Due dates, priorities, tags
  - Task queries (overdue, due today, high priority)
```

---

## 1. Bases: Project Database

### File: `projects/projects.base`

**Purpose:** Single source of truth for all project metadata

**Views:**

1. **Active Projects** - Currently in progress
   - Filters: status in [Active, Ideation, Prototyping, Planning]
   - Columns: Project, Priority, Health, Velocity, Progress, Hours/Week, Next Milestone
   - Sort: By priority

2. **All Projects** - Complete history
   - No filters
   - Columns: Project, Status, Priority, Health, Started, Target
   - Sort: By start date (newest first)

3. **Blocked / At-Risk** - Needs attention
   - Filters: health in [red, yellow, at-risk, blocked]
   - Columns: Project, Health, Blockers, Hours/Week
   - Sort: By health (worst first)

**How to Use:**

1. Open `projects/projects.base` in Obsidian
2. Switch between views (Active, All, Blocked)
3. Click any project to open its PRD
4. Edit properties inline (double-click cells)
5. Filter, sort, and bulk-edit as needed

**Benefits:**
- See all projects at a glance
- Quick health checks (red/yellow/green)
- Identify blockers immediately
- Track time allocation across projects

---

## 2. Kanban Boards: Visual Workflow

### Master Kanban: `projects/master-kanban.md`

**Purpose:** Cross-project tactical view for current sprint

**Columns:**
- **Backlog** - Ideas and future tasks
- **To Do** - Ready to start this week/sprint
- **In Progress** - Currently working on (limit: 2-3 items)
- **Done** - Completed (archive weekly)

**Task Format:**
```markdown
- [ ] Task description #project-tag #priority
- [ ] Task with due date ⏰ 2025-11-15 #project
```

**How to Use:**

1. Open `projects/master-kanban.md`
2. Drag cards between columns
3. Add new tasks with tags (#minerva, #blog, #voice-assistant)
4. Mark done with `[x]` or drag to Done column
5. Archive Done column weekly (move to review notes)

**Best Practices:**
- Limit In Progress to 2-3 items (focus!)
- Review Backlog weekly, pull into To Do
- Tag all tasks with project and priority
- Archive Done items weekly to daily reviews

### Project-Specific Kanbans

**Project Alpha Kanban:** `projects/minerva-kanban.md`

**Columns:**
- 📋 Backlog
- 🎯 Validation Phase (Current)
- 💬 Interviewing
- 📊 Analysis
- ✅ Completed

**Purpose:** Track Project Alpha validation phase with specific workflow

**Other Project Kanbans:**
- `blog-kanban.md` - Content pipeline (Ideation → Drafting → Editing → Published)
- `voice-assistant-kanban.md` - Feature development
- Create more as needed per active project

---

## 3. Tasks: Daily Execution

### Template: `templates/daily-tasks.md`

**Purpose:** Daily task list with GTD-style task management

**Sections:**

1. **🎯 Top 3 Priorities** - Most important tasks for today
   - Use ⏫ emoji for high priority
   - Add due dates with 📅 YYYY-MM-DD

2. **📧 Communications** - Email, Slack, messages

3. **🏢 Day Job** - Full-time work tasks

4. **💼 Side Projects** - Project Alpha, Blog, Voice Assistant tasks

5. **🎨 Art Practice** - Daily non-negotiable anchor

6. **🐕 your pet Care** - Dog care checklist

7. **📝 Admin** - Life operations

**Task Syntax (Tasks Plugin):**

```markdown
- [ ] Task description 📅 2025-10-18 ⏫ #project-tag
- [ ] Task with due date 📅 2025-10-20
- [ ] High priority ⏫
- [ ] Medium priority 🔼
- [ ] Low priority 🔽
- [ ] Recurring task 🔁 every week
```

**Task Queries:**

The template includes three dynamic queries:

1. **Overdue Tasks** - Anything past due date
2. **Due Today** - Tasks due today
3. **High Priority** - All high-priority tasks

**How to Use:**

1. Create daily note from template
2. Fill in Top 3 Priorities
3. Add tasks to relevant sections
4. Use checkboxes to mark complete
5. Task queries automatically show relevant tasks from ALL notes

---

## Workflow: How They Work Together

### Weekly Planning (Sunday Evening)

1. **Review Bases** (`projects/projects.base`)
   - Check Active Projects view
   - Update project health
   - Identify blockers
   - Adjust time allocation

2. **Update Master Kanban** (`projects/master-kanban.md`)
   - Archive last week's Done items
   - Pull new items from Backlog to To Do
   - Limit In Progress to 2-3 items
   - Ensure tasks aligned with project priorities

3. **Review Project Kanbans**
   - Update Project Alpha kanban with interview progress
   - Check blog content pipeline
   - Move voice assistant features through workflow

### Daily Planning (Morning)

1. **Create daily note** from `templates/daily-tasks.md`

2. **Set Top 3 Priorities**
   - Pull from Master Kanban "In Progress"
   - Add due dates and priority markers
   - Ensure alignment with weekly goals

3. **Check Task Queries**
   - Review overdue tasks
   - See what's due today
   - Address high-priority items first

### Daily Execution

1. **Work from Top 3** - Focus on priorities first

2. **Update Kanban** - Move cards as you complete work

3. **Check off tasks** - Mark complete in daily note

### Evening Review

1. **Archive completed tasks** - Move done items to Done column

2. **Plan tomorrow** - Set Top 3 for next day

3. **Update project health** - If status changed, update Bases

---

## File Locations

```
LifeOS/
├── projects/
│   ├── projects.base              # Project database (Bases)
│   ├── master-kanban.md           # Master Kanban board
│   ├── minerva-kanban.md          # Project Alpha project Kanban
│   ├── blog-kanban.md             # Blog content pipeline
│   └── voice-assistant-kanban.md  # Voice assistant features
├── templates/
│   └── daily-tasks.md             # Daily task template
└── reviews/
    └── daily/
        └── YYYY-MM-DD.md          # Daily notes with tasks
```

---

## Task Priority System

Use emoji markers for visual priority:

- **⏫ High Priority** - Must do today, blocks other work
- **🔼 Medium Priority** - Should do this week
- **🔽 Low Priority** - Nice to have, can defer

**Priority Rules:**
1. Top 3 daily priorities should be ⏫ high priority
2. Limit ⏫ tasks to 3-5 per day (can't all be urgent)
3. Review 🔽 low priority monthly - delete or promote

---

## Tags System

Use consistent tags across all systems:

**Project Tags:**
- `#minerva` - Project Alpha AI Research Assistant
- `#blog` - Personal blog and portfolio
- `#voice-assistant` - Voice-activated Cabinet
- `#obsidian` - LifeOS infrastructure
- `#histomap` - Interactive timeline (paused)
- `#okami` - Japanese art tool (paused)

**Context Tags:**
- `#day-job` - Full-time work
- `#art` - Art practice
- `#lobo` - Dog care
- `#admin` - Life operations
- `#learning` - Courses, books, tutorials

**Priority Tags:**
- `#p1` - Primary focus (revenue path)
- `#p2` - Secondary focus
- `#p3` - Maintenance

---

## Best Practices

### Bases
- Update project health weekly during Cabinet meeting
- Review Blocked/At-Risk view daily
- Adjust time allocation based on actual hours worked
- Archive completed projects to keep Active view clean

### Kanban
- **Limit WIP** - Max 2-3 items in In Progress
- **Archive weekly** - Move Done items to weekly review
- **Tag everything** - Use consistent project tags
- **Use due dates** - Add ⏰ YYYY-MM-DD for deadlines
- **Be specific** - "Write blog post" → "Write blog post: Voice Assistant Architecture"

### Tasks
- **Top 3 rule** - Only 3 high-priority items per day
- **Due dates matter** - Use them or don't, but be consistent
- **Review overdue daily** - Don't let them pile up
- **Defer low priority** - Move to Backlog if not started in 2 weeks
- **Recurring tasks** - Use 🔁 for habits (art practice, your pet care)

---

## Troubleshooting

### "I have too many tasks in In Progress"
→ Limit to 2-3 items. Move others back to To Do.

### "Overdue tasks keep piling up"
→ Either do them, defer them, or delete them. Decide daily.

### "My Kanban board is a mess"
→ Archive Done items weekly. Be ruthless with Backlog pruning.

### "I'm not using task queries"
→ That's fine! They're optional. Use if helpful, ignore if not.

### "Project health is always yellow/red"
→ You're overcommitted. Pause a project. Update time allocation in Bases.

---

## Integration with LifeOS

### Morning Brief
- Includes Top 3 priorities from daily task note
- Checks overdue tasks
- Reviews In Progress items from Master Kanban

### Cabinet Meetings
- Atlas reviews Master Kanban (focus, WIP limit)
- Bases provides project health data
- Agents comment on blockers and priorities

### Weekly Reviews
- Archive Master Kanban Done column
- Update all project health in Bases
- Plan next week's To Do items
- Review time allocation vs actual

### Daily Reviews
- Complete daily task note
- Note wins (what got done)
- Note learnings (what to improve)
- Plan tomorrow's Top 3

---

## Keyboard Shortcuts (Obsidian)

**Kanban Plugin:**
- `Cmd/Ctrl + Enter` - Create new card
- Drag and drop - Move cards between columns
- `x` - Mark card complete

**Tasks Plugin:**
- `Cmd/Ctrl + Enter` - Toggle task complete
- Type `- [ ]` - Create task
- Type `📅` - Add due date picker

**Bases:**
- Double-click cell - Edit property
- Click column header - Sort by that column
- Right-click - Filter, group, bulk edit

---

## Next Steps

1. ✅ Open `projects/projects.base` - See all projects
2. ✅ Open `projects/master-kanban.md` - Move cards around
3. ✅ Create daily note from `templates/daily-tasks.md`
4. ✅ Add a few tasks with due dates and priorities
5. ✅ Observe task queries populate automatically

---

## Philosophy

**From Atlas:**

"This isn't about tracking every minute detail of your life. It's about having the right view at the right time.

- **Bases** when you're strategizing (weekly Cabinet meetings)
- **Kanban** when you're executing (daily work)
- **Tasks** when you're in the weeds (hourly focus)

Don't over-optimize the system. Use what works, ignore what doesn't. The goal is clarity, not complexity."

---

*Last Updated: 2025-10-17*
*System Owner: User*
*Maintained by: Atlas (COO)*
