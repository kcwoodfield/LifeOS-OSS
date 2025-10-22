# Book Schema Template

Use this frontmatter structure for all book files in `databases/books/`.

```yaml
---
title: "Book Title"
author: "Author Name"
status: to-read              # to-read | reading | finished | abandoned
year: null                   # Publication year (YYYY)
genre: null                  # Fiction | Non-Fiction | Biography | etc.
pages: null                  # Page count
rating: null                 # 1-5 stars (when finished)
started_date: null           # YYYY-MM-DD
finished_date: null          # YYYY-MM-DD
tags: []
created: 2025-10-19
updated: 2025-10-19
---

# Book Title by Author Name

Brief description or why you want to read this book.

## Reading Notes

Key quotes, ideas, and insights as you read.

## Review

(Fill in when finished)

### What I Loved

### What I Learned

### Who Should Read This
```

## Field Definitions

### Required Fields

**title** (string)
- Full book title
- Examples: "The Design of Everyday Things", "Dune", "Sapiens"

**author** (string)
- Author name(s)
- Format: "First Last" or "First Last, First Last" for multiple authors
- Examples: "Donald Norman", "Frank Herbert", "Yuval Noah Harari"

**status** (enum)
- `to-read` - On reading list, not started
- `reading` - Currently reading
- `finished` - Completed reading
- `abandoned` - Started but didn't finish

**created** (date)
- Date added to database: YYYY-MM-DD
- Auto-filled by template

### Optional Fields

**year** (number or null)
- Publication year: YYYY
- Useful for tracking edition or historical context

**genre** (string or null)
- Primary genre/category
- Examples: Fiction, Non-Fiction, Biography, History, Science, Philosophy, Technical, Art

**pages** (number or null)
- Page count
- Useful for estimating reading time

**rating** (number or null)
- Your rating: 1-5 stars
- Only fill in when status = `finished`
- See rating guidelines below

**started_date** (date or null)
- When you began reading: YYYY-MM-DD
- Set when changing status to `reading`

**finished_date** (date or null)
- When you completed: YYYY-MM-DD
- Set when changing status to `finished`

**tags** (array)
- Free-form categorization
- Examples: `[creativity, systems-thinking, stoicism, craft, career, art]`
- Empty array `[]` if no tags

**updated** (date)
- Last modified date: YYYY-MM-DD
- Update when status changes or notes added

## Rating Guidelines

**5 stars:** Masterpiece, life-changing, will reread
- Fundamentally changed how you think
- Exceptional craft and insight
- Reference book you'll return to repeatedly

**4 stars:** Excellent, highly recommend
- Outstanding quality
- Significant insights or enjoyment
- Would recommend enthusiastically

**3 stars:** Good, worth reading
- Solid book with value
- No major flaws
- Glad you read it

**2 stars:** Mediocre, some value
- Has redeeming qualities but flawed
- Might be valuable for niche audience
- Wouldn't broadly recommend

**1 star:** Waste of time, DNF (did not finish)
- Poorly written or misleading
- No redeeming value
- Abandoned or regret finishing

## Example Book Entry

```yaml
---
title: "The Timeless Way of Building"
author: "Christopher Alexander"
status: reading
year: 1979
genre: Architecture
pages: 552
rating: null
started_date: 2025-10-15
finished_date: null
tags: [architecture, design, patterns, craft, philosophy]
created: 2025-10-12
updated: 2025-10-19
---

# The Timeless Way of Building by Christopher Alexander

Alexander's foundational work on pattern language - the philosophical underpinning of his design methodology. Exploring how buildings and spaces can have "quality without a name" - that ineffable rightness.

## Reading Notes

### Part One: The Timeless Way

"There is one timeless way of building. It is thousands of years old, and the same today as it has always been." (p. 7)

Key insight: The quality without a name isn't mystery - it's wholeness, achieved through pattern language.

### Part Two: The Gate

Starting to see connections to software design patterns and the quality of good code...

## Review

(Will fill in when finished)
```

---

**See:** `databases/books/README.md` for usage guide and workflow
