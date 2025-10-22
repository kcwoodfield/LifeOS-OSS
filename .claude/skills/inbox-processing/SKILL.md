# Inbox Processing Skill

**Triggers:** "Process my inbox", "Process inbox", "Clear inbox", "Evening review"

---

## What This Skill Does

Guides you through processing your `_inbox_.md` file by transforming unstructured captures into structured data in the appropriate databases. This is the core of the GTD (Getting Things Done) workflow in LifeOS/WorkOS.

**Philosophy:** Quick capture during the day → Structured processing during evening review

---

## How to Use

Simply say:
- "Process my inbox"
- "Process inbox"
- "Help me clear my inbox"
- "Evening review" (triggers inbox processing)

---

## Skill Instructions

When this skill is invoked, follow these steps:

### 1. Read the Inbox

**Read file:** `_inbox_.md`

**Look for:**
- Captured items (bullets, paragraphs, notes)
- Anything below the "## Captured Items" header
- Quick thoughts, ideas, tasks, meeting notes, etc.

**If inbox is empty:**
- Congratulate user: "Inbox is already clear! Well done. 🎉"
- Exit skill

### 2. Present Items for Processing

**For each captured item in the inbox:**

Show the item to the user and ask:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INBOX ITEM:
[Show the captured text]

What is this?
1. Task - Action to take
2. Idea - Project or product idea
3. Meeting Note - Meeting discussion
4. Journal Entry - Personal reflection
5. Book - Book to read
6. Reference - Save for later
7. Delete - No longer relevant

[Type number or description]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3. Process Based on Type

Based on user's answer, guide them through creating the appropriate structured entry:

---

#### **Type 1: Task**

**Questions to ask:**
- What's the task title?
- Priority? (high / medium / low)
- Related project? (if any)
- Due date? (YYYY-MM-DD or leave blank)
- Effort estimate? (small / medium / large)

**Create file:** `databases/tasks/[date]-[title-slug].md`

**Template:**
```markdown
---
title: "[User's title]"
status: "todo"
priority: "[high/medium/low]"
project: "[[project-name]]"  # if applicable
due_date: [YYYY-MM-DD]  # if provided
effort: "[small/medium/large]"
tags: []
created: [TODAY]
---

# [Title]

## Description
[Original inbox capture text]

## Notes
[Any additional context user provides]
```

**After creating:**
- "✅ Task created: databases/tasks/[filename].md"
- "Want to add more details now, or move to next item?"

---

#### **Type 2: Idea**

**Questions to ask:**
- What's the idea title?
- Domain? (engineering / business / personal / creative / other)
- Confidence level? (high / medium / low)
- Potential impact? (high / medium / low)
- Effort required? (small / medium / large)

**Create file:** `projects/ideas/[title-slug].md`

**Template:**
```markdown
---
title: "[User's title]"
status: "new"
confidence: "[high/medium/low]"
effort: "[small/medium/large]"
impact: "[high/medium/low]"
domain: "[domain]"
tags: []
created: [TODAY]
---

# [Title]

## Problem
[What problem does this solve? Ask user or use inbox text]

## Solution
[How does this solve it? From inbox text]

## Impact
[Why does this matter? Ask user]

## Next Steps
[What's the first action to validate this?]
```

**After creating:**
- "✅ Idea captured: projects/ideas/[filename].md"
- "This is a [confidence]/[impact]/[effort] idea. Want to refine it or move on?"

---

#### **Type 3: Meeting Note**

**Questions to ask:**
- Meeting title?
- Date of meeting? (YYYY-MM-DD)
- Who attended? (comma-separated names)
- Any decisions made?
- Any action items?

**Create file:** `databases/meetings/[date]-[meeting-slug].md`

**Template:**
```markdown
---
title: "[Meeting title]"
date: [YYYY-MM-DD]
attendees:
  - [Name 1]
  - [Name 2]
type: "[1:1 / team / stakeholder / planning]"
tags: []
---

# [Meeting Title] - [Date]

## Attendees
- [List attendees]

## Notes
[Original inbox capture]

## Decisions
[Decisions made, if any]

## Action Items
- [ ] [Action item 1]
- [ ] [Action item 2]
```

