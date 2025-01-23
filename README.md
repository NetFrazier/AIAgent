# AIAgent

AIAgent is a flexible framework designed to facilitate the creation and deployment of AI agents using the agency-swarm library. This project provides a powerful, modular structure for developing intelligent agents capable of tackling a wide range of tasks across various domains.

## Agency Structure

The **SecDef** agency is designed with a collaborative structure where the CEO communicates with the designer, who in turn communicates with the web developer and copywriter. This ensures a seamless workflow from design to development.
Key Features

## Installation

To install the required dependencies for this agency, run the following command:

```bash
pip install -r requirements.txt
```

Make sure you have `agency_swarm` and `npm` installed as well. For details on how to install `npm`, refer to the official [npm documentation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

## Agents

Agents are created with specific roles:

- **SECDEFCEO Agent**: Acts as the overseer and communicator across the agency, ensuring alignment with the agency's goals.
- **Designer Agent**: Responsible for the UI/UX design, utilizing tools like the browser analysis tool.
- **WebDeveloper Agent**: Handles the development of the web application, equipped with tools like the directory navigator, file reader, and writer.
- **Copywriter Agent**: Creates compelling content for the website.
For the **SecDef** agency, several custom tools were created for each agent to facilitate their tasks in the web development process. Below is a description of the tools created for each agent, as mentioned in the script:

## Tools

### Designer Agent Tools

- **Browser Analysis Tool**: This tool uses GPT-4V to analyze web pages and provide insights on design elements, color schemes, and layout. It helps the designer agent to ensure that the current web page aligns with the provided design.

### Web Developer Agent Tools

- **Directory Navigator Tool**: Utilizes the OS `change dir` method to navigate through directories. This simple yet effective tool helps the web developer agent to move around the file system and locate files necessary for web development.
  
- **File Reader Tool**: Opens and reads the content of files, returning the content as a string. This tool is essential for the web developer agent to read existing code files and make necessary adjustments or additions.
  
- **File Writer Tool**: Takes a filepath and content as input, then opens and writes the content to the file, confirming the action by returning a success message. This tool is crucial for creating new files or updating existing ones with new content.
  
- **Command Executor Tool**: Originally designed to execute commands using subprocess, it was deemed potentially dangerous and was planned to be modified. The idea was to restrict it to run only predefined safe commands, such as `npx create-next-app` or `npm run build`, to ensure the security and integrity of the development process.

- **List Directory Tool** (Proposed for the Web Developer Agent): This tool would list the contents of a directory, providing a view of the current directory tree as a string. It's aimed at enhancing the web developer agent's ability to manage and overview the project's file structure.

These tools are designed to automate specific tasks within the agency, reducing manual effort and streamlining the web development process. Each tool is tailored to the needs of its respective agent, ensuring they can perform their duties effectively and efficiently.

## Usage

Run your agency using the following command:

```bash
python agency.py
```

This command initiates the workflow, where each agent performs its designated tasks, from design to content creation and web development. The process is iterative, with continuous improvements based on feedback.