# 14-foundry-agent-monitor.py
# 
# Azure AI Agent with Observability - Manual Tracing Implementation
#
# This script demonstrates how to add OpenTelemetry tracing to Azure AI Foundry agents
# using manual tracing spans. This approach works with all agents, including those with
# complex tools like Bing search.
#
# Key Features:
# - Configure Azure Monitor with Application Insights
# - Create custom OpenTelemetry spans
# - Add attributes to spans for better observability
# - View metrics in the Foundry Monitor dashboard
# - View detailed traces in the Foundry Tracing view
# - Handle real-world limitations (complex tool parameters)

# Copyright (c) Microsoft. All rights reserved.

import asyncio
import logging
import os
import time

from agent_framework.azure import AzureAIProjectAgentProvider
from agent_framework.observability import create_resource, get_tracer
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import AzureCliCredential
from azure.monitor.opentelemetry import configure_azure_monitor
from dotenv import load_dotenv
from opentelemetry.trace import SpanKind
from opentelemetry.trace.span import format_trace_id

load_dotenv()

# Enable nested asyncio for Jupyter notebooks
import nest_asyncio
nest_asyncio.apply()

# Set up logger
logger = logging.getLogger(__name__)

print("✅ All imports loaded successfully")
print("✅ Ready to run the workshop!")


async def using_provider_get_agent() -> None:
    """Get an existing Azure AI agent and interact with it with tracing."""
    print("=== Get existing Azure AI agent with provider.get_agent() ===\n")

    # Create the client
    async with (
        AzureCliCredential() as credential,
        AIProjectClient(
            endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"], 
            credential=credential
        ) as project_client,
    ):
        # Configure Azure Monitor tracing
        # Note: We configure Azure Monitor but DON'T enable automatic agent instrumentation
        # because it tries to serialize tool parameters that aren't JSON serializable.
        # Instead, we'll use manual tracing with get_tracer().start_as_current_span()
        conn_string = None
        
        try:
            conn_string = await project_client.telemetry.get_application_insights_connection_string()
            print(f"✅ Application Insights connection string retrieved")
        except Exception as e:
            logger.warning(
                "No Application Insights connection string found for the Azure AI Project. "
                "Please ensure Application Insights is configured in your Azure AI project."
            )
            print(f"⚠️ Warning: {e}")
            print("Continuing without tracing...")
    
        if conn_string:
            try:
                configure_azure_monitor(
                    connection_string=conn_string,
                    enable_live_metrics=True,
                    resource=create_resource(),
                    enable_performance_counters=False,
                )
                # NOTE: We do NOT call enable_instrumentation() here because it would
                # automatically instrument agent.run() calls and try to serialize tool
                # parameters, causing "BingGroundingSearchToolParameters is not JSON serializable"
                # Instead, we use manual tracing with get_tracer().start_as_current_span()
                print("✅ Azure Monitor configured for tracing")
                print("✅ Using manual tracing spans (not automatic agent instrumentation)\n")
                print("ℹ️ Note: Automatic agent instrumentation is disabled to avoid")
                print("   serialization issues with complex tool parameters like Bing search.")
                print("   You'll still see traces in Application Insights for the overall flow.\n")
            except Exception as e:
                logger.error(f"Failed to configure Azure Monitor: {e}")
                print(f"⚠️ Failed to configure Azure Monitor: {e}")
                print("Continuing without tracing...")
                conn_string = None
        
        # Get existing agent by name
        provider = AzureAIProjectAgentProvider(project_client=project_client)
        agent = await provider.get_agent(name="Travel-agent")  # Replace with your actual agent name

        # Verify agent properties
        print(f"Agent ID: {agent.id}")
        print(f"Agent name: {agent.name}")
        print(f"Agent description: {agent.description}\n")

        # List of questions to ask
        questions = [
            "Which destination fits a relaxed food-focused traveler?",
            "What festivals are happening in Rio this month?",
            "I want to visit Paris. What persona best meets this location? Also, what is the closest hotel to the Eiffel Tower?",
        ]

        # Create a manual tracing span for the agent interaction
        # This allows us to trace the overall flow without the automatic agent instrumentation
        # that fails on complex tool parameter serialization
        with get_tracer().start_as_current_span("Travel Agent Chat", kind=SpanKind.CLIENT) as current_span:
            if conn_string:
                trace_id = format_trace_id(current_span.get_span_context().trace_id)
                print(f"📊 Trace ID: {trace_id}")
                print("   Use this Trace ID to find traces in Application Insights\n")
                current_span.set_attribute("agent.id", agent.id)
                current_span.set_attribute("agent.name", agent.name)
                current_span.set_attribute("question.count", len(questions))
            
            # Ask each question with a delay
            for i, query in enumerate(questions, 1):
                # Create a span for each individual question
                with get_tracer().start_as_current_span(f"Question {i}", kind=SpanKind.CLIENT) as question_span:
                    if conn_string:
                        question_span.set_attribute("question.number", i)
                        question_span.set_attribute("question.text", query)
                    
                    print(f"\n{'='*60}")
                    print(f"Question {i} of {len(questions)}")
                    print(f"{'='*60}")
                    print(f"User: {query}")
                    print()
                    
                    try:
                        result = await agent.run(query)
                        print(f"Agent: {result}")
                        
                        if conn_string:
                            question_span.set_attribute("response.received", True)
                            question_span.set_attribute("response.length", len(str(result)))
                    except Exception as e:
                        print(f"❌ Error running agent: {e}")
                        if conn_string:
                            question_span.set_attribute("error", True)
                            question_span.set_attribute("error.type", type(e).__name__)
                            question_span.set_attribute("error.message", str(e))
                        raise
                
                # Wait 5 seconds before next question (except after the last one)
                if i < len(questions):
                    print("\n⏳ Waiting 5 seconds before next question...")
                    time.sleep(5)
        
        print("\n✅ All questions completed")
        if conn_string:
            print("📊 Check Application Insights for detailed traces and metrics")
            print("   You should see:")
            print("   - A 'Travel Agent Chat' span containing all questions")
            print("   - Individual 'Question N' spans for each question")
            print("   - Custom attributes like question text and response length")


if __name__ == "__main__":
    # Run the agent interaction with tracing
    asyncio.run(using_provider_get_agent())
    
    # Example: Additional questions you can add to the list
    print("\n" + "="*60)
    print("Additional questions you can try:")
    print("="*60)
    additional_questions = [
        "Tell me about things to do in New York.",
        "What is the best destination for a family vacation of 5?",
        "Recommend a destination for a traveler who enjoys nature, scenery, and light physical activity.",
        "Which destination fits a high-energy traveler who wants iconic city experiences without burnout?",
        "For Barcelona, create a food-focused itinerary with minimal transit.",
    ]
    for i, q in enumerate(additional_questions, 1):
        print(f"{i}. {q}")
