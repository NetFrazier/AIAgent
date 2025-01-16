from agency_swarm import Agency
from Copywriter import Copywriter
from WebDeveloper import WebDeveloper
from Designer import Designer
from SecDefCEO import SecDefCEO

sec_def_ceo = SecDefCEO()
designer = Designer()
web_developer = WebDeveloper()
copywriter = Copywriter()

agency = Agency([sec_def_ceo, designer, 
                 [sec_def_ceo, designer],
                 [designer, web_developer],
                 [designer, copywriter]],
                shared_instructions='./agency_manifesto.md',
                max_prompt_tokens=25000,
                temperature=0.3)

if __name__ == '__main__':
    agency.demo_gradio()