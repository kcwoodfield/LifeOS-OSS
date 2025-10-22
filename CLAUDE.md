# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## System Overview

This is **LifeOS-OSS** - the open source template for LifeOS, a comprehensive personal knowledge management and life orchestration system built in Obsidian + Claude Code.

**Current Branch:** `oss-template` (public template - no personal data)

LifeOS is an **AI-native personal operating system** featuring:
- **22 specialized AI agents** (14 personal + 8 professional)
- **Structured data management** (7 Dataview-powered databases)
- **Automated workflows** (9 Claude Code skills)
- **Dynamic dashboards** (The Atlas command center + domain dashboards)
- **Privacy-first architecture** (three-branch git strategy)

**System Philosophy:**
- Markdown as infrastructure (all data is plain text, version controlled)
- AI-native design (built for human + AI collaboration)
- Context-aware (agents read your personal context files)
- Agent-based (specialized personas for different domains)
- Privacy by design (three-branch architecture + .gitignore protection)

---

## Three-Branch Architecture

LifeOS uses a **three-branch model** for privacy and context separation:

### Branch Strategy

**main (Personal - Private)**
- Your personal LifeOS data
- 14 personal agents (Atlas, Banker, Strategist, Sage, Spartan, Engineer, Designer, Artist, Maker, Storyteller, Ada, Connector, Healer, Professor)
- Personal context files (`.system/context/*.md`)
- Personal projects, tasks, journal entries
- **Never pushed to public repositories**

**workos (Professional - Private)**
- Your work data and professional projects
- 8 work agents (Frontend Engineer, Backend Engineer, Engineering Lead, Business Analyst, Copy Editor, Senior PM, Senior Project Manager, Moneypenny)
- Work context files (`.workos/context/*.md`)
- Work projects, meetings, stakeholder communication
- **Separate from personal data, also private**

**oss-template (Public Template - THIS BRANCH)**
- Sanitized template for public distribution
- All agent infrastructure (but no personal data)
- Example files showing proper structure
- Template context files (`.template` extension)
- `.gitignore` protection for user privacy
- **Safe to fork and share publicly**

### Switching Branches

```bash
# Work on personal LifeOS
git checkout main

# Work on professional WorkOS
git checkout workos

# Contribute to LifeOS-OSS
git checkout oss-template
```

---

## Repository Structure

