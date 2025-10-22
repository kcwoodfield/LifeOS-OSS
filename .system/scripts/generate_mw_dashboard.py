#!/usr/bin/env python3
"""
Modern Warfare Dashboard Generator

Reads LifeOS data from markdown files and generates a dynamic
Call of Duty Modern Warfare themed HTML dashboard.

Usage:
    python .system/scripts/generate_mw_dashboard.py

Output:
    dashboards/modern-warfare-live.html
"""

import os
import re
from pathlib import Path
from datetime import datetime
import yaml
import requests

# ============================================================================
# Configuration
# ============================================================================

VAULT_ROOT = Path(__file__).parent.parent.parent
DASHBOARDS_DIR = VAULT_ROOT / "dashboards"
OUTPUT_FILE = DASHBOARDS_DIR / "modern-warfare-live.html"

# Data sources
QUEUE_FILE = VAULT_ROOT / ".system/context/queue.md"
TASKS_DIR = VAULT_ROOT / "databases/tasks"
CONTEXT_DIR = VAULT_ROOT / ".system/context"

# Weather API (optional - using wttr.in)
WEATHER_LOCATION = "YourCity"  # Change to your city (e.g., "Austin,TX", "London,UK")


# ============================================================================
# Data Parsing Functions
# ============================================================================

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}


