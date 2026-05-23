import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

async def main():
    async for message in query(
        prompt="Create a README.md documenting the functions in utils.py",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Edit", "Glob", "WebSearch"],
            permission_mode="acceptEdits",
            model="haiku",
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
