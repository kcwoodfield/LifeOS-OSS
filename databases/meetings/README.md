# Meetings Database

> **Purpose:** Archive meeting notes with structured frontmatter for searchability
> **Integration:** Cabinet meetings, 1:1s, project meetings, all captured here

---

## Overview

This database stores all meeting notes - from work meetings to Cabinet consultations to coffee chats. Each meeting is a searchable, queryable record with participants, topics, decisions, and action items.

## Schema

See `_schema.md` for the complete frontmatter template.

**Required Fields:**
- `title` - Meeting name/purpose
- `date` - Meeting date
- `type` - Meeting category
- `created` - Record creation date

**Optional Fields:**
- `participants` - Who attended
- `duration` - Length in minutes
- `project` - Link to related project
- `tags` - Topics, themes
- `decisions` - Key decisions made
- `action_items` - Tasks spawned from meeting
- `notes` - Free-form meeting notes

## Workflow

### Before Meeting
1. Create meeting file: `databases/meetings/YYYY-MM-DD-meeting-name.md`
2. Fill in frontmatter (date, type, participants)
3. Add agenda items

### During Meeting
1. Take notes in markdown body
2. Flag decisions and action items

### After Meeting
1. Clean up notes
2. Extract action items → `databases/tasks/`
3. Link to relevant projects
4. Update `decisions` and `action_items` frontmatter

## Views

### Dashboard Queries

**Recent Meetings:**
```dataview
TABLE participants, type, duration as "Duration (min)"
FROM "databases/meetings"
SORT date DESC
LIMIT 10
```

**Meetings by Type:**
```dataview
TABLE date, participants, duration
FROM "databases/meetings"
WHERE type = "cabinet"
SORT date DESC
```

**Meetings for Project:**
```dataview
TABLE date, participants, type
FROM "databases/meetings"
WHERE contains(project, "[[Project Name]]")
SORT date DESC
```

**Action Items by Meeting:**
```dataview
TABLE action_items, date
FROM "databases/meetings"
WHERE length(action_items) > 0
SORT date DESC
LIMIT 20
```

## Naming Convention

**File naming:** `YYYY-MM-DD-meeting-name.md`
**Examples:**
- `2025-10-19-weekly-cabinet-meeting.md`
- `2025-10-19-yourproject-kickoff.md`
- `2025-10-19-1on1-with-manager.md`

**Why this format:**
- Chronological sorting by meeting date
- Clear meeting purpose in filename
- Easy to find recent meetings

## Meeting Types

**Cabinet Meeting:**
- Weekly strategic review
- Multi-agent consultation
- Major life decisions

**Work Meeting:**
- Job-related meetings
- Sprint planning, standups, retrospectives
- 1:1s with manager/reports

**Project Meeting:**
- Side project planning
- Design reviews
- Technical architecture discussions

**Social:**
- Coffee chats
- Networking meetings
- Casual conversations with friends

**Other:**
- Doctor appointments with notes
- Financial advisor meetings
- Any meeting worth documenting

## Tips

**Action Items:**
- Extract to `databases/tasks/` as individual task files
- Link back to meeting note: `meeting: [[2025-10-19-meeting-name]]`
- Set due dates and priorities

**Decisions:**
- Document context: what was decided and why
- Link to relevant project or context files
- Note dissenting opinions or trade-offs considered

**Participants:**
- Use consistent naming (full names or handles)
- Link to contact files if you maintain them
- Note roles: "facilitator", "decision maker", etc.

**Duration Tracking:**
- Helps identify meeting bloat
- Can analyze time spent in meetings vs. deep work
- Query: "How many hours in meetings this week?"

**Cabinet Meeting Integration:**
- Tag with `cabinet` type
- Reference agent perspectives in notes
- Link decisions to context files (career, wealth, art)

---

**Last Updated:** 2025-10-19
