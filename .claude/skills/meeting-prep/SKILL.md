# Meeting Prep Assistant

**Triggers:** "Prepare for meeting", "Meeting prep", "Briefing for [meeting name]", "Help me prepare for [meeting]"

---

## What This Skill Does

Generates a comprehensive meeting briefing with context, agenda, talking points, decisions needed, and success criteria. Ensures you never walk into a meeting unprepared.

**Output:** `meetings/prep/YYYY-MM-DD-[meeting-name].md`

---

## How to Use

Simply say:
- "Prepare briefing for tomorrow's stakeholder meeting"
- "Meeting prep for my 1:1 with Sarah"
- "Help me prepare for the API design review"
- "Briefing for the quarterly business review"

---

## Skill Instructions

When this skill is invoked, follow these steps:

### 1. Gather Meeting Information

**Ask user for details if not provided:**
- Meeting name/topic
- Date and time
- Duration
- Attendees
- Meeting type (1:1, stakeholder review, technical discussion, planning session, etc.)

### 2. Gather Context

**Read relevant files:**
- `.workos/context/stakeholders.md` - Who's attending, what they care about
- `.workos/context/team-directory.md` - Roles and relationships
- `.workos/context/current-projects.md` - Project status relevant to meeting
- `projects/prds/*.md` - If meeting is project-specific
- `databases/meetings/*.md` - Previous meeting notes with same attendees
- `communications/exec-updates/` - Recent status updates

**Look for:**
- Relationships between attendees (manager, peer, exec, cross-team)
- Meeting history (what was discussed before, decisions made, action items)
- Relevant project status or blockers
- Open questions or pending decisions
- Stakeholder priorities and concerns

### 3. Generate Meeting Briefing

Use this comprehensive template:

```markdown
# Meeting Briefing: [Meeting Name]

**Date:** [Day, Month DD, YYYY] at [Time]
**Duration:** [X minutes]
**Location:** [Zoom/Room/etc.]
**Type:** [1:1 / Team Sync / Stakeholder Review / Technical Discussion / etc.]

---

## Attendees

### Primary
- **[Name]** - [Role] - **Cares about:** [Their priorities/concerns]
- **[Name]** - [Role] - **Cares about:** [Their priorities/concerns]

### Optional/FYI
- [Name] - [Role]

---

## Meeting Purpose

[1-2 sentences: Why this meeting exists and what it should accomplish]

---

## Meeting Context

**Background:**
[What's the relevant context? Previous discussions, project status, recent events]

**Why Now:**
[What triggered this meeting? Milestone, decision needed, regular cadence, etc.]

**Previous Meetings:**
[If recurring, what was discussed last time? Outstanding action items?]

---

## Agenda

[Proposed agenda - adjust based on meeting type]

1. **[Topic 1]** (X min)
   - [Sub-point if needed]
2. **[Topic 2]** (X min)
3. **[Topic 3]** (X min)
4. **Next Steps & Action Items** (5 min)

---

## Your Talking Points

[These are YOUR key points to communicate]

### Must Communicate
1. **[Point 1]** - [Why it matters]
2. **[Point 2]** - [Why it matters]
3. **[Point 3]** - [Why it matters]

### If Time Permits
- [Nice-to-have point 1]
- [Nice-to-have point 2]

---

## Questions to Expect

Based on attendees and context, you may be asked:

1. **[Likely question 1]**
   - **Answer:** [Your prepared response]
   - **Data to support:** [Metrics, examples, references]

2. **[Likely question 2]**
   - **Answer:** [Your prepared response]

3. **[Likely question 3]**
   - **Answer:** [Your prepared response]

---

## Decisions Needed

[What needs to be decided in this meeting?]

1. **[Decision 1]**
   - **Options:** [A, B, C]
   - **Your recommendation:** [Option X because Y]
   - **Trade-offs:** [What we gain/lose with each option]

2. **[Decision 2]**
   - **Options:** [...]
   - **Your recommendation:** [...]

---

## Your Asks

[What do you need from attendees?]

1. **[Ask 1]** - [Why you need it, by when]
2. **[Ask 2]** - [Why you need it, by when]

---

## Potential Risks/Landmines

[What could go wrong or be sensitive?]

- ⚠️ **[Risk 1]:** [Why it's sensitive] - **How to handle:** [Approach]
- ⚠️ **[Risk 2]:** [Why it's sensitive] - **How to handle:** [Approach]

---

## Success Criteria

This meeting is successful if:
- ✅ [Outcome 1]
- ✅ [Outcome 2]
- ✅ [Outcome 3]

---

## Materials to Bring

[What docs, slides, demos, data to have ready?]

- [ ] [Document/link 1]
- [ ] [Document/link 2]
- [ ] [Demo/prototype if applicable]

---

## Follow-Up Plan

[What happens after this meeting?]

- [ ] Send summary notes by [date]
- [ ] Update [project/stakeholder] on decisions
- [ ] Schedule [follow-up if needed]

---

## Quick Reference

**Key Numbers:** [Any metrics or data you might reference]
- [Metric 1]: [Value]
- [Metric 2]: [Value]

**Key Dates:** [Relevant deadlines or milestones]
- [Date 1]: [Milestone]
- [Date 2]: [Milestone]

**Key People:** [Who to mention or reference]
- [Person]: [Why relevant]

---

## Notes Section
[Leave blank for meeting notes during the call]

```

