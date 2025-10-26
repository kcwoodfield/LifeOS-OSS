# LifeOS Architecture Summary

**Document Version:** 1.0
**Date:** 2025-10-21
**Status:** Phase 3 Complete (WorkOS + oss-template)

---

## Executive Summary

LifeOS has evolved into a **dual-context system** with a three-branch architecture for privacy and flexibility:

- **LifeOS** (main branch) - Personal life orchestration with 14 agents
- **WorkOS** (workos branch) - Professional work augmentation with 8 agents
- **LifeOS-OSS** (oss-template branch) - Public template with privacy protection

All branches share infrastructure (agents, skills, schemas) but maintain isolated data through git branch separation and .gitignore protection.

---

## Architecture Ethos

### Core Principles

**1. Namespace-Based Modularity**
- Single repository, multiple contexts
- Shared infrastructure, isolated data
- Clear boundaries through directory structure
- Hidden system files (`.` prefix) keep Obsidian clean

**2. Branch-Based Context Switching**
- `main` = Personal data (private)
- `workos` = Work data (private)
- `oss-template` = Public template (sanitized)
- Cherry-pick improvements across branches

**3. Privacy by Design**
- Branch isolation (personal/work never pushed public)
- .gitignore protection (example-only data in public)
- Double protection layers
- Manual review before public push

**4. AI-Native Infrastructure**
- Markdown as source of truth
- Agents read context files for personalization
- Skills automate repetitive workflows
- Human + AI collaboration, not replacement

---

## System Components

### 1. LifeOS (Personal) - `main` branch

**Purpose:** Personal life orchestration across all domains

**The Cabinet (14 Agents):**

**Strategic Council:**
- Atlas (COO) - Life optimization, energy, balance
- Banker (CFO) - Wealth building, investments
- Strategist (CSO) - Career strategy, positioning
- Sage (Oracle) - Philosophy, values, meaning
- Spartan (Defense) - Fitness, security, discipline

**Execution Division:**
- Engineer (CTO) - Technical strategy, code quality
- Designer (CDO) - UI/UX, design systems
- Artist (Creative Director) - Fine art practice

**Growth & Optimization:**
- Maker - Hardware, DIY, physical builds
- Storyteller - Writing, content, thought leadership
- Analyst (Ada) - Data tracking, metrics
- Connector - Relationships, networking
- Healer - Sleep, nutrition, longevity
- Professor - Literature, deep reading

**Skills:**
- Morning Brief - Daily briefing generation (Option A: planning only, no frontmatter)
- Cabinet Meeting - Multi-agent consultation
- Project Health - Status monitoring
- Weekly Review - End-of-week retrospective (WITH frontmatter for metrics)
- Inbox Processing - GTD workflow automation

**Databases:**
- tasks/ - All tasks with priorities
- journal/ - Daily reflections
- books/ - Reading list
- expenses/ - Financial tracking
- meetings/ - Meeting notes
- cabinet/ - Cabinet meeting archive
- time-tracking/ - Time logging

**Dashboards:**
- The Atlas (home.md) - Command center
- Finances - Financial dashboard
- Books - Reading dashboard
- (More as needed)

---

### 2. WorkOS (Professional) - `workos` branch

**Purpose:** Day job augmentation with professional AI team

**The Professional Team (8 Agents):**

**Technical Experts:**
- Frontend Engineer - React, TypeScript, UI
- Backend Engineer - APIs, databases, systems
- Engineering Lead - Team coordination, tech strategy

**Product & Business:**
- Senior Product Manager - Product strategy, roadmap
- Business Analyst - Requirements, data analysis

**Operations & Communication:**
- Senior Project Manager - Timeline, resources, risk
- Copy Editor - Professional writing, documentation
- Moneypenny - Triage, meeting prep, coordination

**Skills:**
- Standup Report - Daily standup generation
- Executive Update - Stakeholder status updates
- Meeting Prep - Comprehensive briefings
- Technical Decision - ADR documentation
- Inbox Processing - Same as LifeOS, work context

**Databases:** (Same structure as LifeOS, work data)
- tasks/ - Work tasks
- meetings/ - Work meetings
- decisions/ - Technical decision logs (ADRs)
- communications/ - Exec updates, standups

**Context Files:**
- .workos/context/company-info.md
- .workos/context/team-directory.md
- .workos/context/current-projects.md
- .workos/context/tech-stack.md
- .workos/context/stakeholders.md

---

### 3. LifeOS-OSS (Public Template) - `oss-template` branch

