# Technical Decision Framework

**Triggers:** "Help document this technical decision", "Create ADR", "Technical decision record", "Document this architecture decision"

---

## What This Skill Does

Guides you through documenting a technical decision using the ADR (Architecture Decision Record) format. Ensures important technical choices are captured with context, rationale, and trade-offs for future reference.

**Output:** `decisions/YYYY-MM-DD-[decision-name].md`

---

## How to Use

Simply say:
- "Help me document this technical decision"
- "Create an ADR for choosing PostgreSQL"
- "Document the API authentication approach"
- "Technical decision record for microservices architecture"

---

## Skill Instructions

When this skill is invoked, follow these steps:

### 1. Gather Decision Information

**Ask user for details:**
- What's the decision about? (Brief description)
- What problem are you solving?
- What options did you consider?
- What did you decide?
- Why did you choose this option?

### 2. Consult Relevant Agents

**Based on decision type, consult:**

- **Backend decisions** (database, API, architecture) → Backend Engineer
- **Frontend decisions** (framework, state management, UI patterns) → Frontend Engineer
- **Cross-cutting decisions** (tech stack, architecture patterns) → Engineering Lead
- **Product trade-offs** (scope, features, priorities) → Senior PM
- **Timeline implications** (resources, risks, dependencies) → Senior Project Manager

**What to ask agents:**
- "What are the technical pros/cons of this approach?"
- "What are the risks and mitigation strategies?"
- "Are there alternatives I'm not considering?"
- "What are the long-term maintenance implications?"

### 3. Generate ADR Document

Use the standard ADR template:

```markdown
# ADR-[Number]: [Decision Title]

**Date:** [YYYY-MM-DD]
**Status:** [Proposed / Accepted / Deprecated / Superseded by ADR-XXX]
**Deciders:** [Names of people involved in decision]
**Consulted:** [Agents or people consulted]

---

## Context

### Problem Statement
[What problem are we trying to solve? Why do we need to make this decision now?]

### Background
[Relevant context: technical constraints, business requirements, user needs, current state]

### Requirements
[What must the solution provide? What are the non-negotiables?]

---

## Decision

**We will [decision statement in clear, active voice].**

Example: "We will use PostgreSQL as the primary database for user data."

---

## Options Considered

### Option 1: [Name]
**Description:** [Brief explanation of this approach]

**Pros:**
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]

**Cons:**
- [Disadvantage 1]
- [Disadvantage 2]
- [Disadvantage 3]

**Technical Considerations:**
- [Performance implications]
- [Scalability implications]
- [Security implications]
- [Maintenance implications]

---

### Option 2: [Name]
**Description:** [Brief explanation]

**Pros:**
- [...]

**Cons:**
- [...]

**Technical Considerations:**
- [...]

---

### Option 3: [Name]
[Same structure]

---

## Rationale

### Why We Chose This Option
[Explain the reasoning behind the decision. What made this option better than the alternatives?]

**Key factors:**
1. [Factor 1 - e.g., "Team expertise with PostgreSQL"]
2. [Factor 2 - e.g., "Better fit for relational data model"]
3. [Factor 3 - e.g., "Lower total cost of ownership"]

### Trade-offs Accepted
[What are we giving up by choosing this option?]
- [Trade-off 1]
- [Trade-off 2]

### Assumptions Made
[What are we assuming to be true?]
- [Assumption 1]
- [Assumption 2]

---

## Consequences

### Positive Consequences
- [Benefit 1]
- [Benefit 2]
- [Benefit 3]

### Negative Consequences
- [Cost/limitation 1]
- [Cost/limitation 2]
- [Cost/limitation 3]

### Risks & Mitigation
| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|-------------------|
| [Risk 1] | High/Med/Low | High/Med/Low | [How we'll address it] |
| [Risk 2] | High/Med/Low | High/Med/Low | [How we'll address it] |

---

## Implementation

### Required Changes
- [Change 1]
- [Change 2]
- [Change 3]

### Migration Path
[If replacing something existing, how do we transition?]
- [Step 1]
- [Step 2]
- [Step 3]

### Timeline
- **Decision made:** [Date]
- **Implementation start:** [Date]
- **Expected completion:** [Date]
- **Review date:** [When should we revisit this decision?]

---

## Validation

### Success Criteria
How will we know this decision was correct?
- [Metric 1]
- [Metric 2]
- [Metric 3]

### Review Schedule
- **First review:** [Date] - Check if assumptions still hold
- **Ongoing:** [Frequency] - Periodic reassessment

---

## References

**Documentation:**
- [Link to technical docs]
- [Link to related ADRs]
- [Link to RFCs or proposals]

**Research:**
- [Articles or blog posts consulted]
- [Vendor documentation]
- [Competitor analysis]

**Consultation:**
- [Agent consultations performed]
- [Team members consulted]
- [External experts consulted]

---

## Notes

[Any additional context, discussion points, or future considerations]

---

## Metadata

**Tags:** [database, architecture, backend, etc.]
**Related Projects:** [Link to PRDs or projects affected]
**Supersedes:** [Previous ADR if applicable]
**Superseded By:** [Future ADR if this is deprecated]
```

