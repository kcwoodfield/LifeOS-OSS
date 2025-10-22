# LifeOS Home Dashboard Guide

**Three-panel command center for daily productivity**

---

## Overview

The LifeOS Home Dashboard v2 is a three-panel system inspired by minimalist productivity systems. It provides a comprehensive view of your values, daily priorities, and tasks all in one place.

---

## Three Panels

### 🎯 LEFT: Alignment
**File:** `dashboards/home-left-alignment.md`

**Purpose:** Strategic overview - your values, goals, and active projects

**Sections:**
- **VALUES** - Core principles (Fitness, Freedom, Purpose, Time, Learning)
- **GOALS** - Key objectives with targets and deadlines
- **PROJECTS** - Active projects with health status
- **TIME ALLOCATION** - Hours per week across projects
- **MILESTONES** - Next 30/90 day targets
- **NORTH STAR** - 10-year vision

**When to use:** Weekly planning, quarterly reviews, strategic decisions

---

### 📅 CENTER: Daily
**File:** `dashboards/home-center-daily.md`

**Purpose:** Tactical execution - today's priorities, habits, and journal

**Sections:**
- **TOP 3 PRIORITIES** - Most important tasks today
- **TODAY'S TASKS** - Organized by project/domain
- **MORNING JOURNAL** - Energy, gratitude, intention
- **HABITS** - Morning, work, art, fitness, evening, your pet
- **EVENING JOURNAL** - Wins, learnings, blockers, tomorrow's plan
- **DAILY FEED** - Messages, reading, learning
- **WORDS OF WISDOM** - Daily inspiration

**When to use:** Every morning (set priorities) and evening (review day)

---

### ✅ RIGHT: Tasks
**File:** `dashboards/home-right-tasks.md`

**Purpose:** Operational execution - task management across all projects

**Sections:**
- **INBOX** - Unprocessed tasks
- **TODAY** - Due today
- **TOMORROW** - Due tomorrow
- **UPCOMING** - Next 7 days
- **OVERDUE** - Needs attention!
- **COMPLETED** - Last 7 days
- **HIGH PRIORITY** - Urgent tasks
- **TASK STATS** - By project
- **FROM KANBAN BOARDS** - Live feeds

**When to use:** Throughout the day for task tracking

---

## How to Use

### Option 1: Three Panels Side-by-Side (Recommended)

**Step-by-step:**
1. Open `dashboards/home-left-alignment.md`
2. Right-click tab → "Split right"
3. In right pane, open `dashboards/home-center-daily.md`
4. Right-click that tab → "Split right"
5. In right pane, open `dashboards/home-right-tasks.md`

**Result:** Three panels visible simultaneously

**Pro tip:** Pin these panels so they stay open

---

### Option 2: Canvas (Visual Layout)

**Step-by-step:**
1. Open `dashboards/home-canvas.canvas`
2. See all three panels plus quick links and stats
3. Zoom in/out to focus on specific panels
4. Click any panel to edit inline

**Result:** Visual card-based layout

**Pro tip:** Great for touchscreen or tablet use

---

### Option 3: Master Dashboard

**Step-by-step:**
1. Open `dashboards/home-v2.md`
2. Scroll through all sections
3. Click "→ Open Full Panel" links to expand

**Result:** All-in-one scrollable view

**Pro tip:** Use this on mobile or small screens

---

## Daily Workflow

### Morning Routine (10 minutes)

1. **Open Center Panel** (`home-center-daily.md`)
2. **Fill in Morning Journal:**
   - Energy level
   - Gratitude (3 things)
   - Today's intention
   - Top challenge

3. **Set Top 3 Priorities:**
   - What MUST ship today?
   - Pull from Right Panel (Tasks) if needed

4. **Check habits checklist:**
   - Review what's due today
   - Set intention for non-negotiables

5. **Review Left Panel** (Alignment) briefly:
   - Are today's priorities aligned with goals?
   - Any project deadlines approaching?

---

### During the Day

1. **Work from Center Panel:**
   - Focus on Top 3 Priorities first
   - Check off habits as completed
   - Add tasks as they come up

2. **Reference Right Panel** for task management:
   - Process Inbox throughout day
   - Mark tasks done
   - Add new tasks

3. **Check Left Panel** when making decisions:
   - Does this align with VALUES?
   - Does this support active PROJECTS?
   - Is this worth the TIME ALLOCATION?

---

### Evening Routine (10 minutes)

1. **Open Center Panel** (`home-center-daily.md`)
2. **Fill in Evening Journal:**
   - Did you complete Top 3? (Yes/Partial/No)
   - Wins today (3 things)
   - Learnings (what to improve)
   - Blockers (what got in the way)
   - Energy level (end of day)
   - Focus hours (deep work time)

3. **Plan Tomorrow's Top 3:**
   - What are the 3 most important tasks?
   - Pull from Right Panel (Tasks) - what's due tomorrow?

4. **Review habits:**
   - What did you complete?
   - What did you miss?
   - Why?