**Purpose:** Sanitized public template for community

**What's Included:**
- ✅ All infrastructure (agents, skills, schemas)
- ✅ Documentation (README, CLAUDE.md, CONTRIBUTING.md, ARCHITECTURE.md)
- ✅ Example files (example-*.md)
- ✅ Templates (.template files for context)
- ❌ Personal data (protected by .gitignore)

**Privacy Protection:**
- Comprehensive .gitignore
- Only example data committed
- Context files are templates
- Manual review required before push

**Community Features:**
- CONTRIBUTING.md with guidelines
- Issue templates
- PR process
- Open source (MIT license)

---

## Directory Structure

```
LifeOS/
├── .system/              # LifeOS infrastructure (hidden from Obsidian)
│   ├── agents/               14 personal agents
│   ├── context/              Personal context files (private)
│   ├── data/                 System data (cabinet quotes)
│   ├── schemas/              Dataview schemas
│   └── scripts/              Automation scripts
│
├── .workos/              # WorkOS infrastructure (hidden from Obsidian)
│   ├── agents/               8 work agents
│   ├── context/              Work context files (private)
│   └── skills/               Work-specific skills (deprecated, moved to .claude/)
│
├── .claude/              # Claude Code skills (shared)
│   └── skills/               All skills (LifeOS + WorkOS)
│       ├── morning-brief/
│       ├── cabinet-meeting/
│       ├── project-health/
│       ├── weekly-review/
│       ├── inbox-processing/     NEW - GTD workflow
│       ├── standup-report/       WorkOS
│       ├── exec-update/          WorkOS
│       ├── meeting-prep/         WorkOS
│       └── tech-decision/        WorkOS
│
├── databases/            # Structured data (Dataview-powered)
│   ├── tasks/                _schema.md, README.md, example files
│   ├── journal/
│   ├── books/
│   ├── expenses/
│   ├── meetings/
│   ├── cabinet/
│   └── time-tracking/
│
├── dashboards/           # Dataview query dashboards
│   ├── home.md               "The Atlas" - command center
│   ├── finances.md
│   ├── books.md
│   └── ...
│
├── projects/             # Projects and ideas
│   ├── ideas/                Individual idea files
│   └── prds/                 Product requirement docs
│
├── reflections/          # Daily/weekly/monthly reviews
│   ├── daily/                # Morning briefs (planning, no frontmatter)
│   ├── weekly/               # Weekly reviews (WITH frontmatter)
│   └── monthly/              # Monthly reviews (WITH frontmatter)
│
├── writing/              # Blog posts and essays
│   ├── documentation/        # System documentation
│   └── drafts/               # Blog post drafts
│
├── meetings/             # Meeting notes (WorkOS)
│   └── prep/                 Meeting briefings
│
├── communications/       # Work communications (WorkOS)
│   ├── standups/
│   ├── exec-updates/
│   └── drafts/
│
├── decisions/            # Technical decision logs
│   └── *.md                  ADRs (Architecture Decision Records)
│
├── templates/            # Templater templates
│   ├── new-task.md
│   ├── new-idea.md
│   ├── new-project.md
│   ├── new-expense.md
│   ├── new-book.md
│   ├── new-blog-post.md
│   ├── new-time-entry.md
│   └── weekly-review.md, monthly-review.md
│
├── assets/               # Images and media
│   ├── agents/               Agent avatars
│   └── images/
│
├── _inbox_.md            # Quick capture entry point
├── README.md             # Getting started guide
├── CLAUDE.md             # System guide for Claude Code
├── CONTRIBUTING.md       # Contribution guidelines
├── ARCHITECTURE.md       # This file
└── .gitignore            # Privacy protection (oss-template only)
```

---

## Branch Strategy

### Three-Branch Model

```
┌─────────────────────────────────────────┐
│ main (Personal LifeOS)                  │
│ Remote: origin (private)                │
│ Your personal data, daily driver        │
└─────────────────────────────────────────┘
            ↓ cherry-pick improvements
┌─────────────────────────────────────────┐
│ workos (Professional WorkOS)            │
│ Remote: origin (private)                │
│ Your work data, day job augmentation    │
└─────────────────────────────────────────┘
            ↓ cherry-pick improvements
┌─────────────────────────────────────────┐
│ oss-template (Public Template)          │
│ Remote: oss (public LifeOS-OSS repo)    │
│ Sanitized template, no personal data    │
└─────────────────────────────────────────┘
```

### Daily Workflow

