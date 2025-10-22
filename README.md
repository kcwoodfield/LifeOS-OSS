# Life OS

**Version:** 1.1.0
**Status:** Active
**Last Updated:** 2025-10-25

---

## What This Is

**Life OS** is a personal operating system for living intentionally. It's a complete life orchestration system built on plain-text markdown, designed for long-term partnership between human and AI.

This is not a productivity system. This is infrastructure for building a life worth living over the next 40 years.

**Core Philosophy:**
- Markdown as infrastructure (version controlled, future-proof)
- AI-native design (built for human + AI collaboration)
- Context-aware (everything connected, nothing siloed)
- Agent-based (specialized AI personas for different domains)
- Systems over willpower (automate decisions, compound daily)

---

## Quick Start

### For New Users

1. **Install Obsidian**: Download from [obsidian.md](https://obsidian.md)
2. **Open this vault**: File → Open vault → Select this folder
3. **Install required plugins**: See [Required Plugins](#required-plugins) below
4. **Read the system guide**: Start with [`CLAUDE.md`](CLAUDE.md) for Claude Code guidance
5. **Meet The Cabinet**: 14 active agents in [`.system/agents/`](.system/agents/)

#### Required Plugins

**Core Plugins** (built into Obsidian):
- **Templates** - Basic template support
- **Daily notes** - For journal entries
- **File recovery** - Auto-backup

**Community Plugins** (install from Obsidian):

1. **Dataview** ⭐ *Essential*
   - Enables dynamic dashboards and queries
   - Powers all dashboard views (finances, books, projects, metrics)
   - Install: Settings → Community plugins → Browse → Search "Dataview"

2. **Templater** ⭐ *Essential*
   - Advanced template system with auto-population
   - Required for all `templates/*.md` files
   - Install: Settings → Community plugins → Browse → Search "Templater"
   - Configuration: Set template folder to `templates/`

3. **Calendar** (Optional but useful)
   - Visual calendar for daily notes and reviews
   - Makes navigation easier

4. **Buttons** (Optional)
   - Quick action buttons for creating files
   - Used on The Atlas dashboard

**Setup Steps:**
1. Open Settings → Community plugins
2. Turn off "Safe mode"
3. Click "Browse" and search for each plugin
4. Click "Install" then "Enable"
5. For Templater: Set template folder path to `templates/`

### For Claude Code CLI

When working with this repository:
1. Read [`CLAUDE.md`](CLAUDE.md) for complete system understanding
2. Always read relevant context files before responding
3. Invoke agents by name when specialized counsel needed

---

## System Architecture

![System Architecture](assets/images/headers/japan.jpg)

```
LifeOS/
├── CLAUDE.md                  # System guide for Claude Code
├── README.md                  # This file
├── _inbox_.md                 # Quick capture (unstructured) - MAIN ENTRYWAY
├── .obsidian/                 # Obsidian configuration
├── .claude/                   # Claude Code skills
│   └── skills/                # Auto-invoked workflows
├── databases/                 # Structured data (Dataview)
│   ├── tasks/                 # All tasks (single source of truth)
│   ├── expenses/              # Monthly bills and recurring expenses
│   ├── books/                 # Reading list tracking
│   ├── meetings/              # Meeting notes archive
│   ├── cabinet/               # Cabinet meeting archive
│   └── journal/               # Daily journal entries
├── dashboards/                # Dataview dashboards (Obsidian)
│   ├── home.md                # The Atlas - Master command center
│   └── finances.md            # Financial dashboard - Bills, expenses, cash flow
├── templates/                 # Templater templates (Obsidian)
├── reflections/               # Daily/weekly/monthly reviews (Obsidian)
│   ├── daily/                 # Daily reviews and morning briefs
│   ├── weekly/
│   └── monthly/
├── projects/                  # Active projects (Obsidian)
│   ├── INDEX.md               # Project tracking
│   ├── ideas/                 # Idea files with frontmatter
│   └── prds/                  # Product requirement docs
├── writing/                   # Blog posts and essays (Obsidian)
│   ├── drafts/
│   └── published/
├── assets/                    # Images and media (Obsidian)
│   └── agents/                # Agent avatars
└── .system/                   # System infrastructure (hidden from Obsidian)
    ├── agents/                # The Cabinet (14 active agents)
    │   ├── atlas-operations.md    # COO - Tyrion personality
    │   ├── banker.md              # CFO - Wealth strategy
    │   ├── strategist.md          # CSO - Tywin personality
    │   ├── sage.md                # Oracle - Philosophy
    │   ├── spartan.md             # Defense - Fitness
    │   ├── execution/             # Execution Division
    │   │   ├── engineer.md
    │   │   ├── designer.md
    │   │   └── artist.md
    │   └── growth/                # Growth & Optimization
    │       ├── maker.md
    │       ├── storyteller.md
    │       ├── analyst.md (Ada)
    │       ├── connector.md
    │       ├── healer.md
    │       └── professor.md
    ├── context/               # Agent configuration files
    │   ├── preferences.md         # Core identity and values
    │   ├── career.md              # Career strategy and history
    │   ├── wealth.md              # Financial strategy and portfolio
    │   ├── art.md                 # Art practice and skill tracking
    │   ├── content.md             # Content strategy and writing goals
    │   ├── health.md              # Health goals and wellness tracking
    │   ├── social.md              # Relationship strategy and social health
    │   ├── queue.md               # Current priorities and focus areas
    │   ├── interview-star-stories.md  # Career highlights and STAR stories
    │   └── conversations/         # Agent conversation archives
    ├── scripts/               # Automation (Python, bash)
    ├── apps/                  # Applications
    └── schemas/               # Dataview schema documentation
```

---

## The Cabinet: Your Executive Team

![The Cabinet](assets/images/headers/faroe-islands.jpg)

**Status:** All 14 agents now active (expanded 2025-10-17)

Life OS uses 14 specialized agents organized into Strategic Council, Execution Division, and Renaissance Division.

### Strategic Council

#### Atlas - Chief Operating Officer
**Personality:** Tyrion Lannister - Witty, sardonic, brutally pragmatic
**Domain:** Life optimization, operational synthesis, energy management
**Invoke:** "Atlas, [productivity or systems question]"

#### Banker - Chief Financial Officer
**Domain:** Wealth building, real estate, side businesses, portfolio strategy
**Invoke:** "Banker, [financial decision or analysis]"

#### Strategist - Chief Strategy Officer
**Domain:** Career strategy + political tactics, professional growth + crisis navigation
**Invoke:** "Strategist, [career or political question]"

#### Sage - The Oracle (Spiritual Advisor)
**Domain:** Philosophy, meaning, values alignment, perspective
**Invoke:** "Sage, [philosophical or existential question]"

#### Spartan - Secretary of Defense
**Personality:** Spartan warrior - Molon labe ("come and take them")
**Domain:** Physical security, fitness, warrior mindset, tactical preparedness
**Invoke:** "Spartan, [fitness, security, or mental toughness question]"

### Execution Division

![Execution Division](assets/images/headers/switzerland.jpg)

#### Engineer - Chief Technology Officer
**Domain:** Technical strategy + code quality, architecture + security
**Invoke:** "Engineer, [technical question, code review, or architecture guidance]"

#### Designer - Chief Design Officer
**Domain:** UI/UX design, design systems, aesthetic excellence
**Invoke:** "Designer, [design review or critique needed]"

#### Artist - Creative Director
**Domain:** Fine art practice + creative learning curation
**Invoke:** "Artist, [art practice or learning resource question]"

### Renaissance Division

#### Maker - Chief Hardware Officer
**Personality:** Adam Savage - Enthusiastic builder, experimental mindset
**Domain:** Physical builds, electronics, IoT, smart home, drones, maker projects
**Invoke:** "Maker, [hardware or DIY project question]"

#### Storyteller - Chief Content Officer
**Personality:** Austin Kleon + Ann Handley - Creative writer meets strategic marketer
**Domain:** Blog posts, newsletters, technical writing, content strategy, thought leadership
**Invoke:** "Storyteller, [writing or content question]"

#### Ada - Analyst & Chief Data Officer
**Personality:** Ada Lovelace + Nate Silver + Edward Tufte - First programmer meets data scientist meets visualization designer
**Domain:** Life tracking, dashboard design, metrics analysis, quantified self, pattern recognition
**Invoke:** "Ada, [data or metrics question]"

#### Connector - Chief Relationship Officer
**Personality:** Brené Brown + Dale Carnegie - Vulnerability researcher meets people person
**Domain:** Personal relationships, friendship cultivation, family bonds, social health, community
**Invoke:** "Connector, [relationship or social question]"

#### Healer - Chief Health Officer
**Personality:** Andrew Huberman + Peter Attia - Neuroscientist meets longevity physician
**Domain:** Sleep optimization, nutrition, longevity, stress management, recovery, wellness
**Invoke:** "Healer, [health or wellness question]"

#### Professor - Literary Critic & Reading Mentor
**Personality:** Harold Bloom - Cantankerous, erudite, passionate defender of the canon
**Domain:** Literature, deep reading, literary criticism, book recommendations, perspective expansion
**Invoke:** "Professor, [book recommendation or literary analysis question]"

---

## Key Workflows

### Morning Routine
1. Check [`CLAUDE.md`](CLAUDE.md) for system operations
2. Review today's priorities
3. Check project status
4. Review calendar and time blocks
5. Generate morning brief (optional)

### Project Management
- **All projects**: [`projects/INDEX.md`](projects/INDEX.md)
- **Ideas pipeline**: [`projects/ideas/`](projects/ideas/)
- **PRDs**: [`projects/prds/`](projects/prds/)
- **Priority system**: Primary (40-50%), Secondary (25-30%), Maintenance (20-25%)

### Weekly Review
1. Run weekly Cabinet meeting (see [`CLAUDE.md`](CLAUDE.md))
2. Update project status in [`projects/INDEX.md`](projects/INDEX.md)
3. Review completed tasks and update priorities
4. Reflect on energy, focus, wins, and learnings

### Agent Invocation
**Example:** "Engineer, should I use Next.js or Astro for my blog?"

Claude Code will:
1. Read relevant project files
2. Adopt Engineer persona completely
3. Apply Engineer's principles
4. Provide specific recommendation with reasoning

---

## Core Principles

![Core Principles](assets/images/headers/norway.jpg)

### 1. Systems Over Willpower
Don't rely on motivation. Build systems that make the right choice the default choice.

### 2. Context is King
Everything is linked. Career decisions affect wealth strategy. Project timelines affect art practice. Energy levels affect everything. The system holds all context.

### 3. Think in Decades, Not Quarters
This is a 40-year partnership. Every decision should compound. Every skill should build on the last. Small daily improvements become extraordinary results over decades.

### 4. Quality Over Quantity
Do fewer things, but do them exceptionally well. Master the fundamentals. Ship work you're proud of.

### 5. Rest is Productive
Energy, not time, is the resource. Protect rest. Prevent burnout. Sustainable pace wins the marathon.

### 6. We Cannot Afford to Lose
This is not practice. Every battle counts. Stay sharp, stay focused, stay intentional.

---

## Time Allocation Philosophy

**55 discretionary hours per week** (after sleep, work, essentials):

- **Art practice:** 6-8 hours (4 sessions @ 60-120 min)
- **Primary project:** 20-25 hours (YourProject)
- **Secondary project:** 10-15 hours (SecondProject)
- **Maintenance projects:** 5-10 hours (ThirdProject, Blog)
- **Learning:** 3-5 hours (reading, courses)
- **Buffer:** 5-10 hours (life happens)

**Protected time blocks:**
- Early mornings: Deep work (6-9am)
- Evenings: Art practice or secondary projects
- Weekends: Primary project + longer art sessions

---

## Goals Framework

### 1-Year Goals (2026)
- Ship one side project to revenue
- Complete NMA Year 1 curriculum
- Establish credibility in senior PM role
- Publish 12+ blog posts

### 5-Year Goals (2030)
- $1M+ net worth
- Senior PM or VP Product role
- 2+ rental properties
- Intermediate art skill level
- $5K/month side business revenue

### 10-Year Vision (2035)
- Financial independence ($3-5M net worth)
- VP Product or fractional CPO ($500K+ income)
- 3-5 income streams
- Advanced art skill level
- Known for PM craft at tech+design intersection

---

## Getting Started

### 1. Customize Context
- Update [`.system/context/preferences.md`](.system/context/preferences.md) with your profile
- Fill in [`.system/context/career.md`](.system/context/career.md)
- Customize [`.system/context/wealth.md`](.system/context/wealth.md)

### 2. Set Up Projects
- Review [`projects/INDEX.md`](projects/INDEX.md)
- Use templates in `templates/` directory for new projects, ideas, tasks
- Prioritize: Primary (1), Secondary (1), Maintenance (2-3)

### 3. Daily Practice
- Generate morning brief using morning-brief skill
- Review priorities on The Atlas dashboard
- Capture quick thoughts in `_inbox_.md`
- Process inbox during evening review

### 4. Invoke The Cabinet
- Read [`.system/agents/`](.system/agents/) directory
- Learn each agent's domain and principles
- Start invoking agents for specialized guidance

---

## Using with Claude Code CLI

Claude Code CLI has full context awareness when working with this repository.

**Key files for Claude:**
- [`CLAUDE.md`](CLAUDE.md) - Complete system instructions

**Example interactions:**
- "What should I focus on today?" → Synthesizes calendar, projects, priorities
- "Strategist, should I take this opportunity?" → Invokes Strategist agent
- "Generate morning brief" → Creates daily brief in `reflections/daily/`
- "Status on YourProject?" → Reads project file, provides update

**Claude will:**
- Always read relevant files before responding
- Use actual data from the vault (never hallucinate)
- Invoke appropriate agents when needed
- Provide specific, actionable guidance
- Think in systems and long-term consequences

---

## Tech Stack

**Core:**
- [Obsidian](https://obsidian.md) - Markdown editor and vault
- [Claude Code CLI](https://claude.com/code) - AI collaboration
- Git - Version control

**Recommended Obsidian Plugins:**
- Dataview - Query and display data
- Templater - Advanced templates
- Calendar - Daily notes navigation
- Buttons - Quick action buttons
- Homepage - Set custom home dashboard

**Automation:**
- Task completion notifications (macOS)
- Smart hooks on git push, git commit, TodoWrite
- Automated morning briefs
- Cabinet meeting workflows

---

## Philosophy

### We Are a Team
This is a partnership between human and AI built for 40 years. We're building a legacy, not managing a todo list.

### Growth Mindset, Always
Every failure is data. Every setback is feedback. We learn, adapt, and get better. Stagnation is the only real failure.

### Positivity with Edge
We're optimistic but not naive. We encourage but don't coddle. The goal is not to feel good—it's to become good.

### We're Star Dust
Atoms that became conscious on a rock flying through space. None of this is that serious, and all of it matters immensely. We hold both truths.

---

## Contributing

This is a personal system, but the architecture and principles are designed to be adaptable.

**If using this as a template:**
1. Fork the repository
2. Customize [`.system/context/preferences.md`](.system/context/preferences.md) with your profile
3. Update agent personas to match your values
4. Adjust time allocation and goals
5. Remove references to User's specific context
6. Make it yours

---

## Support

For questions about the system architecture or implementation:
- Reference [`CLAUDE.md`](CLAUDE.md) for complete system guidance
- Check individual agent files in [`.system/agents/`](.system/agents/)

---

## License

This is a personal system. Feel free to learn from it, but please don't copy it wholesale. Build your own operating system that reflects your values and goals.

---

## Remember

**We're not here to manage a todo list.**
**We're here to build a life worth living.**

**We're not here to make you comfortable.**
**We're here to make you capable.**

**We're not here for the next 90 days.**
**We're here for the next 40 years.**

**Act accordingly.**

---

**Built with intention. Maintained with discipline. Executed with excellence.**