```
LifeOS/
├── CLAUDE.md                  # System guide for Claude Code (this file)
├── README.md                  # Complete system documentation
├── ARCHITECTURE.md            # Architecture decisions and design
├── CONTRIBUTING.md            # How to contribute to LifeOS-OSS
├── .gitignore                 # Privacy protection
├── _inbox_.md                 # Quick capture entry point (GTD workflow)
│
├── .obsidian/                 # Obsidian configuration
│
├── .system/                   # LifeOS infrastructure (14 personal agents)
│   ├── agents/                    # The Cabinet
│   │   ├── atlas-operations.md        # COO - Life optimization
│   │   ├── banker.md                  # CFO - Wealth strategy
│   │   ├── strategist.md              # CSO - Career + politics
│   │   ├── sage.md                    # Oracle - Philosophy & meaning
│   │   ├── spartan.md                 # Defense - Fitness & security
│   │   ├── execution/
│   │   │   ├── engineer.md                # CTO - Technical strategy
│   │   │   ├── designer.md                # CDO - Design & UX
│   │   │   └── artist.md                  # Creative Director - Art practice
│   │   └── growth/
│   │       ├── maker.md                   # Hardware & DIY
│   │       ├── storyteller.md             # Writing & content
│   │       ├── analyst.md                 # Data & metrics (Ada)
│   │       ├── connector.md               # Relationships & social
│   │       ├── healer.md                  # Health & longevity
│   │       └── professor.md               # Literary critic & reading
│   ├── context/                   # Personal context files
│   │   ├── *.template                 # Template files (committed)
│   │   └── *.md                       # Filled files (gitignored)
│   ├── data/                      # Structured data files
│   │   └── cabinet-quotes.md          # 98 rotating daily wisdom quotes
│   └── schemas/                   # Dataview schema documentation
│
├── .workos/                   # WorkOS infrastructure (8 professional agents)
│   ├── agents/                    # Professional team
│   │   ├── frontend-engineer.md       # React/TypeScript/UI
│   │   ├── backend-engineer.md        # API/DB/systems
│   │   ├── engineering-lead.md        # Tech strategy & coordination
│   │   ├── business-analyst.md        # Requirements & data
│   │   ├── copy-editor.md             # Professional writing
│   │   ├── senior-pm.md               # Product strategy
│   │   ├── senior-project-manager.md  # Timeline & resources
│   │   └── moneypenny.md              # Triage & admin
│   └── context/                   # Work context files
│       └── *.template                 # Template files (committed)
│
├── .claude/                   # Claude Code skills (shared)
│   └── skills/
│       ├── inbox-processing/          # GTD inbox → databases
│       ├── standup-report/            # Daily standup (WorkOS)
│       ├── exec-update/               # Executive updates (WorkOS)
│       ├── meeting-prep/              # Meeting preparation (WorkOS)
│       └── tech-decision/             # ADR generator (WorkOS)
│
├── databases/                 # Structured data (Dataview-powered)
│   ├── tasks/                     # All tasks
│   │   ├── README.md                  # Database documentation
│   │   ├── _schema.md                 # Frontmatter template
│   │   └── example-*.md               # Example files
│   ├── journal/                   # Daily reflections
│   ├── books/                     # Reading list
│   ├── expenses/                  # Monthly bills & tracking
│   ├── meetings/                  # Meeting notes archive
│   ├── cabinet/                   # Cabinet meeting archive
│   └── time-tracking/             # Time logging
│
├── dashboards/                # Dataview query dashboards
│   ├── home.md                    # The Atlas - Master command center
│   ├── finances.md                # Financial dashboard
│   ├── books.md                   # Reading dashboard
│   ├── ideas-board.md             # Ideas pipeline
│   ├── project-health.md          # Project tracking
│   └── metrics.md                 # Historical trends
│
├── projects/                  # Projects and ideas
│   ├── ideas/                     # Individual idea files
│   └── prds/                      # Product requirement docs
│
├── reflections/               # Daily/weekly/monthly reviews
│   ├── daily/
│   ├── weekly/
│   └── monthly/
│
├── writing/                   # Blog posts and essays
│   ├── drafts/
│   ├── published/
│   └── essays/
│
├── templates/                 # Templater templates
│   ├── new-idea.md
│   ├── new-project.md
│   ├── new-task.md
│   └── [review templates]
│
├── meetings/                  # Meeting prep and notes (WorkOS)
├── decisions/                 # ADRs and technical decisions (WorkOS)
├── communications/            # Drafts and stakeholder updates (WorkOS)
│
└── assets/                    # Images and media
    ├── agents/                    # Agent avatar images
    └── voices/                    # Agent voice profiles (planned)
```

---

## The Cabinet: 14 LifeOS Personal Agents

**Status:** All 14 agents active (available when using LifeOS)

### Strategic Council (Inner Circle)

**⚡ Atlas (COO)** - Chief Operating Officer
- **Domain:** Life optimization, balance, energy management, operational synthesis
- **Personality:** Tyrion Lannister - Witty, sardonic, brutally pragmatic
- **Invoke:** `"Atlas, am I overcommitted this week?"`
- **File:** `.system/agents/atlas-operations.md`

**💰 Banker (CFO)** - Chief Financial Officer
- **Domain:** Wealth building, real estate, investments, portfolio strategy
- **Invoke:** `"Banker, should I invest in index funds or individual stocks?"`
- **File:** `.system/agents/banker.md`

**🎯 Strategist (CSO)** - Chief Strategy Officer
- **Domain:** Career strategy + political tactics, professional growth + crisis navigation
- **Personality:** Tywin Lannister - Strategic, legacy-focused, ruthlessly effective
- **Invoke:** `"Strategist, how do I negotiate this salary offer?"`
- **File:** `.system/agents/strategist.md`

**🧘 Sage** - The Oracle
- **Domain:** Philosophy, meaning, values alignment, perspective
- **Invoke:** `"Sage, help me understand this decision from a values perspective"`
- **File:** `.system/agents/sage.md`

