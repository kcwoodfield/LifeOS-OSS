# Review Schema

Template for review frontmatter in `reviews/daily/`, `reviews/weekly/`, `reviews/monthly/` files.

## Daily Review Schema

```yaml
---
review_type: "daily"
date: 2025-10-16
day_of_week: "Wednesday"
energy_level: 4  # 1-5 scale
focus_time_hours: 6
domains_active:
  - career
  - art
top_3_completed: 2  # How many of top 3 priorities completed
wins:
  - "Shipped feature X"
  - "2 hour deep work session"
learnings:
  - "Morning sessions more productive"
blockers:
  - "Meeting interrupted flow state"
---
```

## Weekly Review Schema

```yaml
---
review_type: "weekly"
date: 2025-10-16  # Sunday date of the week
week_number: 42  # ISO week number
energy_level: 4  # Average for the week (1-5)
focus_time_hours: 28  # Total for the week
domains_active:
  - career
  - wealth
  - art
  - operations
projects_shipped: 1
wins:
  - "Launched MVP of X"
  - "Negotiated raise"
learnings:
  - "Need more buffer time between meetings"
  - "Art practice consistency improved"
challenges:
  - "Overcommitted on side projects"
next_week_priorities:
  - "Ship feature Y"
  - "Complete weekly review automation"
---
```

## Monthly Review Schema

```yaml
---
review_type: "monthly"
date: 2025-10-31  # Last day of month
month: "October"
year: 2025
energy_level: 4  # Average for the month
focus_time_hours: 120  # Total for the month
domains_review:
  career: "Strong progress on new role onboarding"
  wealth: "Net worth increased 3%"
  art: "Completed 12 practice sessions"
  operations: "Morning brief automation shipped"
projects_completed: 2
major_wins:
  - "90-day review went well"
  - "LifeOS v1 shipped"
major_learnings:
  - "System beats willpower - automation works"
  - "Weekly reviews catch problems early"
challenges:
  - "Calendar integration needed"
next_month_goals:
  - "Ship Project Alpha MVP"
  - "Complete NMA anatomy module"
---
```

## Field Definitions

### Common Fields (all review types)

**review_type** (required, enum)
- `daily` | `weekly` | `monthly`

**date** (required, date)
- Date of review (YYYY-MM-DD)
- Daily: the specific day
- Weekly: Sunday date
- Monthly: last day of month

**energy_level** (required, number)
- Scale: 1 (drained) to 5 (energized)
- Daily: energy for that day
- Weekly/Monthly: average

**focus_time_hours** (required, number)
- Deep work hours (no interruptions)
- Daily: total for day
- Weekly: total for week
- Monthly: total for month

**domains_active** (required, array)
- Which life domains had activity
- Options: `career`, `wealth`, `art`, `operations`, `health`, `relationships`

**wins** (required, array)
- Accomplishments and positive outcomes
- Be specific and measurable

**learnings** (required, array)
- Insights, patterns, lessons learned
- What to do differently next time

**challenges** / **blockers** (optional, array)
- What got in the way
- What needs attention

### Daily-Specific Fields

**day_of_week** (required, string)
- Monday, Tuesday, etc.
- For pattern analysis (are Mondays worse?)

**top_3_completed** (optional, number)
- How many of the day's top 3 priorities were completed (0-3)

### Weekly-Specific Fields

**week_number** (required, number)
- ISO week number (1-52)

**projects_shipped** (optional, number)
- Count of projects/features shipped this week

**next_week_priorities** (required, array)
- Top priorities for coming week

### Monthly-Specific Fields

**month** (required, string)
- Month name (January, February, etc.)

**year** (required, number)
- Year (2025, 2026, etc.)

**domains_review** (required, object)
- Per-domain summary of the month
- Each domain gets a brief summary string

**projects_completed** (optional, number)
- Count of projects completed this month

**major_wins** (required, array)
- Most significant accomplishments of the month

**major_learnings** (required, array)
- Most important insights from the month

**next_month_goals** (required, array)
- Top goals for next month

## Example Queries

**Recent energy levels:**
```dataview
TABLE date, energy_level, focus_time_hours
FROM "reviews/daily"
WHERE review_type = "daily"
SORT date DESC
LIMIT 7
```

**Weekly velocity:**
```dataview
TABLE week_number, projects_shipped, focus_time_hours
FROM "reviews/weekly"
WHERE review_type = "weekly"
SORT date DESC
LIMIT 12
```

**Monthly domain summary:**
```dataview
TABLE month, domains_review.career, domains_review.wealth, domains_review.art
FROM "reviews/monthly"
WHERE review_type = "monthly"
SORT date DESC
```
