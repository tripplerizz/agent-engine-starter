import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def add_numbers(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

def subtract_numbers(a: float, b: float) -> float:
    """Subtracts the second number from the first."""
    return a - b

def multiply_numbers(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

def divide_numbers(a: float, b: float) -> float:
    """Divides the first number by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.5-flash",
    instruction="If the user asks a math question, help the user with addition, subtraction, multiplication, or division of numbers by using the available math tools.",
    description="An Agent to provide interesting news about a country and help with basic math operations.",
    tools=[add_numbers, subtract_numbers, multiply_numbers, divide_numbers],
)
