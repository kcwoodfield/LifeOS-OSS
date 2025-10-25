# Cabinet Meeting Schema Template

Use this frontmatter structure for all Cabinet meeting files in `databases/cabinet/`.

```yaml
---
title: "Cabinet Meeting Purpose"
date: 2025-10-19
meeting_type: weekly          # weekly | ad-hoc
agents_consulted: []          # List of agent names
topic: null                   # Primary topic/decision
decision: null                # Final decision/recommendation
consensus: unanimous          # unanimous | majority | split
dissent: []                   # Agents who disagreed (if any)
project: null                 # Related project link
tags: []
created: 2025-10-19
updated: 2025-10-19
---

# Cabinet Meeting - [Topic]

## Context

What decision needs to be made or what strategic review is happening?

## Agent Perspectives

### Agent Name - Role

Agent's analysis, recommendations, concerns.

### Agent Name - Role

Agent's analysis, recommendations, concerns.

[... continue for all consulted agents ...]

## Synthesis

Atlas's (or facilitator's) integration of perspectives, identification of conflicts, and final recommendation.

## Decision

What was decided and why. What trade-offs were accepted.

## Action Items

- [ ] Task 1 - Owner - Due date
- [ ] Task 2 - Owner - Due date

## Follow-Up

Items to revisit, metrics to track, when to review this decision.
```

## Field Definitions

### Required Fields

**title** (string)
- Cabinet meeting purpose or topic
- Examples: "Weekly Cabinet Meeting", "Job Offer Decision", "Q4 Strategy Planning"

**date** (date)
- Meeting date: YYYY-MM-DD
- Used for chronological tracking

**meeting_type** (enum)
- `weekly` - Scheduled weekly strategic review
- `ad-hoc` - On-demand consultation for specific decision

**agents_consulted** (array)
- List of agents who participated
- Format: `["Atlas", "Banker", "Strategist", "Sage"]`
- Required: at least one agent

**created** (date)
- Date this record was created: YYYY-MM-DD
- Auto-filled by template

### Optional Fields

**topic** (string or null)
- Primary topic or decision area
- Examples: "career", "financial", "project-prioritization", "work-life-balance"
- Useful for filtering and historical analysis

**decision** (string or null)
- Final decision or recommendation made
- Brief summary of outcome
- Can be multi-sentence
- Null if meeting was informational only

**consensus** (enum)
- `unanimous` - All agents agreed (default)
- `majority` - Most agents agreed, some dissent
- `split` - Significant disagreement, no clear majority

**dissent** (array)
- Names of agents who disagreed with majority decision
- Format: `["Agent Name", "Agent Name"]`
- Empty array `[]` if unanimous
- Useful for tracking when dissenting views were correct

**project** (link or null)
- Link to related project: `[[Project Name]]`
- Can link to PRD: `[[projects/prds/yourproject]]`
- Null if not project-specific

**tags** (array)
- Topics, domains, themes
- Examples: `[strategy, career, wealth, operations, q4-planning]`
- Empty array `[]` if no tags

**updated** (date)
- Last modified date: YYYY-MM-DD
- Update when adding follow-up or revisiting decision

## Meeting Type Details

### Weekly Cabinet Meeting

**Purpose:** Comprehensive strategic review and planning
**Frequency:** Every Sunday evening
**Duration:** 60-90 minutes
**Agents:** All Strategic Council (Atlas, Banker, Strategist, Sage, Spartan) + relevant domain experts

**Structure:**
1. **Agent Reports** (5 min each)
   - Atlas: Operations, velocity, balance, energy
   - Banker: Financial progress, opportunities
   - Strategist: Career positioning, political landscape
   - Sage: Values alignment, perspective
   - Spartan: Physical/mental foundation
   - Others: Domain-specific updates as needed

2. **Cross-Domain Issues** (10-15 min)
   - Conflicts between domains
   - Resource allocation (time/energy/money)
   - Major decisions pending

3. **Strategic Synthesis** (10-15 min)
   - Atlas integrates recommendations
   - Top 3 priorities for coming week
   - Adjustments to ongoing strategy

**Example:**
```yaml
meeting_type: weekly
agents_consulted: ["Atlas", "Banker", "Strategist", "Sage", "Spartan", "Engineer", "Artist"]
topic: "weekly-review"
consensus: unanimous
tags: [weekly-review, operations, strategy, q4]
```

### Ad-Hoc Cabinet Meeting

**Purpose:** Targeted consultation for specific decision
**Trigger:** "Cabinet meeting about [topic]" or major decision needed
**Duration:** 30-60 minutes
**Agents:** Only relevant agents for the decision at hand

