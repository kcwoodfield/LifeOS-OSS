# Life OS Scripts

**Purpose:** Automation scripts for Life OS operations

**Last Updated:** 2025-10-17

---

## 🎉 Obsidian Database System - Phases 4-6 Complete!

**Completed:** 2025-10-17

The Obsidian Database System (Phases 4-6) is now fully operational:

### Phase 4: Review & Metrics Tracking ✅
- Example review files created with frontmatter (daily, weekly, monthly)
- Comprehensive metrics dashboard (`dashboards/metrics.md`)
- Historical tracking for energy, focus, wins, learnings, velocity

### Phase 5: Context Versioning ✅
- Version frontmatter added to all context files (career, wealth, art, preferences)
- Context history dashboard (`dashboards/context-history.md`)
- Semantic versioning for tracking context evolution over time

### Phase 6: Advanced Views & Automation ✅
- 5 Templater templates created (`templates/`)
  - new-idea.md
  - new-project.md
  - daily-review.md
  - weekly-review.md
  - monthly-review.md
- Master home dashboard (`dashboards/home.md`)
- Complete dashboard documentation (`dashboards/README.md`)

**What This Means:**
- All markdown files are now queryable via Dataview
- Context files track version history
- Templates auto-populate frontmatter for new files
- Dashboards provide real-time system insights
- Personal data is structured, portable, and future-proof

**See:** `dashboards/README.md` for complete query documentation

---

## Available Scripts

### 🔔 Claude Task Completion Notifications

**Script:** `claude_task_complete.sh`
**Purpose:** Trigger macOS notifications when Claude Code completes tasks

**Usage:**
```bash
# Manual test
./scripts/claude_task_complete.sh "Custom message"

# Automatic via Claude Code hooks (configured in .claude/settings.local.json)
```

**Features:**
- macOS notification with "Glass" sound
- Logs all notifications to `.logs/notifications.log`
- Triggered automatically via PostToolUse hook on TodoWrite

**Configuration:** See `.claude/settings.local.json` → `hooks.PostToolUse`

**Logs:** `.logs/notifications.log` (git ignored)

---

### 🌅 Morning Brief Generator

**Script:** `morning_brief.py`
**Purpose:** Generate daily briefing in `reviews/daily/briefs/YYYY-MM-DD.md`

**Usage:**
```bash
# Generate brief for today
python3 scripts/morning_brief.py

# Generate brief for specific date
python3 scripts/morning_brief.py --date 2025-10-17
```

**Features:**
- Pulls project priorities from `projects/INDEX.md`
- Displays top 3 priorities (Primary, Secondary, Maintenance)
- Includes all project status and blockers
- Your Pet care checklist
- Cabinet quick check prompts
- Weather/calendar placeholders
- Art practice planning section

**Output:** `reviews/daily/briefs/YYYY-MM-DD.md`

**Requirements:** Python 3.7+

---

### Modern Warfare Dashboard Generator

**Script:** `generate_mw_dashboard.py`
**Purpose:** Generate Call of Duty Modern Warfare themed dashboard with live LifeOS data

**Usage:**
```bash
# Generate dashboard with latest data
python3 .system/scripts/generate_mw_dashboard.py

# Output will be written to:
# dashboards/modern-warfare-live.html
```

**Features:**
- Reads current mission from `.system/context/queue.md`
- Pulls top 3 priority tasks from `databases/tasks/`
- Counts active and completed tasks
- Fetches live weather from wttr.in API
- Generates fully styled Modern Warfare HUD
- Auto-refresh every 60 seconds when viewed in browser

**Output:** `dashboards/modern-warfare-live.html`