**After creating:**
- "✅ Meeting note saved: databases/meetings/[filename].md"
- "Should I create tasks for any action items?"

---

#### **Type 4: Journal Entry**

**Questions to ask:**
- Is this for today or a specific date?
- Energy level today? (1-10)
- Overall mood? (focused / tired / excited / stressed / etc.)
- Any specific gratitude?

**Options:**
- **Option A:** Add to today's journal entry (if exists)
- **Option B:** Create new journal entry

**File:** `databases/journal/[date].md`

**Template (if creating new):**
```markdown
---
date: [YYYY-MM-DD]
energy: [1-10]
mood: "[user's mood]"
gratitude: []
tags: []
---

# Daily Journal - [Date]

## Reflection
[Original inbox text]

## Gratitude
- [Item 1]
- [Item 2]

## Notes
[Additional thoughts]
```

**After creating/updating:**
- "✅ Added to journal: databases/journal/[date].md"

---

#### **Type 5: Book**

**Questions to ask:**
- Book title?
- Author?
- Genre? (fiction / non-fiction / technical / biography / etc.)
- Where did you hear about it?
- Priority to read? (high / medium / low)

**Create file:** `databases/books/[title-slug].md`

**Template:**
```markdown
---
title: "[Book title]"
author: "[Author name]"
genre: "[genre]"
status: "to-read"
priority: "[high/medium/low]"
source: "[Where you heard about it]"
tags: []
added: [TODAY]
---

# [Book Title]

**Author:** [Author]
**Genre:** [Genre]

## Why Read This
[From inbox or ask user]

## Notes
[Reading notes will go here]

## Quotes
[Memorable quotes will go here]
```

**After creating:**
- "✅ Book added to reading list: databases/books/[filename].md"
- "Professor will help you with reading recommendations!"

---

#### **Type 6: Reference**

**For reference material (articles, links, research):**

**Questions:**
- What category? (article / research / tool / resource)
- Title?
- URL (if applicable)?
- Why save this?

**Create file:** `reference/[category]/[title-slug].md`

**Template:**
```markdown
# [Title]

**Category:** [category]
**URL:** [url if applicable]
**Saved:** [TODAY]

## Summary
[Original inbox text or summary]

## Why This Matters
[Why you saved it]

## Related
[Links to related projects, ideas, or topics]
```

**After creating:**
- "✅ Reference saved: reference/[category]/[filename].md"

---

#### **Type 7: Delete**

**Confirm:**
"Are you sure you want to delete this item? (yes/no)"

**If yes:**
- "✅ Deleted."
- Move to next item

**If no:**
- "Let's try again. What is this?"

---

### 4. After Processing Each Item

**Ask:** "Next item, or done for now?"

**Options:**
- **Next** → Process next inbox item
- **Done** → Stop and summarize
- **Skip** → Skip this item, come back later

### 5. Clear Processed Items from Inbox

**After all items processed:**

**Update `_inbox_.md`:**
```markdown
# Inbox

**Quick capture for anything that comes to mind. Process daily during evening review.**

---

## Instructions

- **During the day:** Dump everything here - tasks, ideas, meeting notes, thoughts
- **Don't organize** - Just capture quickly and get back to work
- **Evening review:** Process each item into proper location
- **Goal:** Empty inbox daily

---

## Captured Items

<!-- Add items below. Inbox cleared [TODAY] -->


```

**Summary message:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INBOX PROCESSING COMPLETE ✅

Processed: [X] items
- [N] tasks created
- [N] ideas captured
- [N] meetings logged
- [N] journal entries
- [N] books added
- [N] deleted

Your inbox is now clear!

Next: Review databases/tasks/ for tomorrow's priorities
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Context-Aware Processing