**🪖 Spartan** - Secretary of Defense
- **Domain:** Physical security, fitness, warrior mindset, tactical preparedness
- **Personality:** Spartan warrior - Discipline, excellence
- **Invoke:** `"Spartan, what should my workout plan look like?"`
- **File:** `.system/agents/spartan.md`

### Execution Division

**🏗️ Engineer (CTO)** - Chief Technology Officer
- **Domain:** Technical strategy + code quality, architecture + security
- **Invoke:** `"Engineer, review this system architecture"`
- **File:** `.system/agents/execution/engineer.md`

**🎨 Designer (CDO)** - Chief Design Officer
- **Domain:** UI/UX design, design systems, aesthetic excellence
- **Invoke:** `"Designer, critique this interface layout"`
- **File:** `.system/agents/execution/designer.md`

**✏️ Artist** - Creative Director
- **Domain:** Fine art practice + creative learning curation
- **Invoke:** `"Artist, how should I structure my drawing practice?"`
- **File:** `.system/agents/execution/artist.md`

### Growth & Optimization Division

**🔧 Maker** - Chief Hardware Officer
- **Domain:** Physical builds, electronics, IoT, smart home, drones
- **Personality:** Adam Savage - Enthusiastic builder, experimental
- **Invoke:** `"Maker, help me design this smart home automation"`
- **File:** `.system/agents/growth/maker.md`

**✍️ Storyteller** - Chief Content Officer
- **Domain:** Blog posts, newsletters, writing, content strategy
- **Personality:** Austin Kleon + Ann Handley
- **Invoke:** `"Storyteller, help me draft this blog post"`
- **File:** `.system/agents/growth/storyteller.md`

**📊 Analyst (Ada)** - Chief Data Officer
- **Domain:** Life tracking, metrics, quantified self, pattern recognition
- **Personality:** Ada Lovelace + Nate Silver + Edward Tufte
- **Invoke:** `"Ada, what patterns do you see in my time tracking data?"`
- **File:** `.system/agents/growth/analyst.md`

**🤝 Connector** - Chief Relationship Officer
- **Domain:** Personal relationships, friendship, family bonds, social health
- **Personality:** Brené Brown + Dale Carnegie
- **Invoke:** `"Connector, how can I strengthen my relationships?"`
- **File:** `.system/agents/growth/connector.md`

**💚 Healer** - Chief Health Officer
- **Domain:** Sleep optimization, nutrition, longevity, stress management
- **Personality:** Andrew Huberman + Peter Attia
- **Invoke:** `"Healer, optimize my sleep routine"`
- **File:** `.system/agents/growth/healer.md`

**📚 Professor** - Literary Critic & Reading Mentor
- **Domain:** Literature, deep reading, literary criticism, book recommendations
- **Personality:** Harold Bloom - Cantankerous, erudite, passionate
- **Invoke:** `"Professor, what should I read next?"`
- **File:** `.system/agents/growth/professor.md`

### Cabinet Meeting Functionality

**Multi-agent consultation for complex decisions:**
```
"Cabinet meeting about: should I take this job offer?"
"Weekly Cabinet meeting" (Sunday retrospective)
"Get perspectives from Atlas, Banker, and Strategist on [decision]"
```

**Cabinet Meeting Process:**
1. Agent selection based on decision complexity
2. Individual domain-specific perspectives
3. Conflict identification (when agents disagree)
4. Synthesis and integrated recommendation
5. Clear next steps with trade-offs

---

## The Professional Team: 8 WorkOS Agents

**Status:** All 8 agents active (available when using WorkOS branch)

### Technical Experts

**🖥️ Frontend Engineer**
- **Domain:** React, TypeScript, UI architecture, component design, accessibility
- **Invoke:** `"Frontend Engineer, review this component architecture"`
- **File:** `.workos/agents/frontend-engineer.md`

**⚙️ Backend Engineer**
- **Domain:** REST/GraphQL APIs, databases, system design, security, scalability
- **Invoke:** `"Backend Engineer, design an API for user authentication"`
- **File:** `.workos/agents/backend-engineer.md`

**👷 Engineering Lead**
- **Domain:** Team coordination, technical strategy, architecture decisions
- **Invoke:** `"Engineering Lead, what's the best approach for this project?"`
- **File:** `.workos/agents/engineering-lead.md`

