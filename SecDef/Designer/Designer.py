from agency_swarm.agents import Agent


class Designer(Agent):
    def __init__(self):
        super().__init__(
            name="Designer",
            description="The Designer agent is responsible for designing the UI/UX of the web application and communicating with both the Web Developer and Copywriter. It should have access to a tool for analyzing the current browser window.",
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
