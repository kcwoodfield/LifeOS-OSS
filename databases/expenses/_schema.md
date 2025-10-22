# Expense Schema Template

Use this frontmatter structure for all expense files in `databases/expenses/`.

```yaml
---
name: "Expense name"
category: housing              # housing | utilities | subscriptions | insurance | debt | food | transport | health | entertainment | other
amount: 0.00
frequency: monthly             # monthly | annual | quarterly | weekly | one-time
due_day: 1                     # Day of month (1-31) or null for non-monthly
status: pending                # pending | paid | overdue | cancelled
payment_method: auto           # auto | manual | credit-card | bank-transfer
account: null                  # Which account/card this comes from
url: null                      # Login URL or payment portal
notes: null
created: 2025-10-19
updated: 2025-10-19
---

# Expense Details

Any additional notes, payment history, or context.

## Payment History

- 2025-10: Paid on [date]
- 2025-09: Paid on [date]

## Notes

- Account info, credentials location, cancellation policy, etc.
```

## Field Definitions

### Required Fields

**name** (string)
- Clear expense name
- Examples: "Rent - Main St Apartment", "Netflix Subscription", "Car Insurance"

**category** (enum)
- `housing` - Rent, mortgage, HOA fees
- `utilities` - Electric, water, gas, internet, phone
- `subscriptions` - Software, streaming, memberships
- `insurance` - Health, auto, home, life
- `debt` - Credit cards, loans, student loans
- `food` - Groceries, dining (if tracked separately)
- `transport` - Car payment, gas, public transit
- `health` - Medical bills, prescriptions, gym
- `entertainment` - Hobbies, activities, fun money
- `other` - Miscellaneous

**amount** (number)
- Dollar amount (no $ sign)
- Examples: `1500.00`, `12.99`, `250`

**frequency** (enum)
- `monthly` - Bills every month
- `annual` - Once per year
- `quarterly` - Every 3 months
- `weekly` - Every week
- `one-time` - Single payment

**due_day** (number or null)
- Day of month when due (1-31)
- Null for non-monthly expenses or variable dates
- Used for auto-sorting by due date

**status** (enum)
- `pending` - Not yet paid this cycle
- `paid` - Paid for current cycle
- `overdue` - Missed payment date
- `cancelled` - No longer active

**created** (date)
- Date expense was added to system

**updated** (date)
- Last modified date

### Optional Fields

**payment_method** (enum)
- `auto` - Auto-pay enabled (default)
- `manual` - Must pay manually
- `credit-card` - Paid via credit card
- `bank-transfer` - Bank account transfer

**account** (string)
- Which bank account or credit card
- Examples: "Chase Sapphire", "Capital One Checking", "Amex Gold"

**url** (string)
- Payment portal or login URL
- For quick access to pay bills

**notes** (string)
- Any additional context, account numbers, cancellation info

## Example Expenses

### Monthly Recurring Bill

```yaml
---
name: "Rent - 123 Main St"
category: housing
amount: 2200.00
frequency: monthly
due_day: 1
status: pending
payment_method: bank-transfer
account: Chase Checking
url: https://portal.propertymanager.com
notes: "Auto-pay disabled, pay manually by 1st of month"
created: 2025-10-19
updated: 2025-10-19
---
```

### Subscription Service

```yaml
---
name: "Netflix Premium"
category: subscriptions
amount: 19.99
frequency: monthly
due_day: 15
status: paid
payment_method: credit-card
account: Amex Gold
url: https://netflix.com/account
notes: "Family plan, auto-renews"
created: 2025-10-19
updated: 2025-10-19
---
```

### Annual Expense

```yaml
---
name: "Amazon Prime"
category: subscriptions
amount: 139.00
frequency: annual
due_day: null
status: pending
payment_method: credit-card
account: Chase Sapphire
url: https://amazon.com/prime
notes: "Renews every March"
created: 2025-10-19
updated: 2025-10-19
---
```

---

**See:** `databases/expenses/README.md` for usage guide and workflow
