from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    information = """sachin tendulkar"""
    summarytemplate="""
    Give the information about a person, create:
    1.A short summary
    2.The intresting facts about the person
    """
    summaryprompt = PromptTemplate(
        template=summarytemplate, 
        input_variables=["information"])   
    #llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
    llm=ChatOllama(model="qwen3.5:latest", temperature=0.9)
    chain = summaryprompt|llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()