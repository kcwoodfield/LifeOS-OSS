# ADR-001: Use PostgreSQL for Primary Database

**Date:** 2025-01-10
**Status:** Accepted
**Deciders:** Engineering Team
**Consulted:** Backend Engineer agent, Engineering Lead agent

---

## Context

### Problem Statement
We need to choose a primary database for our new application. The application will handle user data, transactional operations, and complex queries.

### Requirements
- ACID compliance for financial transactions
- Support for complex queries and joins
- Scalability to 100K+ users
- Team familiarity to minimize ramp-up time
- Strong community support and tooling

---

## Decision

**We will use PostgreSQL as our primary database.**

---

## Options Considered

### Option 1: PostgreSQL
**Pros:**
- ACID compliant and reliable
- Excellent support for complex queries
- JSON support for flexible schema where needed
- Strong ecosystem and tooling
- Team has experience with it

**Cons:**
- Vertical scaling limits (can mitigate with read replicas)
- Slightly more complex than simpler databases

### Option 2: MongoDB
**Pros:**
- Flexible schema
- Horizontal scaling built-in
- Good for document-based data

**Cons:**
- Less suitable for relational data
- Team has limited experience
- ACID only at document level (not great for transactions)

### Option 3: MySQL
**Pros:**
- Similar to PostgreSQL
- Wide adoption

**Cons:**
- PostgreSQL has better JSON support
- Slightly less feature-rich

---

## Rationale

1. **Data model is relational** - Users, accounts, transactions have clear relationships
2. **ACID compliance required** - Financial operations need transaction guarantees
3. **Team expertise** - 3/4 backend engineers have PostgreSQL experience
4. **JSON flexibility** - Can store semi-structured data where needed
5. **Proven at scale** - Many companies run PostgreSQL at our target scale

---

## Consequences

### Positive
- Reliable and battle-tested technology
- Team productive immediately
- Rich feature set (full-text search, JSON, arrays)
- Strong migration path if we outgrow it

### Negative
- Will need to think about read replicas as we scale
- Slightly higher operational complexity than managed NoSQL

### Risks & Mitigation
| Risk | Mitigation |
|------|------------|
| Vertical scaling limits | Plan for read replicas, connection pooling (PgBouncer) |
| Data migration complexity | Use schema migrations from day 1 (Flyway/Liquibase) |

---

## Implementation

- Use PostgreSQL 15 (latest stable)
- Managed service: AWS RDS for ease of operations
- Schema migrations: Flyway
- Connection pooling: PgBouncer
- Backups: Automated daily with 30-day retention

---

## Success Criteria

- Zero data loss incidents
- Query performance <100ms p95
- Successful scaling to 100K users
- Team velocity not impacted by database choice

**Review date:** 2026-01-10 (1 year)

---

## References

- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Use The Index, Luke](https://use-the-index-luke.com/) - Query optimization
- Backend Engineer agent consultation notes
