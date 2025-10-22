"""
Agent configuration and wake word mapping
Defines all Cabinet agents and their properties
"""

# Agent wake word mapping
AGENT_MAP = {
    "atlas": {
        "file": "atlas-operations.md",
        "name": "Atlas",
        "wake_words": ["atlas", "hey atlas"],
        "voice_id": "63sBmV7S2RAUbcLcDUeW",  # Tyrion Lannister voice clone
    },
    "banker": {
        "file": "banker.md",
        "name": "Banker",
        "wake_words": ["banker", "hey banker", "gordon"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Banker voice
    },
    "strategist": {
        "file": "strategist.md",
        "name": "Strategist",
        "wake_words": ["strategist", "hey strategist", "miyagi"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Strategist voice
    },
    "sage": {
        "file": "sage.md",
        "name": "Sage",
        "wake_words": ["sage", "hey sage", "morpheus"],
        "voice_id": "0zUZ5qUGb8wympsfJH8d",  # Katherine voice (ElevenLabs)
    },
    "commander": {
        "file": "commander.md",
        "name": "Commander",
        "wake_words": ["commander", "hey commander"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Commander voice
    },
    "engineer": {
        "file": "engineer.md",
        "name": "Engineer",
        "wake_words": ["engineer", "hey engineer", "cipher"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Engineer voice
    },
    "designer": {
        "file": "designer.md",
        "name": "Designer",
        "wake_words": ["designer", "hey designer", "elena"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Designer voice
    },
    "artist": {
        "file": "artist.md",
        "name": "Artist",
        "wake_words": ["artist", "hey artist", "maestro"],
        "voice_id": "21m00Tcm4TlvDq8ikWAM",  # TODO: Clone Artist voice
    },
}

# Default agent if none specified
DEFAULT_AGENT = "atlas"
