# LifeOS - Personal Operating System

**Your AI-native life orchestration system**

LifeOS is a comprehensive personal knowledge management and life orchestration system built on Obsidian + Claude Code. It combines 14 specialized AI agents, structured data management, and automated workflows to help you live intentionally across all life domains.

---

## What is LifeOS?

LifeOS provides you with an AI-powered personal operating system featuring:

**The Cabinet:** 14 specialized AI agents across 3 divisions
- **Strategic Council:** Atlas (COO), Banker (CFO), Strategist (CSO), Sage (Oracle), Spartan (Defense)
- **Execution Division:** Engineer (CTO), Designer (CDO), Artist (Creative Director)
- **Growth Division:** Maker, Storyteller, Analyst (Ada), Connector, Healer, Professor

**Structured Data Management:**
- 7 databases (tasks, journal, books, expenses, meetings, cabinet, time-tracking)
- Dynamic Dataview dashboards
- Version-controlled markdown

**Automated Workflows:**
- Morning briefings
- Cabinet meetings
- Project health checks
- Weekly reviews

---

## Quick Start

### Prerequisites

1. **Obsidian** - Download from [obsidian.md](https://obsidian.md)
2. **Claude Code** - Install from [claude.com/code](https://claude.com/code)
3. **Git** - For version control (recommended)

### Installation

1. **Fork or clone this repository:**
   ```bash
   git clone https://github.com/kcwoodfield/LifeOS-OSS.git
   cd LifeOS-OSS
   ```

2. **Open in Obsidian:**
   - Open Obsidian
   - Click "Open folder as vault"
   - Select the `LifeOS-OSS` directory

3. **Install required Obsidian plugins:**
   - Dataview (required - for dashboards)
   - Templater (recommended - for templates)
   - Database Folder (optional - for database management)

   Settings → Community Plugins → Browse → Search for each plugin

4. **Fill in your context files:**
   - Navigate to `.system/context/`
   - Copy each `.template` file and remove the `.template` extension
   - Fill in your personal information
   - **Important:** Add these to .gitignore to keep private

5. **Set up git privacy (if using version control):**
   ```bash
   # Add your personal context files to .gitignore
   echo ".system/context/*.md" >> .gitignore
   echo "!.system/context/*.template" >> .gitignore
   ```

6. **Test agent invocation:**
   Open Claude Code in the vault directory:
   ```bash
   claude-code .
   ```

   Try: "Atlas, what should I focus on today?"

---

## Core Features

### 1. The Cabinet (14 AI Agents)

Your personal advisory team, available 24/7:

**Strategic Council:**
- **Atlas (COO)** - Life optimization, energy management, operational balance
- **Banker (CFO)** - Wealth building, investments, financial freedom
- **Strategist (CSO)** - Career strategy, professional positioning
- **Sage (Oracle)** - Philosophy, values, meaning, perspective
- **Spartan (Defense)** - Fitness, security, discipline, mental toughness

**Execution Division:**
- **Engineer (CTO)** - Technical strategy, code quality, architecture
- **Designer (CDO)** - UI/UX design, aesthetics, design systems
- **Artist (Creative Director)** - Fine art practice, creative learning

**Growth & Optimization:**
- **Maker** - Hardware, DIY, electronics, physical builds
- **Storyteller** - Writing, content, thought leadership
- **Analyst (Ada)** - Data tracking, metrics, quantified self
- **Connector** - Relationships, networking, social health
- **Healer** - Sleep, nutrition, longevity, wellness
- **Professor** - Literature, deep reading, intellectual growth

**Usage:**
```
"Atlas, am I overcommitted this week?"
"Banker, should I invest in index funds or individual stocks?"
"Cabinet meeting about: should I take this new job offer?"
```

### 2. Database System (Dataview-Powered)

Seven structured databases for different life domains:

- **tasks/** - All tasks with priority, due dates, effort tracking
- **journal/** - Daily reflections with energy and mood tracking
- **books/** - Reading list with Professor integration
- **expenses/** - Monthly bills and financial tracking
- **meetings/** - Meeting notes archive
- **cabinet/** - Cabinet meeting archive
- **time-tracking/** - Time logging and analysis

Each database has:
- `_schema.md` - Frontmatter template
- `README.md` - Documentation
- Example files to learn from

### 3. Dynamic Dashboards

**The Atlas** (`dashboards/home.md`) - Your command center:
- Daily Cabinet wisdom (98 rotating quotes)
- Top 5 priorities (auto-sorted)
- Today's tasks and action items
- Active projects and health status
- Recent wins and learnings

**Financial Dashboard** (`dashboards/finances.md`):
- Bills due this week
- Monthly burn rate
- Income vs. expenses
- Cash flow analysis

**Books Dashboard** (`dashboards/books.md`):
- Currently reading
- Reading queue
- Reading statistics
- Professor recommendations

### 4. Claude Code Skills

Automated workflows triggered by natural language:

- **Morning Brief** - "Generate my morning brief"
- **Cabinet Meeting** - "Cabinet meeting about [topic]"
- **Project Health** - "Check project health"
- **Weekly Review** - "Weekly review"

---

## Daily Workflow

**Morning (5-10 minutes):**
1. Check The Atlas dashboard
2. Review top 3 priorities
3. Optional: Generate morning brief

**During Day:**
- Quick capture to `_inbox_.md`
- Consult agents as needed
- Update task statuses

**Evening Review (15-20 minutes):**
1. Process inbox → structured databases
2. Update tasks (mark complete, note blockers)
3. Journal entry in `databases/journal/`
4. Prepare tomorrow's priorities

**Weekly (Sunday evening, 60-90 minutes):**
1. Weekly Cabinet meeting
2. Review project health
3. Plan next week priorities
4. Financial check-in

---

## Architecture

### Directory Structure

```
LifeOS/
├── .system/              # LifeOS infrastructure (hidden)
│   ├── agents/               Personal agents (14 agents)
│   ├── context/              Personal context files
│   ├── data/                 System data (cabinet quotes)
│   ├── schemas/              Dataview schemas
│   └── scripts/              Automation scripts
│
├── .workos/              # WorkOS infrastructure (optional)
│   ├── agents/               Work agents (8 professional agents)
│   ├── context/              Work context files
│   └── skills/               Work-specific skills
│
├── .claude/              # Claude Code skills
│   └── skills/               Shared automation skills
│
├── databases/            # Structured data
│   ├── tasks/
│   ├── journal/
│   ├── books/
│   ├── expenses/
│   ├── meetings/
│   ├── cabinet/
│   └── time-tracking/
│
├── dashboards/           # Dataview dashboards
├── projects/             # Projects and ideas
├── reflections/          # Daily/weekly/monthly reviews
├── writing/              # Blog posts and essays
├── templates/            # Templater templates
├── assets/               # Images and media
└── _inbox_.md            # Quick capture entry point
```

### Branch Strategy (for advanced users)

LifeOS supports a three-branch model for privacy:

- **main** - Your personal data (private)
- **workos** - Your work data (private, optional)
- **oss-template** - Public template (this branch)

See CONTRIBUTING.md for details on contributing back to LifeOS-OSS.

---

## Customization

### Adding Custom Agents

1. Create new file: `.system/agents/your-agent.md`
2. Define domain, personality, and principles
3. Add example use cases
4. Invoke with: "Your Agent, [question]"

### Creating Custom Dashboards

1. Create file in `dashboards/your-dashboard.md`
2. Use Dataview Query Language (DQL)
3. See `dashboards/README.md` for query examples

### Building Custom Skills

1. Create directory: `.claude/skills/your-skill/`
2. Add `SKILL.md` with skill definition
3. Define trigger phrases
4. See existing skills for examples

---

## WorkOS: Professional Work Companion

LifeOS includes **WorkOS** - a professional AI team for your day job:

**8 Work Agents:**
- Frontend Engineer, Backend Engineer, Engineering Lead
- Business Analyst, Copy Editor
- Senior Product Manager, Senior Project Manager
- Moneypenny (Admin Assistant)

**4 Work Skills:**
- Standup Report Generator
- Executive Update Generator
- Meeting Prep Assistant
- Technical Decision Framework

**To use WorkOS:**
1. Switch to `workos` branch (or create separate vault)
2. Fill in `.workos/context/` files with your company info
3. Invoke work agents: "Frontend Engineer, review this component"

---

## Privacy & Security

**Your data stays private:**
- All files are local markdown (no cloud required)
- Version control is optional
- `.gitignore` protects personal data if you use git
- No telemetry, no tracking, no external dependencies

**Best practices:**
- Don't commit `.system/context/` files (keep private)
- Use branches for work/personal separation
- Encrypt sensitive files if needed

---

## FAQ

**Q: Do I need coding skills?**
A: No. LifeOS is markdown-first. If you can write notes, you can use LifeOS.

**Q: Can I use this without Claude Code?**
A: Partially. The databases and dashboards work in Obsidian alone, but agents and skills require Claude Code.

**Q: How is this different from other productivity systems?**
A: LifeOS is AI-native, not bolt-on. Agents understand your context and provide personalized guidance across all life domains.

**Q: Can I use this with my own AI assistant?**
A: The infrastructure is compatible with any AI that can read markdown context. Claude Code integration provides the best experience.

**Q: What if I change jobs or life circumstances?**
A: Update your context files and the system adapts. LifeOS is designed to evolve with you over decades.

---

## Contributing

LifeOS-OSS is open source! We welcome contributions:

- Agent improvements
- New skills
- Dashboard templates
- Documentation improvements
- Bug reports

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Roadmap

### Current (v1.0)
- ✅ 14 personal agents
- ✅ 7 databases
- ✅ Dynamic dashboards
- ✅ 4 LifeOS skills
- ✅ WorkOS (8 work agents + 4 skills)

### Planned (v1.1)
- [ ] Mobile app companion
- [ ] Voice interface for agents
- [ ] Calendar integration
- [ ] Email automation (morning brief delivery)
- [ ] Additional skills (inbox processing, habit tracking)

### Future
- [ ] LifeOS community hub
- [ ] Plugin marketplace
- [ ] Agent prompt library
- [ ] Cross-platform sync

---

## Credits

Built on the shoulders of giants:
- **[Obsidian](https://obsidian.md)** - Knowledge management platform
- **[Claude Code](https://claude.com/code)** - AI-powered development environment
- **[Dataview](https://blacksmithgu.github.io/obsidian-dataview/)** - Query engine for Obsidian

Created by [LifeOS Creator](https://github.com/kcwoodfield)

---

## License

MIT License - Fork, customize, and make it your own.

---

## Support

- **Documentation:** See [CLAUDE.md](CLAUDE.md) for complete system guide
- **Issues:** [GitHub Issues](https://github.com/kcwoodfield/LifeOS-OSS/issues)
- **Discussions:** [GitHub Discussions](https://github.com/kcwoodfield/LifeOS-OSS/discussions)

---

**LifeOS: Your Personal Operating System**

*AI-native infrastructure for living intentionally*

**Get started in 15 minutes. Transform how you work and live.**
