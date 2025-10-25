# Meeting Schema Template

Use this frontmatter structure for all meeting files in `databases/meetings/`.

```yaml
---
title: "Meeting Name/Purpose"
date: 2025-10-19
type: work                   # cabinet | work | project | social | other
participants: []             # List of attendees
duration: null               # Meeting length in minutes
project: null                # [[Project Name]] or null
decisions: []                # Key decisions made
action_items: []             # Tasks spawned from meeting
tags: []
created: 2025-10-19
updated: 2025-10-19
---

# Meeting Name

## Agenda

1. Topic 1
2. Topic 2
3. Topic 3

## Notes

### Discussion

Meeting notes go here...

### Decisions Made

- **Decision 1:** Context and rationale
- **Decision 2:** Context and rationale

### Action Items

- [ ] Task 1 - Assigned to X - Due YYYY-MM-DD
- [ ] Task 2 - Assigned to Y - Due YYYY-MM-DD

## Follow-Up

Next steps, items to revisit, parking lot issues.
```

## Field Definitions

### Required Fields

**title** (string)
- Meeting name or purpose
- Examples: "Weekly Cabinet Meeting", "YourProject Kickoff", "1:1 with Manager", "Sprint Planning"

**date** (date)
- Meeting date: YYYY-MM-DD
- Used for sorting and queries

**type** (enum)
- `cabinet` - Cabinet meeting (multi-agent consultation)
- `work` - Job-related meeting
- `project` - Side project meeting
- `social` - Coffee chat, networking, casual
- `other` - Any other type of meeting

**created** (date)
- Date this note was created: YYYY-MM-DD
- Auto-filled by template

### Optional Fields

**participants** (array)
- List of attendees
- Format: `["Name 1", "Name 2", "Name 3"]`
- Can include agent names for Cabinet meetings: `["Atlas", "Banker", "Strategist"]`
- Empty array `[]` if solo meeting or not applicable

**duration** (number or null)
- Meeting length in minutes
- Examples: `30`, `60`, `90`
- Null if not tracked or not applicable

**project** (link or null)
- Link to related project: `[[Project Name]]`
- Can link to PRD: `[[projects/prds/yourproject]]`
- Null if not project-specific

**decisions** (array)
- Key decisions made during meeting
- Format: `["Decision 1", "Decision 2"]`
- Empty array `[]` if no major decisions

**action_items** (array)
- Tasks spawned from meeting
- Format: `["Task 1 - User - Due 2025-10-20", "Task 2 - Team - Due 2025-10-22"]`
- Should also be created as individual task files in `databases/tasks/`
- Empty array `[]` if no action items

**tags** (array)
- Topics, themes, categories
- Examples: `[strategy, technical, planning, retrospective]`
- Empty array `[]` if no tags

**updated** (date)
- Last modified date: YYYY-MM-DD
- Update when adding notes or follow-up

## Meeting Type Definitions

### Cabinet Meeting
**Purpose:** Multi-agent strategic consultation
**Participants:** Agent names (Atlas, Banker, Strategist, etc.)
**Format:** Structured agent reports + synthesis
**Frequency:** Weekly (Sunday evening) or ad-hoc for major decisions

**Example:**
```yaml
type: cabinet
participants: ["Atlas", "Banker", "Strategist", "Sage"]
project: null
tags: [weekly-review, strategy, operations]
```

### Work Meeting
**Purpose:** Job-related meetings
**Participants:** Colleagues, managers, reports
**Format:** Standard meeting notes
**Examples:** Sprint planning, standups, 1:1s, all-hands

**Example:**
```yaml
type: work
participants: ["Manager", "Tech Lead", "Designer"]
project: null
tags: [sprint-planning, q4-roadmap]
```

### Project Meeting
**Purpose:** Side project planning and coordination
**Participants:** Collaborators or solo
**Format:** Project-specific discussion
**Examples:** Design reviews, technical planning, brainstorming

**Example:**
```yaml
type: project
participants: ["User", "Designer Friend"]
project: [[projects/prds/yourproject]]
tags: [design, architecture, planning]
```

### Social Meeting
**Purpose:** Networking, relationship building
**Participants:** Friends, contacts, mentors
**Format:** Casual notes
**Examples:** Coffee chats, networking events, informational interviews

**Example:**
```yaml
type: social
participants: ["John Doe", "Jane Smith"]
project: null
tags: [networking, career, advice]
```

## Example Meeting

```yaml
---
title: "Weekly Cabinet Meeting"
date: 2025-10-19
type: cabinet
participants: ["Atlas", "Banker", "Strategist", "Sage", "Spartan", "Engineer"]
duration: 75
project: null
decisions:
  - "Prioritize YourProject over blog for Q4"
  - "Increase art practice to 3x per week"
  - "Hold off on rental property purchase until Q1 2026"
action_items:
  - "Update projects/INDEX.md with new priorities - User - Due 2025-10-20"
  - "Create art practice schedule - Artist - Due 2025-10-21"
  - "Research rental markets for Q1 - Banker - Due 2025-11-01"
tags: [weekly-review, strategy, priorities, q4]
created: 2025-10-19
updated: 2025-10-19
---

# Weekly Cabinet Meeting - October 19, 2025

## Agent Reports

### Atlas (COO) - Operations Report

*"Ah yes, another week where we've somehow convinced ourselves that working 60 hours while painting like Da Vinci and reading Proust is 'sustainable.' Delightful."*

**Velocity:** Shipped 3 major features on YourProject, completed 2 blog drafts
**Balance:** Work 50hrs, art 4hrs, side projects 15hrs - art practice slipping
**Energy:** 7/10 average, Thursday dip notable
**Next week capacity:** High, no major meetings scheduled

**Recommendation:** Block 3x 2-hour art sessions on calendar (non-negotiable)

### Banker (CFO) - Financial Report

**Net Worth:** Up 3.2% this month
**Portfolio:** Tech stocks recovering, bonds stable
**Side Income:** YourProject beta revenue $2K (first paying customers!)
**Opportunities:** Rental property showing 8% cap rate but market cooling

**Recommendation:** Wait on real estate until Q1 2026, market indicators suggest better deals coming

### Strategist (CSO) - Career & Politics Report

**Tactical Situation:** New PM role going well, stakeholder relationships building
**Strategic Position:** Ahead of pace for Staff PM promotion (12-18 months)
**Political Landscape:** Reorg rumors - position yourself as infrastructure lead
**Opportunities:** Visibility on Q4 roadmap planning - volunteer to lead

**Recommendation:** Focus on high-visibility wins Q4, build coalition with eng leadership

[... continues with other agents ...]

## Synthesis (Atlas)

**Key Themes:**
1. YourProject momentum is real - paying customers validate product direction
2. Art practice suffering - needs protected time blocks
3. Career trajectory on track - stay the course
4. Financial position strong - patience on real estate

**Decisions Made:**
1. **Q4 Priority:** YourProject over blog (paying customers > audience building right now)
2. **Art Practice:** 3x per week minimum, calendar blocked, non-negotiable
3. **Real Estate:** Hold until Q1 2026, continue research and save for larger down payment

**Action Items:**
See frontmatter above - tasks created in databases/tasks/

## Follow-Up

**Next Cabinet Meeting:** 2025-10-26 (Sunday evening)
**Items to Revisit:**
- YourProject beta metrics (track weekly)
- Art practice consistency (did we hit 3x per week?)
- Reorg developments (monitor via Strategist)
```

---

**See:** `databases/meetings/README.md` for usage guide and workflow
