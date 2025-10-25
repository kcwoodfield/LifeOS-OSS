# Time Tracking Database

> **Purpose:** Track time invested in projects, analyze productivity patterns, measure ROI

---

## Overview

This database tracks work sessions across all projects and domains. Use it to understand where time goes, identify productivity patterns, and measure return on investment.

## Schema

See `_schema.md` for the complete frontmatter template.

**Core Fields:**
- `date` - Session date
- `project` - Project/domain name
- `start_time` / `end_time` - Session duration
- `duration_hours` - Calculated hours (decimal)
- `category` - Type of work (development, planning, research, documentation, meeting)
- `focus` - Specific area of work
- `energy` / `productivity` - Self-assessment metrics

## Workflow

### During Work Session

**Option 1: Log at start**
1. Create new file: `YYYY-MM-DD-project-focus.md`
2. Use template (if created) or copy `_schema.md`
3. Fill in: date, project, start_time
4. Work on project
5. At end: Fill in end_time, duration_hours, notes

**Option 2: Log at end**
1. After finishing work session
2. Create file with today's date
3. Estimate start/end times
4. Calculate duration
5. Write brief notes on what shipped

### Retroactive Logging

For past work (like the LifeOS build):
1. Estimate session dates and durations
2. Create files for each major session
3. Document what shipped in each session
4. Use notes to capture key learnings/milestones

## Analytics Queries

### Total Hours by Project

```dataview
TABLE
  project,
  sum(rows.duration_hours) as "Total Hours"
FROM "databases/time-tracking"
GROUP BY project
SORT sum(rows.duration_hours) DESC
```

### Hours This Week

```dataview
TABLE
  date,
  project,
  duration_hours as "Hours",
  focus,
  productivity
FROM "databases/time-tracking"
WHERE date >= date(today) - dur(7 days)
SORT date DESC
```

### Hours This Month by Category

```dataview
TABLE
  category,
  sum(rows.duration_hours) as "Hours",
  round(sum(rows.duration_hours) / sum(rows.duration_hours) * 100, 1) + "%" as "Percentage"
FROM "databases/time-tracking"
WHERE date >= date(today) - dur(30 days)
GROUP BY category
SORT sum(rows.duration_hours) DESC
```

### Productivity Patterns

```dataview
TABLE
  date,
  project,
  duration_hours as "Hours",
  energy,
  productivity as "Score",
  focus
FROM "databases/time-tracking"
WHERE productivity >= 8
SORT date DESC
LIMIT 10
```

### ROI Analysis (Time vs. Output)

```dataview
TABLE
  project,
  sum(rows.duration_hours) as "Total Hours",
  count(rows) as "Sessions",
  round(sum(rows.duration_hours) / count(rows), 1) as "Avg Session"
FROM "databases/time-tracking"
GROUP BY project
SORT sum(rows.duration_hours) DESC
```

## Integration with Projects

Link time entries to project PRDs:

In time entry:
```yaml
project: [[projects/prds/yourproject]]
```

In project PRD, query total time invested:
```dataview
TABLE sum(duration_hours) as "Total Hours"
FROM "databases/time-tracking"
WHERE contains(project, "YourProject")
```

## Tips

**Accurate time tracking:**
- Log immediately after sessions (memory fades fast)
- Be honest about energy/productivity (data is for you, not performance reviews)
- Track breaks separately (focused work time only)
- Round to nearest 0.5 hours for simplicity

**Productivity scoring guidelines:**
- **9-10**: Deep flow state, shipped major features, highly productive
- **7-8**: Good focus, steady progress, few distractions
- **5-6**: Average session, some distractions, moderate output
- **3-4**: Low focus, many interruptions, minimal progress
- **1-2**: Wasted time, context switching, no real work done

**Energy tracking:**
- `high` - Energized, motivated, could work for hours
- `medium` - Normal working state, sustainable pace
- `low` - Tired, forcing it, should have taken a break

**What to capture in notes:**
- What shipped (concrete deliverables)
- Key learnings or breakthroughs
- Blockers encountered
- What to tackle next session

## Long-Term Value

After 3 months of tracking:
- **See patterns:** When are you most productive? Which projects drain energy?
- **Optimize schedule:** Block deep work when energy is highest
- **Measure ROI:** Is Project X worth the time investment?
- **Improve estimates:** How long do similar tasks actually take?
- **Justify decisions:** "I spent 40 hours on this feature - here's what I learned"

**This isn't about being a productivity robot. It's about understanding yourself.**

---

**Last Updated:** 2025-10-19
