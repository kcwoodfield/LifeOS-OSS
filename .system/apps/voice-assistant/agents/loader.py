"""
Agent prompt loader
Loads agent system prompts and context from markdown files
"""
from config.settings import AGENTS_DIR, CONTEXT_DIR
from config.agents import AGENT_MAP
from utils import print_status


class AgentLoader:
    """Loads agent prompts and LifeOS context"""

    @staticmethod
    def load_agent_prompt(agent_name):
        """Load agent system prompt from markdown file"""
        agent_file = AGENTS_DIR / AGENT_MAP[agent_name]["file"]

        if not agent_file.exists():
            print_status(f"Warning: Agent file not found: {agent_file}", "⚠️")
            return f"You are {AGENT_MAP[agent_name]['name']}, a helpful AI assistant."

        with open(agent_file, 'r') as f:
            content = f.read()
            # Extract content after frontmatter (if any)
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    content = parts[2].strip()
            return content

    @staticmethod
    def load_context():
        """Load relevant LifeOS context for agent"""
        context = {}

        for context_file in ["career.md", "wealth.md", "preferences.md"]:
            file_path = CONTEXT_DIR / context_file
            if file_path.exists():
                with open(file_path, 'r') as f:
                    context[context_file.replace('.md', '')] = f.read()

        return context

    @staticmethod
    def build_system_message(agent_name):
        """Build complete system message for Claude API"""
        agent_prompt = AgentLoader.load_agent_prompt(agent_name)
        context = AgentLoader.load_context()

        # Build context string
        context_str = "\n\n".join([f"# {k.upper()}\n{v}" for k, v in context.items()])

        return f"""{agent_prompt}

You have access to User's context:

{context_str}

Use this context to provide personalized, specific advice.

IMPORTANT: You are speaking via text-to-speech. Do not use markdown formatting (no asterisks, no bold, no headers). Speak naturally in plain text only. Use your wit and personality through word choice, not formatting."""
