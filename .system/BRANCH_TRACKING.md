# Branch Feature Tracking

Track which features exist in which branches to maintain consistency.

## Legend
- ✅ Implemented and merged
- 🚧 In progress
- ⏳ Planned
- 🔒 Main only (personal data/integrations)
- 📦 OSS only (template-specific)

---

## Infrastructure Features

| Feature | Main | OSS | Notes |
|---------|------|-----|-------|
| 14 Cabinet agents | ✅ | ✅ | Synced |
| Agent metadata formatting | ✅ | ✅ | Synced |
| Dashboard system | ✅ | ✅ | Synced |
| Example files | ✅ | ✅ | Synced |
| LICENSE.md | ✅ | ✅ | Synced |
| SETUP.md | ✅ | ✅ | Synced |
| Plugin installation guide | ✅ | ✅ | Synced |

## Personal Features (Main Only)

| Feature | Main | OSS | Notes |
|---------|------|-----|-------|
| Personal PRDs | ✅ | ❌ | Contains real project data |
| Personal reflections | ✅ | ❌ | Daily/weekly reviews with PII |
| Personal ideas | ✅ | ❌ | Real ideas and business plans |
| Google Calendar integration | ⏳ | ❌ | 🔒 Personal account only |
| Newsletter automation | ⏳ | ❌ | 🔒 Uses personal email |
| Morning brief with real data | ✅ | ❌ | 🔒 Real calendar/tasks |

## Template Features (OSS Only)

| Feature | Main | OSS | Notes |
|---------|------|-----|-------|
| Example PRD | ✅ | ✅ | 📦 Template demonstration |
| Example idea | ✅ | ✅ | 📦 Template demonstration |
| Example weekly review | ✅ | ✅ | 📦 Template demonstration |
| Empty-state dashboard messages | ✅ | ✅ | 📦 For new users |

## Planned Features

| Feature | Target | Main | OSS | Notes |
|---------|--------|------|-----|-------|
| Newsletter automation | Tomorrow | 🚧 | ❌ | 🔒 Personal only |
| Google Calendar integration | Tomorrow | 🚧 | ❌ | 🔒 Personal only |
| Streamlined dashboards | Tomorrow | ⏳ | ⏳ | Both branches |
| Demo branch with fake data | Tomorrow | N/A | N/A | New branch |
| Voice interface | Future | ⏳ | ⏳ | Both branches |
| Mobile app | Future | ⏳ | ⏳ | Both branches |

---

## Sync Strategy

**When to sync Main → OSS:**
- Infrastructure improvements (agents, dashboards, scripts)
- Documentation updates (README, CLAUDE.md)
- Bug fixes in core system
- New agent additions

**Never sync Main → OSS:**
- Personal data files (reflections, real PRDs, ideas)
- API keys or credentials
- Personal calendar/email integrations
- Anything with PII

**When to sync OSS → Main:**
- Template improvements that help personal use
- Example files (can keep for reference)
- Documentation improvements

---

## How to Sync

### Sync infrastructure feature from Main to OSS:

```bash
# 1. Identify commit with feature
git log main --oneline -10

# 2. Switch to OSS
git checkout oss

# 3. Cherry-pick the commit
git cherry-pick <commit-hash>

# 4. Remove any PII if accidentally included
# ... edit files if needed ...

# 5. Push to OSS remote
git push oss oss:main
```

### Sync documentation from OSS to Main:

```bash
# 1. Switch to main
git checkout main

# 2. Cherry-pick from OSS
git cherry-pick oss/<commit-hash>

# 3. Push to origin
git push origin main
```

---

**Last Updated:** 2025-10-18
