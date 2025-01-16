from agency_swarm.agents import Agent


class SecDefCEO(Agent):
    def __init__(self):
        super().__init__(
            name="SecDefCEO",
            description="The SecDefCEO agent is responsible for overseeing the project and coordinating communication between the Designer and other roles. It will serve as the main point of contact for the user.",
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
