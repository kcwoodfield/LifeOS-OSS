# Expenses Database

> **Purpose:** Track all monthly recurring expenses, bills, and subscriptions
> **Owner:** Banker (CFO) - Financial tracking and wealth building

---

## Overview

This database tracks all recurring expenses, bills, and subscriptions. Expenses auto-sort by due date, with items due today appearing at the top. Status updates automatically move paid items down the list.

**Key Features:**
- Auto-sorted checklist by due date
- Category-based expense tracking
- Payment status monitoring (pending, paid, overdue)
- Monthly and annual expense totals
- Financial dashboard integration

---

## Schema

See `_schema.md` for the complete frontmatter template.

**Required Fields:**
- `name` - Expense name
- `category` - Expense type (housing, utilities, subscriptions, etc.)
- `amount` - Dollar amount
- `frequency` - monthly | annual | quarterly | weekly | one-time
- `due_day` - Day of month when due (1-31) or null
- `status` - pending | paid | overdue | cancelled

**Optional Fields:**
- `payment_method` - auto | manual | credit-card | bank-transfer
- `account` - Which bank/card this comes from
- `url` - Payment portal URL
- `notes` - Additional context

---

## Workflow

### Adding New Expenses

1. **Use template:** `templates/new-expense.md`
2. Fill in all required fields
3. Set `status: pending` for upcoming bills
4. Set `due_day` to enable auto-sorting
5. Save to `databases/expenses/`

### Monthly Bill Paying Routine

1. **View dashboard:** `dashboards/finances.md` shows bills due soon
2. **Pay bill:** Visit payment portal (URL in frontmatter)
3. **Update status:** Change `status: pending` → `status: paid`
4. **Log payment:** Add date to payment history in file body
5. **Next month:** At month-end, reset all to `status: pending`

### End of Month Reset

On the last day of the month:
1. Review all expenses with `status: paid`
2. Reset to `status: pending` for next month
3. Check for any `overdue` items and resolve

---

## Views & Queries

### Bills Due This Month (Auto-sorted by due date)

```dataview
TABLE
  due_day as "Due",
  amount as "Amount",
  category as "Category",
  payment_method as "Method",
  status as "Status"
FROM "databases/expenses"
WHERE frequency = "monthly" AND status != "cancelled"
SORT due_day ASC
```

This query powers the auto-sorted checklist - items due today appear at top, then subsequent days.

### Bills Due Today or Overdue

```dataview
TABLE
  amount as "Amount",
  category as "Category",
  url as "Pay Here"
FROM "databases/expenses"
WHERE
  frequency = "monthly"
  AND status = "pending"
  AND due_day <= number(date(today).day)
SORT due_day ASC
```

### Total Monthly Expenses

```dataviewjs
const expenses = dv.pages('"databases/expenses"')
  .where(p => p.frequency === "monthly" && p.status !== "cancelled");

const total = expenses
  .map(p => p.amount || 0)
  .reduce((sum, amt) => sum + amt, 0);

dv.header(3, `Total Monthly Expenses: $${total.toFixed(2)}`);
```

### Expenses by Category

```dataview
TABLE
  rows.file.link as "Expense",
  sum(rows.amount) as "Total"
FROM "databases/expenses"
WHERE frequency = "monthly" AND status != "cancelled"
GROUP BY category
SORT sum(rows.amount) DESC
```

### Annual Expenses (Upcoming)

```dataview
TABLE
  amount as "Amount",
  notes as "Renewal Info"
FROM "databases/expenses"
WHERE frequency = "annual" AND status != "cancelled"
SORT amount DESC
```

---

## Naming Convention

**File naming:** `category-expense-name.md`

**Examples:**
- `housing-rent-main-st.md`
- `subscriptions-netflix.md`
- `utilities-electric-pge.md`
- `insurance-auto-geico.md`

**Why this format:**
- Groups by category in file browser
- Clear identification
- Easy to find specific expenses

---

## Tips

**Setting Up Auto-Pay:**
- Mark `payment_method: auto` for auto-pay bills
- These require less monitoring but check monthly for errors
- Keep login URLs handy in case auto-pay fails

**Tracking Variable Expenses:**
- For utilities with variable amounts, use average monthly cost
- Update `amount` quarterly based on actual usage
- Track seasonality (higher electric in summer, etc.)

**Subscription Audits:**
- Quarterly review: Are you using all subscriptions?
- Cancel unused services immediately
- Look for annual vs. monthly pricing (often cheaper annually)

**Payment Methods:**
- Use specific credit cards for categories (travel cards for subscriptions, etc.)
- Track which account each expense comes from
- Useful for budgeting and fraud detection

**Overdue Tracking:**
- Set reminder to check dashboard weekly
- Any `status: overdue` items need immediate attention
- Late fees compound quickly

---

## Integration with Financial Dashboard

The expenses database feeds into `dashboards/finances.md`:
- **This Month's Bills:** Due today and upcoming
- **Monthly Burn Rate:** Total recurring expenses
- **Income vs. Expenses:** Cash flow calculation
- **Category Breakdown:** Where money goes
- **Annual Snapshot:** Projected yearly spend

---

**Last Updated:** 2025-10-19
