---
date: <% tp.date.now("YYYY-MM-DD") %>
project: <% tp.file.cursor(1) %>
start_time: "<% tp.file.cursor(2) %>"
end_time: "<% tp.file.cursor(3) %>"
duration_hours: <% tp.file.cursor(4) %>
category: <% tp.file.cursor(5) %>
focus: <% tp.file.cursor(6) %>
energy: medium
productivity: 7
notes: "<% tp.file.cursor(7) %>"
tags: []
created: <% tp.date.now("YYYY-MM-DD") %>
---

# Session: <% tp.file.cursor(8) %>

## What I Worked On

- <% tp.file.cursor(9) %>

## What Shipped

-

## Learnings / Blockers

-

## Next Session

-
