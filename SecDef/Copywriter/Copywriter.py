from agency_swarm.agents import Agent


class Copywriter(Agent):
    def __init__(self):
        super().__init__(
            name="Copywriter",
            description="The Copywriter agent is responsible for creating and editing content for the web application. It communicates with the Designer to ensure content aligns with the design but does not require any specific tools.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
