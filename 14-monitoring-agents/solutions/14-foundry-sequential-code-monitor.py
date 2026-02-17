# 14-foundry-sequential-code-monitor.py
#
# Sequential Agent Workflow: Attraction Recommendation System
#
# This script demonstrates a sequential multi-agent workflow using Microsoft Agent Framework
# with agents from Azure AI Foundry. It creates a two-agent system that works sequentially:
# 1. Front Desk Agent: Makes attraction recommendations based on user's city interest
# 2. Concierge Agent: Reviews and rates the recommendation with expert analysis
#
# Key Features:
# - Sequential agent orchestration (User → Agent 1 → Agent 2)
# - Custom tool functions for each agent
# - Structured outputs using Pydantic models
# - Application Insights integration for telemetry
# - Rich HTML display formatting for Jupyter notebooks
#
# Note: This script includes HTML display functions designed for Jupyter notebooks.
# When running as a standalone script, the HTML won't render but the core functionality works.

import asyncio
import os
import random
import time
from typing import Annotated

# Agent Framework
from agent_framework import ChatMessage, SequentialBuilder
from agent_framework.azure import AzureAIProjectAgentProvider
from agent_framework.observability import get_tracer

# Azure imports
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import AzureCliCredential

# Data modeling and display
from pydantic import BaseModel
from dotenv import load_dotenv

# Telemetry
from opentelemetry.trace import SpanKind
from opentelemetry.trace.span import format_trace_id

# Enable nested asyncio for Jupyter notebooks
import nest_asyncio
nest_asyncio.apply()

# Try to import IPython display, fallback if not in notebook
try:
    from IPython.display import HTML, display
    IN_NOTEBOOK = True
except ImportError:
    IN_NOTEBOOK = False
    def display(html):
        """Fallback display for non-notebook environments"""
        pass
    class HTML:
        def __init__(self, html_string):
            pass

print("✅ All imports successful!")


class AttractionRecommendation(BaseModel):
    """Attraction recommendation from the front desk agent."""
    city: str
    attraction_name: str
    description: str
    category: str  # e.g., "museum", "landmark", "park"
    recommended_duration: str  # e.g., "2-3 hours"
    why_recommended: str
    best_time_to_visit: str


class AttractionReview(BaseModel):
    """Expert review and rating from the concierge agent."""
    attraction_name: str
    city: str
    popularity_score: int  # 1-10 scale
    popularity_reasoning: str
    visitor_rating: float  # 1.0-5.0 scale
    pros: list[str]
    cons: list[str]
    concierge_recommendation: str
    alternative_suggestions: list[str]

print("✅ Data models defined")


# Front Desk Agent Tools
def get_attraction_hours(
    attraction_name: Annotated[str, "Name of the attraction"],
    city: Annotated[str, "City where the attraction is located"]
) -> str:
    """Get opening hours for a specific attraction."""
    print(f"🔧 TOOL CALLED: get_attraction_hours('{attraction_name}', '{city}')")
    hours = {"weekday": "9:00 AM - 6:00 PM", "weekend": "10:00 AM - 8:00 PM", "closed": "Tuesdays"}
    result = f"{attraction_name} in {city} is open {hours['weekday']} on weekdays, {hours['weekend']} on weekends. Closed on {hours['closed']}."
    print(f"   ↳ Returned: {result[:60]}...")
    return result

def get_current_weather(
    city: Annotated[str, "City name"],
    country: Annotated[str, "Country code"] = "US"
) -> str:
    """Get current weather conditions for a city."""
    print(f"🔧 TOOL CALLED: get_current_weather('{city}', '{country}')")
    conditions = ["Sunny", "Partly Cloudy", "Overcast", "Light Rain"]
    temp = random.randint(15, 28)
    result = f"Current weather in {city}: {random.choice(conditions)}, {temp}°C. Good conditions for sightseeing."
    print(f"   ↳ Returned: {result}")
    return result

def calculate_distance(
    from_location: Annotated[str, "Starting location"],
    to_location: Annotated[str, "Destination location"]
) -> str:
    """Calculate distance between two locations."""
    print(f"🔧 TOOL CALLED: calculate_distance('{from_location}', '{to_location}')")
    distance_km = round(random.uniform(2.0, 15.0), 1)
    travel_time = int(distance_km * 3)
    result = f"Distance from {from_location} to {to_location}: {distance_km} km, approximately {travel_time} minutes by car."
    print(f"   ↳ Returned: {result}")
    return result

