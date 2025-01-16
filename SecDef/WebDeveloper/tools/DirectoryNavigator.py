from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class DirectoryNavigator(BaseTool):
    """
    A tool to navigate through directories in the file system. It provides functionalities
    to list the contents of a directory, change the current working directory, and retrieve
    the current directory path.
    """

    action: str = Field(
        ..., description="The action to perform: 'list_contents', 'change_directory', or 'get_current_directory'."
    )
    path: str = Field(
        default="", description="The path to perform the action on. Required for 'change_directory'."
    )

    def run(self):
        """
        Executes the specified action and returns the result.
        """
        if self.action == 'list_contents':
            return self.list_contents(self.path)
        elif self.action == 'change_directory':
            return self.change_directory(self.path)
        elif self.action == 'get_current_directory':
            return self.get_current_directory()
        else:
            return "Invalid action specified. Please use 'list_contents', 'change_directory', or 'get_current_directory'."

    def list_contents(self, path):
        """
        Lists the contents of the specified directory.
        """
        if os.path.isdir(path):
            return os.listdir(path)
        else:
            return f"The directory '{path}' does not exist."

    def change_directory(self, path):
        """
        Changes the current working directory to the specified path.
        """
        try:
            os.chdir(path)
            return f"Changed current working directory to '{path}'."
        except FileNotFoundError:
            return f"The directory '{path}' does not exist."
        except NotADirectoryError:
            return f"The path '{path}' is not a directory."
        except PermissionError:
            return f"Permission denied to change to directory '{path}'."

    def get_current_directory(self):
        """
        Retrieves the current working directory path.
        """
        return os.getcwd()