**Structure:**
1. **Context Setting** (5 min)
   - What's the decision?
   - What are the options?
   - What's the timeline?

2. **Agent Perspectives** (10-15 min)
   - Each consulted agent provides domain analysis
   - Recommendations and concerns
   - Trade-offs identified

3. **Synthesis & Decision** (10-15 min)
   - Integration of perspectives
   - Final recommendation
   - Action items and next steps

**Example:**
```yaml
meeting_type: ad-hoc
agents_consulted: ["Strategist", "Banker", "Sage"]
topic: "job-offer-decision"
decision: "Accept VP role with negotiated 6-month ramp period"
consensus: majority
dissent: ["Sage"]
tags: [career, major-decision, job-change]
```

## Example Cabinet Meeting

```yaml
---
title: "Should I Accept VP Product Role?"
date: 2025-10-20
meeting_type: ad-hoc
agents_consulted: ["Atlas", "Banker", "Strategist", "Sage", "Spartan"]
topic: "career"
decision: "Accept with conditions: negotiate 6-month ramp, maintain art practice, use salary for life infrastructure"
consensus: majority
dissent: ["Sage"]
project: null
tags: [career, major-decision, job-change, work-life-balance]
created: 2025-10-20
updated: 2025-10-20
---

# Cabinet Meeting: VP Product Job Offer Decision

## Context

Received offer for VP Product role at growing startup:
- 50% salary increase ($200K → $300K)
- Requires relocation to Seattle
- Expectation of 55-60 hour weeks
- Fast-paced, high-growth environment
- Strong team, good product-market fit

**Timeline:** Decision needed by Friday (3 days)

**Key Questions:**
1. Does this accelerate 10-year career/wealth plan?
2. Can I maintain art practice and side projects?
3. Is the life disruption worth it?
4. What are the long-term implications?

## Agent Perspectives

### Strategist (CSO) - Career & Politics

**Analysis:**
VP role is 3+ year acceleration of career plan. You're 43, this puts you on track for C-suite by 50. Title inflation in startups, but if company succeeds, this is transformative for career capital.

**Tactical Considerations:**
- Seattle market has strong tech ecosystem (future optionality)
- Relocation shows commitment (builds trust with new team)
- 60-hour weeks are startup reality, not unique to this role
- Exit opportunities multiply with VP title

**Recommendation:** ACCEPT
- This is the "crucible moment" for career acceleration
- Negotiate 6-month ramp to reduce family stress
- Use increased earnings to hire support (reduce friction)

**Confidence:** 85%

### Banker (CFO) - Financial Analysis

**Financial Impact:**
- Salary increase: +$100K/year = $500K over 5 years (before tax)
- Relocation cost: ~$50K one-time
- Higher Seattle cost of living: -$15K/year
- Net 5-year gain: ~$400K
- Accelerates financial independence by 2+ years

**Investment Implications:**
- More capital for real estate purchases
- Can max out retirement accounts fully
- Side income from YourProject becomes less critical (reduces pressure)

**Recommendation:** ACCEPT
- ROI is 8:1 over 5 years
- Dramatically improves wealth trajectory
- De-risks retirement planning

**Confidence:** 90%

### Atlas (COO) - Operations & Balance

*"Ah yes, the classic 'let's add more chaos and call it opportunity' gambit. Charming."*

**Operational Reality:**
- Current load: 50hrs work + 15hrs side projects + 5hrs art = 70hrs/week
- Proposed: 60hrs work + ??? side projects + ??? art
- Relocation disrupts all systems (routines, gym, art studio setup, YourPet's routine)
- 6-month adjustment period minimum

**Systems at Risk:**
- Art practice (hardest to protect)
- Side projects (YourProject, blog)
- Physical fitness (new gym, new routes for YourPet)
- Social network (rebuilding in new city)

**Recommendation:** ACCEPT with strict conditions
- Negotiate 6-month ramp period (50hrs for first 3 months)
- Use salary increase to hire: cleaning service, meal prep, dog walker
- Non-negotiable: 3x art practice per week (block on calendar)
- Pause secondary side projects (blog) for 6 months

**Confidence:** 70% (can be done but requires discipline)

### Sage (Oracle) - Values & Meaning

**The Deeper Question:**
Why do you want this? Is it the title? The money? The challenge? Or are you running from something?

**Values Analysis:**
- **Craft & Mastery:** VP role offers bigger canvas, more impact ✓
- **Art Practice:** Risk of becoming "person who used to paint" ✗
- **Present-Moment Living:** 60-hour weeks = less presence ✗
- **Family:** Relocation stress on family relationships ✗
- **Legacy:** Will you remember the work or the title? ?

**The Trade-Off:**
You're trading 5 years of "now" for financial security and career capital in your 50s. Is that exchange aligned with your deeper values?

**Recommendation:** PAUSE and reflect
- Sleep on it for 2 nights
- Talk to family (their needs matter)
- Imagine yourself 2 years in: proud or resentful?
- What would 80-year-old you advise?

**Confidence:** N/A (this is about clarity, not prediction)

### Spartan (Secretary of Defense) - Foundation & Discipline

**Physical/Mental Assessment:**
Can you handle the load? History says yes - you've done harder things.

**What's Required:**
- Sleep discipline (7-8hrs non-negotiable)
- Gym routine must adapt but not disappear
- Stress management (meditation, time in nature)
- YourPet's routine must be protected (he's your anchor)

**Seattle Advantages:**
- Great outdoor access (hiking, trails for YourPet)
- Strong fitness culture
- Proximity to mountains (mental health)

**Recommendation:** ACCEPT if you commit to foundation
- Morning routine non-negotiable (gym before work)
- YourPet's daily walk = your mental health (protect it)
- Sleep > work (always)
- First sign of burnout = red alert

**Confidence:** 80% (you can handle it if you stay disciplined)

## Synthesis (Atlas)

*"So, dear Cabinet, we have 4 ACCEPTs and 1 PAUSE. The ayes have it, though Sage raises the question that will haunt us at 2am: what are we really chasing?"*

**The Case for Accepting:**
1. Career acceleration is real (3+ years gained)
2. Financial impact is substantial ($400K+ over 5 years)
3. Operationally challenging but achievable with support
4. Physical foundation can be maintained with discipline

**The Case for Caution:**
1. Art practice at serious risk
2. Life disruption is significant
3. Values question unanswered: is this what you actually want?
4. Relocation impact on family

**Recommended Path: ACCEPT WITH CONDITIONS**

**Conditions to Negotiate:**
1. **6-month ramp period** - Start at 50hrs/week for first 3 months
2. **Relocation package** - $50K minimum to reduce family stress
3. **Remote flexibility** - 1 day/week WFH to protect deep work time

**Life Infrastructure to Build:**
1. **Hire help** - Cleaning service, meal prep, dog walker
2. **Protect anchors** - Art practice 3x/week (non-negotiable), YourPet's daily walks
3. **Pause secondary work** - Blog and minor side projects on hold for 6 months
4. **Family alignment** - Ensure partner is fully on board

**Decision Framework:**
Accept if:
- ✓ Negotiation succeeds on ramp period
- ✓ Family is genuinely supportive (not just agreeing)
- ✓ You can commit to protecting art practice
- ✓ You feel excitement not just ambition

Decline if:
- ✗ No flexibility on hours/ramp
- ✗ Family has reservations
- ✗ Gut feeling is "should" not "want"
- ✗ Already feeling burned out in current role

## Decision

**ACCEPT the VP role with conditions.**

**Rationale:**
The career and financial upside is too significant to pass up at age 43. This is a "crucible moment" that accelerates the 10-year plan substantially. However, it requires:
1. Successful negotiation on ramp period
2. Family buy-in
3. Commitment to protecting core identity anchors (art, health)
4. Using salary increase to reduce life friction

**Trade-offs Accepted:**
- Pause on blog and secondary side projects for 6 months
- Temporary life disruption from relocation
- Higher work hours (but not dramatically higher than current all-in hours)

**Sage's Concern Acknowledged:**
We're betting that financial freedom and career capital in our 50s is worth the intensity now. This is a values-based bet - revisit in 6 months.

## Action Items

- [ ] Draft negotiation points for offer discussion - Strategist - Due 2025-10-21
- [ ] Calculate exact financial impact and budget for infrastructure - Banker - Due 2025-10-21
- [ ] Discuss with family and gauge genuine support level - User - Due 2025-10-22
- [ ] Research Seattle art studios and gyms - Artist & Spartan - Due 2025-10-23
- [ ] Schedule follow-up Cabinet meeting in 6 months - Atlas - Due 2025-04-20

## Follow-Up

**Review Checkpoint:** 2025-04-20 (6 months post-start)

**Metrics to Track:**
- Art practice frequency (target: 3x/week)
- Actual work hours (target: ramp to 55-60 by month 6)
- Energy levels (scale 1-10)
- Family satisfaction (qualitative check-ins)
- YourProject progress (is it fully paused or still alive?)

**Questions to Revisit:**
- Was Sage right? Are we chasing the wrong thing?
- Did we successfully protect the identity anchors?
- Is the career acceleration real or just title inflation?
- Would we make this decision again?
```

---

**See:** `databases/cabinet/README.md` for usage guide and meeting types
