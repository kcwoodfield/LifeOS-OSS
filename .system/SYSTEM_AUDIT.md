# LifeOS System Audit & Restructure Plan

> **Date:** 2025-10-19
> **Branch:** feature/database-system
> **Status:** Pre-implementation audit

---

## Current State Analysis

### Directory Structure (Before)

```
LifeOS/
├── Root Level (5 files)
│   ├── README.md
│   ├── CLAUDE.md
│   ├── SETUP.md
│   ├── LICENSE.md
│   └── _inbox_.md
├── .claude/ (Skills - 4 skills)
├── .system/ (Infrastructure)
│   ├── agents/ (14 agents in 3 divisions)
│   ├── context/ (6 context files + conversations/)
│   ├── schemas/ (3 schema files)
│   ├── scripts/ (Python scripts)
│   └── apps/
├── assets/
│   ├── images/
│   └── voices/
├── dashboards/ (1 file: home.md)
├── projects/
│   ├── INDEX.md
│   ├── ideas/ (15+ files)
│   ├── prds/ (9 files)
│   ├── *-kanban.md (4 kanban boards)
│   └── projects.base
├── reflections/
│   ├── daily/ (+ briefs/)
│   ├── weekly/
│   └── monthly/
├── templates/ (7 templates)
├── tasks/ (empty directory)
└── writing/
    ├── drafts/
    ├── essays/
    ├── published/
    └── documentation/
```

---

## Issues Identified

### 1. Duplicate/Overlapping Functionality

**Problem:** Multiple systems for tracking tasks
- `projects/INDEX.md` - High-level project tracking
- `projects/*-kanban.md` - 4 separate kanban boards (blog, master, yourproject, voice-assistant)
- `templates/daily-tasks.md` - Daily task template
- `templates/new-task.md` - Individual task template
- `tasks/` directory - Empty, purpose unclear
- `_inbox_.md` - Mix of todo list and capture

