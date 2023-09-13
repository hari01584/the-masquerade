# import connector.base
from langchain import HuggingFacePipeline
from langchain import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain import HuggingFacePipeline
from langchain import LLMChain
from langchain.llms import OpenAI

class GPT():
    def __init__(self, api_key):
        self.API_KEY = api_key

    def _init_model(self):
        return OpenAI(api_key=self.API_KEY, model="davinci")