### 4. Guide User Through Each Section

**For each section, help the user think through:**

**Context Section:**
- "Why now?" - What triggered this decision?
- "What constraints?" - Technical, business, timeline
- "What requirements?" - Must-haves vs. nice-to-haves

**Options Section:**
- "Did you consider at least 3 options?" - Including "do nothing"
- "What are objective pros/cons?" - Not just opinions
- "What are the technical implications?" - Consult engineers

**Rationale Section:**
- "What's the #1 reason for this choice?" - Primary driver
- "What data supports this?" - Metrics, research, proof points
- "What are we optimizing for?" - Speed? Cost? Maintainability?

**Consequences Section:**
- "What happens next?" - Immediate and long-term effects
- "What problems might this create?" - Be honest
- "How do we mitigate risks?" - Proactive planning

**Implementation Section:**
- "What actually needs to change?" - Code, infrastructure, process
- "How do we get from A to B?" - Migration plan
- "When do we revisit?" - Schedule review date

### 5. Number ADRs Sequentially

Check `decisions/` directory for existing ADRs:
- Count existing ADR files
- Assign next sequential number (ADR-001, ADR-002, etc.)
- Use leading zeros for sorting (ADR-001 not ADR-1)

### 6. Apply Best Practices

**Good ADRs are:**
- ✅ **Concise** - 1-2 pages max
- ✅ **Specific** - Clear decision statement
- ✅ **Honest** - Document trade-offs and downsides
- ✅ **Timely** - Written when decision is fresh
- ✅ **Permanent** - Never delete, only deprecate/supersede

**Avoid:**
- ❌ Vague decision statements ("We'll improve performance")
- ❌ Only listing pros for chosen option (be objective)
- ❌ Missing the "why" (rationale is key)
- ❌ Ignoring downsides (every decision has trade-offs)

### 7. Consult Copy Editor

**Always consult Copy Editor to:**
- Ensure decision statement is clear and active voice
- Polish rationale section for stakeholder consumption
- Check for professional tone (ADRs are permanent record)
- Verify structure flows logically

### 8. Save Output

Save to: `decisions/YYYY-MM-DD-[decision-name].md`

Create directory if needed: `decisions/`

Use kebab-case for decision name: `postgresql-database`, `jwt-authentication`, `microservices-architecture`

### 9. Present to User

Show the ADR and offer:
- "Here's your ADR-[number]. Would you like me to expand any section?"
- "Should I consult [specific agent] for more technical depth?"
- "Ready to share with the team for feedback?"

**Suggest next steps:**
- "Post this in your team's docs for review"
- "Share with stakeholders before implementing"
- "Schedule a review date to validate assumptions"

---

## Example Output

