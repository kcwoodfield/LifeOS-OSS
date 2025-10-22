"""
Conversation history management
Maintains context across multiple interactions in a session
"""
from config.settings import CONVERSATION_HISTORY_LIMIT


class ConversationHistory:
    """Manages conversation history for context continuity"""

    def __init__(self):
        self.messages = []

    def add_exchange(self, user_message, assistant_message):
        """Add a question/answer pair to history"""
        self.messages.append({"role": "user", "content": user_message})
        self.messages.append({"role": "assistant", "content": assistant_message})

        # Keep history reasonable (last N messages)
        if len(self.messages) > CONVERSATION_HISTORY_LIMIT:
            self.messages = self.messages[-CONVERSATION_HISTORY_LIMIT:]

    def get_messages(self):
        """Get current conversation history"""
        return self.messages

    def clear(self):
        """Clear conversation history"""
        self.messages = []

    def __len__(self):
        """Get number of messages in history"""
        return len(self.messages)