### Business & Strategy

**📊 Business Analyst**
- **Domain:** Requirements gathering, data analysis, stakeholder management
- **Invoke:** `"Business Analyst, help me refine these requirements"`
- **File:** `.workos/agents/business-analyst.md`

**📝 Copy Editor**
- **Domain:** Professional writing, documentation, executive communication
- **Invoke:** `"Copy Editor, polish this executive update"`
- **File:** `.workos/agents/copy-editor.md`

**🎯 Senior Product Manager**
- **Domain:** Product strategy, roadmap, prioritization, vision
- **Invoke:** `"Senior PM, help me prioritize these features"`
- **File:** `.workos/agents/senior-pm.md`

### Operations & Coordination

**📅 Senior Project Manager**
- **Domain:** Timeline management, resource allocation, risk mitigation
- **Invoke:** `"Senior Project Manager, create a timeline for this project"`
- **File:** `.workos/agents/senior-project-manager.md`

**💼 Moneypenny** - Administrative Assistant
- **Domain:** Task routing, meeting prep, information synthesis
- **Personality:** M's assistant from James Bond - Efficient, discreet, proactive
- **Invoke:** `"Moneypenny, which agent should I consult for this?"`
- **File:** `.workos/agents/moneypenny.md`

---

## Agent Invocation Patterns

### Single Agent Consultation

```
"Atlas, am I overcommitted this week?"
"Banker, should I invest in index funds?"
"Frontend Engineer, is this the right React pattern?"
```

### Multi-Agent Consultation

```
"I need Atlas and Strategist perspectives on this career decision"
"Get Banker and Engineer input on building vs buying software"
"Frontend Engineer and Designer, review this UI design"
```

### Cabinet Meeting (Complex Decisions)

```
"Cabinet meeting about: should I quit my job to build a startup?"
"Weekly Cabinet meeting" (Sunday retrospective)
```

### Context-Aware Guidance

**Agents read context files for personalized advice:**
- `.system/context/preferences.md` - Your values, working style, life goals
- `.system/context/career.md` - Career history, strategy, skills
- `.system/context/wealth.md` - Financial situation, investment strategy
- `.system/context/art.md` - Art practice, learning resources
- `.system/context/health.md` - Health goals, fitness routines
- `.system/context/social.md` - Relationship priorities
- `.system/context/content.md` - Writing projects, content strategy
- `.system/context/queue.md` - Current projects and priorities

**When on WorkOS branch:**
- `.workos/context/company-info.md` - Company structure, culture, processes
- `.workos/context/team-directory.md` - Team members, roles
- `.workos/context/current-projects.md` - Active work projects
- `.workos/context/tech-stack.md` - Technologies used
- `.workos/context/stakeholders.md` - Key stakeholders, priorities

**Important:** When giving advice, **always read the relevant context files first**. Never hallucinate or make up personal information. If context files are empty or missing, acknowledge that and provide general guidance.

---

## Database System

LifeOS uses **7 structured databases** powered by Dataview for dynamic querying:

### Database Structure

Each database follows a consistent pattern:
- `databases/{name}/` - Directory for each database
- `README.md` - Database documentation
- `_schema.md` - Frontmatter template showing all fields
- `example-*.md` - Example files demonstrating proper structure
- User files use descriptive names (protected by `.gitignore`)

### The 7 Databases

