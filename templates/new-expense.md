---
name: "<% tp.file.cursor(1) %>"
category: subscriptions
amount: 0.00
frequency: monthly
due_day: <% tp.date.now("D") %>
status: pending
payment_method: auto
account: null
url: null
notes: null
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

## Payment History

- <% tp.date.now("YYYY-MM") %>:

## Notes

-
