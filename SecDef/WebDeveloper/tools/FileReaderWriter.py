from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class FileReaderWriter(BaseTool):
    """
    A tool to read from and write to files. It supports reading the contents of a file,
    writing data to a file, and appending data to an existing file. The tool handles
    different file encodings and ensures data integrity during read/write operations.
    """

    action: str = Field(
        ..., description="The action to perform: 'read', 'write', or 'append'."
    )
    file_path: str = Field(
        ..., description="The path of the file to perform the action on."
    )
    data: str = Field(
        default="", description="The data to write or append to the file. Used for 'write' and 'append' actions."
    )
    encoding: str = Field(
        default="utf-8", description="The encoding to use for reading or writing the file."
    )

    def run(self):
        """
        Executes the specified action on the given file path and returns the result.
        """
        if self.action == 'read':
            return self.read_file(self.file_path, self.encoding)
        elif self.action == 'write':
            return self.write_file(self.file_path, self.data, self.encoding)
        elif self.action == 'append':
            return self.append_file(self.file_path, self.data, self.encoding)
        else:
            return "Invalid action specified. Please use 'read', 'write', or 'append'."

    def read_file(self, file_path, encoding):
        """
        Reads the contents of the specified file using the given encoding.
        """
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"The file '{file_path}' does not exist."
        except UnicodeDecodeError:
            return f"Failed to decode the file '{file_path}' with encoding '{encoding}'."
        except Exception as e:
            return f"An error occurred while reading the file: {str(e)}"

    def write_file(self, file_path, data, encoding):
        """
        Writes data to the specified file using the given encoding.
        """
        try:
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(data)
            return f"Data written to '{file_path}' successfully."
        except Exception as e:
            return f"An error occurred while writing to the file: {str(e)}"

    def append_file(self, file_path, data, encoding):
        """
        Appends data to the specified file using the given encoding.
        """
        try:
            with open(file_path, 'a', encoding=encoding) as file:
                file.write(data)
            return f"Data appended to '{file_path}' successfully."
        except Exception as e:
            return f"An error occurred while appending to the file: {str(e)}"