**Automation Options:**
```bash
# Option 1: Manual refresh
python3 .system/scripts/generate_mw_dashboard.py

# Option 2: Cron job (every 5 minutes)
*/5 * * * * cd /path/to/LifeOS && /usr/bin/python3 .system/scripts/generate_mw_dashboard.py >> /tmp/mw_dashboard.log 2>&1

# Option 3: Shell alias (add to ~/.zshrc or ~/.bashrc)
alias mw-refresh="cd /path/to/LifeOS && python3 .system/scripts/generate_mw_dashboard.py"
```

**Requirements:**
- Python 3.7+
- PyYAML (`pip install pyyaml`)
- requests (`pip install requests`)

**Data Sources:**
- Mission status: `.system/context/queue.md`
- Tasks: `databases/tasks/*.md`
- Frontmatter parsed from YAML blocks
- Weather: wttr.in API (configure location in script)

---

## Claude Code Skills

Several automations are now implemented as Claude Code skills (`.claude/skills/`) that auto-invoke based on natural language:

### ✅ Cabinet Meeting
**Status:** Completed (Claude Code skill)
**Description:** Multi-agent consultation for decisions and weekly reviews
**Invocation:** "Cabinet meeting about [topic]" or "Weekly Cabinet meeting"

### ✅ Project Health Check
**Status:** Completed (Claude Code skill)
**Description:** Scans projects, identifies blockers, assesses velocity
**Invocation:** "Project status" or "How are my projects"

### ✅ Weekly Review
**Status:** Completed (Claude Code skill)
**Description:** End-of-week retrospective and planning
**Invocation:** "Weekly review" or "Week in review"

### 📝 Daily Review Template
**Status:** Planned
**Description:** Auto-populate daily review template with context

---

## Relationship: Scripts vs Skills

**Scripts** (`scripts/` directory):
- Standalone automation (Python, bash)
- Can run via cron or manual execution
- Generate files, process data

**Skills** (`.claude/skills/` directory):
- Claude Code auto-invoked processes
- Natural language triggers
- Can call scripts OR implement logic directly

**Example:** Morning Brief uses both - Python script (`morning_brief.py`) generates the markdown, and the Claude Code skill can invoke it or generate directly.

---

## Development

### Adding New Scripts

1. Create script in `scripts/` directory
2. Make executable: `chmod +x scripts/script_name.py`
3. Add documentation to this README
4. Test thoroughly before committing
5. Update `projects/ideas/` to mark automation as complete (or create new completed idea file)

### Testing

Always test scripts with:
- Today's date (default)
- Future dates (using --date flag)
- Edge cases (missing files, empty data)

### Style Guidelines

- Use Python 3.7+ features
- Include docstrings for all functions
- Add usage examples in script header
- Print helpful next steps after execution
- Handle errors gracefully with informative messages

---

## Integration with Life OS

These scripts are designed to work with the Life OS structure:

```
LifeOS/
├── .claude/
│   └── skills/           # Claude Code auto-invoked skills
├── scripts/              # Automation scripts (this directory)
├── schemas/              # Frontmatter schemas for Dataview
│   ├── README.md
│   ├── idea-schema.md
│   ├── project-schema.md
│   └── review-schema.md
├── dashboards/           # Dataview query dashboards
│   ├── test-query.md
│   └── ideas-board.md    # Dynamic ideas dashboard
├── reviews/
│   ├── daily/
│   │   └── briefs/       # Morning brief outputs
│   ├── weekly/
│   └── monthly/
├── projects/
│   ├── INDEX.md          # Project data source
│   ├── _ideas.md         # Ideas backlog (deprecated, see ideas/)
│   ├── ideas/            # Individual idea files with frontmatter
│   └── prds/             # Product requirement docs
├── writing/
│   ├── drafts/           # Blog post drafts
│   ├── published/        # Published content
│   └── essays/           # Long-form reflections
├── agents/               # Agent definitions (8 active + 5 reserve)
└── context/              # Personal context files
    ├── preferences.md
    ├── career.md
    ├── wealth.md
    └── art.md
```

---

*Automation makes consistency effortless. Build systems, not habits.*
