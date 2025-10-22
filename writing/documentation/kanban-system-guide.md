# Kanban System Guide

**Visual workflow management for LifeOS projects**

---

## Overview

The LifeOS Kanban system uses the **Obsidian Kanban plugin** to provide visual task boards for project management. This guide covers all features, syntax, and best practices.

---

## Kanban Boards

### Master Kanban
**File:** `projects/master-kanban.md`

**Purpose:** Cross-project tactical view for weekly sprints

**Columns:**
- 📋 **Backlog** - Future tasks and ideas
- 🎯 **To Do** - Ready to start this week
- 🚀 **In Progress** - Currently working on (WIP limit: 2-3)
- ✅ **Done** - Completed this week
- 🗄️ **Archive** - Historical completed items

### Project-Specific Kanbans

**Project Alpha:** `projects/minerva-kanban.md`
- Columns: Backlog | Validation Phase | Interviewing | Analysis | Completed | Archive
- Purpose: Track Project Alpha validation workflow

**Blog:** `projects/blog-kanban.md`
- Columns: Ideation | Drafting | Editing | Assets | Ready to Publish | Published | Archive
- Purpose: Content pipeline management

**Voice Assistant:** `projects/voice-assistant-kanban.md`
- Columns: Backlog | Phase 2 (Current) | In Progress | Completed | Bugs | Documentation | Archive
- Purpose: Feature development tracking

---

## Obsidian Kanban Plugin Features

### Card Syntax

**Basic Card:**
```markdown
- [ ] Task name
```

**Card with Due Date:**
```markdown
- [ ] Task name 📅 2025-10-20
```

**Card with Time:**
```markdown
- [ ] Task name 📅 2025-10-20 ⏰ 14:00
```

**Card with Tags:**
```markdown
- [ ] Task name #project #category
```

**Card with Priority (@ mentions):**
```markdown
- [ ] Task name @high
- [ ] Task name @medium
- [ ] Task name @low
- [ ] Task name @critical
```

**Card with Multiple Attributes:**
```markdown
- [ ] Schedule 10 PM interviews #minerva @high #p1 📅 2025-10-20 ⏰ 09:00
```

**Completed Card:**
```markdown
- [x] Task name #project @high 📅 2025-10-17 ✅ 2025-10-17
```

---

## Kanban Plugin Settings

### Frontmatter Configuration

Every Kanban board includes settings in the frontmatter:

```yaml
---
kanban-plugin: basic
kanban-plugin-settings:
  hide-tags-in-title: false         # Show tags on cards
  hide-date-in-title: false         # Show dates on cards
  prepend-archive-date: true        # Add date when archiving
  archive-with-date: true           # Include completion date
  new-card-insertion-method: top    # Add new cards at top
  show-checkboxes: true             # Show checkboxes on cards
  lane-width: 280                   # Column width in pixels
  date-format: YYYY-MM-DD           # Date format
  time-format: HH:mm                # Time format
---
```

**Settings Explained:**

- `hide-tags-in-title: false` - Keep tags visible (helps with filtering)
- `hide-date-in-title: false` - Show due dates on cards
- `prepend-archive-date: true` - Adds archive date when moving to Archive
- `archive-with-date: true` - Includes completion date (✅ 2025-10-17)
- `new-card-insertion-method: top` - New cards appear at top of column
- `show-checkboxes: true` - Display checkbox for completion
- `lane-width: 280` - Column width (280-300 works well)
- `date-format: YYYY-MM-DD` - ISO date format
- `time-format: HH:mm` - 24-hour time format

---

## Priority System

Use @ mentions for priority levels:

**Levels:**
- `@critical` - Must do immediately, blocks everything
- `@high` - Important, should complete this week
- `@medium` - Normal priority, schedule when possible
- `@low` - Nice to have, defer if needed

**Visual:**
- 🔴 @critical
- 🟠 @high
- 🟡 @medium
- 🟢 @low

**Best Practice:** Don't mark everything @critical. Reserve for true emergencies.

---

## Tag System

### Project Tags
- `#minerva` - Project Alpha validation
- `#blog` - Blog content
- `#voice-assistant` - Voice assistant features
- `#obsidian` - LifeOS infrastructure
- `#histomap` - Project Beta (paused)
- `#okami` - Project Gamma (paused)

### Category Tags
- `#research` - Research tasks
- `#interviews` - Interview scheduling/conducting
- `#analysis` - Data analysis and synthesis
- `#writing` - Writing and documentation
- `#code` - Coding tasks
- `#design` - Design work
- `#infra` - Infrastructure setup

### Priority Tags
- `#p1` - Primary focus (revenue path)
- `#p2` - Secondary focus
- `#p3` - Maintenance

