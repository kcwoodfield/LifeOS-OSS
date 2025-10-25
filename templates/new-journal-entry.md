---
title: "<% tp.date.now("YYYY-MM-DD") %> Journal"
date: <% tp.date.now("YYYY-MM-DD") %>
mood: neutral
energy: 7
gratitude: []
highlights: []
challenges: []
insights: []
tags: []
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# Journal Entry - <% tp.date.now("MMMM DD, YYYY") %>

## Morning

<% tp.file.cursor(1) %>

## Day

<% tp.file.cursor(2) %>

## Evening

<% tp.file.cursor(3) %>

## Gratitude

1. <% tp.file.cursor(4) %>
2.
3.

---

**Energy:** <% tp.file.cursor(5) %>/10
**Mood:** <% tp.file.cursor(6) %>
