# Cabinet Database

> **Purpose:** Archive of all Cabinet meeting consultations and decisions
> **Note:** This is a specialized subset of the meetings database for historical Cabinet tracking

---

## Overview

The Cabinet database stores all multi-agent consultations - both weekly strategic reviews and ad-hoc decision meetings. This creates a historical record of agent perspectives, strategic decisions, and how thinking evolved over time.

## Schema

See `_schema.md` for the complete frontmatter template.

**Required Fields:**
- `title` - Meeting purpose
- `date` - Meeting date
- `meeting_type` - weekly | ad-hoc
- `agents_consulted` - Which agents participated
- `created` - Record creation date

**Optional Fields:**
- `topic` - Primary discussion topic
- `decision` - Final decision/recommendation
- `consensus` - Agreement level among agents
- `dissent` - Which agents disagreed
- `project` - Related project
- `tags` - Categorization

## Workflow

### Weekly Cabinet Meeting (Scheduled)
1. **Trigger:** Sunday evening, use morning-brief or cabinet-meeting skill
2. **Format:** All agents report on their domain
3. **Output:** Structured meeting with synthesis
4. **Archive:** Save to `databases/cabinet/YYYY-MM-DD-weekly-cabinet.md`

### Ad-Hoc Cabinet Meeting (On-Demand)
1. **Trigger:** "Cabinet meeting about [topic]" or major decision needed
2. **Format:** Targeted consultation with relevant agents
3. **Output:** Agent perspectives + synthesis
4. **Archive:** Save to `databases/cabinet/YYYY-MM-DD-topic-slug.md`

### Cross-Referencing
- Cabinet meetings also stored in `databases/meetings/` (type: cabinet)
- This database is for specialized Cabinet tracking and historical analysis
- Can query both databases independently

## Views

### Dashboard Queries

**Recent Cabinet Meetings:**
```dataview
TABLE meeting_type, agents_consulted, decision
FROM "databases/cabinet"
SORT date DESC
LIMIT 10
```

**Decisions by Topic:**
```dataview
TABLE date, decision, consensus
FROM "databases/cabinet"
WHERE contains(topic, "career")
SORT date DESC
```

**Agent Participation:**
```dataview
TABLE date, topic, decision
FROM "databases/cabinet"
WHERE contains(agents_consulted, "Strategist")
SORT date DESC
```

**Consensus vs. Dissent:**
```dataview
TABLE date, topic, consensus, dissent
FROM "databases/cabinet"
WHERE consensus = "split"
SORT date DESC
```

## Naming Convention

**File naming:** `YYYY-MM-DD-meeting-type-topic.md`
**Examples:**
- `2025-10-19-weekly-cabinet.md`
- `2025-10-20-adhoc-job-offer-decision.md`
- `2025-10-22-adhoc-rental-property-analysis.md`

**Why this format:**
- Chronological sorting
- Clear meeting type
- Topic/purpose in filename

## Meeting Types

**Weekly Cabinet:**
- Scheduled Sunday evening
- All agents report on their domains
- Synthesis of week's progress
- Planning for next week
- Broad strategic review

**Ad-Hoc Cabinet:**
- On-demand for specific decisions
- Only relevant agents consulted
- Focused on single topic/decision
- Quick turnaround
- Action-oriented

## Agent Roles in Cabinet

### Strategic Council (Always Present)
- **Atlas (COO):** Operations, balance, synthesis
- **Banker (CFO):** Financial implications
- **Strategist (CSO):** Career and political tactics
- **Sage (Oracle):** Values alignment, perspective
- **Spartan (Defense):** Physical/mental foundation

### Domain Experts (As Needed)
- **Engineer (CTO):** Technical decisions
- **Designer (CDO):** Design and UX decisions
- **Artist (Creative Director):** Art practice guidance
- **Maker (Hardware):** Physical builds
- **Storyteller (Content):** Writing and content strategy
- **Analyst (Data):** Metrics and tracking
- **Connector (Relationships):** Social/networking decisions
- **Healer (Health):** Wellness and longevity
- **Professor (Literary):** Reading and intellectual growth

## Tips

**Decision Documentation:**
- Capture not just what was decided, but why
- Document dissenting views (they might be right later)
- Link to context files that were updated
- Note confidence level in decision

**Agent Disagreements:**
- Healthy tension is valuable (Atlas vs. Banker on pace)
- Document the trade-off being navigated
- Revisit in future Cabinet meetings
- Track if decisions were right over time

**Historical Analysis:**
- Query past decisions: "Did we make the right call on X?"
- Track decision velocity: "Are we getting faster or more deliberate?"
- Identify patterns: "Do we always delay real estate purchases?"
- Learn from dissent: "When dissenting agents were right"

**Integration with Context Files:**
- Update `.system/context/career.md` after career decisions
- Update `.system/context/wealth.md` after financial decisions
- Update `.system/context/art.md` after creative decisions
- Cabinet meeting references context files for decision-making

**Metrics to Track:**
- Meeting frequency (weekly vs. ad-hoc ratio)
- Decision implementation rate (did we actually do what we decided?)
- Agent participation (are some agents overused/underused?)
- Consensus level (unanimous vs. split decisions)

---

**Last Updated:** 2025-10-19
