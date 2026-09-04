from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def calculate(expression: str) -> str:
    """Evaluate a simple Python expression provided as a string and return the result.

    This tool is intended for basic arithmetic expressions. It returns the
    stringified result or an error message on failure.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Error occurred while evaluating the expression."

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
agent = create_agent(
    model=model,
    tools=[calculate],
    system_prompt="You are a helpful assistant use calculate tool to solve the math problems."
)
response = agent.invoke({
    "messages": [{"role": "user", "content": "What is the sum of 2 and 2?"}]
})

print(response["messages"][-1].content)