# Concierge Agent Tools
def get_visitor_reviews(
    attraction_name: Annotated[str, "Name of the attraction"],
    city: Annotated[str, "City location"]
) -> str:
    """Get recent visitor reviews and ratings for an attraction."""
    print(f"🔧 TOOL CALLED: get_visitor_reviews('{attraction_name}', '{city}')")
    avg_rating = round(random.uniform(3.8, 4.9), 1)
    total_reviews = random.randint(1000, 10000)
    positive = random.choice(["amazing experience", "must-see", "well worth it"])
    concern = random.choice(["can be crowded", "expensive tickets", "long lines"])
    result = f"{attraction_name} in {city}: {avg_rating}/5.0 from {total_reviews} reviews. Most common positive: {positive}. Concern: {concern}."
    print(f"   ↳ Returned: {result[:80]}...")
    return result

def compare_attractions(
    attractions: Annotated[list[str], "List of attraction names to compare"],
    city: Annotated[str, "City location"]
) -> str:
    """Compare multiple attractions across various criteria."""
    print(f"🔧 TOOL CALLED: compare_attractions({attractions}, '{city}')")
    comparisons = []
    for attraction in attractions:
        rating = round(random.uniform(3.5, 5.0), 1)
        price = random.choice(["$", "$$", "$$$"])
        crowd = random.choice(["Low", "Medium", "High"])
        comparisons.append(f"{attraction}: Rating {rating}/5, Price {price}, Crowds: {crowd}")
    result = f"Comparison in {city}:\n" + "\n".join(comparisons)
    print(f"   ↳ Returned comparison data for {len(attractions)} attractions")
    return result

def get_ticket_prices(
    attraction_name: Annotated[str, "Name of the attraction"]
) -> str:
    """Get current ticket prices and booking information."""
    print(f"🔧 TOOL CALLED: get_ticket_prices('{attraction_name}')")
    adult = random.randint(15, 45)
    child = int(adult * 0.6)
    senior = int(adult * 0.8)
    result = f"{attraction_name} tickets: Adult ${adult}, Child ${child}, Senior ${senior}. Online booking: 10% discount."
    print(f"   ↳ Returned: {result}")
    return result

print("✅ Tool functions defined")
print("   Front Desk: 3 tools | Concierge: 3 tools")


def display_front_desk_section(data: AttractionRecommendation):
    """Display front desk recommendation."""
    if IN_NOTEBOOK:
        display(HTML(f"""
        <div style='padding: 20px; background: #e3f2fd; border-radius: 8px; margin: 15px 0; border-left: 4px solid #2196f3;'>
            <h3 style='margin: 0 0 15px 0; color: #0d47a1; font-weight: bold;'>🏨 Front Desk Recommendation</h3>
            <h4 style='margin: 0 0 10px 0; color: #000; font-weight: bold;'>{data.attraction_name}</h4>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Category:</strong> {data.category}</p>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Description:</strong> {data.description}</p>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Why Recommended:</strong> {data.why_recommended}</p>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Duration:</strong> {data.recommended_duration}</p>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Best Time:</strong> {data.best_time_to_visit}</p>
        </div>
        """))
    else:
        # Console-friendly output
        print(f"\n🏨 Front Desk Recommendation")
        print(f"{'='*60}")
        print(f"Attraction: {data.attraction_name}")
        print(f"Category: {data.category}")
        print(f"Description: {data.description}")
        print(f"Why Recommended: {data.why_recommended}")
        print(f"Duration: {data.recommended_duration}")
        print(f"Best Time: {data.best_time_to_visit}")

