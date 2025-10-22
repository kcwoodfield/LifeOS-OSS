# WorkOS Skills

This directory contains automated workflows (skills) for common work tasks.

---

## Planned Skills

### 1. Standup Report Generator
**Trigger:** "Generate my standup report"
**Output:** `communications/standups/YYYY-MM-DD.md`
**Content:**
- Yesterday's work (from task updates)
- Today's plan (from task priorities)
- Blockers (from task/project status)

### 2. Executive Update Generator
**Trigger:** "Create exec update for this week"
**Output:** `communications/exec-updates/YYYY-MM-DD.md`
**Content:**
- Progress summary
- Key wins
- Risks/blockers
- Next steps

### 3. Meeting Prep Assistant
**Trigger:** "Prepare briefing for [meeting name]"
**Output:** `meetings/prep/YYYY-MM-DD-meeting-name.md`
**Content:**
- Meeting context
- Agenda
- Key talking points
- Decisions needed
- Action items to follow up

### 4. Technical Decision Framework
**Trigger:** "Help document this technical decision"
**Output:** `decisions/YYYY-MM-DD-decision-name.md`
**Content:**
- Decision context
- Options considered (pros/cons)
- Decision made
- Rationale
- Stakeholders consulted

---

## Implementation Status

**Phase 2: Skills & Automation** ✅ **COMPLETE**
- [x] Standup generator
- [x] Exec update generator
- [x] Meeting prep assistant
- [x] Technical decision framework

## Available Skills

All 4 WorkOS automation skills are now available:

### 1. [Standup Report Generator](standup-report/)
**Trigger:** "Generate my standup report"
- Creates daily standup in Yesterday/Today/Blockers format
- Pulls from task database and project status
- Output: `communications/standups/YYYY-MM-DD.md`

### 2. [Executive Update Generator](exec-update/)
**Trigger:** "Create exec update"
- Generates weekly status update for stakeholders
- Bottom-line-up-front format with progress, risks, next steps
- Output: `communications/exec-updates/YYYY-MM-DD.md`

### 3. [Meeting Prep Assistant](meeting-prep/)
**Trigger:** "Prepare for meeting"
- Comprehensive meeting briefing with context, agenda, talking points
- Researches attendees and previous meetings
- Output: `meetings/prep/YYYY-MM-DD-meeting-name.md`

### 4. [Technical Decision Framework](tech-decision/)
**Trigger:** "Help document this technical decision"
- Guides ADR (Architecture Decision Record) creation
- Structured decision documentation with options, rationale, consequences
- Output: `decisions/YYYY-MM-DD-decision-name.md`

---

## How Skills Work

Skills are automated workflows triggered by natural language commands in Claude Code. They:
- Read relevant context from your vault
- Generate structured output
- Save to appropriate directories
- Follow consistent templates

---

## Creating Custom Skills

Want to create your own skills?

1. Create a directory: `.workos/skills/[skill-name]/`
2. Add `SKILL.md` file with skill definition
3. Define trigger phrases and output format
4. Test with Claude Code

See Claude Code docs for skill creation guide.

---

## Contributing

Share your custom skills with the WorkOS community:
- Submit skill definitions
- Share templates
- Suggest new skill ideas

Visit the [WorkOS GitHub repo](https://github.com/kcwoodfield/WorkOS) to contribute.
