from azure.ai.projects import AIProjectClient
from azure.identity import AzureCliCredential

client = AIProjectClient(
    endpoint='https://dyufoundryai.services.ai.azure.com/api/projects/firstProject',
    credential=AzureCliCredential()
)

openai = client.get_openai_client()
print(f"OpenAI client type: {type(openai).__name__}")
print(f"Has beta: {hasattr(openai, 'beta')}")

if hasattr(openai, 'beta'):
    print(f"Beta attrs: {[x for x in dir(openai.beta) if not x.startswith('_')][:10]}")
    if hasattr(openai.beta, 'assistants'):
        print("Has assistants!")
        print(f"Assistants methods: {[x for x in dir(openai.beta.assistants) if not x.startswith('_')][:10]}")