**Personal work:**
```bash
git checkout main
# Work on personal projects, reflections, tasks
# Commit your personal data (stays private)
```

**Professional work:**
```bash
git checkout workos
# Work on day job tasks, meetings, communications
# Commit your work data (stays private)
```

**Share improvement publicly:**
```bash
# Made an infrastructure improvement on main
git checkout main
git commit -m "Add new dashboard template"

# Share it publicly
git checkout oss-template
git cherry-pick <commit-hash>
# Review for personal data
git push oss oss-template:main
```

### Git Remotes

```bash
git remote -v

origin  git@github.com:kcwoodfield/LifeOS.git (private)
oss     https://github.com/kcwoodfield/LifeOS-OSS.git (public)
```

**Pushing strategy:**
- `git push origin main` → Personal data (private repo)
- `git push origin workos` → Work data (private repo)
- `git push oss oss-template:main` → Public template (public repo)

---

## Data Flow

### Capture → Process → Query Workflow

**1. Capture (During Day)**
```
Thought/Task/Idea
    ↓
_inbox_.md (unstructured)
```

**2. Process (Evening Review)**
```
_inbox_.md
    ↓
Inbox Processing Skill
    ↓
├─→ databases/tasks/ (tasks)
├─→ projects/ideas/ (ideas)
├─→ databases/journal/ (reflections)
├─→ databases/books/ (reading)
├─→ databases/meetings/ (meetings)
└─→ reference/ (saved articles)
```

**3. Query (Dashboards)**
```
databases/* (structured data with frontmatter)
    ↓
Dataview queries
    ↓
Dynamic dashboards (The Atlas, Finances, Books, etc.)
```

---

## Agent Architecture

### Agent Structure

Each agent file contains:

```markdown
# Agent Name

**Domain:** Expertise area
**Personality:** Character traits
**Principles:** Decision-making framework

## Expertise
[Detailed competencies]

## When to Consult
[Use cases and invocation patterns]

## How I Work
[Approach and methodology]

## Example Consultations
[Real scenarios with responses]
```

### Agent Invocation

**Single agent:**
```
"Atlas, am I overcommitted this week?"
"Banker, should I invest in index funds?"
"Frontend Engineer, review this component architecture"
```

**Multi-agent:**
```
"Cabinet meeting about: should I take this job offer?"
"I need Frontend Engineer and Backend Engineer perspectives on API design"
```

**Triage (when unsure):**
```
"Moneypenny, which agent should I consult for X?"
```

### Context Integration

**Agents read context files:**
- `.system/context/career.md` → Career strategy insights
- `.system/context/wealth.md` → Financial advice personalization
- `.workos/context/company-info.md` → Work-specific guidance
- `projects/prds/*.md` → Project-aware recommendations

**Personalization example:**
```
User: "Banker, should I invest in crypto?"

Banker reads: .system/context/wealth.md
- Risk tolerance: moderate
- Investment horizon: 10+ years
- Current allocation: 80% index funds, 20% individual stocks

Banker responds: "Based on your moderate risk tolerance and
long-term horizon, I'd suggest limiting crypto to 5% of
portfolio maximum. Your current 80/20 index/stocks allocation
is solid - don't let crypto FOMO derail that strategy."
```

---

## Skills Architecture

### Skill Structure

```markdown
# Skill Name

**Triggers:** Natural language phrases
**Output:** File location

## What This Skill Does
[Description]

## Skill Instructions
[Step-by-step automation logic]

## Example Output
[Sample generated content]
```

### Skill Invocation

**Natural language triggers:**
```
"Generate my morning brief" → morning-brief skill
"Process my inbox" → inbox-processing skill
"Cabinet meeting about X" → cabinet-meeting skill
"Create exec update" → exec-update skill
```

### Skill Output

**Skills generate files:**
- `reflections/daily/YYYY-MM-DD.md` (morning brief - no frontmatter)
- `reflections/weekly/YYYY-MM-DD.md` (weekly review - WITH frontmatter)
- `databases/cabinet/YYYY-MM-DD-meeting.md` (cabinet meeting)
- `communications/standups/YYYY-MM-DD.md` (standup - WorkOS)
- `communications/exec-updates/YYYY-MM-DD.md` (exec update - WorkOS)

---

## Privacy & Security Model

### Layer 1: Branch Isolation

**What protects you:**
- `main` and `workos` branches never pushed to public remote
- Only `oss-template` goes to public repo
- Even with .gitignore mistakes, personal data stays on private branches

