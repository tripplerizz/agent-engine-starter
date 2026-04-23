import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city: The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary with 'status' and 'report' or 'error_message'.
    """
    mock_weather = {
        "new york": "Sunny, 25°C",
        "london": "Cloudy, 15°C",
        "tokyo": "Light rain, 18°C",
    }
    report = mock_weather.get(city.lower())
    if report:
        return {"status": "success", "report": f"Weather in {city}: {report}"}
    return {"status": "error", "error_message": f"No weather data for '{city}'."}


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city: The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary with 'status' and 'report' or 'error_message'.
    """
    timezones = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
    }
    tz_name = timezones.get(city.lower())
    if tz_name:
        now = datetime.datetime.now(ZoneInfo(tz_name))
        return {"status": "success", "report": f"Time in {city}: {now.strftime('%H:%M:%S %Z')}"}
    return {"status": "error", "error_message": f"No timezone data for '{city}'."}


root_agent = Agent(
    name="tool_agent",
    model="gemini-flash-latest",
    description="Agent that provides weather and time information for cities.",
    instruction=(
        "You are a helpful assistant that provides weather and time information. "
        "Use 'get_weather' for weather requests and 'get_current_time' for time requests. "
        "If a tool returns an error, inform the user politely."
    ),
    tools=[get_weather, get_current_time],
)