**Recommendation:** Consolidate into database system
- **databases/tasks/** - Single source of truth for all tasks
- **dashboards/tasks-kanban.md** - Unified kanban view via Dataview
- Delete separate kanban files
- Keep inbox for quick capture only

### 2. Unclear Directory Purposes

**Problem:** Some directories lack clear purpose or documentation
- `tasks/` - Empty, never used
- `.system/apps/voice-assistant/` - Unclear relationship to projects/prds/voice-assistant.md
- `reflections/daily/briefs/` vs `reflections/daily/` - Distinction unclear
- `writing/documentation/` - Different from root-level docs?

**Recommendation:**
- Delete or repurpose empty directories
- Document directory purposes in README files
- Consolidate where redundant

### 3. Schema/Template Confusion

**Problem:** Schemas and templates serve similar purposes
- `.system/schemas/` - Documents frontmatter structure
- `templates/` - Templater templates with frontmatter

**Recommendation:**
- Keep both but clarify:
  - **Schemas:** Documentation reference (read-only)
  - **Templates:** Actual files to use with Templater
- Ensure consistency between them

### 4. Dashboard Underutilization

**Problem:** Only one dashboard exists
- `dashboards/home.md` - Single command center
- CLAUDE.md mentions 5 dashboards that don't exist:
  - ideas-board.md
  - project-health.md
  - metrics.md
  - context-history.md

**Recommendation:**
- Build the missing dashboards OR
- Update documentation to reflect single-dashboard approach
- Consolidate everything into home.md if single-dashboard is preferred

### 5. Writing Organization

**Problem:** writing/ has 4 subdirectories but purpose isn't clear
- drafts/ - In-progress posts
- essays/ - Long-form content
- published/ - Archive
- documentation/ - System docs?

**Recommendation:**
- Clarify: Is documentation/ for LifeOS docs or blog docs?
- If LifeOS docs, move to .system/
- If blog docs, rename to writing/guides/ or similar

---

## Proposed New Structure

### Clean, Purpose-Driven Architecture

```
LifeOS/
├── Root (Entry Points)
│   ├── README.md              # System overview
│   ├── CLAUDE.md              # AI integration guide
│   ├── SETUP.md               # Installation guide
│   ├── LICENSE.md
│   └── inbox.md               # Quick capture (rename from _inbox_.md)
│
├── .claude/ (Skills - No changes)
│   └── skills/
│       ├── morning-brief/
│       ├── cabinet-meeting/
│       ├── project-health/
│       └── weekly-review/
│
├── .system/ (Infrastructure - Enhanced)
│   ├── agents/ (14 agents)
│   ├── context/ (6 context files)
│   ├── schemas/ (Enhanced with database schemas)
│   ├── scripts/
│   ├── docs/ (NEW - system documentation)
│   │   ├── SYSTEM_AUDIT.md (this file)
│   │   ├── BRANCH_TRACKING.md
│   │   └── ARCHITECTURE.md (new)
│   └── [Remove apps/ if unused]
│
├── assets/ (No changes)
│   ├── images/
│   └── voices/
│
├── dashboards/ (Consolidated or Expanded - TBD)
│   ├── home.md                # Main dashboard
│   └── [Additional dashboards if needed]
│
├── databases/ (NEW - Core structured data)
│   ├── tasks/
│   │   ├── README.md          # Database documentation
│   │   ├── _schema.md         # Frontmatter template
│   │   └── [task files]
│   ├── books/
│   │   ├── README.md
│   │   ├── _schema.md
│   │   └── [book files]
│   ├── meetings/
│   │   └── [meeting notes]
│   ├── cabinet/
│   │   └── [cabinet meeting archives]
│   └── journal/
│       └── [daily journal entries]
│
├── projects/ (Streamlined)
│   ├── INDEX.md               # Project registry
│   ├── ideas/                 # Idea files (keep as is)
│   ├── prds/                  # Full PRDs (keep as is)
│   └── [DELETE kanban files - replaced by database views]
│
├── reflections/ (Consolidated)
│   ├── daily/                 # Merge briefs/ into this
│   ├── weekly/
│   └── monthly/
│
├── templates/ (No changes)
│   ├── daily-review.md
│   ├── weekly-review.md
│   ├── monthly-review.md
│   ├── new-idea.md
│   ├── new-project.md
│   └── new-task.md (update to point to databases/)
│
├── writing/ (Clarified)
│   ├── drafts/
│   ├── published/
│   └── essays/
│   └── [DELETE or MOVE documentation/]
│
└── [DELETE tasks/ - replaced by databases/tasks/]
```

---

## Migration Plan

### Phase 1: Database Foundation (Today)

**Create new structure:**
- [ ] Create `databases/` directory
- [ ] Create subdirectories: tasks/, books/, meetings/, cabinet/, journal/
- [ ] Write README.md for each database (purpose, schema, usage)
- [ ] Write _schema.md templates for frontmatter
- [ ] Create .system/docs/ and move audit files there

**Files to create:**
- databases/tasks/README.md
- databases/tasks/_schema.md
- databases/books/README.md
- databases/books/_schema.md
- databases/meetings/README.md
- databases/meetings/_schema.md
- databases/cabinet/README.md
- databases/cabinet/_schema.md
- databases/journal/README.md
- databases/journal/_schema.md

### Phase 2: Cleanup & Delete (Today)

**Remove duplicates:**
- [ ] Delete `tasks/` directory (empty, replaced by databases/tasks/)
- [ ] Delete `projects/blog-kanban.md`
- [ ] Delete `projects/master-kanban.md`
- [ ] Delete `projects/yourproject-kanban.md`
- [ ] Delete `projects/voice-assistant-kanban.md`
- [ ] Delete `projects/projects.base` (if unused)
- [ ] Evaluate `.system/apps/` - delete if unused

**Consolidate:**
- [ ] Merge `reflections/daily/briefs/` content into `reflections/daily/`
- [ ] Delete `reflections/daily/briefs/` directory
- [ ] Evaluate `writing/documentation/` - move or delete

### Phase 3: Update References (Today)

**Update documentation:**
- [ ] Update CLAUDE.md - remove references to non-existent dashboards OR create them
- [ ] Update README.md - reflect new structure
- [ ] Update SETUP.md - document databases/
- [ ] Update templates/new-task.md - point to databases/tasks/

**Update dashboards:**
- [ ] Update dashboards/home.md - query from databases/ instead of scattered files
- [ ] Create unified kanban view using Dataview (replace separate kanban files)

### Phase 4: Enhanced Schemas (Today)

**Create comprehensive schemas:**
- [ ] Update .system/schemas/ to include database schemas
- [ ] Ensure templates/ match schemas exactly
- [ ] Document workflow: inbox → process → databases

### Phase 5: Testing (Today)

**Verify everything works:**
- [ ] Test creating new task in databases/tasks/
- [ ] Test Dataview queries pull from databases/
- [ ] Test kanban view in dashboard
- [ ] Verify morning brief skill still works
- [ ] Verify cabinet meeting skill still works

---

## Workflow Design

### The New Flow

**1. Quick Capture (Anytime)**
```
Thought/idea/task → inbox.md (brain dump, unstructured)
```

**2. Evening Review (Daily)**
```
Process inbox.md:
- Tasks → databases/tasks/
- Books → databases/books/
- Meeting notes → databases/meetings/
- Journal thoughts → databases/journal/
- Ideas → projects/ideas/
- Clear inbox.md
```

**3. Structured Work (Daily)**
```
Query databases via dashboards:
- home.md shows today's tasks
- Kanban view shows task flow
- Books shows reading list
- Meetings shows recent meetings
```

**4. Reflection (Daily/Weekly/Monthly)**
```
- Daily: databases/journal/ entry
- Weekly: databases/cabinet/ Cabinet meeting
- Monthly: reflections/monthly/ retrospective
```

---

## Success Criteria

### What "Done" Looks Like

**Structure:**
- ✅ No duplicate files or directories
- ✅ Clear purpose for every directory
- ✅ READMEs document each database
- ✅ Schemas match templates exactly

**Functionality:**
- ✅ Single source of truth for tasks (databases/tasks/)
- ✅ Unified kanban view (not 4 separate files)
- ✅ Dashboard queries work correctly
- ✅ Templates create files in correct locations
- ✅ Skills (morning brief, cabinet meeting, etc.) still work

**Documentation:**
- ✅ CLAUDE.md reflects actual structure
- ✅ README.md shows new architecture
- ✅ SETUP.md includes database workflow
- ✅ This audit document archived for reference

**Workflow:**
- ✅ inbox.md → databases flow is clear
- ✅ Evening review process documented
- ✅ Quick capture still fast
- ✅ Structured data still queryable

---

## Risks & Mitigation

### Potential Issues

**Risk 1: Breaking existing workflows**
- **Mitigation:** Work in feature branch, test before merging
- **Rollback:** Git history allows easy revert

**Risk 2: Losing data during cleanup**
- **Mitigation:** Only delete truly empty or redundant files
- **Rollback:** Commit before each deletion

**Risk 3: Dataview queries break**
- **Mitigation:** Update queries incrementally, test each
- **Rollback:** Keep old queries commented out until verified

**Risk 4: Skills stop working**
- **Mitigation:** Test each skill after structural changes
- **Rollback:** Update skill prompts to point to new locations

---

## Timeline

**Today (2025-10-19):** Phases 1-5 (Full implementation)
**Tomorrow (2025-10-20):** User testing, refinement
**This Week:** Documentation updates, example data

---

## Notes

**Branch:** feature/database-system
**Will merge to:** main (after testing)
**Will sync to:** oss (template benefits from this cleanup)

**Team involved:**
- Engineer (CTO) - Technical implementation
- Designer (CDO) - UX and information architecture
- Atlas (COO) - Workflow integration
- Analyst (Ada) - Schema design

---

**Last Updated:** 2025-10-19
**Status:** Ready to implement
