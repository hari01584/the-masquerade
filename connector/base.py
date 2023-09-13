# import connector.base
from langchain import HuggingFacePipeline
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain import HuggingFacePipeline
from langchain import LLMChain
from langchain.llms import OpenAI

class Connector():
    def __init__(self):
        self.connector = GPT3Connector()
            

    def connect(self):
        return self.connector.connect()

    def disconnect(self):
        return self.connector.disconnect()

    def evaluate(self, query):
        return self.connector.evaluate(query)
    
    # -- Internal function to craft a prompt! -- #
    def _craft_prompt(self, query):
        company_profile = query["company_profile"]
        projects = query["projects"]
        experience = query["experience"]
        extra_misc = query["extra_misc"]
        contact = query["contact"]

        template = "Create a personalized concise email, I am looking for intern in my winter semester (6 months) and full time opportunities\n" 

        template += f"The company profile is: {company_profile}\n"
        template += f"Based upon the profile, take only appropriate projects, my projects are: {projects}\n"

        template += f"Also mention brief about my experience, that is: {experience}\n"

        if (extra_misc.strip() != ""):
            template += f"You can also include some extra or misc details, that is: {extra_misc}\n"

        template += f"Also mention my profiles, contact info and websites: {contact}\n"

        template += f"Mention why I am good fit for them, for more information, resume is attached\n"

        generated_prompt = template

        print("Generated prompt is: ", generated_prompt)

        return generated_prompt

class GPT3Connector(Connector):
    MYGPTKEY = ""

    def __init__(self):
        self.llm = OpenAI(model_name="gpt-3.5-turbo")

    def connect(self):
        pass

    def disconnect(self):
        pass

    def evaluate(self, query):
        return self.llm(self._craft_prompt(query))