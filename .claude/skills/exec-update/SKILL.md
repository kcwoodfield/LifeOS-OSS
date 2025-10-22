# Executive Update Generator

**Triggers:** "Create exec update", "Generate executive update", "Weekly status update", "Write stakeholder update"

---

## What This Skill Does

Generates a professional executive-level status update summarizing progress, wins, risks, and next steps for your projects. Formatted for busy executives who want the bottom line upfront.

**Output:** `communications/exec-updates/YYYY-MM-DD.md`

---

## How to Use

Simply say:
- "Create exec update for this week"
- "Generate executive update"
- "Help me write a stakeholder update"
- "Weekly status update"

---

## Skill Instructions

When this skill is invoked, follow these steps:

### 1. Gather Context

**Read these files:**
- `projects/prds/*.md` - Check project status, progress, blockers
- `databases/tasks/*.md` - Review completed and in-progress tasks
- `.workos/context/current-projects.md` - Understand active initiatives
- `.workos/context/stakeholders.md` - Know your audience and their priorities
- `communications/exec-updates/` - Review last update to track progress since then

**Look for:**
- Project milestones completed
- Key metrics or business impact
- Risks, blockers, or timeline changes
- Major decisions made
- Upcoming deadlines or launches

### 2. Generate Update Structure

Use this **executive-friendly template:**

```markdown
# Executive Update - [Week of Date]

**Status:** [🟢 On Track / 🟡 At Risk / 🔴 Off Track]

---

## Summary (TL;DR)
[2-3 sentence executive summary of the week - what they absolutely need to know]

---

## Progress This Week

### [Project Name 1]
**Status:** [Green/Yellow/Red]
- [Key achievement 1]
- [Key achievement 2]
- [Metric impact if applicable]

### [Project Name 2]
**Status:** [Green/Yellow/Red]
- [Key achievement 1]
- [Key achievement 2]

---

## Wins & Impact
- [Win 1 with business impact]
- [Win 2 with business impact]
- [Metric: X% improvement in Y]

---

## Risks & Blockers
### High Priority
- [Risk/blocker 1] - **Impact:** [what's at stake] - **Mitigation:** [what you're doing about it]

### Medium Priority
- [Risk/blocker 2] - **Mitigation:** [plan]

### Resolved This Week
- [Previously flagged risk that's now resolved]

---

## Next Week Priorities
1. [Top priority 1] - [why it matters]
2. [Top priority 2] - [why it matters]
3. [Top priority 3] - [why it matters]

---

## Action Needed (if any)
- [Specific ask with deadline] - **Owner:** [who you need]
- OR: *No action needed - FYI only*

---

## Additional Context
[Optional: Anything else execs should know]
```

### 3. Populate Content with Executive Mindset

**Summary Section:**
- Lead with impact, not activity
- Answer: "What changed this week that execs care about?"
- Example: ❌ "We had 3 meetings" vs. ✅ "Dashboard launch on track for Nov 1, 15% DAU increase projected"

**Progress Section:**
- Group by project, not task
- Use traffic light status (Green/Yellow/Red) for scanability
- Include metrics when available ("reduced latency 40%" not "improved performance")
- Be specific but concise

**Wins & Impact:**
- Connect wins to business outcomes
- Quantify when possible (%, $, time saved, users impacted)
- This is where you highlight value delivered
- Example: "Shipped mobile app beta → 4.6⭐ rating from 100 early users → validates Q1 launch"

**Risks & Blockers:**
- **Always include mitigation** - Don't just report problems, show you're handling them
- Tier by urgency (High/Medium/Resolved)
- Be honest but not alarmist
- Include what you need from execs (approval, resources, unblocking)

**Next Week Priorities:**
- Max 3 priorities - focus matters
- Connect to business goals when possible
- Include why each priority matters (not just what)

**Action Needed:**
- Be specific: who, what, by when
- Make it easy for execs to help you
- If no action needed, explicitly say "FYI only"

### 4. Apply Executive Communication Standards

**Consult Copy Editor for:**
- Polishing tone for specific stakeholders (check `.workos/context/stakeholders.md`)
- Softening bad news while staying honest
- Strengthening impact statements
- Ensuring BLUF (Bottom Line Up Front)

**Writing Guidelines:**
- **Concise:** Execs are busy - respect their time
- **Scannable:** Use bullets, headers, bold for key info
- **Specific:** Dates, numbers, names - not vague language
- **Honest:** Transparency builds trust
- **Professional:** Corporate-appropriate tone

