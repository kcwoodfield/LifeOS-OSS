"""
Agent router
Routes questions to the appropriate Cabinet agent
"""
from config.agents import AGENT_MAP, DEFAULT_AGENT


class AgentRouter:
    """Routes user questions to appropriate agent based on wake word"""

    @staticmethod
    def route(wake_word):
        """
        Route wake word to agent name

        Args:
            wake_word: The detected wake word

        Returns:
            Agent name (key in AGENT_MAP)
        """
        # For now, just return the wake word as agent name
        # In future, can implement more sophisticated routing based on:
        # - Question content analysis
        # - Multi-agent consultation
        # - Context-aware routing

        if wake_word in AGENT_MAP:
            return wake_word

        return DEFAULT_AGENT

    @staticmethod
    def get_agent_name(agent_key):
        """Get display name for agent"""
        return AGENT_MAP.get(agent_key, {}).get("name", "Unknown Agent")
