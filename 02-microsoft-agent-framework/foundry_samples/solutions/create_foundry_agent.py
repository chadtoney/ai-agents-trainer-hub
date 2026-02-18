# Copyright (c) Microsoft. All rights reserved.

import asyncio
import os
from random import randint
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity.aio import DefaultAzureCredential
from dotenv import load_dotenv
from pydantic import Field

load_dotenv()

"""
Azure AI Agent Basic Example

This sample demonstrates basic usage of AzureAIProjectAgentProvider.
Shows both streaming and non-streaming responses with function tools.
"""


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."


async def non_streaming_example() -> None:
    """Example of non-streaming response (get the complete result at once)."""
    print("=== Non-streaming Response Example ===")

    project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    model_deployment = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o")
    
    # For authentication, run `az login` command in terminal or use DefaultAzureCredential
    async with (
        DefaultAzureCredential() as credential,
        AzureAIProjectAgentProvider(
            credential=credential,
            project_endpoint=project_endpoint
        ) as provider,
    ):
        agent = await provider.create_agent(
            name="BasicWeatherAgent",
            instructions="You are a helpful weather agent.",
            model=model_deployment,
            tools=get_weather,
        )

        query = "What's the weather like in Seattle?"
        print(f"User: {query}")
        result = await agent.run(query)
        print(f"Agent: {result}\n")


async def streaming_example() -> None:
    """Example of streaming response (get results as they are generated)."""
    print("=== Streaming Response Example ===")

    project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
    model_deployment = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME", "gpt-4o")
    
    # For authentication, run `az login` command in terminal or use DefaultAzureCredential
    async with (
        DefaultAzureCredential() as credential,
        AzureAIProjectAgentProvider(
            credential=credential,
            project_endpoint=project_endpoint
        ) as provider,
    ):
        agent = await provider.create_agent(
            name="BasicWeatherAgent",
            instructions="You are a helpful weather agent.",
            model=model_deployment,
            tools=get_weather,
        )

        query = "What's the weather like in Tokyo?"
        print(f"User: {query}")
        print("Agent: ", end="", flush=True)
        async for chunk in agent.run_stream(query):
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print("\n")


async def main() -> None:
    print("=== Basic Azure AI Chat Client Agent Example ===")
    mode = input("Choose mode (1: Non-streaming, 2: Streaming, 3: Both): ").strip()
    if mode == "1":
        await non_streaming_example()
    elif mode == "2":
        await streaming_example()
    elif mode == "3":
        await non_streaming_example()
        await streaming_example()


if __name__ == "__main__":
    asyncio.run(main())