def get_current_mission():
    """Read current mission from queue.md."""
    try:
        with open(QUEUE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for top priority heading
        match = re.search(r'## 🎯 Top Priority: (.+)', content)
        if match:
            return match.group(1).strip()

        # Fallback to first h2
        match = re.search(r'## (.+)', content)
        if match:
            return match.group(1).strip()

        return "NO ACTIVE MISSION"
    except Exception as e:
        print(f"Error reading queue: {e}")
        return "ERROR LOADING MISSION"


def get_mission_status():
    """Parse mission status from queue.md."""
    try:
        with open(QUEUE_FILE, 'r', encoding='utf-8') as f:
            content = f.read()

        # Look for status line
        if re.search(r'\*\*Status:\*\* Active', content):
            return "ACTIVE"
        elif re.search(r'\*\*Status:\*\* Paused', content):
            return "PAUSED"
        else:
            return "ACTIVE"
    except:
        return "UNKNOWN"


def get_top_tasks(limit=3):
    """Get top priority tasks from databases/tasks/."""
    tasks = []

    try:
        task_files = sorted(TASKS_DIR.glob("*.md"), key=os.path.getmtime, reverse=True)

        for task_file in task_files:
            if task_file.name == "_schema.md":
                continue

            with open(task_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter = parse_frontmatter(content)

            # Skip completed tasks
            if frontmatter.get('status') in ['done', 'completed', 'cancelled']:
                continue

            # Extract title and metadata
            title = frontmatter.get('title', task_file.stem)
            priority = frontmatter.get('priority', 'medium')
            status = frontmatter.get('status', 'todo')
            effort = frontmatter.get('effort', 'M')
            due_date = frontmatter.get('due_date', 'TBD')

            # Convert effort to hours estimate
            effort_hours = {'S': '1H', 'M': '2H', 'L': '4H', 'XL': '8H'}.get(effort, '2H')

            # Format due date
            if due_date and due_date != 'TBD':
                try:
                    due_obj = datetime.strptime(str(due_date), '%Y-%m-%d')
                    today = datetime.now()
                    if due_obj.date() == today.date():
                        due_str = "TODAY"
                    elif due_obj.date() < today.date():
                        due_str = "OVERDUE"
                    else:
                        due_str = due_obj.strftime('%b %d')
                except:
                    due_str = str(due_date)
            else:
                due_str = "TBD"

            tasks.append({
                'title': title.upper(),
                'priority': priority,
                'status': status.upper(),
                'effort': effort_hours,
                'due': due_str
            })

            if len(tasks) >= limit:
                break

    except Exception as e:
        print(f"Error reading tasks: {e}")
        tasks = [
            {'title': 'ERROR LOADING TASKS', 'priority': 'high', 'status': 'PENDING', 'effort': '0H', 'due': 'N/A'}
        ]

    # Pad with placeholders if not enough tasks
    while len(tasks) < limit:
        tasks.append({
            'title': 'NO ACTIVE OBJECTIVE',
            'priority': 'low',
            'status': 'PENDING',
            'effort': '0H',
            'due': 'N/A'
        })

    return tasks


def get_weather():
    """Fetch weather from wttr.in (no API key needed)."""
    try:
        # Use wttr.in simple format
        url = f"https://wttr.in/{WEATHER_LOCATION}?format=%l:+%t+%C"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            weather_str = response.text.strip()
            # Parse "City: +72°F Clear"
            match = re.search(r':\s*([+-]?\d+)°F\s+(.+)', weather_str)
            if match:
                temp = match.group(1) + "°F"
                condition = match.group(2).upper()
                return f"{WEATHER_LOCATION.upper()} // {temp} // {condition}"

        return f"{WEATHER_LOCATION.upper()} // WEATHER UNAVAILABLE"
    except:
        return f"{WEATHER_LOCATION.upper()} // OFFLINE"


def get_operator_energy():
    """Read energy level from latest journal or context."""
    # For now, return a default - could read from journal entries
    return "7/10"


def count_active_tasks():
    """Count tasks by status."""
    active = 0
    completed_today = 0

    try:
        today = datetime.now().date()

        for task_file in TASKS_DIR.glob("*.md"):
            if task_file.name == "_schema.md":
                continue

            with open(task_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter = parse_frontmatter(content)
            status = frontmatter.get('status', 'todo')

            if status in ['in_progress', 'todo']:
                active += 1
            elif status in ['done', 'completed']:
                # Check if completed today
                updated = frontmatter.get('updated')
                if updated:
                    try:
                        updated_date = datetime.strptime(str(updated), '%Y-%m-%d').date()
                        if updated_date == today:
                            completed_today += 1
                    except:
                        pass
    except Exception as e:
        print(f"Error counting tasks: {e}")

    return active, completed_today


# ============================================================================
# HTML Template Generation
# ============================================================================

def generate_html(data):
    """Generate the full HTML dashboard with dynamic data."""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LifeOS // MODERN WARFARE COMMAND [LIVE]</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Orbitron:wght@700;900&display=swap');

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Rajdhani', sans-serif;
            background: #0a0f1a;
            color: #e0e6f0;
            font-size: 14px;
            line-height: 1.5;
            height: 100vh;
            overflow: hidden;
            position: relative;
        }}

        /* Hexagon grid background */
        body::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image:
                repeating-linear-gradient(0deg, rgba(0, 173, 239, 0.03) 0px, transparent 2px, transparent 4px, rgba(0, 173, 239, 0.03) 6px),
                repeating-linear-gradient(90deg, rgba(0, 173, 239, 0.03) 0px, transparent 2px, transparent 4px, rgba(0, 173, 239, 0.03) 6px);
            background-size: 30px 30px;
            pointer-events: none;
            z-index: 0;
        }}

        /* Scan line effect */
        body::after {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                to bottom,
                rgba(0, 173, 239, 0) 0%,
                rgba(0, 173, 239, 0.05) 50%,
                rgba(0, 173, 239, 0) 100%
            );
            animation: scan 8s linear infinite;
            pointer-events: none;
            z-index: 5;
        }}

        @keyframes scan {{
            0% {{ transform: translateY(-100%); }}
            100% {{ transform: translateY(100%); }}
        }}

        .hud-container {{
            display: grid;
            grid-template-columns: 480px 1fr 480px;
            grid-template-rows: 280px 1fr 340px;
            height: 100vh;
            padding: 25px;
            gap: 25px;
            position: relative;
            z-index: 1;
        }}

        .hud-panel {{
            background: linear-gradient(135deg, rgba(10, 15, 26, 0.92), rgba(15, 25, 40, 0.88));
            border: 2px solid rgba(0, 173, 239, 0.5);
            padding: 22px;
            position: relative;
            box-shadow:
                0 0 30px rgba(0, 173, 239, 0.15),
                inset 0 0 30px rgba(0, 173, 239, 0.05);
            backdrop-filter: blur(8px);
            clip-path: polygon(
                0 0,
                calc(100% - 15px) 0,
                100% 15px,
                100% 100%,
                15px 100%,
                0 calc(100% - 15px)
            );
        }}

        .hud-panel::before,
        .hud-panel::after {{
            content: '';
            position: absolute;
            width: 20px;
            height: 20px;
            border: 2px solid #00adef;
        }}

        .hud-panel::before {{
            top: 8px;
            left: 8px;
            border-right: none;
            border-bottom: none;
        }}

        .hud-panel::after {{
            bottom: 8px;
            right: 8px;
            border-left: none;
            border-top: none;
        }}

        .hud-panel {{
            border-image: linear-gradient(135deg, #00adef, #0066ff) 1;
        }}

        .panel-header {{
            text-transform: uppercase;
            letter-spacing: 4px;
            margin-bottom: 18px;
            padding-bottom: 12px;
            font-weight: 700;
            font-size: 13px;
            color: #00adef;
            position: relative;
            font-family: 'Orbitron', sans-serif;
            border-bottom: 2px solid rgba(0, 173, 239, 0.4);
        }}

        .panel-header::before {{
            content: '//';
            color: #ffd700;
            margin-right: 10px;
            font-weight: 900;
        }}

        .panel-header::after {{
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 60px;
            height: 2px;
            background: linear-gradient(90deg, #00adef, transparent);
        }}

        .panel-content {{
            font-size: 14px;
            font-weight: 500;
        }}

        .status-active {{
            color: #00ff88;
            text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
        }}
        .status-warning {{
            color: #ffd700;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }}
        .status-critical {{
            color: #ff3333;
            text-shadow: 0 0 10px rgba(255, 51, 51, 0.5);
        }}
        .status-inactive {{ color: #5a6a7a; }}

        .progress-container {{
            margin: 15px 0;
            position: relative;
        }}

        .progress-bar {{
            display: flex;
            gap: 3px;
            margin: 10px 0;
            height: 12px;
        }}

        .progress-segment {{
            flex: 1;
            background: rgba(0, 173, 239, 0.15);
            border: 1px solid rgba(0, 173, 239, 0.4);
            position: relative;
            clip-path: polygon(5% 0, 100% 0, 95% 100%, 0 100%);
        }}

        .progress-segment.filled {{
            background: linear-gradient(90deg, #00adef, #0066ff);
            box-shadow: 0 0 15px rgba(0, 173, 239, 0.6);
            border-color: #00adef;
        }}

        .metric-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 8px 0;
            padding: 8px 0;
            border-bottom: 1px solid rgba(0, 173, 239, 0.1);
            font-size: 13px;
        }}

        .metric-row:last-child {{
            border-bottom: none;
        }}

        .metric-label {{
            color: #7a8a9a;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-size: 11px;
        }}

        .metric-value {{
            color: #e0e6f0;
            font-weight: 600;
            font-size: 14px;
        }}

        .objective-item {{
            margin: 15px 0;
            padding: 14px;
            background: linear-gradient(90deg, rgba(0, 173, 239, 0.1), rgba(0, 102, 255, 0.05));
            border-left: 4px solid #00adef;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            clip-path: polygon(0 0, calc(100% - 10px) 0, 100% 10px, 100% 100%, 0 100%);
        }}

        .objective-item:hover {{
            background: linear-gradient(90deg, rgba(0, 173, 239, 0.2), rgba(0, 102, 255, 0.1));
            border-left-color: #ffd700;
            transform: translateX(5px);
            box-shadow: 0 0 20px rgba(0, 173, 239, 0.3);
        }}

        .objective-number {{
            color: #ffd700;
            font-weight: 700;
            font-size: 16px;
            margin-right: 8px;
            font-family: 'Orbitron', sans-serif;
        }}

        .objective-meta {{
            font-size: 11px;
            color: #7a8a9a;
            margin-top: 8px;
            padding-left: 25px;
            letter-spacing: 1px;
        }}

        .agent-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid rgba(0, 173, 239, 0.15);
            font-size: 13px;
            transition: all 0.2s;
        }}

        .agent-row:hover {{
            background: rgba(0, 173, 239, 0.05);
            padding-left: 5px;
        }}

        .agent-row:last-child {{
            border-bottom: none;
        }}

        .agent-name {{
            font-weight: 600;
            letter-spacing: 1px;
        }}

        .agent-status {{
            color: #00ff88;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 1px;
        }}

        .agent-role {{
            font-size: 10px;
            color: #5a6a7a;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .quick-action {{
            padding: 12px 16px;
            margin: 8px 0;
            background: linear-gradient(135deg, rgba(0, 173, 239, 0.15), rgba(0, 102, 255, 0.1));
            border: 2px solid rgba(0, 173, 239, 0.4);
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 2px;
            font-size: 12px;
            position: relative;
            clip-path: polygon(5px 0, 100% 0, 100% calc(100% - 5px), calc(100% - 5px) 100%, 0 100%, 0 5px);
        }}

        .quick-action::before {{
            content: '>';
            color: #ffd700;
            margin-right: 10px;
            font-weight: 900;
        }}

        .quick-action:hover {{
            background: linear-gradient(135deg, rgba(0, 173, 239, 0.3), rgba(0, 102, 255, 0.2));
            border-color: #00adef;
            box-shadow: 0 0 20px rgba(0, 173, 239, 0.4);
            transform: translateY(-2px);
        }}

        .divider {{
            margin: 18px 0;
            height: 2px;
            background: linear-gradient(
                90deg,
                rgba(0, 173, 239, 0),
                rgba(0, 173, 239, 0.6),
                rgba(0, 173, 239, 0)
            );
            position: relative;
        }}

        .divider::after {{
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 8px;
            height: 8px;
            background: #00adef;
            clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        }}

        .top-left {{ grid-column: 1; grid-row: 1; }}
        .top-right {{ grid-column: 3; grid-row: 1; }}
        .bottom-left {{ grid-column: 1; grid-row: 3; }}
        .bottom-right {{ grid-column: 3; grid-row: 3; }}

        .center {{
            grid-column: 2;
            grid-row: 2;
            background: none;
            border: none;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            text-transform: uppercase;
            letter-spacing: 8px;
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            color: rgba(0, 173, 239, 0.15);
            text-shadow: 0 0 30px rgba(0, 173, 239, 0.3);
        }}

        .center-subtitle {{
            font-size: 14px;
            letter-spacing: 4px;
            margin-top: 10px;
            color: rgba(0, 173, 239, 0.2);
            font-weight: 600;
        }}

        .callsign {{
            color: #ffd700;
            font-weight: 700;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }}

        .time-display {{
            font-size: 28px;
            font-weight: 700;
            letter-spacing: 3px;
            font-family: 'Orbitron', sans-serif;
            color: #00adef;
            text-shadow: 0 0 15px rgba(0, 173, 239, 0.5);
            margin-bottom: 10px;
        }}

        .date-display {{
            font-size: 14px;
            letter-spacing: 2px;
            color: #7a8a9a;
            margin-bottom: 5px;
        }}

        @keyframes pulse-active {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.7; }}
        }}

        .status-active {{
            animation: pulse-active 2s infinite;
        }}

        .energy-bar {{
            display: flex;
            gap: 2px;
            margin: 10px 0;
        }}

        .energy-block {{
            width: 8px;
            height: 20px;
            background: rgba(0, 173, 239, 0.2);
            border: 1px solid rgba(0, 173, 239, 0.4);
            clip-path: polygon(0 20%, 100% 0, 100% 80%, 0 100%);
        }}

        .energy-block.filled {{
            background: linear-gradient(180deg, #00ff88, #00adef);
            box-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            border-color: #00ff88;
        }}

        .generated-timestamp {{
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 10px;
            color: #5a6a7a;
            z-index: 1000;
        }}
    </style>
</head>
<body>
    <div class="hud-container">
        <!-- TOP-LEFT: Mission Command -->
        <div class="hud-panel top-left">
            <div class="panel-header">Mission Command</div>
            <div class="panel-content">
                <div class="metric-row">
                    <span class="metric-label">Operation:</span>
                    <span class="metric-value" style="color: #ffd700;">{data['mission']}</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Status:</span>
                    <span class="status-active">{data['mission_status']}</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Timeline:</span>
                    <span class="metric-value">DAY 1 / WEEK 1 OF 8</span>
                </div>

                <div class="progress-container">
                    <div class="progress-bar">
                        <div class="progress-segment filled"></div>
                        <div class="progress-segment filled"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                        <div class="progress-segment"></div>
                    </div>
                    <div style="font-size: 11px; color: #7a8a9a; text-align: right;">PROGRESS: 20% COMPLETE</div>
                </div>

                <div class="divider"></div>

                <div class="metric-row">
                    <span class="metric-label">Callsign:</span>
                    <span class="callsign">OPERATOR</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Energy Level:</span>
                    <span class="status-active">{data['energy']} HIGH</span>
                </div>
                <div class="energy-bar">
                    {''.join([f'<div class="energy-block {("filled" if i < 7 else "")}"></div>' for i in range(10)])}
                </div>
                <div class="metric-row">
                    <span class="metric-label">Focus State:</span>
                    <span class="status-active">OPTIMAL</span>
                </div>
            </div>
        </div>

        <!-- TOP-RIGHT: System Status -->
        <div class="hud-panel top-right">
            <div class="panel-header">System Status</div>
            <div class="panel-content">
                <div class="time-display" id="time-display">
                    <span id="current-time">{data['time']}</span>
                </div>
                <div class="date-display">
                    {data['date']} // {data['day_of_week']}
                </div>
                <div style="margin-top: 5px; font-size: 13px; color: #7a8a9a;">
                    {data['weather']}
                </div>

                <div class="divider"></div>

                <div class="metric-row">
                    <span class="metric-label">System Health:</span>
                    <span class="status-active">95% OPERATIONAL</span>
                </div>
                <div class="progress-bar">
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment filled"></div>
                    <div class="progress-segment"></div>
                </div>

                <div class="metric-row" style="margin-top: 15px;">
                    <span class="metric-label">Network:</span>
                    <span class="status-active">ONLINE</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Vault Sync:</span>
                    <span class="status-active">SYNCHRONIZED</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Agents:</span>
                    <span class="status-active">14/14 READY</span>
                </div>
            </div>
        </div>

        <!-- BOTTOM-LEFT: Priority Objectives -->
        <div class="hud-panel bottom-left">
            <div class="panel-header">Priority Objectives</div>
            <div class="panel-content">
"""

    # Add tasks dynamically
    for i, task in enumerate(data['tasks'], 1):
        html += f"""
                <div class="objective-item">
                    <div><span class="objective-number">[{i}]</span> {task['title']}</div>
                    <div class="objective-meta">DUE: {task['due']} // EFFORT: {task['effort']} // STATUS: {task['status']}</div>
                </div>
"""

    html += f"""
                <div class="divider"></div>

                <div class="metric-row">
                    <span class="metric-label">Active Operations:</span>
                    <span class="metric-value">{data['active_tasks']}/8</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Completed Today:</span>
                    <span class="metric-value">{data['completed_today']}</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Blockers:</span>
                    <span class="status-active">NONE</span>
                </div>
            </div>
        </div>

        <!-- BOTTOM-RIGHT: Cabinet Agents & Quick Actions -->
        <div class="hud-panel bottom-right">
            <div class="panel-header">Cabinet Agents</div>
            <div class="panel-content">
                <div class="agent-row">
                    <span class="agent-name">ATLAS</span>
                    <span class="agent-status">[ONLINE]</span>
                    <span class="agent-role">COO</span>
                </div>
                <div class="agent-row">
                    <span class="agent-name">BANKER</span>
                    <span class="agent-status">[ONLINE]</span>
                    <span class="agent-role">CFO</span>
                </div>
                <div class="agent-row">
                    <span class="agent-name">STRATEGIST</span>
                    <span class="agent-status">[ONLINE]</span>
                    <span class="agent-role">CSO</span>
                </div>
                <div class="agent-row">
                    <span class="agent-name">SAGE</span>
                    <span class="agent-status">[ONLINE]</span>
                    <span class="agent-role">ORACLE</span>
                </div>
                <div class="agent-row">
                    <span class="agent-name">SPARTAN</span>
                    <span class="agent-status">[ONLINE]</span>
                    <span class="agent-role">DEFENSE</span>
                </div>

                <div class="divider"></div>

                <div style="font-size: 11px; margin-bottom: 10px; color: #7a8a9a; text-transform: uppercase; letter-spacing: 1px;">Quick Actions:</div>
                <div class="quick-action">Convene Cabinet</div>
                <div class="quick-action">New Task</div>
                <div class="quick-action">View Projects</div>
            </div>
        </div>

        <!-- CENTER: Command Logo -->
        <div class="center">
            LIFEOS
            <div class="center-subtitle">// MODERN WARFARE COMMAND</div>
        </div>
    </div>

    <div class="generated-timestamp">
        GENERATED: {data['generated']} // AUTO-REFRESH: 60s
    </div>

    <script>
        // Update time every second
        function updateTime() {{
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            document.getElementById('current-time').textContent = `${{hours}}:${{minutes}}`;
        }}

        updateTime();
        setInterval(updateTime, 1000);

        // Auto-refresh page every 60 seconds to get latest data
        setTimeout(() => {{
            location.reload();
        }}, 60000);

        // Interactive elements
        document.querySelectorAll('.objective-item').forEach(item => {{
            item.addEventListener('click', function() {{
                console.log('Objective selected:', this.textContent);
            }});
        }});

        document.querySelectorAll('.quick-action').forEach(action => {{
            action.addEventListener('click', function() {{
                console.log('Action executed:', this.textContent);
            }});
        }});

        document.querySelectorAll('.agent-row').forEach(agent => {{
            agent.addEventListener('click', function() {{
                console.log('Agent contacted:', this.textContent);
            }});
        }});
    </script>
</body>
</html>
"""

    return html


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """Main execution function."""
    print("🎮 Modern Warfare Dashboard Generator")
    print("=" * 60)

    # Gather all data
    print("📊 Gathering LifeOS data...")

    now = datetime.now()

    data = {
        'mission': get_current_mission(),
        'mission_status': get_mission_status(),
        'tasks': get_top_tasks(3),
        'weather': get_weather(),
        'energy': get_operator_energy(),
        'date': now.strftime('%Y.%m.%d'),
        'day_of_week': now.strftime('%A').upper(),
        'time': now.strftime('%H:%M'),
        'generated': now.strftime('%Y-%m-%d %H:%M:%S'),
    }

    # Count tasks
    active, completed = count_active_tasks()
    data['active_tasks'] = active
    data['completed_today'] = completed

    print(f"  ✓ Mission: {data['mission']}")
    print(f"  ✓ Status: {data['mission_status']}")
    print(f"  ✓ Tasks loaded: {len(data['tasks'])}")
    print(f"  ✓ Active operations: {active}")
    print(f"  ✓ Completed today: {completed}")
    print(f"  ✓ Weather: {data['weather']}")

    # Generate HTML
    print("\n🔨 Generating HTML dashboard...")
    html_content = generate_html(data)

    # Write to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"  ✓ Dashboard written to: {OUTPUT_FILE}")
    print(f"\n✅ Dashboard generated successfully!")
    print(f"\n📂 Open in browser: file://{OUTPUT_FILE.absolute()}")
    print(f"📂 Or in Obsidian: dashboards/modern-warfare-live.html")
    print("\n💡 Tip: Run this script every time you want to refresh the dashboard")
    print("    or set up a cron job to auto-generate every 5 minutes.")


if __name__ == "__main__":
    main()
