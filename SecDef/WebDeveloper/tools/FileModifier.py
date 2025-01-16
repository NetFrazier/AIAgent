from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class FileModifier(BaseTool):
    """
    A tool to modify the contents of a file. It supports operations like searching for
    specific text, replacing text, and deleting text within a file. The tool ensures
    that modifications do not corrupt the file and maintain data integrity.
    """

    action: str = Field(
        ..., description="The action to perform: 'search', 'replace', or 'delete'."
    )
    file_path: str = Field(
        ..., description="The path of the file to perform the action on."
    )
    search_text: str = Field(
        default="", description="The text to search for in the file. Used for 'search', 'replace', and 'delete' actions."
    )
    replace_text: str = Field(
        default="", description="The text to replace the search text with. Used for 'replace' action."
    )
    encoding: str = Field(
        default="utf-8", description="The encoding to use for reading and writing the file."
    )

    def run(self):
        """
        Executes the specified action on the given file path and returns the result.
        """
        if self.action == 'search':
            return self.search_text_in_file(self.file_path, self.search_text, self.encoding)
        elif self.action == 'replace':
            return self.replace_text_in_file(self.file_path, self.search_text, self.replace_text, self.encoding)
        elif self.action == 'delete':
            return self.delete_text_in_file(self.file_path, self.search_text, self.encoding)
        else:
            return "Invalid action specified. Please use 'search', 'replace', or 'delete'."

    def search_text_in_file(self, file_path, search_text, encoding):
        """
        Searches for specific text in the file and returns the lines containing the text.
        """
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                lines = file.readlines()
            matching_lines = [line for line in lines if search_text in line]
            return matching_lines if matching_lines else f"No occurrences of '{search_text}' found."
        except FileNotFoundError:
            return f"The file '{file_path}' does not exist."
        except UnicodeDecodeError:
            return f"Failed to decode the file '{file_path}' with encoding '{encoding}'."
        except Exception as e:
            return f"An error occurred while searching the file: {str(e)}"

    def replace_text_in_file(self, file_path, search_text, replace_text, encoding):
        """
        Replaces specific text in the file with new text.
        """
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            new_content = content.replace(search_text, replace_text)
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(new_content)
            return f"Replaced occurrences of '{search_text}' with '{replace_text}' in '{file_path}'."
        except FileNotFoundError:
            return f"The file '{file_path}' does not exist."
        except UnicodeDecodeError:
            return f"Failed to decode the file '{file_path}' with encoding '{encoding}'."
        except Exception as e:
            return f"An error occurred while replacing text in the file: {str(e)}"

    def delete_text_in_file(self, file_path, search_text, encoding):
        """
        Deletes specific text from the file.
        """
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            new_content = content.replace(search_text, "")
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(new_content)
            return f"Deleted occurrences of '{search_text}' from '{file_path}'."
        except FileNotFoundError:
            return f"The file '{file_path}' does not exist."
        except UnicodeDecodeError:
            return f"Failed to decode the file '{file_path}' with encoding '{encoding}'."
        except Exception as e:
            return f"An error occurred while deleting text from the file: {str(e)}"