```markdown
# ADR-003: Use JWT for API Authentication

**Date:** 2025-10-21
**Status:** Accepted
**Deciders:** User (Senior PM), Tom (Engineering Lead)
**Consulted:** Backend Engineer agent, Security team

---

## Context

### Problem Statement
We need to implement authentication for our REST API to secure user data and enable third-party integrations. Current system has no authentication, which blocks enterprise customers and creates security risks.

### Background
- API currently public and unprotected (launched as prototype)
- Enterprise customers require SSO and API keys
- Mobile app launching next quarter needs secure authentication
- Team has experience with both JWT and session-based auth

### Requirements
- **Must support:** API keys for third-party integrations
- **Must support:** User login via web and mobile
- **Must be:** Scalable to 10K+ concurrent users
- **Must be:** Secure (industry standard)
- **Nice to have:** SSO compatibility for future

---

## Decision

**We will implement JWT (JSON Web Tokens) for API authentication.**

---

## Options Considered

### Option 1: JWT (JSON Web Tokens)
**Description:** Stateless authentication using signed tokens. Client sends token with each request, server validates signature.

**Pros:**
- Stateless - no server-side session storage needed
- Scales horizontally (no shared session state)
- Works seamlessly across multiple services/domains
- Industry standard, well-supported libraries
- Supports API keys and user sessions with same mechanism

**Cons:**
- Tokens can't be invalidated before expiry (must wait for timeout)
- Token payload visible (base64 encoded, not encrypted)
- Larger request size (tokens in header every request)
- Requires secure secret management

**Technical Considerations:**
- Performance: Fast (no DB lookup per request)
- Scalability: Excellent (stateless)
- Security: Good if implemented correctly (HTTPS required)
- Complexity: Medium (need refresh token strategy)

---

### Option 2: Session-Based Authentication
**Description:** Traditional server-side sessions stored in Redis/database. Client gets session ID cookie.

**Pros:**
- Easy to invalidate sessions immediately
- Smaller request size (just session ID)
- Simpler mental model
- Better for traditional web apps

**Cons:**
- Requires shared session storage (Redis cluster)
- Harder to scale horizontally
- CORS complications for API access
- Not ideal for mobile apps or third-party integrations
- Additional infrastructure (Redis) required

**Technical Considerations:**
- Performance: Good (Redis is fast)
- Scalability: Harder (requires session replication)
- Security: Good (server-side control)
- Complexity: Lower for web, higher for API

---

### Option 3: OAuth 2.0 (with Auth0/Okta)
**Description:** Outsource authentication to third-party provider.

**Pros:**
- Enterprise SSO out of the box
- Security handled by experts
- Faster implementation (no auth code)
- Built-in features (MFA, social login)

**Cons:**
- Vendor lock-in
- Monthly cost ($200-500/mo for our scale)
- Less control over auth flow
- External dependency (outage risk)

**Technical Considerations:**
- Performance: Depends on provider
- Scalability: Excellent (vendor handles it)
- Security: Excellent (industry experts)
- Complexity: Low for implementation, high for customization

---

## Rationale

### Why We Chose This Option

**Key factors:**
1. **Scalability requirements** - Microservices architecture planned, stateless auth is better fit
2. **API-first design** - JWT works naturally with API keys and mobile apps
3. **Team expertise** - Team has JWT experience from previous projects
4. **Cost** - No vendor fees, infrastructure we already have
5. **Future SSO** - Can integrate SSO with JWT later (not blocked)

### Trade-offs Accepted
- **Can't instantly revoke tokens** - Mitigated with short expiry (15 min access tokens, refresh token rotation)
- **Token management complexity** - Accepted for scalability benefits
- **Need HTTPS everywhere** - Already planned, not additional cost

### Assumptions Made
- HTTPS is enforced across all services
- Token expiry of 15 minutes is acceptable UX
- Team can implement secure token refresh mechanism
- Secret rotation process will be documented

---

## Consequences

### Positive Consequences
- API scales horizontally without session coordination
- Mobile app and web use same auth mechanism
- Third-party integrations supported with API keys
- No additional infrastructure needed (Redis avoided)
- Future microservices use same auth pattern

### Negative Consequences
- Must implement refresh token rotation (security best practice, adds complexity)
- Logout requires token blacklist or wait for expiry
- Secret management becomes critical (leaks are serious)

### Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation Strategy |
|------|------------|--------|-------------------|
| Token secret leaked | Low | Critical | Rotate secrets monthly, use env vars, monitor for unusual activity |
| Token replay attacks | Medium | High | Short expiry (15 min), refresh token rotation, HTTPS only |
| Users can't logout immediately | Low | Medium | Implement token blacklist for critical logout scenarios |
| XSS token theft | Medium | High | HttpOnly cookies for web, secure storage for mobile |

---

## Implementation

### Required Changes
- Add JWT library (jsonwebtoken npm package)
- Create token generation endpoint (/auth/login)
- Create token refresh endpoint (/auth/refresh)
- Add middleware to validate tokens on protected routes
- Implement token blacklist for logout (Redis)
- Add secret rotation process

### Migration Path
1. **Phase 1:** Implement JWT auth alongside current no-auth (2 weeks)
2. **Phase 2:** Update web app to use JWT (1 week)
3. **Phase 3:** Update mobile app to use JWT (1 week)
4. **Phase 4:** Require auth for all endpoints (1 week)
5. **Phase 5:** Remove no-auth fallback

### Timeline
- **Decision made:** 2025-10-21
- **Implementation start:** 2025-10-28
- **Expected completion:** 2025-11-25 (4 weeks)
- **Review date:** 2025-12-25 (1 month post-launch)

---

## Validation

### Success Criteria
- 99.9% auth request success rate
- <50ms token validation latency (p95)
- Zero security incidents in first 3 months
- Mobile and web apps successfully using JWT
- API keys working for 3+ third-party integrations

### Review Schedule
- **First review:** 2025-12-25 - Check success criteria, any security issues?
- **Ongoing:** Quarterly - Is JWT still the right choice as we scale?

---

## References

**Documentation:**
- [JWT.io](https://jwt.io) - JWT introduction and debugger
- [OWASP JWT Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html)
- Internal: API Authentication RFC (link)

**Research:**
- [Auth0: JWT vs. Sessions](https://auth0.com/blog/...)
- [How to store JWT securely](https://...)

**Consultation:**
- Backend Engineer agent: Technical implementation guidance
- Security team: Secret rotation process review
- Engineering Lead: Microservices auth strategy alignment

---

## Notes

- If we add SSO in future, JWT makes integration easier (use JWT after SSO flow)
- Consider OAuth wrapper around JWT for third-party integrations (more standard)
- Monitor token size - if payload grows, evaluate impact on bandwidth

---

## Metadata

**Tags:** #authentication #api #security #backend
**Related Projects:** API v2 Migration, Mobile App Launch
**Supersedes:** None (first auth implementation)
**Superseded By:** None
```