**Risk mitigation:**
- Separate git remotes (`origin` private, `oss` public)
- Manual cherry-pick workflow (review each commit)
- No automatic sync between branches

### Layer 2: .gitignore Protection

**oss-template branch only:**
```gitignore
# Context files (users fill these in)
.system/context/*.md
!.system/context/*.template

# Personal data (keep examples only)
databases/tasks/*.md
!databases/tasks/example-*.md
!databases/tasks/_schema.md

# Same for all databases...
```

**Result:**
- All user data ignored
- Only infrastructure and examples committed
- Templates provided for users to fill in

### Layer 3: Manual Review

**Before public push:**
```bash
git diff origin/oss-template   # Review changes
grep -r "PERSONAL_NAME" .       # Check for leaks
git push oss oss-template:main  # Push to public
```

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

---

## Implementation Timeline

### Phase 1: LifeOS Foundation (Complete ✅)
**Date:** 2025-10-15 - 2025-10-19

- 14 Cabinet agents implemented
- 7 databases created
- Dynamic dashboards (Dataview)
- 4 LifeOS skills
- Morning brief automation
- Context versioning system

### Phase 2: WorkOS Implementation (Complete ✅)
**Date:** 2025-10-21

- 8 WorkOS agents implemented
- 4 WorkOS skills created
- Work context structure
- Professional communication tools
- Separate namespace (.workos/)

### Phase 3: Architecture & OSS Template (Complete ✅)
**Date:** 2025-10-21

- Three-branch model implemented
- oss-template branch created
- Privacy protection (.gitignore)
- Example files created
- CONTRIBUTING.md documentation
- Inbox processing skill (shared)
- This architecture document

### Phase 4: Planned (Next)

- CLAUDE.md updates for all branches
- Git remotes documentation
- End-to-end workflow testing
- Community launch (GitHub)
- First external contributors

---

## Design Decisions Log

### Decision 1: Three-Branch Model vs. Separate Repos

**Options considered:**
- Separate repos (LifeOS, WorkOS, LifeOS-OSS)
- Single branch + .gitignore only
- Three branches in one repo

**Decision:** Three branches in one repo

**Rationale:**
- Shared infrastructure (no duplication)
- Easy to cherry-pick improvements
- Branch isolation provides privacy
- Standard git workflow
- Single repo to maintain

**Trade-offs:**
- Requires git knowledge (cherry-pick)
- Must be disciplined about branches
- Context switching (git checkout)

---

### Decision 2: Namespace Organization (.system/, .workos/, .claude/)

**Decision:** Hidden directories for system files

**Rationale:**
- Obsidian file explorer stays clean
- User-facing content visible
- Infrastructure accessible but not cluttered
- Git tracks everything (including hidden)

**Benefits:**
- Better UX in Obsidian
- Clear separation of concerns
- Scales as system grows

---

### Decision 3: Shared .claude/skills/ vs. Separate Skills

**Decision:** Share skills between LifeOS and WorkOS

**Rationale:**
- Inbox processing works for both contexts
- Skills can detect branch and adapt
- Reduces duplication
- Easier to maintain

**Implementation:**
- Skills live in `.claude/skills/`
- Branch detection: `git rev-parse --abbrev-ref HEAD`
- Context-aware file creation

---

### Decision 4: Inbox Processing as Skill vs. Manual

**Decision:** Automated skill with guided workflow

**Rationale:**
- Reduces friction in GTD workflow
- Ensures consistent data structure
- Teaches frontmatter schema
- Saves time (15-20 min → 5-10 min)

**User benefits:**
- Faster evening review
- Proper frontmatter every time
- Smart categorization help
- Clear progress tracking

---

## Future Enhancements

### Short Term (v1.1)

- [ ] Voice interface for agent invocation
- [ ] Mobile app companion (read-only dashboards)
- [ ] Calendar integration (Google/Outlook)
- [ ] Email delivery of morning brief
- [ ] Habit tracking skill
- [ ] Financial import automation (Plaid API)

### Medium Term (v1.2)

- [ ] Cross-platform sync (iOS/Android)
- [ ] Agent prompt library (community)
- [ ] Plugin marketplace
- [ ] Voice profiles for agents (ElevenLabs)
- [ ] Advanced analytics dashboards
- [ ] API for external integrations

### Long Term (v2.0)

- [ ] LifeOS community hub
- [ ] Shared agent improvements
- [ ] Collaborative dashboards
- [ ] Enterprise WorkOS offering
- [ ] LifeOS certification program
- [ ] Conference talks / workshops

---

## Maintenance Guidelines