**Example:**
```markdown
- [ ] Schedule 10 PM interviews #minerva #interviews @high #p1 📅 2025-10-20
```

---

## Kanban Workflow

### Daily

**Morning:**
1. Open Master Kanban
2. Review "In Progress" (should be 2-3 items max)
3. Check "To Do" for today's work
4. Move 1-2 items from "To Do" to "In Progress"

**During Day:**
5. Work on "In Progress" items
6. Move completed items to "Done"
7. Add new tasks to "Backlog" or "To Do"

**Evening:**
8. Review "In Progress" (what's still active?)
9. Move completed items to "Done"
10. Check tomorrow's "To Do"

### Weekly

**Sunday Evening Planning:**
1. Open Master Kanban
2. **Archive "Done" column** - Move to Archive section with date header
3. **Review "In Progress"** - Should be empty or 1-2 items max
4. **Pull from "Backlog" to "To Do"** - Select 5-10 tasks for next week
5. **Prioritize** - Ensure @high and #p1 tasks are in "To Do"
6. **Check due dates** - Anything overdue?

**Project Kanbans:**
7. Open each project Kanban
8. Move cards through workflow
9. Archive completed items
10. Add new ideas/tasks to Backlog

### Monthly

**End of Month:**
1. Review all Kanban boards
2. Archive old completed items (>30 days)
3. Clean up Backlog (delete stale items)
4. Review project progress vs. goals

---

## WIP Limits

**Work In Progress (WIP) Limits prevent overcommitment:**

### Master Kanban
- **Backlog:** Unlimited
- **To Do:** 10-15 items max
- **In Progress:** **2-3 items MAX** (strictly enforced)
- **Done:** Archive weekly

### Project Kanbans
- **Backlog:** Unlimited
- **Current Phase:** 5-10 items
- **In Progress:** 1-2 items per person
- **Completed:** Archive monthly

**Why WIP limits?**
- Focus on finishing vs. starting
- Reduce context switching
- Identify blockers faster
- Increase throughput

**Rule:** If "In Progress" is full, finish something before starting new work.

---

## Card Management

### Creating Cards

**In Obsidian Kanban view:**
1. Click "+" at top of column
2. Or type in column and press Enter
3. Or drag card from another column

**In markdown:**
```markdown
## To Do

- [ ] New task here
```

### Moving Cards

**Drag and drop:**
- Click and hold card
- Drag to target column
- Drop in position

**Keyboard:**
- Arrow keys to navigate
- Ctrl/Cmd + arrow to move between columns

### Editing Cards

**In Kanban view:**
- Click card to open
- Edit title, description, metadata
- Add tags, dates, priorities

**In markdown:**
- Edit directly in source mode
- Use Tasks plugin syntax

### Archiving Cards

**Manual:**
- Drag to Archive column

**Automatic:**
- Complete card (check checkbox)
- Kanban plugin adds ✅ completion date
- Move to Archive column weekly

---

## Date Management

### Due Dates

**Add due date:**
```markdown
- [ ] Task 📅 2025-10-20
```

**With time:**
```markdown
- [ ] Task 📅 2025-10-20 ⏰ 14:00
```

**Date picker:**
- Type `📅` then space
- Calendar picker appears
- Select date

### Date Formats

**Supported:**
- `📅 2025-10-20` (ISO format - recommended)
- `📅 Oct 20, 2025`
- `📅 10/20/2025`

**Best practice:** Use ISO format (YYYY-MM-DD) for consistency

### Completion Dates

**Automatic:**
When you check a card, plugin adds:
```markdown
- [x] Task 📅 2025-10-17 ✅ 2025-10-17
```

**Format:**
- `✅ YYYY-MM-DD` - Completion date
- Prepended if `prepend-archive-date: true`

---

## Keyboard Shortcuts

**Obsidian Kanban Plugin:**
- `Ctrl/Cmd + Enter` - Create new card
- `Enter` - Edit card
- `Escape` - Close card editor
- Arrow keys - Navigate cards
- `Ctrl/Cmd + Arrow` - Move card between columns
- `Space` - Toggle card checkbox
- `Delete` - Delete card (with confirmation)

**Custom shortcuts (set in Obsidian settings):**
- Open Master Kanban: `Ctrl + K`
- Create new card: `Ctrl + N`

---

## Advanced Features

### Card Descriptions

**Multi-line cards:**
```markdown
- [ ] Task title
  Task description goes here
  Can span multiple lines
  - Sub-task 1
  - Sub-task 2
```

### Linked Cards

**Link to notes:**
```markdown
- [ ] Review [[projects/prds/minerva|Project Alpha PRD]] #minerva @high
```

**Link to other cards:**
```markdown
- [ ] Task A (blocked by [[Task B]])
```

### Card Colors

**Use Obsidian highlights:**
```markdown
- [ ] ==High priority task== @critical
- [ ] **Important task** @high
```

### Recurring Cards

**Not built-in to Kanban, but can use Tasks plugin:**
```markdown
- [ ] Weekly review 🔁 every week on Sunday
```

---

## Integration with Other Systems

### Tasks Plugin

Kanban cards are markdown checkboxes, so Tasks plugin can query them:

```tasks
not done
path includes projects/master-kanban
```

### Dataview

Query Kanban cards with Dataview:

```dataview
TASK
FROM "projects/master-kanban"
WHERE !completed
```

### Bases

Link Kanban cards to Base items:

```markdown
- [ ] Update [[projects/projects.base|Projects Database]] #obsidian
```

---

## Best Practices

### 1. Keep "In Progress" Small
- **Rule:** Max 2-3 items in progress
- **Why:** Focus on finishing, not starting
- **Action:** Move items back to "To Do" if too many

### 2. Archive Weekly
- **Rule:** Move "Done" to "Archive" every Sunday
- **Why:** Keep board clean and fast
- **Action:** Add date header in Archive section

### 3. Use Specific Card Titles
- **Bad:** "Work on Project Alpha"
- **Good:** "Schedule 10 PM interviews for Project Alpha validation"
- **Why:** Clear, actionable, measurable

### 4. Add Due Dates
- **Rule:** Every card should have a due date
- **Why:** Creates urgency and accountability
- **Action:** Use 📅 emoji + date

### 5. Tag Everything
- **Rule:** Every card has project tag (#minerva) and category (#research)
- **Why:** Enables filtering and querying
- **Action:** Add tags when creating card

### 6. Limit Backlog
- **Rule:** Review Backlog monthly, delete stale items
- **Why:** Prevents "backlog bloat"
- **Action:** If not starting in 90 days, delete it

### 7. Use Priority Sparingly
- **Rule:** Not everything is @critical or @high
- **Why:** Priority inflation makes everything urgent
- **Action:** Most tasks should be @medium or @low

### 8. Review Daily
- **Rule:** Check Kanban every morning and evening
- **Why:** Keeps work visible and organized
- **Action:** Part of daily routine

---

## Troubleshooting

### "Cards aren't showing up in Kanban view"
→ Make sure file has `kanban-plugin: basic` in frontmatter
→ Use proper markdown checkbox syntax: `- [ ]`
→ Reload Obsidian

### "Dates aren't displaying"
→ Check `hide-date-in-title` setting (should be `false`)
→ Use proper date format: `📅 YYYY-MM-DD`
→ Ensure space after emoji

### "Can't drag cards between columns"
→ Click and hold, then drag (not just click)
→ Make sure you're in Kanban view mode (not markdown)
→ Try reloading board

### "Archive column is huge"
→ Move old items to a separate archive file
→ Keep only recent (last 30 days) in Archive column

### "Board is slow to load"
→ Too many cards (>100)
→ Archive old completed items
→ Split into multiple boards if needed

---

## Tips & Tricks

### 1. Color-Code Columns
Use emojis in column headers for visual distinction:
- 📋 Backlog
- 🎯 To Do
- 🚀 In Progress
- ✅ Done
- 🗄️ Archive

### 2. Use Card Templates
Create card templates for common tasks:
```markdown
- [ ] [Task name] #project @priority 📅 YYYY-MM-DD
  Description:
  Acceptance criteria:
  - [ ] Criterion 1
  - [ ] Criterion 2
```

### 3. Link Related Cards
```markdown
- [ ] Task A (depends on [[Task B]])
```

### 4. Add Context to Cards
```markdown
- [ ] Schedule interviews #minerva @high 📅 2025-10-20
  Goal: 10 interviews by Nov 15
  Criteria: Mix of B2B and B2C PMs
  Resources: [[Interview Guide]], [[PM List]]
```

### 5. Use Hotkeys
Set up custom hotkeys for:
- Open Master Kanban
- Create new card
- Toggle card completion

### 6. Daily Standup View
Use Master Kanban for daily standup:
- **Yesterday:** What moved to "Done"?
- **Today:** What's in "In Progress"?
- **Blockers:** Any cards stuck?

---

## Philosophy

**From Atlas:**

"A Kanban board is a mirror. It shows you what you're actually working on, not what you think you're working on.

If your 'In Progress' column has 15 items, you're not making progress on any of them. You're context-switching yourself into mediocrity.

The discipline of Kanban isn't moving cards. It's the discipline of saying 'no' to new work until you finish what's already started.

Two items shipped beats ten items started. Every time."

---

*Last Updated: 2025-10-17*
*Kanban Plugin Version: Compatible with Obsidian Kanban plugin*
