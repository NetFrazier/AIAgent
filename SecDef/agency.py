from agency_swarm import Agency, set_openai_key, set_openai_client
from Copywriter import Copywriter
from WebDeveloper import WebDeveloper
from Designer import Designer
from SecDefCEO import SecDefCEO
import os, json
import openai
import httpx

sec_def_ceo = SecDefCEO()
designer = Designer()
web_developer = WebDeveloper()
copywriter = Copywriter()

set_openai_key(os.environ["OPENAI_API_KEY"])

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"],
                    #    timeout=httpx.Timeout(1800000.0, read=18000000, connect=15.0),
                       max_retries=10,
                       default_headers={"OpenAI-Beta": "assistants=v2"})
set_openai_client(client)

def load_threads(chat_id):
    if os.path.exists(f"{chat_id}_threads.json"):
        with open(f"{chat_id}_threads.json", "r") as file:
            threads = json.load(file)
    else:
        threads = []
    return threads

def save_threads(new_threads, chat_id):
    # Save threads to a file or database using the chat_id
    with open(f"{chat_id}_threads.json", "w") as file:
        json.dump(new_threads, file)
        
agency = Agency([sec_def_ceo, designer, web_developer,
                 [sec_def_ceo, designer],
                 [designer, web_developer],
                 [designer, copywriter]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)

if __name__ == '__main__':
    agency.demo_gradio()