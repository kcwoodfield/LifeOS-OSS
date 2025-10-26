# Time Tracking Schema

Use this frontmatter structure for all time-tracking entries in `databases/time-tracking/`.

```yaml
---
date: 2025-10-19              # YYYY-MM-DD (session date)
project: LifeOS               # Project/domain name
start_time: "14:00"           # HH:MM (24-hour format)
end_time: "18:30"             # HH:MM (24-hour format)
duration_hours: 4.5           # Calculated hours (decimal)
category: development         # development | planning | research | documentation | meeting
focus: database-system        # What you worked on specifically
energy: high                  # high | medium | low
productivity: 8               # 1-10 scale
notes: ""                     # Brief summary of what shipped/learned
tags: []
created: 2025-10-19
---

# Session Notes

## What I Worked On

-

## What Shipped

-

## Learnings / Blockers

-

## Next Session

-
```

## Field Definitions

### Required Fields

**date** (date)
- Session date: YYYY-MM-DD
- Used for daily/weekly/monthly aggregation

**project** (string)
- Project or domain name
- Examples: LifeOS, YourProject, SecondProject, Career, Personal

**start_time** (string)
- Session start: "HH:MM" in 24-hour format
- Example: "14:00" for 2:00 PM

**end_time** (string)
- Session end: "HH:MM" in 24-hour format
- Example: "18:30" for 6:30 PM

**duration_hours** (number)
- Calculated hours worked (decimal)
- Example: 4.5 hours

**category** (enum)
- `development` - Coding, building features
- `planning` - System design, architecture
- `research` - Learning, exploration
- `documentation` - Writing docs, blog posts
- `meeting` - Collaboration, consultations

**created** (date)
- When this entry was created: YYYY-MM-DD

### Optional Fields

**focus** (string)
- Specific work focus for this session
- Examples: database-system, books-feature, cabinet-wisdom, architecture-refactor

**energy** (enum)
- `high` - Felt energized, in flow
- `medium` - Normal working state
- `low` - Tired, distracted, low focus

**productivity** (number)
- Self-rated productivity: 1-10 scale
- 1 = Completely unproductive
- 10 = Extremely productive, deep flow state

**notes** (string)
- Brief summary of session (1-2 sentences)
- What shipped, what you learned, what blocked you

**tags** (array)
- Free-form tags for categorization
- Examples: [sprint, deep-work, pairing, debugging]

## Example Entry

```yaml
---
date: 2025-10-19
project: LifeOS
start_time: "14:00"
end_time: "18:30"
duration_hours: 4.5
category: development
focus: books-database
energy: high
productivity: 9
notes: "Built Books database with spreadsheet view, created templates, added 3 example books"
tags: [database, dataview, obsidian]
created: 2025-10-19
---

# Session: Books Database Build

## What I Worked On

- Created Books database schema and documentation
- Built Dataview table view for spreadsheet display
- Created book template with structured notes
- Added 3 example books (Moby-Dick, Sexual Personae, The Odyssey)
- Troubleshot Database plugin vs Dataview confusion

## What Shipped

- Full books database with 3 examples
- Working Dataview table (Books-Table.md)
- Book template for future entries
- Documentation in README and schema files

## Learnings / Blockers

- Advanced Tables plugin doesn't auto-sync with markdown files
- Need to clarify editable spreadsheet vs. read-only Dataview tables
- Database plugin recommendations were incorrect (plugin doesn't exist as described)

## Next Session

- Finalize books workflow
- Consider time-tracking system for better ROI analysis
```

---

## Naming Convention

**File naming:** `YYYY-MM-DD-project-focus.md`

**Examples:**
- `2025-10-19-lifeos-books-database.md`
- `2025-10-18-lifeos-kernel-refactor.md`
- `2025-10-17-minerva-api-design.md`

**Why this format:**
- Chronological sorting automatically
- Easy to find sessions by date or project
- Clear what each session focused on

---

**See:** `databases/time-tracking/README.md` for usage guide and analytics queries