---

## Weekly Workflow

### Sunday Evening Planning (30 minutes)

1. **Review Left Panel** (Alignment):
   - Check GOALS progress
   - Update PROJECT health
   - Review TIME ALLOCATION
   - Check MILESTONES

2. **Cabinet Meeting:**
   - Use weekly-review skill or manual review
   - Get each agent's perspective
   - Update project priorities

3. **Update Center Panel template:**
   - Set weekly habits/focus areas
   - Update words of wisdom rotation

4. **Clean Right Panel:**
   - Archive completed tasks (last week)
   - Process OVERDUE (do, defer, delete)
   - Plan next week's big tasks

---

## Customization

### Adding Images

Like the inspiration examples, you can add header images:

**Method 1: Markdown images**
```markdown
![Beautiful sunset](assets/sunset.jpg)

# 🎯 Alignment
```

**Method 2: CSS snippets**
Create a CSS snippet to add background images to panels

---

### Habit Tracking Visualization

The inspiration examples show colored dots for habit tracking. You can achieve this with:

**Option 1: Checkboxes (current)**
Simple checkbox lists in Center Panel

**Option 2: Tracker plugin**
Install "Tracker" community plugin for visual habit tracking

**Option 3: Custom CSS**
Style completed checkboxes with colored circles

**Example CSS:**
```css
.task-list-item.is-checked::before {
  content: "🟢";
  margin-right: 4px;
}
```

---

### News Feed

To add a news feed to the Right Panel:

**Option 1: RSS plugin**
Install "RSS Reader" community plugin

**Option 2: Dataview queries**
Query recent files across vault

**Option 3: Manual updates**
Add daily news/updates manually in Center Panel → DAILY FEED section

---

## Integration with Existing Systems

### Bases
- Left Panel queries `projects.base` for project health
- Right Panel can show Base views inline

### Kanban
- Right Panel shows tasks from Kanban boards
- Link to Master Kanban from all panels

### Tasks Plugin
- Right Panel uses Tasks queries extensively
- Center Panel includes task checkboxes
- All tasks sync via Tasks plugin syntax

### Dataview
- All panels use Dataview queries for dynamic content
- Customize queries to show what matters

---

## Tips & Tricks

### 1. Pin Panels
Right-click panel tabs → "Pin" to keep them open

### 2. Use Workspace
Save three-panel layout as Workspace:
- Settings → Core Plugins → Workspaces: ON
- Left sidebar → Workspaces → "Save current workspace"
- Name it "Home Dashboard"
- Load it anytime from sidebar

### 3. Mobile Usage
On mobile, use `home-v2.md` (master dashboard)
Three panels don't work well on small screens

### 4. Daily Template
Create daily notes from `home-center-daily.md` template via Templater

### 5. Keyboard Shortcuts
Set keyboard shortcuts for:
- Open Left Panel: `Ctrl+1`
- Open Center Panel: `Ctrl+2`
- Open Right Panel: `Ctrl+3`

---

## Maintenance

### Daily
- Update Center Panel morning & evening
- Check off habits
- Process Right Panel Inbox

### Weekly
- Review and update Left Panel
- Archive Right Panel completed tasks
- Clean up overdue tasks

### Monthly
- Update VALUES if changed
- Review GOALS progress
- Adjust PROJECT priorities
- Clean up old tasks

---

## Troubleshooting

### "Dataview queries aren't working"
→ Install Dataview community plugin
→ Enable in Settings → Community Plugins

### "Tasks queries show nothing"
→ Install Tasks community plugin
→ Use Tasks plugin syntax (📅 YYYY-MM-DD)

### "Canvas is blank"
→ Open `home-canvas.canvas`
→ Make sure linked files exist
→ Refresh canvas view

### "Three panels don't fit on screen"
→ Zoom out in Obsidian (Ctrl/Cmd + -)
→ Use smaller font size
→ Use `home-v2.md` master dashboard instead

---

## Examples from Inspiration

### Beautiful Headers
Add scenic images to top of each panel:
```markdown
![Cosmic scene](assets/cosmic.jpg)

# 🎯 Alignment
```

### Colored Sections
Use Obsidian callouts for colored sections:
```markdown
> [!success] VALUES
> Exceptional Fitness | Financial Freedom | ...

> [!info] GOALS
> Goal 1, Goal 2, Goal 3

> [!warning] OVERDUE
> These tasks need attention!
```

### Visual Habit Tracking
Install Tracker or Habits plugin for visual dot matrix like the examples

---

## Philosophy

**From Atlas:**

"This dashboard isn't about tracking every detail of your life. It's about having the right view at the right time.

- **Alignment** when you're strategizing
- **Daily** when you're executing
- **Tasks** when you're in the weeds

Don't over-optimize the system. Use what works, ignore what doesn't. The goal is clarity, not complexity."

---

*Last Updated: 2025-10-17*
*Version: 2.0 (Three-Panel Layout)*