### 5. Tailor to Audience

Check `.workos/context/stakeholders.md` for:
- Communication preferences (detail level, frequency)
- What each stakeholder cares about (business metrics vs. technical progress)
- Sensitive topics or hot buttons

**Adjust accordingly:**
- Technical stakeholders → More technical detail
- Business stakeholders → More business impact
- CEO/Execs → Maximum brevity, maximum impact

### 6. Save Output

Save to: `communications/exec-updates/YYYY-MM-DD.md`

Create directory if needed: `communications/exec-updates/`

Use date format: `YYYY-MM-DD` (e.g., `2025-10-21.md`)

### 7. Present to User

Show the generated update and offer:
- "Here's your executive update for [week of date]. Would you like me to adjust tone, add detail, or tailor for specific stakeholders?"
- "Ready to send? I can polish specific sections if needed."
- Offer to create subject line for email: **"[Project Name] - [Status] Update - Week of [Date]"**

---

## Example Output

```markdown
# Executive Update - Week of October 21, 2025

**Status:** 🟢 On Track

---

## Summary (TL;DR)
Dashboard feature launched on schedule (Oct 20), early metrics show 15% DAU increase. Mobile app progressing toward Nov launch, but API dependency flagged as medium risk requiring early testing.

---

## Progress This Week

### User Dashboard (Launched 🚀)
**Status:** 🟢 Complete
- Launched Oct 20 to 100% of users
- Early metrics: +15% DAU (10K → 11.5K daily active)
- User engagement: 2.3x more interactions with data
- Zero critical bugs reported

### Mobile App (Beta)
**Status:** 🟢 On Track
- UI complete, in QA review (95% test coverage)
- Backend API integration 70% complete
- Beta cohort identified: 100 power users

### API Performance Optimization
**Status:** 🟢 Complete
- Reduced latency 40% (800ms → 480ms)
- Improved page load speed 25%
- Deployed to production Oct 19

---

## Wins & Impact
- **Dashboard adoption exceeding projections:** 15% DAU increase vs. 10% projected
- **Performance improvement shipped:** API latency down 40%, directly improving UX
- **Mobile beta on schedule:** Nov 1 public launch achievable

---

## Risks & Blockers

### Medium Priority
- **Mobile API dependency** - Third-party API integration more complex than estimated (auth requires custom OAuth not documented)
  - **Impact:** Could delay mobile launch 1-2 weeks if issues found late
  - **Mitigation:** Moved integration testing up 2 weeks, adding senior engineer for early validation

### Resolved This Week
- ✅ Dashboard deployment blocker (DevOps environment issue) - resolved Oct 18

---

## Next Week Priorities
1. **Complete mobile API integration** (target: Oct 27) - Critical path for Nov 1 launch
2. **Mobile beta rollout** (100 users) - Validates stability before public launch
3. **Dashboard metrics analysis** - Confirm 15% DAU increase is sustained after week 1

---

## Action Needed
*No action needed - FYI only*

(Mobile launch timeline remains Nov 1 pending API integration completion)

---

## Additional Context
- Dashboard post-launch monitoring continues through Oct 27
- Planning Q4 roadmap review for next week - will share draft priorities
```

---

## Customization

**Adjust for different audiences:**

**For CEO/C-Suite:**
- Ultra-brief (1 page max)
- Business impact only
- Strategic implications
- Clear asks

**For Director/VP:**
- Moderate detail
- Balance business + technical
- Cross-team dependencies
- Resource needs

**For Team/Peers:**
- More technical depth
- Implementation details
- Team velocity
- Blockers to collaborate on

**Ask user:** "Who's the primary audience for this update? I can adjust the detail level and focus."

---

## Integration with Agents

This skill should consult:
- **Copy Editor** - Polish tone and structure (ALWAYS - exec comms are high stakes)
- **Senior PM** - Validate business impact claims and priorities
- **Senior Project Manager** - Confirm timeline and risk assessments
- **Business Analyst** - Verify metrics and data accuracy

---

## Notes for Implementation

- If no projects found in `projects/prds/`, prompt user for manual input
- Check last exec update date - flag if it's been >7 days
- Scan for "yellow" or "red" project statuses - flag risks prominently
- Offer to create email subject line + intro paragraph
- Consider adding "Wins" section by default - positivity builds credibility

---

*Executive Update Generator - Bottom-line-up-front, impact-focused, executive-ready communication*
