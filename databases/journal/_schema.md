# Journal Entry Schema Template

Use this frontmatter structure for all journal files in `databases/journal/`.

```yaml
---
title: "YYYY-MM-DD Journal"
date: 2025-10-19
mood: neutral                # great | good | neutral | low | difficult
energy: 7                    # 1-10 scale
gratitude: []                # List of things grateful for
highlights: []               # Best moments of the day
challenges: []               # Difficult moments
insights: []                 # Learnings or realizations
tags: []
created: 2025-10-19
updated: 2025-10-19
---

# Journal Entry - October 19, 2025

## Morning

What's on your mind as you start the day? Intentions, anxieties, hopes?

## Day

What happened today? Stream of consciousness or structured reflection.

## Evening

How are you feeling now? What went well? What was hard?

## Gratitude

1. Thing 1
2. Thing 2
3. Thing 3
```

## Field Definitions

### Required Fields

**title** (string)
- Journal entry title
- Format: "YYYY-MM-DD Journal" or custom title
- Examples: "2025-10-19 Journal", "A Day of Breakthroughs", "Processing Grief"

**date** (date)
- Entry date: YYYY-MM-DD
- Used for chronological tracking

**created** (date)
- Date this note was created: YYYY-MM-DD
- Auto-filled by template

### Optional Fields

**mood** (enum or null)
- Overall emotional state for the day
- `great` - Exceptionally good day, high spirits
- `good` - Positive, content, stable
- `neutral` - Balanced, neither high nor low
- `low` - Down, tired, unmotivated
- `difficult` - Struggling, anxious, stressed
- Null if not tracking mood

**energy** (number or null)
- Physical/mental energy level: 1-10 scale
- 10 = Peak energy, fully charged, ready for anything
- 7-9 = Good energy, productive capacity
- 4-6 = Moderate energy, can function but limited
- 1-3 = Low energy, depleted, need rest
- Null if not tracking energy

**gratitude** (array)
- Things you're grateful for today
- Format: `["Thing 1", "Thing 2", "Thing 3"]`
- Can be big or small: `["Family health", "Good coffee", "Sunset colors"]`
- Empty array `[]` if none captured

**highlights** (array)
- Best moments or wins from the day
- Format: `["Moment 1", "Moment 2"]`
- Examples: `["Breakthrough on YourProject bug", "Great conversation with friend", "Nailed the presentation"]`
- Empty array `[]` if none

**challenges** (array)
- Difficult moments, frustrations, struggles
- Format: `["Challenge 1", "Challenge 2"]`
- Examples: `["Conflict with coworker", "Couldn't focus all morning", "Anxiety about deadline"]`
- Empty array `[]` if none
- Safe space to vent

**insights** (array)
- Learnings, realizations, patterns noticed
- Format: `["Insight 1", "Insight 2"]`
- Examples: `["I work better in morning than evening", "Need to set boundaries with manager", "Art practice grounds me"]`
- Empty array `[]` if none

**tags** (array)
- Themes, emotions, topics
- Examples: `[art-practice, career, anxiety, breakthrough, relationships, health]`
- Empty array `[]` if no tags
- Useful for finding entries by theme later

**updated** (date)
- Last modified date: YYYY-MM-DD
- Update if you add to entry later

## Mood & Energy Scale Details

### Mood Definitions

**great:** Peak experience
- Feeling exceptionally good
- High spirits, energized, optimistic
- Things are flowing
- Rare but worth noting

**good:** Positive day
- Content and stable
- Productive and engaged
- General sense of well-being
- This is the sustainable baseline

**neutral:** Balanced
- Neither high nor low
- Going through motions
- Not bad, just existing
- Most days fall here

**low:** Down day
- Unmotivated, tired
- Harder to engage
- Not quite struggling but not okay
- Need self-compassion

**difficult:** Struggling
- Anxious, stressed, overwhelmed
- Hard to function
- Need support or intervention
- Track patterns to prevent spiraling

### Energy Scale

**8-10:** Peak Energy
- Fully charged, ready for hard problems
- Can tackle creative work, strategic thinking
- Best time for important decisions
- Protect this time for high-leverage work

**5-7:** Good Energy
- Solid productive capacity
- Can do most work effectively
- May need breaks but functional
- This is "normal operating mode"

**3-4:** Low Energy
- Limited capacity
- Do routine tasks, avoid hard decisions
- Need rest and recharge soon
- Not ideal for creative work

**1-2:** Depleted
- Running on fumes
- Survival mode only
- Cancel non-essentials
- Rest is priority, not luxury

## Example Journal Entries

### Example 1: Simple Daily Entry

```yaml
---
title: "2025-10-19 Journal"
date: 2025-10-19
mood: good
energy: 7
gratitude: ["Morning walk with YourPet", "Progress on YourProject", "Sunny weather"]
highlights: ["Shipped authentication feature", "Great call with Designer"]
challenges: ["Struggled with focus in afternoon"]
insights: ["I need to block afternoon for admin, mornings for deep work"]
tags: [work, productivity, pet]
created: 2025-10-19
updated: 2025-10-19
---

# Journal Entry - October 19, 2025

Solid day. Shipped the authentication feature I've been wrestling with for a week - feels good to close that loop. Morning energy was great, knocked out 3 hours of focused work before lunch.

Afternoon was scattered - too many interruptions, context switching killed momentum. Need to be more protective of morning deep work blocks and just accept that afternoons are for meetings and admin.

Walk with YourPet at sunset was exactly what I needed. He found a stick that was comically oversized and refused to drop it. That dog is pure joy.

## Gratitude

1. Morning walk with YourPet
2. Progress on YourProject (finally!)
3. Sunny weather - feeling the seasonal shift
```

