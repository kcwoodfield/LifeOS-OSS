# Books Database

> **Purpose:** Track reading list, log finished books, analyze reading patterns
> **Integration:** Professor agent uses this for literary recommendations

---

## Overview

This database tracks all books across your reading journey - from to-read wishlist to finished books with ratings and notes.

## Schema

See `_schema.md` for the complete frontmatter template.

**Required Fields:**
- `title` - Book title
- `author` - Author name(s)
- `status` - Current reading status
- `created` - Date added to database

**Optional Fields:**
- `year` - Publication year
- `genre` - Fiction, Non-Fiction, Biography, etc.
- `pages` - Page count
- `rating` - 1-5 stars (when finished)
- `started_date` - When you began reading
- `finished_date` - When you completed
- `tags` - Themes, topics, categories
- `notes` - Reading notes, quotes, insights

## Workflow

### Adding Books

**To-Read List:**
1. Hear about interesting book
2. Create file: `databases/books/AUTHOR-TITLE.md`
3. Set status: `to-read`
4. Add to reading queue

**Starting a Book:**
1. Update status to `reading`
2. Set `started_date`
3. Track progress in notes

**Finishing a Book:**
1. Update status to `finished`
2. Set `finished_date`
3. Add rating (1-5 stars)
4. Write brief review/notes

## Views

### Dashboard Queries

**Currently Reading:**
```dataview
TABLE author, started_date as "Started", pages
FROM "databases/books"
WHERE status = "reading"
SORT started_date ASC
```

**To-Read Queue (Top 10):**
```dataview
TABLE author, genre, pages
FROM "databases/books"
WHERE status = "to-read"
SORT created DESC
LIMIT 10
```

**Recently Finished:**
```dataview
TABLE author, finished_date as "Finished", rating
FROM "databases/books"
WHERE status = "finished"
SORT finished_date DESC
LIMIT 10
```

**Reading Stats:**
```dataview
TABLE
  length(rows.file.link) as "Count",
  choice(status = "to-read", "📚", choice(status = "reading", "📖", "✅")) as "Icon"
FROM "databases/books"
GROUP BY status
```

## Naming Convention

**File naming:** `author-last-name-title-slug.md`
**Examples:**
- `alexander-pattern-language.md`
- `currey-daily-rituals.md`
- `herbert-dune.md`

**Why this format:**
- Easy to find by author
- Clear what book is from filename
- Alphabetical sorting groups by author

## Integration with Professor Agent

Professor (Literary Critic agent) uses this database to:
- Track reading velocity and patterns
- Recommend books based on genres you enjoy
- Identify gaps in reading (too narrow? too broad?)
- Curate high-quality reading list
- Challenge you with canon/classics

## Tips

**Genre Categorization:**
- Fiction: Novel, Sci-Fi, Fantasy, Literary Fiction, Mystery
- Non-Fiction: Biography, History, Science, Philosophy, Business
- Technical: Programming, Design, Product Management, Engineering
- Art: Art History, Drawing, Painting, Photography

**Rating Guidelines:**
- 5 stars: Masterpiece, life-changing, will reread
- 4 stars: Excellent, highly recommend
- 3 stars: Good, worth reading
- 2 stars: Mediocre, some value
- 1 star: Waste of time, DNF (did not finish)

**Reading Notes:**
- Key quotes (with page numbers)
- Main ideas/themes
- How this applies to your life
- Related books to read next

**Tags for Discovery:**
Use tags to find patterns:
- Themes: `creativity`, `systems-thinking`, `stoicism`, `craft`
- Purpose: `career`, `art`, `philosophy`, `technical`
- Format: `reference`, `memoir`, `how-to`, `novel`

---

**Last Updated:** 2025-10-19
