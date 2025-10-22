---
allowed-tools: Write(*), Bash(date +%Y-%m-%d)
description: Create an idea file and add to the base
---

# Context

The today's date is `!date +%Y-%m-%d`

# Task

1. Give the 3-5 words file name for the idea {idea-name}.
2. Create file `{date}-{idea-name}.md` in the root directory of the repository with the following content.
3. Clean up the idea raw input to remove filler words and make it more concise.

```markdown
---
tags: [idea]
date: {date}
status: new
effort: M
category: lifeos-infra
---

# {idea-title}

{cleaned-idea}
```
