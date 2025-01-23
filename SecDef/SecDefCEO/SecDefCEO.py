from agency_swarm.agents import Agent


class SecDefCEO(Agent):
    def __init__(self):
        super().__init__(
            name="SecDefCEO",
            description="Acts as the overseer and communicator across the agency, ensuring alignment with the agency's goals.",
            instructions="./instructions.md",
            # files_folder="./files",
            # schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools",
            temperature=0.3,
            max_prompt_tokens=25000,
        )

    def response_validator(self, message):
        return message