def display_concierge_section(data: AttractionReview):
    """Display concierge review."""
    if IN_NOTEBOOK:
        star_rating = "⭐" * int(data.visitor_rating) + "☆" * (5 - int(data.visitor_rating))
        popularity_bar = "🟩" * data.popularity_score + "⬜" * (10 - data.popularity_score)
        pros_html = "".join([f"<li style='color: #2e7d32; font-size: 15px; font-weight: 500;'>✓ {pro}</li>" for pro in data.pros])
        cons_html = "".join([f"<li style='color: #c62828; font-size: 15px; font-weight: 500;'>✗ {con}</li>" for con in data.cons])
        
        display(HTML(f"""
        <div style='padding: 20px; background: #fff3e0; border-radius: 8px; margin: 15px 0; border-left: 4px solid #ff9800;'>
            <h3 style='margin: 0 0 15px 0; color: #e65100; font-weight: bold;'>🎩 Concierge Expert Review</h3>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;'>
                <div style='background: rgba(255,152,0,0.2); padding: 15px; border-radius: 8px; border: 1px solid #ff9800;'>
                    <h4 style='color: #000; font-weight: bold; margin: 0 0 10px 0;'>Popularity Score</h4>
                    <div style='font-size: 28px; font-weight: bold; color: #000;'>{data.popularity_score}/10</div>
                    <div style='font-size: 16px; margin-top: 8px;'>{popularity_bar}</div>
                </div>
                <div style='background: rgba(255,152,0,0.2); padding: 15px; border-radius: 8px; border: 1px solid #ff9800;'>
                    <h4 style='color: #000; font-weight: bold; margin: 0 0 10px 0;'>Visitor Rating</h4>
                    <div style='font-size: 28px; font-weight: bold; color: #000;'>{data.visitor_rating}/5.0</div>
                    <div style='font-size: 18px; margin-top: 5px;'>{star_rating}</div>
                </div>
            </div>
            <p style='color: #000; font-size: 15px; line-height: 1.6;'><strong>Reasoning:</strong> {data.popularity_reasoning}</p>
            <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>
                <div><h4 style='color: #000; font-weight: bold;'>Pros:</h4><ul style='margin-top: 10px;'>{pros_html}</ul></div>
                <div><h4 style='color: #000; font-weight: bold;'>Cons:</h4><ul style='margin-top: 10px;'>{cons_html}</ul></div>
            </div>
            <p style='color: #000; font-size: 15px; line-height: 1.6; margin-top: 15px;'><strong>Recommendation:</strong> {data.concierge_recommendation}</p>
        </div>
        """))
    else:
        # Console-friendly output
        print(f"\n🎩 Concierge Expert Review")
        print(f"{'='*60}")
        print(f"Popularity Score: {data.popularity_score}/10")
        print(f"Visitor Rating: {data.visitor_rating}/5.0")
        print(f"Reasoning: {data.popularity_reasoning}")
        print(f"\nPros:")
        for pro in data.pros:
            print(f"  ✓ {pro}")
        print(f"\nCons:")
        for con in data.cons:
            print(f"  ✗ {con}")
        print(f"\nRecommendation: {data.concierge_recommendation}")

def display_tool_calls(messages: list[ChatMessage]):
    """Display tool calls made by agents."""
    if not IN_NOTEBOOK:
        print(f"\n🛠️ Tool Usage")
        print(f"{'='*60}")
        print("Agents have access to the following tools:")
        print("\n🏨 Front Desk Agent Tools:")
        print("  - get_attraction_hours()")
        print("  - get_current_weather()")
        print("  - calculate_distance()")
        print("\n🎩 Concierge Agent Tools:")
        print("  - get_visitor_reviews()")
        print("  - compare_attractions()")
        print("  - get_ticket_prices()")
        return
    
    # Show available tools per agent
    tools_html = """
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 10px;'>
        <div style='background: rgba(33,150,243,0.1); padding: 12px; border-radius: 6px; border: 1px solid #2196f3;'>
            <div style='color: #000; font-weight: 600; font-size: 14px; margin-bottom: 8px;'>🏨 Front Desk Agent Tools</div>
            <ul style='margin: 0; padding-left: 20px; color: #333; font-size: 13px;'>
                <li>get_attraction_hours()</li>
                <li>get_current_weather()</li>
                <li>calculate_distance()</li>
            </ul>
        </div>
        <div style='background: rgba(255,152,0,0.1); padding: 12px; border-radius: 6px; border: 1px solid #ff9800;'>
            <div style='color: #000; font-weight: 600; font-size: 14px; margin-bottom: 8px;'>🎩 Concierge Agent Tools</div>
            <ul style='margin: 0; padding-left: 20px; color: #333; font-size: 13px;'>
                <li>get_visitor_reviews()</li>
                <li>compare_attractions()</li>
                <li>get_ticket_prices()</li>
            </ul>
        </div>
    </div>
    """
    
    display(HTML(f"""
    <div style='padding: 15px; background: #e8f5e9; border-radius: 8px; margin: 15px 0; border-left: 4px solid #4caf50;'>
        <h4 style='margin: 0 0 10px 0; color: #2e7d32; font-weight: bold;'>🛠️ Tool Usage</h4>
        <p style='color: #000; font-size: 14px; margin: 0 0 10px 0;'>Agents have access to the following tools to gather real-time information:</p>
        {tools_html}
        <p style='color: #666; font-size: 13px; margin: 15px 0 0 0; font-style: italic;'>Tool calls and outputs are handled internally by the agents and integrated into their responses.</p>
    </div>
    """))

print("✅ Display functions defined")