---

## Customization

**Ask user:**
- "Is this decision reversible or one-way door?" (Changes urgency and depth)
- "Who needs to approve this?" (Affects consultation and review)
- "What's the implementation timeline?" (Affects migration planning)

**Adjust based on decision importance:**
- **Critical** (infrastructure, architecture) → Maximum rigor, multi-agent consultation
- **Medium** (feature tech choices) → Standard ADR
- **Low** (library choice, minor pattern) → Lightweight ADR (can skip some sections)

---

## Integration with Agents

This skill should consult:

**Technical decisions:**
- **Backend Engineer** - Database, API, infrastructure decisions
- **Frontend Engineer** - UI framework, state management, component patterns
- **Engineering Lead** - Architecture, cross-cutting concerns, tech strategy

**Business impact:**
- **Senior PM** - How decision affects product roadmap, user experience
- **Senior Project Manager** - Timeline and resource implications
- **Business Analyst** - Data implications, analytics requirements

**Communication:**
- **Copy Editor** - Polish ADR for stakeholder consumption, ensure clarity

---

## Best Practices

### When to Create an ADR
- Architecture decisions (database, framework, services)
- Security decisions (authentication, authorization, encryption)
- Infrastructure decisions (cloud provider, deployment strategy)
- Third-party integrations (vendor selection, API choices)
- Breaking changes (migrations, deprecations)

### When NOT to Create an ADR
- Implementation details (variable names, code style)
- Temporary workarounds
- Reversible experiments ("let's try this")
- Routine bug fixes

### ADR Maintenance
- **Never delete ADRs** - They're historical record
- **Deprecate instead** - Mark status as "Deprecated" or "Superseded by ADR-XXX"
- **Review annually** - Do assumptions still hold?
- **Update status** - Proposed → Accepted → Deprecated

---

## Notes for Implementation

- Auto-number ADRs by scanning `decisions/` directory
- Offer templates for common decision types (database, auth, framework)
- Link related ADRs automatically (if decision builds on previous)
- Suggest consulting relevant agents based on decision type keywords
- Create index file `decisions/INDEX.md` listing all ADRs with status

---

*Technical Decision Framework - Document the why, not just the what*
