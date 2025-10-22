# Standup Report Generator

**Triggers:** "Generate my standup report", "Create standup", "Daily standup"

---

## What This Skill Does

Generates a structured daily standup report based on your current work tasks and recent activity. The report follows the standard standup format: Yesterday → Today → Blockers.

**Output:** `communications/standups/YYYY-MM-DD.md`

---

## How to Use

Simply say:
- "Generate my standup report"
- "Create standup for today"
- "Help me write my daily standup"

---

## Skill Instructions

When this skill is invoked, follow these steps:

### 1. Gather Context

**Read these files:**
- `databases/tasks/*.md` - Check task statuses for recent work
- `.workos/context/current-projects.md` - Understand active projects
- `communications/standups/` - Check yesterday's standup to see what was planned

**Look for:**
- Tasks marked as "completed" recently (yesterday's work)
- Tasks with status "in_progress" (today's focus)
- Tasks marked with blockers or status "blocked"
- Project updates in PRDs

### 2. Generate Standup Structure

Use this template:

```markdown
# Daily Standup - [Today's Date]

## Yesterday
- [What was completed/worked on]
- [Progress made on ongoing tasks]
- [Meetings attended that moved work forward]

## Today
- [Top 3 priorities for today]
- [Meetings scheduled and their purpose]
- [Tasks to complete]

## Blockers
- [Active blockers preventing progress]
- [Dependencies waiting on others]
- [None if no blockers]

## Notes
- [Any additional context or updates]
```

### 3. Populate Content

**Yesterday Section:**
- List completed tasks from databases/tasks/
- Summarize progress on in-progress work
- Include key meetings if they advanced work
- Be specific: "Completed user auth API" not "worked on stuff"

**Today Section:**
- Prioritize top 3 tasks for today (from highest priority in databases/tasks/)
- List scheduled meetings with context ("1:1 with manager: discuss Q4 roadmap")
- Be realistic about what can be accomplished
- If unsure of priorities, note "TBD after reviewing backlog"

**Blockers Section:**
- List any tasks marked "blocked" with reason
- Note dependencies on other teams/people
- If no blockers, write "None"
- Include who/what is needed to unblock

**Notes Section (optional):**
- Timeline updates or deadline changes
- Quick wins worth mentioning
- Context others on the team should know

### 4. Apply Professional Polish

- **Be concise** - Bullet points, not paragraphs
- **Be specific** - "Reduced API latency 40%" not "improved performance"
- **Be honest** - If blocked, say so clearly
- **Be professional** - This is stakeholder-facing communication

**Consult Copy Editor if:**
- Standup needs to communicate delays or bad news
- Phrasing needs to be more professional
- Unsure how to explain a blocker

### 5. Save Output

Save to: `communications/standups/YYYY-MM-DD.md`

Create the directory if it doesn't exist: `communications/standups/`

### 6. Present to User

Show the generated standup and offer:
- "Here's your standup for [date]. Would you like me to revise anything?"
- "Copy this to Slack or your standup tool when ready."

---

## Example Output

```markdown
# Daily Standup - October 21, 2025

## Yesterday
- Completed user authentication API (JWT implementation, tested with 100 users)
- Reviewed and merged 3 PRs for the dashboard feature
- Met with Design team to finalize mobile app mockups

## Today
- Implement password reset flow (backend + email templates)
- Code review for Frontend's component refactor PR
- 1:1 with manager: Discuss Q4 roadmap priorities

## Blockers
- Dashboard deployment blocked waiting on DevOps to provision staging environment (requested Oct 18, no ETA yet)

## Notes
- Mobile app mockups approved - development can start tomorrow
- API performance improvement shipped: reduced latency from 800ms to 480ms
```

---

## Customization

Users can customize the standup format by:
- Adding additional sections (e.g., "Learnings", "Help Needed")
- Changing the structure (some teams use "Wins" instead of "Yesterday")
- Adjusting detail level based on team culture

**Ask the user:** "Is this standup format right for your team, or would you like me to adjust the structure?"

---

## Integration with Agents

This skill can consult:
- **Moneypenny** - Help prioritize today's tasks if not clear from task list
- **Copy Editor** - Polish phrasing if communicating delays or bad news
- **Senior Project Manager** - Context on blockers and timeline implications

---

## Notes for Implementation

- Check if `communications/standups/` directory exists, create if needed
- Pull date from system (format: YYYY-MM-DD)
- If no tasks found in databases/tasks/, prompt user to add context manually
- Consider reading last 2-3 standups to avoid repetition

---

*Standup Report Generator - Quick, accurate, professional daily updates*
