import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
    async for message in query(
        prompt="Write unit tests for utils.py, run them, and fix any failures",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob", "WebSearch", "bash"],
            permission_mode="acceptEdits",
            model="claude-haiku-4-5-20251001",
            system_prompt="You are a senior Python developer. Always follow PEP 8 style guidelines.",
        ),
    ):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if hasattr(block, "text"):
                    print(block.text)  # Claude's reasoning
                elif hasattr(block, "name"):
                    print(f"Tool: {block.name}")  # Tool being called
        elif isinstance(message, ResultMessage):
            print(f"Done: {message.subtype}") 

asyncio.run(main())
