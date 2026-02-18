"""
Script to check current roles and assign Azure AI Developer role for Lesson 5 RAG.
"""
import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.machinelearningservices import MachineLearningServicesMgmtClient
from dotenv import load_dotenv

load_dotenv()

credential = DefaultAzureCredential()

# Extract subscription ID and resource group from project endpoint
project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
print(f"Project endpoint: {project_endpoint}")

# You'll need to set these based on your Azure resources
subscription_id = input("Enter your Azure subscription ID: ")
resource_group = input("Enter your resource group name (e.g., rg-chadtoneyfoundryhub): ")
project_name = input("Enter your AI Foundry project name (e.g., proj-default): ")

# Get the project resource ID
ml_client = MachineLearningServicesMgmtClient(credential, subscription_id)
workspace = ml_client.workspaces.get(resource_group, project_name)
project_id = workspace.id

print(f"\n✓ Found project: {project_name}")
print(f"  Resource ID: {project_id}")

# Get authorization client
auth_client = AuthorizationManagementClient(credential, subscription_id)

# Get current user's object ID
from azure.graphrbac import GraphRbacManagementClient
from azure.graphrbac.models import GraphErrorException
try:
    # Try to get user info
    import subprocess
    import json
    result = subprocess.run(
        ["powershell", "-Command", 
         "(Get-AzAccessToken -ResourceUrl 'https://graph.microsoft.com').UserId"],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        user_id = result.stdout.strip()
        print(f"\n✓ Your user ID: {user_id}")
    else:
        user_id = input("\nEnter your user object ID (from Azure Portal > Entra ID > Users): ")
except:
    user_id = input("\nEnter your user object ID (from Azure Portal > Entra ID > Users): ")

# Check current role assignments on this project
print(f"\n📋 Current role assignments on project:")
filter_str = f"principalId eq '{user_id}'"
assignments = list(auth_client.role_assignments.list_for_scope(
    scope=project_id,
    filter=filter_str
))

if assignments:
    for assignment in assignments:
        role_def = auth_client.role_definitions.get_by_id(assignment.role_definition_id)
        print(f"  - {role_def.role_name}")
else:
    print("  (No role assignments found)")

# Check if Azure AI Developer role is assigned
has_ai_developer = any(
    "Azure AI Developer" in auth_client.role_definitions.get_by_id(a.role_definition_id).role_name
    for a in assignments
)

if has_ai_developer:
    print(f"\n✅ You already have 'Azure AI Developer' role on this project!")
else:
    print(f"\n⚠️  'Azure AI Developer' role not found.")
    assign = input("Do you want to assign it now? (y/n): ")
    
    if assign.lower() == 'y':
        # Get Azure AI Developer role definition ID
        role_name = "Azure AI Developer"
        role_defs = list(auth_client.role_definitions.list(
            scope=project_id,
            filter=f"roleName eq '{role_name}'"
        ))
        
        if role_defs:
            role_def_id = role_defs[0].id
            
            # Create role assignment
            import uuid
            from azure.mgmt.authorization.models import RoleAssignmentCreateParameters
            
            assignment_params = RoleAssignmentCreateParameters(
                role_definition_id=role_def_id,
                principal_id=user_id,
                principal_type="User"
            )
            
            assignment_name = str(uuid.uuid4())
            
            try:
                assignment = auth_client.role_assignments.create(
                    scope=project_id,
                    role_assignment_name=assignment_name,
                    parameters=assignment_params
                )
                print(f"\n✅ Successfully assigned 'Azure AI Developer' role!")
                print(f"   Wait 5-10 minutes for the role to propagate, then re-run the notebook.")
            except Exception as e:
                print(f"\n❌ Failed to assign role: {e}")
                print(f"\nPlease assign via Azure Portal:")
                print(f"1. Go to https://ai.azure.com")
                print(f"2. Select project: {project_name}")
                print(f"3. Settings → Permissions → Add member")
                print(f"4. Select role: Azure AI Developer")
        else:
            print(f"❌ Role definition not found for '{role_name}'")