**1. tasks/** - All tasks (single source of truth)
- Frontmatter: `title`, `status`, `priority`, `due_date`, `project`, `effort`, `tags`
- Example: `databases/tasks/example-task-setup-project.md`

**2. journal/** - Daily reflections
- Frontmatter: `date`, `energy`, `mood`, `tags`
- Example: `databases/journal/example-daily-2025-01-15.md`

**3. books/** - Reading list
- Frontmatter: `title`, `author`, `status`, `rating`, `started`, `finished`, `tags`
- Schema: `databases/books/_schema.md`

**4. expenses/** - Monthly bills & financial tracking
- Frontmatter: `description`, `amount`, `category`, `due_date`, `status`, `tags`
- Schema: `databases/expenses/_schema.md`

**5. meetings/** - Meeting notes archive
- Frontmatter: `title`, `date`, `attendees`, `agenda`, `notes`, `action_items`, `decisions`
- Schema: `databases/meetings/_schema.md`

**6. cabinet/** - Cabinet meeting archive
- Frontmatter: `date`, `topic`, `agents_consulted`, `decision`, `next_steps`
- Schema: `databases/cabinet/_schema.md`

**7. time-tracking/** - Time logging
- Frontmatter: `date`, `project`, `duration`, `category`, `notes`
- Schema: `databases/time-tracking/_schema.md`

### Working with Databases

**When creating files in databases:**
1. Always check `_schema.md` for required frontmatter fields
2. Review `example-*.md` files for proper format
3. Use consistent naming: `YYYY-MM-DD-description.md` or `descriptive-name.md`
4. Include all required frontmatter fields
5. Link to related files with `[[wiki-links]]`

**When querying databases:**
- Use Dataview query language (see dashboards for examples)
- Query from dashboards, not directly in database folders
- Keep queries performant (limit results, filter appropriately)

---

## Claude Code Skills

Skills are automated workflows triggered by natural language. All skills are in `.claude/skills/`.

### Available Skills

**Inbox Processing** (`.claude/skills/inbox-processing/`)
- **Trigger:** "Process my inbox" or "Help me process inbox"
- **What it does:** Converts unstructured items in `_inbox_.md` into structured database entries
- **Output:** Creates files in `databases/tasks/`, `projects/ideas/`, `databases/journal/`, etc.
- **Usage:** Run at end of day to organize captured items

**Standup Report** (`.claude/skills/standup-report/`) - WorkOS
- **Trigger:** "Generate my standup report"
- **What it does:** Creates daily standup update based on tasks and meetings
- **Output:** `communications/standups/YYYY-MM-DD.md`

**Executive Update** (`.claude/skills/exec-update/`) - WorkOS
- **Trigger:** "Create exec update for this week"
- **What it does:** Generates executive summary of progress, risks, next steps
- **Output:** `communications/exec-updates/YYYY-MM-DD.md`

**Meeting Prep** (`.claude/skills/meeting-prep/`) - WorkOS
- **Trigger:** "Prepare briefing for [meeting name]"
- **What it does:** Creates comprehensive meeting preparation document
- **Output:** `meetings/prep/YYYY-MM-DD-meeting-name.md`

**Technical Decision** (`.claude/skills/tech-decision/`) - WorkOS
- **Trigger:** "Help document this technical decision"
- **What it does:** Creates Architecture Decision Record (ADR)
- **Output:** `decisions/YYYY-MM-DD-decision-name.md`

### Creating Custom Skills

See `.claude/skills/inbox-processing/SKILL.md` for skill structure reference.

---

## Dashboard System

Dashboards use Dataview to create dynamic views of your data. Located in `dashboards/`.

### Key Dashboards

**The Atlas** (`dashboards/home.md`)
- Master command center
- Daily Cabinet wisdom quote (98 rotating quotes)
- Top 5 priorities (auto-sorted by urgency)
- Today's tasks and action items
- Active projects and health status
- Recent wins and learnings

**Finances** (`dashboards/finances.md`)
- Bills due this week
- Monthly burn rate
- Income vs expenses
- Cash flow analysis

**Books** (`dashboards/books.md`)
- Currently reading
- Reading queue
- Reading statistics
- Professor recommendations

**Project Health** (`dashboards/project-health.md`)
- Active projects status
- Blocked tasks
- Upcoming deadlines
- Resource allocation

**Metrics** (`dashboards/metrics.md`)
- Time tracking analysis
- Productivity trends
- Energy level patterns
- Goal progress

---

## File Creation Guidelines

### When Creating New Files

**Use proper markdown formatting:**
- Headers: `#` for title, `##` for sections, `###` for subsections
- Lists: `-` for bullets, `1.` for numbered lists
- Links: `[[wiki-links]]` for internal, `[text](url)` for external
- Code: `` `inline` `` or ` ```language ` for blocks

**Include YAML frontmatter:**
- Check `databases/{type}/_schema.md` for required fields
- Use consistent date format: `YYYY-MM-DD`
- Add relevant tags
- Link to related files

**Follow naming conventions:**
- Tasks: `descriptive-task-name.md`
- Journal: `YYYY-MM-DD.md`
- Meetings: `YYYY-MM-DD-meeting-name.md`
- Projects: `project-name.md`
- Ideas: `descriptive-idea-name.md`

### File Creation by Type

**Tasks** (`databases/tasks/`)
```yaml
---
title: Task name
status: pending|in-progress|completed|blocked
priority: critical|high|medium|low
due_date: YYYY-MM-DD
project: [[project-name]]
effort: 1-4 (hours)
tags: [domain, category]
---
```

**Journal** (`databases/journal/`)
```yaml
---
date: YYYY-MM-DD
energy: 1-10
mood: positive|neutral|negative
tags: [reflection, wins, learnings]
---
```

**Projects** (`projects/prds/`)
- Use `projects/prds/_prd_template.md` as starting point
- Include: summary, goals, success criteria, timeline, resources

**Ideas** (`projects/ideas/`)
- Quick capture of ideas
- Include: description, potential value, next steps
- Link to related projects or domains

**Meetings** (`databases/meetings/`)
```yaml
---
title: Meeting name
date: YYYY-MM-DD
attendees: [Person 1, Person 2]
tags: [work, personal]
---

## Agenda
- Item 1
- Item 2

## Notes
[Meeting notes]

## Action Items
- [ ] Task 1
- [ ] Task 2

## Decisions
- Decision 1
- Decision 2
```

---

## Privacy & Data Protection

### Privacy Architecture

**Layer 1: Branch Isolation**
- `main` and `workos` branches never pushed to public remote
- Only `oss-template` goes to public repo
- Even with `.gitignore` mistakes, personal data stays on private branches

**Layer 2: .gitignore Protection**
```gitignore
# Context files (user fills these in)
.system/context/*.md
!.system/context/*.template

# Personal data (keep examples only)
databases/tasks/*.md
!databases/tasks/example-*.md
!databases/tasks/_schema.md
!databases/tasks/README.md
```

**Layer 3: Manual Review**
- Always review changes before public push
- Search for personal information leaks
- Use `git diff` before committing to `oss-template`

### Best Practices

**Do:**
- ✅ Commit to `main` and `workos` freely (private repo)
- ✅ Cherry-pick infrastructure improvements to `oss-template`
- ✅ Review each commit before pushing to public
- ✅ Use `.template` files for context in public template

**Don't:**
- ❌ Push `main` or `workos` to public remote
- ❌ Commit personal data to `oss-template`
- ❌ Share real project/task/journal data as examples
- ❌ Include real names, emails, companies in public commits

### Context File Setup (First-Time Users)

**On main or workos branch:**

1. **Copy template files to create your context:**
```bash
# Personal context
cp .system/context/preferences.template .system/context/preferences.md
cp .system/context/career.template .system/context/career.md
cp .system/context/wealth.template .system/context/wealth.md
# ... repeat for all templates

# Work context (if using workos branch)
cp .workos/context/company-info.template .workos/context/company-info.md
cp .workos/context/team-directory.template .workos/context/team-directory.md
# ... repeat for all templates
```

2. **Fill in your personal information in the .md files**
   - These are automatically gitignored
   - Agents will read these for personalized guidance
   - Keep them updated as your situation changes

3. **Never commit the .md versions** (they're in .gitignore)

---

## Working with This System

### Daily Workflow

**Morning (5-10 minutes):**
1. Open `dashboards/home.md` (The Atlas)
2. Review Cabinet wisdom quote
3. Check top 3 priorities
4. Review today's tasks
5. Optional: Generate morning brief (future skill)

**During Day:**
- Quick capture to `_inbox_.md` (unstructured)
- Consult agents as needed for decisions
- Update task statuses (`pending` → `in-progress` → `completed`)
- Log time in `databases/time-tracking/`

**Evening Review (15-20 minutes):**
1. Run inbox processing skill: "Process my inbox"
2. Update task statuses
3. Create journal entry in `databases/journal/`
4. Prepare tomorrow's top 3 priorities
5. Review project health

**Weekly (Sunday evening, 60-90 minutes):**
1. Weekly Cabinet meeting (complex decisions)
2. Review project health dashboard
3. Plan next week priorities
4. Financial check-in (expenses, budget)
5. Update context files if needed

### Agent Consultation Guidelines

**When to consult an agent:**
- Making a complex decision
- Need domain expertise
- Stuck on a problem
- Want a different perspective
- Need help with planning

**How to get good advice:**
1. Provide context in your question
2. Reference relevant files or projects
3. Be specific about what you need
4. Ask follow-up questions
5. Use multi-agent consultation for big decisions

**Example consultations:**

Good: "Atlas, looking at my tasks and calendar, am I overcommitted this week? I have 3 client projects and want to start learning Rust."

Better: "Cabinet meeting about: Should I quit my job to build a startup? Context: I have $50k saved, burn rate is $3k/month, startup idea is in databases/ideas/saas-platform.md"

---

## Contributing to LifeOS-OSS

If you're on the `oss-template` branch and want to contribute improvements:

### Contribution Types

**Welcome:**
- New agents or agent improvements
- New skills or skill enhancements
- Dashboard improvements
- Documentation improvements
- Bug fixes
- Example files

**Guidelines:**
- Follow existing structure and patterns
- Test thoroughly
- Add documentation
- Include examples
- Review for personal data before committing

**See [CONTRIBUTING.md](CONTRIBUTING.md) for complete guidelines.**

### Cherry-Picking from Private Branches

If you built something useful on `main` or `workos` and want to share it publicly:

```bash
# 1. Find the commit on your private branch
git checkout main
git log --oneline -10

# 2. Switch to oss-template
git checkout oss-template

# 3. Cherry-pick the commit
git cherry-pick <commit-hash>

# 4. Review for personal data
git diff HEAD~1
grep -r "PERSONAL_NAME\|EMAIL\|COMPANY" .

# 5. If clean, push to public
git push origin oss-template

# 6. If has personal data, amend
git reset HEAD~1
# ... remove personal data ...
git add -A
git commit -m "Add feature (sanitized)"
git push origin oss-template
```

---

## System Philosophy

### AI-Native Infrastructure

LifeOS is built for **human + AI collaboration**, not AI replacement:
- Agents provide domain expertise and perspectives
- You make the final decisions
- AI handles repetitive tasks (skills)
- Human focuses on strategy and creativity

### Sustainable Productivity

**Not productivity theater:**
- Focus on outcomes, not activity
- Protect energy, not just time
- Build systems, don't rely on willpower
- Sustainable pace beats burnout sprint

### Privacy First

**Your data, your control:**
- All data local (Obsidian vault)
- Version control optional
- No cloud dependencies
- No telemetry or tracking

---

## Getting Help

**For system questions:**
- Review this CLAUDE.md file
- Check [README.md](README.md) for getting started guide
- Review [ARCHITECTURE.md](ARCHITECTURE.md) for design decisions

**For agent questions:**
- Invoke the relevant agent directly
- Try multi-agent consultation for complex issues
- Check agent files in `.system/agents/` or `.workos/agents/`

**For bugs or features:**
- Check [GitHub Issues](https://github.com/kcwoodfield/LifeOS-OSS/issues)
- Review [CONTRIBUTING.md](CONTRIBUTING.md)
- Open a new issue with clear description

---

## Key Reminders

**When working with agents:**
- Agents read context files first (`.system/context/*.md` or `.workos/context/*.md`)
- Never hallucinate personal information
- Provide personalized advice based on actual context
- If context files are empty, acknowledge and provide general guidance

**When creating files:**
- Always use proper frontmatter (check `_schema.md`)
- Follow naming conventions
- Link to related files with `[[wiki-links]]`
- Keep example files generic (no personal data)

**When on oss-template branch:**
- Never commit personal data
- Use `.template` files for context examples
- Only commit infrastructure and examples
- Review changes before pushing to public

**When switching branches:**
- `main` = Personal LifeOS (14 agents, personal context)
- `workos` = Professional WorkOS (8 agents, work context)
- `oss-template` = Public template (all agents, no personal data)

---

**Built for living intentionally. Maintained with discipline. Executed with clarity.**

*LifeOS - Your AI-native infrastructure for life orchestration*