### 4. Customize for Meeting Type

**1:1 with Manager:**
- Focus: Your progress, blockers, career growth
- Agenda: Quick wins, challenges, help needed, career discussion
- Tone: Collaborative, honest about challenges
- Success: Clear on priorities, unblocked, feedback received

**Stakeholder Review:**
- Focus: Business impact, timeline, risks, decisions
- Agenda: Status summary, wins, risks, asks
- Tone: Professional, confident, data-driven
- Success: Stakeholder aligned, approvals gained, expectations managed

**Technical Discussion:**
- Focus: Technical decisions, architecture, trade-offs
- Agenda: Problem statement, options, recommendation, Q&A
- Tone: Collaborative, open to feedback, data-driven
- Success: Decision made, approach agreed, next steps clear

**Planning/Kickoff:**
- Focus: Scope, timeline, resources, dependencies
- Agenda: Goals, requirements, timeline, roles, risks
- Tone: Organized, realistic, collaborative
- Success: Shared understanding, roles clear, plan agreed

**Team Sync:**
- Focus: Coordination, blockers, dependencies, updates
- Agenda: Round-robin updates, blockers, decisions
- Tone: Collaborative, supportive, action-oriented
- Success: Blockers identified, dependencies clear, aligned

### 5. Research Attendees

For each attendee (from `.workos/context/stakeholders.md`):
- **What they care about** (business metrics vs. technical details)
- **Communication style** (data-driven vs. big picture)
- **Current concerns** (what's keeping them up at night)
- **Your relationship** (manager, peer, first time meeting)

**Adapt briefing accordingly:**
- Technical stakeholder → Include technical details
- Business stakeholder → Focus on business impact
- Executive → BLUF, high-level, decisions only
- Peer → Collaborative, mutual problem-solving

### 6. Check Previous Meeting Notes

If recurring meeting, read last meeting notes:
- Outstanding action items (address them)
- Decisions made (build on them)
- Topics postponed (might need to revisit)
- Concerns raised (show you listened)

### 7. Save Output

Save to: `meetings/prep/YYYY-MM-DD-[meeting-name].md`

Create directory if needed: `meetings/prep/`

Use kebab-case for meeting name: `stakeholder-review`, `api-design-discussion`, `1-1-sarah`

### 8. Present to User

Show the briefing and offer:
- "Here's your meeting prep for [meeting name]. Would you like me to expand any section?"
- "Want me to prepare slides or talking points in more detail?"
- "Should I flag any other potential questions or risks?"

**Offer agent consultations:**
- "Want Copy Editor to polish your talking points?"
- "Should Senior PM help refine your asks?"
- "Need Moneypenny to synthesis background from multiple sources?"

---

## Example Output

```markdown
# Meeting Briefing: Q4 Roadmap Review with VP Product

**Date:** Thursday, October 24, 2025 at 2:00 PM
**Duration:** 60 minutes
**Location:** Zoom (link in calendar)
**Type:** Quarterly Planning Review

---

## Attendees

### Primary
- **Sarah Chen** - VP Product - **Cares about:** Business impact, customer value, strategic alignment
- **You** - Senior PM - Presenting roadmap priorities

### Also Attending
- **Tom Rodriguez** - Engineering Lead - Technical feasibility
- **Maria Santos** - Senior PM (Marketplace) - Cross-team dependencies

---

## Meeting Purpose

Quarterly roadmap review to align on Q1 2026 priorities, gain approval for resource allocation, and identify cross-team dependencies.

---

## Meeting Context

**Background:**
- Q4 wrapping up with dashboard launch success (+15% DAU)
- Enterprise expansion is 2026 company priority (CEO directive)
- Your roadmap supports enterprise growth through API v2 and real-time features

**Why Now:**
- Q4 ends in 6 weeks - need Q1 approval to start planning
- Budget planning cycle requires commitment by Nov 1
- Enterprise customers asking for real-time features (sales blockers)

**Previous Meeting:**
- Q3 review (July 15): Approved dashboard build, noted API tech debt

---

## Agenda

1. **Q4 Recap** (10 min)
   - Dashboard launch results
   - Performance improvements
2. **Q1 Roadmap Proposal** (25 min)
   - Priority 1: API v2 Migration
   - Priority 2: Real-time features
   - Priority 3: Enterprise SSO
3. **Resource Needs & Dependencies** (15 min)
4. **Risks & Mitigation** (5 min)
5. **Q&A & Approval** (5 min)

---

## Your Talking Points

### Must Communicate
1. **Q4 delivered business impact** - Dashboard increased DAU 15%, exceeding 10% projection
2. **Q1 priorities unlock enterprise growth** - API v2 and real-time features directly requested by 3 enterprise prospects ($500K+ ARR)
3. **Resource ask is realistic** - 2 engineers + 1 designer for Q1, same team size as Q4

### If Time Permits
- Mobile app beta going well (4.6⭐ rating)
- Performance improvements created headroom for new features

---

## Questions to Expect

1. **"What's the ROI on API v2 migration?"**
   - **Answer:** Unlocks 3 enterprise deals worth $500K+ ARR (Sales confirmed). Also reduces tech debt that's slowing feature development 30%.
   - **Data:** Current API limits us to 100 req/sec, enterprise needs 500+ req/sec

2. **"Why real-time features vs. [other request]?"**
   - **Answer:** Real-time is #1 customer request (mentioned in 12 of 15 recent sales calls). Competitive differentiation - only 1 of 3 competitors offers it.
   - **Data:** User research shows real-time updates increase engagement 40%

3. **"Do we have engineering capacity for this?"**
   - **Answer:** Yes. Same team size (2 eng + 1 design) delivered dashboard on time. Tom (Eng Lead) validated feasibility.

4. **"What if API migration takes longer than expected?"**
   - **Answer:** Built in 20% buffer (8 weeks estimated, 10 weeks committed). Fallback: Ship real-time as beta to subset while API stabilizes.

---

## Decisions Needed

1. **Q1 Roadmap Approval**
   - **Options:** Approve as-is / Adjust priorities / Request more options
   - **Your recommendation:** Approve - aligns with enterprise strategy
   - **Trade-offs:** Saying yes means deferring [other features] to Q2

2. **Resource Allocation**
   - **Options:** 2 eng + 1 design / More resources / Less scope
   - **Your recommendation:** 2 eng + 1 design (matches Q4, realistic)

---

## Your Asks

1. **Q1 roadmap approval by Oct 31** - Need to start planning sprints
2. **Engineering resource commitment** - 2 engineers + 1 designer for full Q1
3. **Budget for third-party services** - $5K/mo for real-time infrastructure (Pusher)

---

## Potential Risks/Landmines

- ⚠️ **Tom might raise concerns about API migration complexity**
  - **How to handle:** Acknowledge risk, show mitigation (early testing, phased rollout, rollback plan)

- ⚠️ **Sarah may push for additional features beyond capacity**
  - **How to handle:** Use data - show Q4 velocity, explain capacity limits, offer to revisit in Q2

---

## Success Criteria

This meeting is successful if:
- ✅ Q1 roadmap approved (API v2, real-time, SSO)
- ✅ Resource commitment secured (2 eng + 1 design)
- ✅ Sarah confident in plan and business impact

---

## Materials to Bring

- [ ] Q4 metrics dashboard (link: [internal analytics])
- [ ] Q1 roadmap slide deck (draft in Google Slides)
- [ ] Customer quotes on real-time needs (from Sales)
- [ ] API v2 technical spec (Tom prepared)

---

## Follow-Up Plan

- [ ] Send meeting summary with decisions by EOD Oct 24
- [ ] Share detailed Q1 timeline with Engineering by Oct 28
- [ ] Update project tracking with approved roadmap

---

## Quick Reference

**Key Numbers:**
- Q4 DAU increase: +15% (10K → 11.5K)
- Enterprise deals: 3 worth $500K+ ARR
- Current API limit: 100 req/sec (need 500+ for enterprise)
- Q1 budget ask: $15K ($5K/mo × 3 months for infrastructure)

**Key Dates:**
- Nov 1: Budget commitment deadline
- Dec 15: Q4 ends
- Jan 6: Q1 starts (ideally with approved roadmap)

---

## Notes Section
[Use this space for meeting notes]
```

---

## Customization

**Ask user:**
- "Is this your first meeting with these people, or is this recurring?"
- "What's your relationship with the attendees? (Manager, peer, exec, etc.)"
- "What's the most important outcome for you?"
- "Are there any sensitive topics I should flag?"

**Adjust detail level based on meeting importance:**
- High-stakes (exec review, major decision) → Maximum prep
- Low-stakes (team sync, routine 1:1) → Lighter briefing

---

## Integration with Agents

This skill should consult:
- **Moneypenny** - Synthesize background from multiple sources
- **Copy Editor** - Polish talking points and questions
- **Senior PM** - Validate strategic asks and priorities
- **Senior Project Manager** - Confirm timeline and resource estimates
- **Business Analyst** - Pull relevant metrics and data

---

## Notes for Implementation

- If no calendar access, ask user for meeting details
- If attendees not in stakeholders.md, ask user about them
- For recurring meetings, ALWAYS check previous notes
- Flag if meeting is <24 hours away (needs urgent prep)
- Offer to create agenda doc to share pre-meeting
- Consider offering post-meeting notes template

---

*Meeting Prep Assistant - Never walk into a meeting unprepared again*
