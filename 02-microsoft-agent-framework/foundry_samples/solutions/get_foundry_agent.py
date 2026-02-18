# Copyright (c) Microsoft. All rights reserved.

import asyncio
import os
import time

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.ai.projects.aio import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition
from azure.identity.aio import AzureCliCredential

"""
Azure AI Agent with Existing Agent Example

This sample demonstrates working with pre-existing Azure AI Agents by using provider.get_agent() method,
showing agent reuse patterns for production scenarios.
"""


async def using_provider_get_agent() -> None:
    print("=== Get existing Azure AI agent with provider.get_agent() ===")

    # Create the client
    async with (
        AzureCliCredential() as credential,
        AIProjectClient(endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"], credential=credential) as project_client,
    ):
        # Get existing agent by name
        provider = AzureAIProjectAgentProvider(project_client=project_client)
        agent = await provider.get_agent(name="Travel-agent")  # Replace with your actual agent name

        # Verify agent properties
        print(f"Agent ID: {agent.id}")
        print(f"Agent name: {agent.name}")
        print(f"Agent description: {agent.description}")

        # List of questions to ask
        questions = [
            "Which destination fits a relaxed food-focused traveler?",
            "What festivals are happening in Rio this month?",
            "I want to visit Paris. What persona best meets this location? Also, what is the closest hotel to the Eiffel Tower?",
        ]

        # Ask each question with a delay
        for i, query in enumerate(questions, 1):
            print(f"\n--- Question {i} of {len(questions)} ---")
            print(f"User: {query}")
            result = await agent.run(query)
            print(f"Agent: {result}")
            
            # Wait 5 seconds before next question (except after the last one)
            if i < len(questions):
                print("\nWaiting 5 seconds before next question...")
                time.sleep(5)


async def main() -> None:
    await using_provider_get_agent()


if __name__ == "__main__":
    asyncio.run(main())