"""
Claude API client
Handles communication with Anthropic's Claude API
"""
from anthropic import Anthropic
from config.settings import ANTHROPIC_API_KEY, CLAUDE_MODEL, CLAUDE_MAX_TOKENS
from config.agents import AGENT_MAP
from utils import print_status
from .loader import AgentLoader


class ClaudeClient:
    """Manages Claude API interactions"""

    def __init__(self):
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)

    def ask_agent(self, agent_name, question, conversation_history):
        """
        Send question to Claude with agent persona and conversation history

        Args:
            agent_name: Name of the agent to consult
            question: User's question
            conversation_history: ConversationHistory object

        Returns:
            Agent's response text, or None if error
        """
        print_status(f"Asking {AGENT_MAP[agent_name]['name']}...", "🤔")

        # Build system message with agent persona and context
        system_message = AgentLoader.build_system_message(agent_name)

        # Build conversation messages with history
        messages = conversation_history.get_messages() + [{
            "role": "user",
            "content": question
        }]

        try:
            # Call Claude API
            response = self.client.messages.create(
                model=CLAUDE_MODEL,
                max_tokens=CLAUDE_MAX_TOKENS,
                system=system_message,
                messages=messages
            )

            answer = response.content[0].text
            print_status(f"{AGENT_MAP[agent_name]['name']} responds:", "🗣️")
            print(f"\n{answer}\n")

            return answer

        except Exception as e:
            print_status(f"Agent error: {e}", "❌")
            return None
