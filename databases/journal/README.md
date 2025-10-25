# Journal Database

> **Purpose:** Daily journal entries for reflection, processing, and tracking inner life
> **Integration:** Morning brief and daily review workflows

---

## Overview

The journal database stores daily reflections - thoughts, feelings, insights, and observations. Unlike task tracking or project notes, this is the space for processing emotions, capturing moments, and tracking personal growth over time.

## Schema

See `_schema.md` for the complete frontmatter template.

**Required Fields:**
- `title` - Journal entry title (usually just the date)
- `date` - Entry date
- `created` - Record creation date

**Optional Fields:**
- `mood` - Overall emotional state
- `energy` - Physical/mental energy level (1-10)
- `gratitude` - Things you're grateful for
- `highlights` - Best moments of the day
- `challenges` - Difficult moments or struggles
- `insights` - Learnings or realizations
- `tags` - Themes, topics, emotions

## Workflow

### Morning Pages (Optional)
1. Wake up, sit with coffee
2. Stream of consciousness writing (500-750 words)
3. No editing, no judgment
4. Capture dreams, anxieties, intentions

### Evening Reflection (Recommended)
1. End of day, review what happened
2. What went well? What was hard?
3. What did you learn?
4. What are you grateful for?
5. Save to `databases/journal/YYYY-MM-DD.md`

### Weekly Review Integration
- Review journal entries from past week
- Identify patterns (energy dips, recurring themes)
- Extract insights for Cabinet meeting

## Views

### Dashboard Queries

**Recent Entries:**
```dataview
TABLE mood, energy, date as "Date"
FROM "databases/journal"
SORT date DESC
LIMIT 7
```

**High Energy Days:**
```dataview
TABLE mood, highlights
FROM "databases/journal"
WHERE energy >= 8
SORT date DESC
LIMIT 10
```

**Gratitude Log:**
```dataview
LIST gratitude
FROM "databases/journal"
WHERE gratitude != null
SORT date DESC
LIMIT 20
```

**Entries by Theme:**
```dataview
TABLE mood, energy, insights
FROM "databases/journal"
WHERE contains(tags, "art-practice")
SORT date DESC
```

**Mood Tracking:**
```dataview
TABLE mood, energy
FROM "databases/journal"
WHERE date >= date(today) - dur(30 days)
SORT date ASC
```

## Naming Convention

**File naming:** `YYYY-MM-DD.md`
**Examples:**
- `2025-10-19.md`
- `2025-10-20.md`

**Why this format:**
- One entry per day
- Chronological sorting
- Clean and simple
- Easy to find by date

## Journal Prompts

### Daily Prompts
- What made today worth living?
- What did I learn about myself today?
- What would I do differently tomorrow?
- Who did I connect with meaningfully?
- What progress did I make on what matters?

### Weekly Prompts
- What pattern am I noticing in my energy?
- What's bringing me joy lately?
- What's draining me?
- Am I living aligned with my values?
- What needs to change?

### Monthly Prompts
- How have I grown this month?
- What habits stuck? What didn't?
- What relationships deepened?
- What did I create or build?
- What do I want for next month?

## Integration with Other Systems

**Morning Brief:**
- Journal can inform daily intentions
- Previous day's insights surface in brief
- Gratitude practice feeds into positive mindset

**Evening Review:**
- Journal is part of evening reflection workflow
- Captures qualitative data (feelings, thoughts)
- Complements quantitative tracking (tasks, metrics)

**Weekly Cabinet Meeting:**
- Atlas reviews journal entries for energy patterns
- Sage uses journal for values alignment check
- Healer tracks stress and wellness signals

**Monthly Review:**
- Read entire month's journal entries
- Extract themes and insights
- Track personal growth over time

## Tips

**Keep It Private:**
- This is for you, not for anyone else
- Be brutally honest
- No performance, no polish
- Let it be messy

**Don't Force It:**
- Some days you'll write 1000 words
- Some days you'll write 50 words
- Both are fine
- Showing up matters more than length

**Track Emotions:**
- Use mood field to track emotional patterns
- Notice: "I'm always low energy on Tuesdays"
- Investigate: "What's happening on Tuesdays?"
- Adjust: "Block deep work on high-energy days"

**Gratitude Practice:**
- End each entry with 3 things you're grateful for
- Can be tiny: "Good coffee. YourPet's tail wag. Sunset colors."
- Builds positive mental patterns over time
- Proven impact on well-being

**Mine for Insights:**
- Review journal weekly
- Look for recurring themes
- What keeps coming up?
- That's probably important
- Turn insights into action

**Permission to Vent:**
- Journal is safe space for frustration
- Get it out, don't hold it in
- Write the angry email you won't send
- Process it, then move forward

---

**Last Updated:** 2025-10-19
