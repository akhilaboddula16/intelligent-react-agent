from typing import Dict
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent


from utils import get_llm

# ==================================================
# 1. LOAD LLM (OLLAMA)
# ==================================================
llm = get_llm()

# ==================================================
# 2. SYSTEM PROMPT
# ==================================================
SYSTEM_PROMPT = """
You are an intelligent ReAct agent.

You can:
- Solve math problems using tools
- Fetch customer information using tools
- Rewrite emails in a specified tone

Rules:
- Use tools only when necessary
- Do not reveal internal reasoning
- Follow the requested tone strictly
"""

# ==================================================
# 3. SUPPORTED EMAIL TONES
# ==================================================
SUPPORTED_TONES = {
    "formal": "Use a professional and respectful tone.",
    "polite": "Use a courteous and friendly tone.",
    "casual": "Use a relaxed and conversational tone.",
    "apology": "Use an apologetic and empathetic tone.",
    "urgent": "Use a firm and time-sensitive tone."
}

# ==================================================
# 4. CUSTOMER DATA
# ==================================================
CUSTOMER_DATA: Dict[str, Dict[str, str]] = {
    "akhila": {
        "name": "Akhila",
        "email": "akhila@gmail.com",
        "phone": "9876543210",
        "city": "Hyderabad"
    }
}

# ==================================================
# 5. TOOL: CALCULATOR
# ==================================================
@tool
def calculate(expression: str) -> str:
    """Perform a mathematical calculation."""
    try:
        result = eval(expression, {"__builtins__": {}})
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

# ==================================================
# 6. TOOL: CUSTOMER LOOKUP
# ==================================================
@tool
def get_customer_info(name: str) -> str:
    """Retrieve customer details by name."""
    key = name.lower()
    if key in CUSTOMER_DATA:
        c = CUSTOMER_DATA[key]
        return (
            f"Name: {c['name']}\n"
            f"Email: {c['email']}\n"
            f"Phone: {c['phone']}\n"
            f"City: {c['city']}"
        )
    return "Customer not found."

# ==================================================
# 7. TOOL: EMAIL TONE REWRITE
# ==================================================
@tool
def rewrite_email(email_text: str, tone: str) -> str:
    """Rewrite an email in a specified tone."""
    tone = tone.lower()
    if tone not in SUPPORTED_TONES:
        return f"Unsupported tone. Choose from: {', '.join(SUPPORTED_TONES.keys())}"

    instruction = SUPPORTED_TONES[tone]
    return f"{instruction}\n\nEmail:\n{email_text}"

# ==================================================
# 8. CREATE REACT AGENT
# ==================================================
tools = [calculate, get_customer_info, rewrite_email]

agent = create_react_agent(
    model=llm,
    tools=tools
)

# ==================================================
# 9. RUN AGENT
# ==================================================
def run_agent(user_input: str) -> str:
    result = agent.invoke(
        {
            "messages": [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=user_input)
            ]
        }
    )
    return result["messages"][-1].content

if __name__ == "__main__":
    print("---- Calculator Test ----")
    print(run_agent("What is 45 * 6 + 10?"))

    print("\n---- Customer Lookup Test ----")
    print(run_agent("Get customer info for Akhila"))

    print("\n---- Email Rewrite Test ----")
    print(run_agent(
        "Rewrite this email in a formal tone: please send the files asap"
    ))

