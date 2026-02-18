# Monitoring AI Agents

Welcome to Lesson 14: Monitoring AI Agents!

## What You'll Learn

This lesson teaches you how to monitor and observe AI agents in production using Azure Application Insights and Azure AI Foundry monitoring tools.

- How to set up Application Insights for agent monitoring
- How to track agent performance and behavior
- How to debug issues using observability tools
- How to implement OpenTelemetry tracing for custom workflows

## Why Monitoring Matters

Production AI agents require careful monitoring to:

- **Track Performance**: Understand latency, token usage, and costs
- **Debug Issues**: Identify and fix problems quickly
- **Improve Quality**: Analyze agent behavior and optimize responses
- **Ensure Reliability**: Detect anomalies and maintain uptime

## Contents

This directory contains:

- **workshop_excercises/**: Hands-on exercises for agent monitoring
  - `14-foundry-agent-monitor.ipynb`: Basic agent monitoring with Application Insights
  - `14-foundry-sequential-portal-monitor.ipynb`: Sequential workflow monitoring via portal
  - `14-foundry-sequential-code-monitor.ipynb`: Sequential workflow monitoring with custom code
- **solutions/**: Reference solutions for workshop exercises

## Prerequisites

Before starting this lesson:

1. Complete the [Course Setup](../00-course-setup/README.md)
2. Have an Azure AI Foundry project configured
3. Basic understanding of AI agents (Lessons 1-10 recommended)
4. Azure subscription with Application Insights access

## Getting Started

1. **Start with Basic Monitoring**: Open `14-foundry-agent-monitor.ipynb`
   - Learn how to connect Application Insights to your AI project
   - Run your first monitored agent
   - View telemetry data in the Azure portal

2. **Explore Sequential Workflows**: Try the sequential monitoring notebooks
   - Learn how to monitor multi-step agent workflows
   - Implement custom tracing with OpenTelemetry
   - Analyze complex agent interactions

3. **Check Solutions**: Reference the `solutions/` directory for complete examples

## Key Concepts

- **Application Insights**: Azure's monitoring service for tracking agent telemetry
- **OpenTelemetry**: Industry-standard observability framework for custom tracing
- **Spans and Traces**: Core concepts for understanding agent execution flow
- **Agent Dashboard**: Azure AI Foundry's built-in monitoring interface

## Additional Resources

### Documentation
- [Azure Application Insights Documentation](https://learn.microsoft.com/azure/azure-monitor/app/app-insights-overview) - Complete monitoring reference
- [Azure AI Foundry Monitoring Guide](https://learn.microsoft.com/azure/ai-foundry/observability/how-to/how-to-monitor-agents-dashboard) - Agent-specific monitoring
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/) - Industry-standard observability
- [Azure Monitor Overview](https://learn.microsoft.com/azure/azure-monitor/) - Platform monitoring capabilities

## Conclusion

Congratulations on completing the Monitoring AI Agents module! You've acquired critical skills for deploying and maintaining production-ready AI agents.

**What You've Accomplished:**

- **Production Observability**: You now know how to set up comprehensive monitoring for AI agents using Application Insights, giving you visibility into agent performance, costs, and behavior.

- **Debugging Capabilities**: You've learned how to use telemetry data and traces to quickly identify and resolve issues in your agent systems, reducing downtime and improving reliability.

- **Custom Tracing**: With OpenTelemetry, you can implement sophisticated monitoring for complex multi-step workflows, giving you fine-grained control over what you observe.

- **Performance Optimization**: You have the tools to analyze agent behavior, identify bottlenecks, and optimize for better performance and cost efficiency.
