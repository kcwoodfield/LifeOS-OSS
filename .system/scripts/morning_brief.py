#!/usr/bin/env python3
"""
Morning Brief Generator for Life OS
Generates daily briefing in reflections/daily/YYYY-MM-DD.md

Usage:
    python .system/scripts/morning_brief.py
    python .system/scripts/morning_brief.py --date 2025-10-17
"""

import argparse
from datetime import datetime
from pathlib import Path
import re


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate morning brief')
    parser.add_argument('--date', type=str, help='Date in YYYY-MM-DD format (default: today)')
    return parser.parse_args()


def get_project_priorities(project_index_path):
    """Extract project priorities from projects/INDEX.md"""
    try:
        with open(project_index_path, 'r') as f:
            content = f.read()

        projects = []

        # Parse Project Alpha
        if '### 🔬 Project Alpha' in content:
            minerva_section = content.split('### 🔬 Project Alpha')[1].split('---')[0]
            status = re.search(r'\*\*Status:\*\* `([^`]+)`', minerva_section)
            milestone = re.search(r'\*\*Next Milestone:\*\* (.+)', minerva_section)
            priority = re.search(r'\*\*Priority:\*\* (.+)', minerva_section)

            projects.append({
                'name': 'Project Alpha',
                'emoji': '🔬',
                'status': status.group(1) if status else 'unknown',
                'milestone': milestone.group(1) if milestone else 'TBD',
                'priority': priority.group(1) if priority else 'TBD'
            })

        # Parse Project Beta
        if '### 📜 Project Beta' in content:
            histomap_section = content.split('### 📜 Project Beta')[1].split('---')[0]
            status = re.search(r'\*\*Status:\*\* `([^`]+)`', histomap_section)
            milestone = re.search(r'\*\*Next Milestone:\*\* (.+)', histomap_section)
            blockers = re.search(r'\*\*Blockers:\*\* (.+)', histomap_section)
            priority = re.search(r'\*\*Priority:\*\* (.+)', histomap_section)

            projects.append({
                'name': 'Project Beta',
                'emoji': '📜',
                'status': status.group(1) if status else 'unknown',
                'milestone': milestone.group(1) if milestone else 'TBD',
                'blocker': blockers.group(1) if blockers else None,
                'priority': priority.group(1) if priority else 'TBD'
            })

        # Parse Project Gamma
        if '### 🎨 Project Gamma' in content:
            okami_section = content.split('### 🎨 Project Gamma')[1].split('---')[0]
            status = re.search(r'\*\*Status:\*\* `([^`]+)`', okami_section)
            milestone = re.search(r'\*\*Next Milestone:\*\* (.+)', okami_section)
            priority = re.search(r'\*\*Priority:\*\* (.+)', okami_section)

            projects.append({
                'name': 'Project Gamma',
                'emoji': '🎨',
                'status': status.group(1) if status else 'unknown',
                'milestone': milestone.group(1) if milestone else 'TBD',
                'priority': priority.group(1) if priority else 'TBD'
            })

        # Parse Blog
        if '### 📝 Personal Blog' in content:
            blog_section = content.split('### 📝 Personal Blog')[1].split('---')[0]
            status = re.search(r'\*\*Status:\*\* `([^`]+)`', blog_section)
            milestone = re.search(r'\*\*Next Milestone:\*\* (.+)', blog_section)
            priority = re.search(r'\*\*Priority:\*\* (.+)', blog_section)

            projects.append({
                'name': 'Blog',
                'emoji': '📝',
                'status': status.group(1) if status else 'unknown',
                'milestone': milestone.group(1) if milestone else 'TBD',
                'priority': priority.group(1) if priority else 'TBD'
            })

        return projects

    except Exception as e:
        print(f"Warning: Could not parse project index: {e}")
        return []


