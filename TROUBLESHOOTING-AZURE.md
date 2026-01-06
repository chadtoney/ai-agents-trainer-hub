# Azure Troubleshooting Guide for Trainers

This guide documents Azure-specific issues encountered during trainer prep and how to resolve them.

---

## 🔐 RBAC Permissions

### Issue: `403 - AuthenticationTypeDisabled`

**Full Error:**
```
Error code: 403 - {'error': {'code': 'AuthenticationTypeDisabled', 'message': 'Key based authentication is disabled for this resource.'}}
```

**Root Cause:**  
Your Azure OpenAI resource has key-based authentication disabled by policy. You must use Microsoft Entra ID (formerly Azure AD) authentication.

**Solution:**

1. **Use InteractiveBrowserCredential** in notebooks:
   ```python
   from azure.identity import InteractiveBrowserCredential
   from agent_framework.azure import AzureOpenAIChatClient
   
   credential = InteractiveBrowserCredential()
   openai_chat_client = AzureOpenAIChatClient(
       azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
       credential=credential,  # Pass credential directly
       azure_deployment=os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"),
       api_version=os.environ.get("AZURE_OPENAI_API_VERSION")
   )
   ```

2. **Ensure you have the required role:**  
   You need **"Cognitive Services OpenAI User"** role assigned on your Azure OpenAI resource.

3. **⚠️ CRITICAL: Remove AZURE_OPENAI_API_KEY from environment**  
   If `AZURE_OPENAI_API_KEY` is set in your `.env` file, the SDK will prefer API key authentication over Microsoft Entra ID, causing the 403 error.
   
   **Fix:**
   - Remove `AZURE_OPENAI_API_KEY` from your `.env` file
   - Restart your Jupyter kernel
   - Recreate the `AzureOpenAIChatClient` instance
   
   **Verify:**
   ```python
   import os
   print(f"API Key set: {os.environ.get('AZURE_OPENAI_API_KEY') is not None}")
   # Should print: API Key set: False
   ```

---

### Issue: `401 - PermissionDenied`

**Full Error:**
```
Error code: 401 - {'error': {'code': 'PermissionDenied', 'message': 'The principal lacks the required data action Microsoft.CognitiveServices/accounts/OpenAI/deployments/chat/completions/action'}}
```

**Root Cause:**  
You're successfully authenticating (getting a token), but you don't have the Azure RBAC role required to call the OpenAI API.

**Solution:**

**Option 1: Request Direct Role Assignment (Recommended)**

Contact David Yu (tenant admin) to assign the role.

**✅ Solution Used for February 2025 Training:**

David Yu assigned "Cognitive Services OpenAI User" role to the entire trainer group **RockstarAIPresentersFeb2025**, which includes all 12 trainers. This is the recommended approach for training events.

```powershell
# Command David Yu used (group-based assignment):
$groupObjectId = (Get-AzADGroup -DisplayName "RockstarAIPresentersFeb2025").Id
$resourceGroup = "your-resource-group"
$accountName = "your-openai-account"

$cognitiveAccount = Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $accountName

New-AzRoleAssignment `
    -ObjectId $groupObjectId `
    -RoleDefinitionName "Cognitive Services OpenAI User" `
    -Scope $cognitiveAccount.Id
```

**Alternative (individual user assignment):**
```powershell
$userEmail = "your.email@MngEnvMCAP295748.onmicrosoft.com"
$resourceGroup = "your-resource-group"
$accountName = "your-openai-account"

$cognitiveAccount = Get-AzCognitiveServicesAccount -ResourceGroupName $resourceGroup -Name $accountName

New-AzRoleAssignment `
    -SignInName $userEmail `
    -RoleDefinitionName "Cognitive Services OpenAI User" `
    -Scope $cognitiveAccount.Id
```

**Option 2: Self-Service via PIM (If Enabled)**

If David Yu has enabled PIM (Privileged Identity Management):