### Regular Updates

**Weekly:**
- Update context files if life changes
- Review agent effectiveness
- Adjust dashboard queries as needed

**Monthly:**
- Review archived data
- Optimize database structure
- Update dependencies (Obsidian plugins)

**Quarterly:**
- Comprehensive system review
- Agent persona refinement
- Skills optimization
- Community contributions review

### Version Control

**Commit frequently:**
```bash
git add -A
git commit -m "Clear description of changes"
```

**Branch strategy:**
- `main` → commit freely (personal)
- `workos` → commit freely (work)
- `oss-template` → commit carefully (public)

### Backup Strategy

**Local:**
- Git version history (every commit)
- Obsidian vault synced to cloud (Obsidian Sync or iCloud)

**Remote:**
- Private repo (GitHub/GitLab)
- Encrypted backup (optional)

---

## Key Metrics

### System Adoption

**Personal (LifeOS):**
- 14 agents available
- 7 databases in use
- 5 skills automated
- Daily morning brief generated
- Weekly Cabinet meetings conducted

**Professional (WorkOS):**
- 8 agents available
- 4 skills automated
- Daily standups generated
- Weekly exec updates
- Meeting prep automated

**Community (LifeOS-OSS):**
- Public template ready
- Contributing guidelines established
- Example files provided
- Privacy protection verified

---

## Success Criteria

**Individual:**
- ✅ System used daily for 30+ days
- ✅ Time saved: 5+ hours/week
- ✅ Better decisions through agent consultation
- ✅ Work-life separation maintained
- ✅ Data privacy protected

**Community:**
- 🔄 10+ external contributors
- 🔄 100+ GitHub stars
- 🔄 Positive user testimonials
- 🔄 Active discussions/issues
- 🔄 Regular improvements merged

---

## Git Remotes Setup & Workflow

### Initial Repository Setup

**For new users (cloning LifeOS-OSS template):**

```bash
# 1. Fork LifeOS-OSS on GitHub (https://github.com/kcwoodfield/LifeOS-OSS)

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/LifeOS-OSS.git LifeOS
cd LifeOS

# 3. Rename oss-template → main (your personal branch)
git checkout oss-template
git branch -m main
git push origin main:main

# 4. Set up remotes
git remote rename origin personal          # Your private fork
git remote add upstream https://github.com/kcwoodfield/LifeOS-OSS.git   # Official template

# 5. Create workos branch (optional - for work separation)
git checkout -b workos
git push personal workos

# 6. Keep oss-template for contributing back
git checkout -b oss-template upstream/oss-template
git push personal oss-template

# 7. Verify remotes
git remote -v
# personal   https://github.com/YOUR_USERNAME/LifeOS-OSS.git (your fork)
# upstream   https://github.com/kcwoodfield/LifeOS-OSS.git (official template)
```

### For Original Author (User's Setup)

**Three remotes for three repos:**

```bash
git remote -v
# origin   https://github.com/kcwoodfield/LifeOS.git      (main private repo)
# workos   https://github.com/kcwoodfield/WorkOS.git      (work private repo)
# oss      https://github.com/kcwoodfield/LifeOS-OSS.git  (public template)
```

**Workflow:**

```bash
# Work on personal (main branch)
git checkout main
# ... make changes ...
git add -A && git commit -m "Personal updates"
git push origin main

# Work on professional (workos branch)
git checkout workos
# ... make changes ...
git add -A && git commit -m "Work updates"
git push workos workos

# Contribute infrastructure improvements to oss-template
git checkout oss-template
# ... make infrastructure changes (agents, skills, docs) ...
git add -A && git commit -m "Add new skill"
git push oss oss-template
```

### Cherry-Picking Improvements Between Branches

**Scenario:** You built a great new skill on `main` and want to share it publicly.

```bash
# 1. On main branch, find the commit
git checkout main
git log --oneline -10
# abc123f Add inbox processing skill
# def456g Update CLAUDE.md

# 2. Switch to oss-template
git checkout oss-template

# 3. Cherry-pick the commit
git cherry-pick abc123f

# 4. Review for personal data leaks
git diff HEAD~1
grep -r "KEVIN\|PERSONAL_INFO" .

# 5. If clean, push to public
git push oss oss-template

# 6. If has personal data, amend the commit
git reset HEAD~1
# ... remove personal data ...
git add -A
git commit -m "Add inbox processing skill (sanitized)"
git push oss oss-template
```

### Syncing Upstream Updates (For Community Users)

**Pull latest template improvements:**

