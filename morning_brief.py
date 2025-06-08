import os
from pydantic_ai import Agent
from pydantic import BaseModel
from data_source.microsoft_graph_api import get_unread_messages, get_calendar_events


os.environ["GEMINI_API_KEY"] = "AIzaSyBfodW-63KLKy6usujfl8-1qd1bdH8cPCE"

class SummaryInput(BaseModel):
    emails: list[str]
    events: list[str]

class SummaryOutput(BaseModel):
    summary: str

def summarize_brief():
    # Fetch data
    unread_emails = get_unread_messages()  
    events =get_calendar_events()         

    print(" Emails:", unread_emails)
    print(" Events:", events)

    # Setup agent
    agent = Agent(
        model="google-gla:gemini-1.5-flash",
        system_prompt=(
            "You are a helpful assistant. Summarize the user's unread emails and calendar events "
            "into a short professional briefing. If there's no data, say 'No updates for now.'"
        ),
        input_model=SummaryInput,
        output_model=SummaryOutput
    )

    input_data = SummaryInput(emails=unread_emails, events=events)

    result = agent.run_sync(input_data)
    print("\n Summary:\n", result.summary)
    return result.summary