**Branch detection:**
- On `main` branch → Process to personal databases (LifeOS)
- On `workos` branch → Process to work databases (WorkOS)
- On `oss-template` → Example mode (don't actually create files)

**Smart defaults:**
- Use current date when not specified
- Auto-generate file slugs from titles
- Suggest related projects based on keywords
- Offer to create related files (e.g., task from meeting action item)

---

## Agent Integration

**This skill can consult:**
- **Moneypenny** - Help categorize ambiguous items
- **Senior PM** - Prioritize tasks and ideas
- **Atlas** - Suggest if something should be a task vs. just a note
- **Professor** - Book recommendations and reading prioritization

---

## Workflow Tips

**For users:**

**Morning:** Inbox should be empty (processed last night)

**During day:** Quick capture to inbox
```
Example inbox captures:
- "Talk to Sarah about API redesign"
- "Idea: automate expense tracking with Plaid API"
- "Read: Atomic Habits by James Clear"
- "Meeting with John - discussed Q4 roadmap, need to follow up on timeline"
```

**Evening (15-20 min):** Process inbox with this skill

**Result:** Structured data in appropriate databases, ready to query and use

---

## Advanced Features

**Batch processing:**
- "Process all tasks" - Create multiple tasks at once
- "Process all ideas" - Batch idea capture
- "Skip meetings for now" - Process only certain types

**Smart suggestions:**
- Detect task keywords ("TODO", "Action:", "Follow up:")
- Detect idea keywords ("Idea:", "What if:", "Build:")
- Detect meeting patterns (names, dates, "discussed")

**Undo:**
- "Undo last item" - Delete last created file, restore to inbox

---

## Example Session

```
User: "Process my inbox"

Skill: "Reading your inbox... Found 3 items. Let's process them!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ITEM 1:
'Review architecture doc and provide feedback by Friday'

What is this?
1. Task
2. Idea
3. Meeting Note
4. Journal Entry
5. Book
6. Reference
7. Delete"

User: "1"

Skill: "Great! Let's create a task.

What's the task title?"

User: "Review architecture doc"

Skill: "Priority? (high/medium/low)"

User: "high"

Skill: "Due date? Friday is Jan 19, 2025. Use that? (yes/no)"

User: "yes"

Skill: "✅ Task created: databases/tasks/2025-01-15-review-architecture-doc.md

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ITEM 2:
'Idea: Build a CLI tool for LifeOS that syncs tasks to Todoist'

What is this?"

User: "2"

Skill: "Great idea! Let's capture it.

What domain? (engineering/business/personal/creative/other)"

User: "engineering"

Skill: "Confidence level? (high/medium/low)"

User: "medium"

Skill: "Potential impact? (high/medium/low)"

User: "medium"

Skill: "Effort required? (small/medium/large)"

User: "medium"

Skill: "✅ Idea captured: projects/ideas/lifeos-todoist-cli.md

This is a medium/medium/medium idea (medium confidence, medium impact, medium effort).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ITEM 3:
'Remember to walk the dog'

What is this?"

User: "7 - already did it"

Skill: "Are you sure you want to delete this? (yes/no)"

User: "yes"

Skill: "✅ Deleted.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INBOX PROCESSING COMPLETE ✅

Processed: 3 items
- 1 task created
- 1 idea captured
- 0 meetings logged
- 0 journal entries
- 0 books added
- 1 deleted

Your inbox is now clear!

Next: Review databases/tasks/ for tomorrow's priorities"
```

---

## Notes for Implementation

**Interactive prompts:**
- Use clear numbered options
- Allow free-text responses
- Validate input (dates, priorities)
- Offer smart defaults

**File creation:**
- Generate slugs from titles (lowercase, hyphens)
- Check if file exists (avoid duplicates)
- Use proper frontmatter from schemas
- Link related files with [[wiki-links]]

**Error handling:**
- If file creation fails, ask user to try again
- If unclear categorization, consult Moneypenny
- If inbox is locked/in use, warn user

**Performance:**
- Process items one at a time (don't overwhelm)
- Allow "pause and resume" (save progress)
- Show progress (item 2 of 5)

---

*Inbox Processing Skill - Transform chaos into clarity, daily*