### Example 2: Processing Difficult Day

```yaml
---
title: "Processing a Hard Day"
date: 2025-10-20
mood: difficult
energy: 3
gratitude: ["YourPet's presence", "Friend's text checking in"]
highlights: []
challenges: ["Conflict with manager", "Anxiety spiral", "Couldn't focus at all"]
insights: ["I avoid conflict and let resentment build", "Need to address this head-on", "My body was telling me something was wrong - I ignored it"]
tags: [career, conflict, anxiety, mental-health, work]
created: 2025-10-20
updated: 2025-10-20
---

# Processing a Hard Day

Rough day. Had the conversation with my manager that I've been avoiding for weeks. It went... not great. He got defensive, I got flustered, we both walked away frustrated.

I can feel the anxiety in my chest - that tight, can't-take-a-full-breath feeling. Tried to work afterward but it was useless. Just stared at the screen for 2 hours.

What's really bothering me: I waited too long to address this. I let small annoyances build into resentment, and then when I finally said something, it came out all wrong. This is a pattern. I avoid conflict until I explode.

Strategist would tell me I need to address things tactically, in real-time, not let them fester. He's right. Sage would ask: why do I avoid conflict? What am I afraid of? Rejection? Being seen as difficult? Yeah, probably both.

I don't have to solve this tonight. But I need to:
1. Sleep on it
2. Talk to a friend tomorrow (get perspective)
3. Draft a follow-up email to manager (clear, non-emotional)
4. Maybe get Cabinet input on this

YourPet sensed something was off. He's been glued to my side all evening, resting his giant head on my lap. Dogs are the best therapists.

## Gratitude

1. YourPet's presence - he knows when I need him
2. Friend texted at exactly the right moment
3. Tomorrow is a new day
```

### Example 3: Breakthrough Insight

```yaml
---
title: "Clarity After Chaos"
date: 2025-10-21
mood: great
energy: 9
gratitude: ["Morning art session", "Breakthrough insight", "Time to think"]
highlights: ["Art practice led to career insight", "Finally understand what's been bothering me"]
challenges: []
insights: ["I've been optimizing for title/money when I actually want creative impact", "The VP role isn't wrong, but my reasons for wanting it were off", "I need work that lets me build and create, not just manage"]
tags: [career, art-practice, breakthrough, values, clarity]
created: 2025-10-21
updated: 2025-10-21
---

# Clarity After Chaos

Holy shit. I just had the clearest insight I've had in months, and it came from painting, not from thinking harder.

I was working on a still life this morning - apples and a copper pot, classic setup. Got into flow state, 2 hours disappeared. When I finished, I sat back and looked at the painting and thought: "This is what I want from my work. Making something that wasn't there before. Solving problems with my hands and brain together."

And then it hit me:

**I've been chasing the VP role because I think I *should* want it. Title. Money. Status. But what I actually want is to BUILD things. To make. To create. The VP role is mostly managing people and politics. Less building, more orchestrating.**

This doesn't mean turning down the offer is right. But it means I need to ask different questions:
- Will I still get to design and build in this role?
- Or will I be 3 layers removed from the actual work?
- Can I negotiate for a "player-coach" model?
- Or am I signing up to become the person I don't want to be?

Sage was right to flag the values question. I was so focused on "Is this good for my career?" that I forgot to ask "Is this good for ME?"

Need to convene Cabinet again. Not to reverse the decision, but to refine it. The conditions I negotiate matter more than I realized. I need to protect the "maker" part of me, not just the art practice but the building/creating in my work too.

This is why art practice matters. It's not a hobby. It's a mirror that shows me who I actually am, not who I think I should be.

## Gratitude

1. Morning art session that led to this insight
2. Flow state - that timeless feeling of making
3. Time and space to think clearly
```

---

## Tips for Consistent Practice

**Make It Easy:**
- Template with frontmatter (one click to create)
- Don't overthink it
- 5 minutes counts as much as 50 minutes

**Find Your Time:**
- Morning pages (stream of consciousness)
- Evening reflection (look back on day)
- Whenever you need to process something

**Give Yourself Permission:**
- To be messy
- To repeat yourself
- To not have insights every day
- To skip days without guilt

**Use Tags for Themes:**
- Track what you write about most
- Notice patterns over time
- "I keep writing about work stress" = signal
- Turn observations into action

**Review Regularly:**
- Read last week's entries during weekly review
- Read last month's entries during monthly review
- Read last year's entries on birthday/new year
- See how much you've grown

**Mine for Cabinet Input:**
- Bring journal insights to Cabinet meetings
- Atlas uses energy tracking for optimization
- Sage uses values questions for alignment checks
- Healer tracks stress signals

---

**See:** `databases/journal/README.md` for usage guide and integration with other systems
