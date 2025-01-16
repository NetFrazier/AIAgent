from agency_swarm.agents import Agent


class WebDeveloper(Agent):
    def __init__(self):
        super().__init__(
            name="WebDeveloper",
            description="The WebDeveloper agent is responsible for developing the web application using Next.js and MUI. It can navigate directories, read, write, and modify files, and execute terminal commands. It communicates with the Designer for design-related tasks.",
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