```bash
# 1. Fetch upstream changes
git fetch upstream

# 2. Switch to your oss-template branch
git checkout oss-template

# 3. Merge upstream changes
git merge upstream/oss-template

# 4. If conflicts, resolve and commit
# (Conflicts usually in CLAUDE.md or context files you've modified)

# 5. Cherry-pick desired improvements to main
git checkout main
git log oss-template --oneline -20   # See what's new
git cherry-pick <commit-hash>        # Pick specific improvements

# OR merge entire oss-template into main (more aggressive)
git merge oss-template
```

### Branch Protection Best Practices

**Ensure you never accidentally push private branches to public remote:**

```bash
# Add to .git/config
[remote "oss"]
    url = https://github.com/kcwoodfield/LifeOS-OSS.git
    fetch = +refs/heads/*:refs/remotes/oss/*
    push = +refs/heads/oss-template:refs/heads/oss-template   # Only allow oss-template

# OR use push.default = nothing (explicit push only)
git config push.default nothing

# Now "git push" without arguments will fail - must specify
git push oss oss-template  # Explicit - safer
```

### Common Workflows

#### Daily Personal Work

```bash
git checkout main
# ... work on tasks, journal, projects ...
git add -A && git commit -m "Daily updates"
git push origin main   # Push to private repo
```

#### Daily Professional Work

```bash
git checkout workos
# ... work on tasks, meetings, stakeholder updates ...
git add -A && git commit -m "Work updates"
git push workos workos   # Push to work private repo (or origin workos)
```

#### Contributing Infrastructure Improvements

```bash
git checkout oss-template

# Add new skill, agent, or documentation
# ... create files, test ...

# Review for personal data
git diff
git status --ignored

# Commit and push
git add -A
git commit -m "Add new feature

- Feature details
- Breaking changes (if any)
- Documentation updated

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"

git push oss oss-template

# Go to GitHub and create Pull Request
```

#### Emergency: Accidentally Committed Personal Data

```bash
# If not yet pushed - amend the commit
git reset HEAD~1
# ... remove personal data ...
git add -A
git commit -m "Corrected commit without personal data"

# If already pushed to PRIVATE repo - force push fix
git reset HEAD~1
# ... remove personal data ...
git add -A
git commit -m "Corrected commit"
git push origin main --force-with-lease

# If already pushed to PUBLIC repo - IMMEDIATELY
# 1. Delete the commit from public
git checkout oss-template
git reset --hard HEAD~1
git push oss oss-template --force

# 2. Notify maintainer if it's a PR
# 3. Consider rotating any exposed secrets
# 4. GitHub's commit history may still cache - contact support if needed
```

### Repository URLs

**Official repositories:**
- LifeOS-OSS (public template): https://github.com/kcwoodfield/LifeOS-OSS
- LifeOS (User's personal - private): https://github.com/kcwoodfield/LifeOS
- WorkOS (User's work - private): https://github.com/kcwoodfield/WorkOS

**For community users:**
- Fork LifeOS-OSS to your account
- Make your fork private if desired
- Contribute back via Pull Requests to LifeOS-OSS

---

## Resources

**Documentation:**
- [README.md](README.md) - Getting started guide
- [CLAUDE.md](CLAUDE.md) - Complete system guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [ARCHITECTURE.md](ARCHITECTURE.md) - This document

**Community:**
- GitHub: https://github.com/kcwoodfield/LifeOS-OSS
- Issues: Report bugs and request features
- Discussions: Ask questions and share ideas

**Related Projects:**
- Obsidian: https://obsidian.md
- Claude Code: https://claude.com/code
- Dataview: https://blacksmithgu.github.io/obsidian-dataview/

---

## Conclusion

LifeOS has evolved into a comprehensive **AI-native life orchestration system** with:

- **Dual contexts** (Personal LifeOS + Professional WorkOS)
- **22 specialized AI agents** (14 personal + 8 work)
- **9 automated skills** (5 personal + 4 work)
- **7 structured databases** (Dataview-powered)
- **Privacy-first architecture** (branch isolation + .gitignore)
- **Open source template** (community contributions welcome)

The three-branch model provides the perfect balance of:
- **Privacy** (personal data never public)
- **Separation** (work vs. life contexts)
- **Sharing** (infrastructure improvements benefit all)

This architecture is designed to evolve with you over decades - a true personal operating system for living intentionally.

---

**Built with care. Maintained with discipline. Executed with clarity.**

*LifeOS - Your AI-native infrastructure for living intentionally*

**Document End**
