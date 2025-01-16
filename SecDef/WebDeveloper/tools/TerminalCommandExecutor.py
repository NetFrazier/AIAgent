from agency_swarm.tools import BaseTool
from pydantic import Field
import subprocess
from typing import Literal

class RunCommand(BaseTool):
    """
    A tool to execute terminal commands. It supports running shell commands,
    capturing the output, and handling any errors that occur during execution.
    """

    command: Literal ['build', 'create-next-app'] = Field(
        default = 'build', 
        title = 'Command',
        description="The terminal command to execute. Create a new Next.js app with 'creat-new-app' or build the current app with 'build'"
    )

    def run(self):
        """
        Executes the specified shell command and returns the output or error message.
        """
        try:
            if self.command == 'create-next-app':
                process = subprocess.run(args:['npx', 'create-next-app', 'my-next-app'], check=True, stdout=subprocess.PIPE, stderr=)
            # Execute the command and capture the output
            result = subprocess.run(self.command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Return the error message if the command fails
            return f"An error occurred while executing the command: {e.stderr}"