1. Go to **Azure Portal** → **PIM**
2. Navigate to **My Roles** → **Azure Resources**
3. Find **Owner** or **User Access Administrator** role
4. Click **Activate** (may require approval)
5. Once active, assign yourself "Cognitive Services OpenAI User":
   ```powershell
   New-AzRoleAssignment `
       -SignInName "your.email@MngEnvMCAP295748.onmicrosoft.com" `
       -RoleDefinitionName "Cognitive Services OpenAI User" `
       -Scope "/subscriptions/SUB-ID/resourceGroups/RG-NAME/providers/Microsoft.CognitiveServices/accounts/ACCOUNT-NAME"
   ```

**Important:** Wait 5-10 minutes after role assignment for Azure RBAC propagation.

---

### Issue: PIM Role Activation Not Working

**Symptoms:**
- You activated a PIM role (like "User Administrator")
- Role assignment commands still return `Forbidden` error

**Root Cause:**  
**Entra ID roles** (like User Administrator) ≠ **Azure RBAC roles** (like Owner, Contributor)

- **Entra ID roles** manage users, groups, applications
- **Azure RBAC roles** manage Azure resources

**Solution:**  
You need an **Azure RBAC role** on the resource, not an Entra ID role:

- **"Owner"** (full access + role assignment)
- **"User Access Administrator"** (can assign roles)
- **"Cognitive Services OpenAI User"** (minimum required)

Contact David Yu to assign an Azure RBAC role.

---

## 🔍 Verifying Your Setup

### Check Azure Connectivity

```powershell
# Connect to Azure
Connect-AzAccount -UseDeviceAuthentication

# List your subscriptions
Get-AzSubscription

# Check role assignments
Get-AzRoleAssignment -SignInName "your.email@MngEnvMCAP295748.onmicrosoft.com" | 
    Select-Object RoleDefinitionName, Scope | 
    Format-Table -AutoSize
```

### Test Azure OpenAI Access

```python
from azure.identity import InteractiveBrowserCredential
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print('Testing Azure OpenAI connection...')
credential = InteractiveBrowserCredential()
token = credential.get_token('https://cognitiveservices.azure.com/.default').token
print('✓ Token obtained')

client = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION'),
    azure_ad_token=token
)

try:
    response = client.chat.completions.create(
        model=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME'),
        messages=[{'role': 'user', 'content': 'Say hello'}],
        max_tokens=10
    )
    print('✓ SUCCESS! Azure OpenAI is working!')
    print(f'Response: {response.choices[0].message.content}')
except Exception as e:
    print(f'✗ FAILED: {e}')
```

---

## 🛠️ Azure CLI Issues

### Issue: Azure CLI DLL Import Errors

**Error:**
```
ImportError: DLL load failed while importing win32file
```

**Solution:**  
Use **Azure PowerShell** instead:

```powershell
# Install Azure PowerShell (if not installed)
Install-Module -Name Az -Repository PSGallery -Force

# Connect to Azure
Connect-AzAccount -UseDeviceAuthentication
```

Azure PowerShell provides equivalent functionality and is more reliable on Windows.

---

## 🌐 Common Environment Issues

### Issue: Wrong API Version

**Symptoms:**
- API calls fail with version-related errors
- Deployments not found

**Solution:**  
Update `AZURE_OPENAI_API_VERSION` in `.env`:

```env
AZURE_OPENAI_API_VERSION="2025-01-01-preview"
```

Latest stable versions:
- `2025-01-01-preview` (recommended)
- `2024-12-01-preview`
- `2024-10-21`

### Issue: Deployment Name Mismatch

**Symptoms:**
- `DeploymentNotFound` errors

**Solution:**  
Verify deployment name matches exactly:

```powershell
# List deployments in your Azure OpenAI account
az cognitiveservices account deployment list \
    --name "your-openai-account" \
    --resource-group "your-resource-group"
```

Update `.env` with the exact deployment name:

```env
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"  # Must match exactly
```

---

## 📋 Pre-Training Checklist

Before the training event, verify:

- [ ] Azure OpenAI resource created and accessible
- [ ] `Cognitive Services OpenAI User` role assigned
- [ ] Authentication working (InteractiveBrowserCredential)
- [ ] `.env` configured with correct endpoints and deployment names
- [ ] Test notebook executes successfully (Lesson 1)
- [ ] Azure AI Search created (if teaching Lessons 5 or 13)
- [ ] Backup plan if Azure has issues (GitHub Models credentials)

---

## 🆘 Emergency Contacts

### Azure Permission Issues
- **David Yu** (tenant owner) - Can assign Azure RBAC roles

### Technical Support
- **Chad Toney** - chad.toney@MngEnvMCAP295748.onmicrosoft.com
- **Trainer Discord Channel** - For real-time help

### Microsoft Support
- **Azure Support Portal** - For Azure resource issues
- **Azure AI Discord** - https://aka.ms/ai-agents/discord

---

## 📚 Useful Documentation

- [Keyless Authentication with Azure AI](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=python%2Cazure-cli)
- [Azure RBAC Overview](https://learn.microsoft.com/azure/role-based-access-control/overview)
- [Azure OpenAI Service RBAC](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control)
- [Privileged Identity Management (PIM)](https://learn.microsoft.com/entra/id-governance/privileged-identity-management/)

---

**Last Updated:** January 6, 2026  
**Maintained by:** Chad Toney
