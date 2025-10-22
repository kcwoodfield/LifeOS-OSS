#!/bin/bash

# Claude Code Task Completion Notification
# Triggers macOS notification with Claude icon and sound
#
# Usage:
#   ./claude_task_complete.sh "Task description"
#
# For Claude Code hooks configuration, see README.md

TASK_DESCRIPTION="${1:-Claude Code task completed}"

# Get the directory where this script lives
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_ICON="$SCRIPT_DIR/../../assets/claude.png"  # Go up from .system/scripts/ to LifeOS root, then to assets/

# Sound options: Glass, Submarine, Tink
SOUND="Submarine"

# Show macOS notification with Claude icon
terminal-notifier \
    -title "Claude Code" \
    -message "$TASK_DESCRIPTION" \
    -sound "$SOUND" \
    -contentImage "$CLAUDE_ICON"