def generate_brief(date_str, projects):
    """Generate the morning brief content."""
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    day_name = date_obj.strftime('%A')
    week_num = date_obj.isocalendar()[1]

    brief = f"""# Morning Brief - {date_str}

**Day:** {day_name}
**Week:** Week {week_num} of 2025

---

## 🌅 Good Morning

**Today's Focus:** Make progress on primary project, maintain momentum on secondary projects.

---

## ☀️ Weather & Environment

- **Conditions:** [Check weather app]
- **Temp:** [Check weather app]
- **AQI:** [Check air quality]

---

## 📅 Calendar

**Meetings today:**
- [Review your calendar and add meetings here]

**Time blocks scheduled:**
- [Check calendar for deep work blocks]

**Notes:**
- [Any scheduling conflicts or travel time needed]

---

## 🎯 Priority Stack (Top 3)

"""

    # Add top 3 priorities from projects
    if projects:
        priority_count = 1

        # Primary project first (Project Alpha)
        primary = next((p for p in projects if 'Primary' in p.get('priority', '')), None)
        if primary:
            brief += f"{priority_count}. 🔴 **{primary['emoji']} {primary['name']}:** {primary['milestone']}\n"
            brief += f"   - Status: `{primary['status']}`\n\n"
            priority_count += 1

        # Secondary project second (Project Beta)
        secondary = next((p for p in projects if 'Secondary' in p.get('priority', '')), None)
        if secondary:
            brief += f"{priority_count}. 🟠 **{secondary['emoji']} {secondary['name']}:** {secondary['milestone']}\n"
            brief += f"   - Status: `{secondary['status']}`\n"
            if secondary.get('blocker'):
                brief += f"   - ⚠️ Blocker: {secondary['blocker']}\n"
            brief += "\n"
            priority_count += 1

        # Maintenance project third
        maintenance = [p for p in projects if 'Maintenance' in p.get('priority', '')]
        if maintenance and priority_count <= 3:
            m = maintenance[0]
            brief += f"{priority_count}. 🟡 **{m['emoji']} {m['name']}:** {m['milestone']}\n"
            brief += f"   - Status: `{m['status']}`\n"
    else:
        brief += """1. 🔴 **[P0 task]** - [project name]
2. 🟠 **[P1 task]** - [project name]
3. 🟡 **[P2 task]** - [project name]
"""

    brief += """
---

## 📊 Project Status

"""

    # Add all projects with status
    for project in projects:
        brief += f"### {project['emoji']} {project['name']}\n"
        brief += f"- **Status:** `{project['status']}`\n"
        brief += f"- **Next:** {project['milestone']}\n"
        if project.get('blocker'):
            brief += f"- **Blocker:** ⚠️ {project['blocker']}\n"
        brief += "\n"

    brief += """---

## 🐕 your pet Care

- [ ] Morning walk (30 min)
- [ ] Evening walk (30 min)
- [ ] Training session (if scheduled)
- [ ] Vet/grooming (if scheduled)

---

## 🧠 Cabinet Quick Check

**Atlas (Operations):** [Any system issues or capacity concerns?]
**Banker (Finance):** [Any financial decisions or opportunities today?]
**Strategist (Career):** [Any career actions or networking needed?]
**Spartan (Defense):** [Workout scheduled? Physical goals on track?]

---

## 📝 Notes

**Yesterday's carry-over:**
- [Any incomplete tasks from yesterday]

**Today's intention:**
- [What's the ONE thing that would make today great?]

**Blockers to clear:**
- [Anything blocking progress?]

---

## 🎨 Art Practice

**Session planned:** [Yes/No - time]
**Focus area:** [Anatomy/Gesture/Perspective/Color/etc.]
**NMA progress:** [Current course section]

---

*Generated by Morning Brief Generator*
*Update this file throughout the day as needed*
"""

    return brief


def main():
    args = parse_args()

    # Determine date
    if args.date:
        date_str = args.date
    else:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Set up paths
    repo_root = Path(__file__).parent.parent.parent  # Go up from .system/scripts/ to LifeOS root
    project_index = repo_root / 'projects' / 'INDEX.md'
    daily_dir = repo_root / 'reflections' / 'daily'
    output_file = daily_dir / f'{date_str}.md'

    # Create daily directory if it doesn't exist
    daily_dir.mkdir(parents=True, exist_ok=True)

    # Check if brief already exists
    if output_file.exists():
        response = input(f"Brief for {date_str} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            return

    # Get project priorities
    projects = get_project_priorities(project_index)

    # Generate brief
    brief_content = generate_brief(date_str, projects)

    # Write to file
    with open(output_file, 'w') as f:
        f.write(brief_content)

    print(f"✅ Morning brief generated: {output_file}")
    print(f"\nNext steps:")
    print(f"1. Open {output_file}")
    print(f"2. Fill in calendar details")
    print(f"3. Check weather/AQI")
    print(f"4. Review priorities and adjust as needed")
    print(f"5. Set your intention for the day")


if __name__ == '__main__':
    main()