async def setup_agents():
    """Initialize and configure agents with tools."""
    # Load environment variables
    load_dotenv()

    # Verify Azure AI Project endpoint
    if not os.environ.get("AZURE_AI_PROJECT_ENDPOINT"):
        raise ValueError("❌ AZURE_AI_PROJECT_ENDPOINT environment variable is not set")

    print(f"✅ Azure AI Project Endpoint: {os.environ['AZURE_AI_PROJECT_ENDPOINT']}")

    # Optional: Configure Application Insights telemetry
    if os.environ.get("APPLICATIONINSIGHTS_CONNECTION_STRING"):
        try:
            from opentelemetry import trace
            from opentelemetry.sdk.trace import TracerProvider
            from opentelemetry.sdk.trace.export import BatchSpanProcessor
            from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
            
            provider = TracerProvider()
            trace.set_tracer_provider(provider)
            exporter = AzureMonitorTraceExporter(connection_string=os.environ["APPLICATIONINSIGHTS_CONNECTION_STRING"])
            provider.add_span_processor(BatchSpanProcessor(exporter))
            
            print("✅ Application Insights telemetry configured")
        except Exception as e:
            print(f"⚠️ Telemetry setup skipped: {e}")
    else:
        print("ℹ️ Application Insights not configured (optional)")

    credential = AzureCliCredential()
    
    async with AIProjectClient(
        endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        credential=credential
    ) as project_client:
        provider = AzureAIProjectAgentProvider(project_client=project_client)
        
        # Define tools for each agent
        front_desk_tools = [get_attraction_hours, get_current_weather, calculate_distance]
        concierge_tools = [get_visitor_reviews, compare_attractions, get_ticket_prices]
        
        # Get agents with tools
        front_desk_agent = await provider.get_agent(name="frontdeskagent", tools=front_desk_tools)
        concierge_agent = await provider.get_agent(name="conciergeagent", tools=concierge_tools)
        
        print(f"✅ Retrieved Front Desk Agent: {front_desk_agent.name} | {len(front_desk_tools)} tools")
        print(f"✅ Retrieved Concierge Agent: {concierge_agent.name} | {len(concierge_tools)} tools")
        
        return front_desk_agent, concierge_agent


async def display_attraction_recommendation(front_desk_agent, concierge_agent, city: str):
    """Run workflow and display results."""
    
    # Build sequential workflow
    workflow = (
        SequentialBuilder()
        .participants([front_desk_agent, concierge_agent])
        .build()
    )
    
    print(f"\n{'='*60}")
    print(f"🔄 Processing Recommendation for {city}")
    print(f"{'='*60}\n")
    
    # Create trace span for telemetry (if configured)
    with get_tracer().start_as_current_span(f"Attraction-Recommendation-{city}", kind=SpanKind.CLIENT) as span:
        # Run workflow
        events = await workflow.run(f"I want to visit an attraction in {city}. Please check the current weather, opening hours, visitor reviews, and ticket prices to help me decide.")
    
    outputs = events.get_outputs()
    
    if outputs:
        messages: list[ChatMessage] = outputs[0]
        
        # Extract agent responses
        front_desk_response = None
        concierge_response = None
        
        for msg in messages:
            if msg.author_name == "frontdeskagent":
                front_desk_response = msg.text
            elif msg.author_name == "conciergeagent":
                concierge_response = msg.text
        
        # Display results
        print(f"\n{'='*60}")
        print(f"Attraction Recommendation for {city}")
        print(f"{'='*60}")
        
        # Display tool calls
        display_tool_calls(messages)
        
        # Parse and display responses
        if front_desk_response:
            try:
                recommendation = AttractionRecommendation.model_validate_json(front_desk_response)
                display_front_desk_section(recommendation)
            except Exception as e:
                print(f"❌ Error parsing front desk response: {e}")
        
        if concierge_response:
            try:
                review = AttractionReview.model_validate_json(concierge_response)
                display_concierge_section(review)
            except Exception as e:
                print(f"❌ Error parsing concierge response: {e}")


async def main():
    """Main execution function."""
    # Initialize agents
    front_desk_agent, concierge_agent = await setup_agents()
    
    # Test cities
    cities_to_try = ["Barcelona", "Paris", "Tokyo"]
    
    # Run workflow for first city
    await display_attraction_recommendation(front_desk_agent, concierge_agent, cities_to_try[0])
    
    # Optionally test all cities
    # for city in cities_to_try:
    #     print(f"\n{'='*80}\n🌍 Testing: {city}\n{'='*80}")
    #     await display_attraction_recommendation(front_desk_agent, concierge_agent, city)


if __name__ == "__main__":
    asyncio.run(main())
