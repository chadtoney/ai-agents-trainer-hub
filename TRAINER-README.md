# AI Agents Training - Trainer Collaboration Hub

**👥 Trainer Team (12 Total)**

This is a private fork for the trainer team delivering the 3-day AI Agents training event.

## Quick Links

- **Original Repo:** [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)
- **Our Fork:** [chadtoney/ai-agents-trainer-hub](https://github.com/chadtoney/ai-agents-trainer-hub)
- **Discord:** https://aka.ms/ai-agents/discord
- **Azure AI Foundry:** https://ai.azure.com

---

## 🎯 Purpose of This Fork

This fork serves as a **trainer collaboration space** to:

1. **Share Azure-specific configurations** (all notebooks converted to Azure OpenAI)
2. **Document common issues** encountered during prep and training
3. **Coordinate lesson delivery** across 12 trainers
4. **Share best practices** for demos, labs, and troubleshooting
5. **Track trainer-specific resources** not suitable for upstream repo

---

## 👥 Trainer Assignments

**Event:** RockstarAI Presenters - February 2025  
**Entra ID Group:** `RockstarAIPresentersFeb2025` (all 12 trainers)  
**Azure RBAC Role:** Cognitive Services OpenAI User (assigned to group by David Yu)

| Trainer | Email | Assigned Lessons |
|---------|-------|------------------|
| Brian Zoucha | brian.zoucha@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Cameron Jackson | cameron.jackson@MngEnvMCAP295748.onmicrosoft.com | TBD |
| **Chad Toney** | chad.toney@MngEnvMCAP295748.onmicrosoft.com | **12 (Context), 13 (Memory)** |
| David Yu | TBD | TBD |
| John Spinella | john.spinella@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Kesha Brooks | kesha.brooks@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Narasimhan Kidambi | kidambi@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Paul Cho | paul.cho@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Phillip Bracher | phillip.bracher@MngEnvMCAP295748.onmicrosoft.com | TBD |
| Seth Brandes | seth.brandes@MngEnvMCAP295748.onmicrosoft.com | TBD |
| +2 more | TBD | TBD |

> **Note:** Update lesson assignments as they're confirmed

---

## 🚀 Azure-First Setup (Trainer Path)

### Prerequisites

- **Python 3.12+** (3.13.5 recommended)
- **Azure Subscription** with permissions to create:
  - Cognitive Services / Azure OpenAI
  - Azure AI Foundry Hub & Project
  - Azure AI Search (for Lessons 5, 13)
- **Azure PowerShell** or Azure CLI

### Step 1: Clone This Fork

```powershell
git clone https://github.com/chadtoney/ai-agents-trainer-hub.git
cd ai-agents-trainer-hub
```

### Step 2: Python Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Step 3: Azure Resources

**Required Resources:**

1. **Azure OpenAI Service**
   - Deploy `gpt-4o-mini` (or `gpt-4o`)
   - Note: Endpoint, Deployment Name, API Version

2. **Azure AI Foundry Hub & Project**
   - Create at https://ai.azure.com
   - Note: Project Endpoint

3. **Azure AI Search** (Lessons 5, 13)
   - Create search service
   - Note: Endpoint, API Key

### Step 4: Environment Variables

Copy `.env.trainer.template` to `.env`:

```powershell
Copy-Item .env.trainer.template .env
```

Edit `.env` with your Azure resource details:

```env
# Azure OpenAI
AZURE_OPENAI_ENDPOINT="https://YOUR-RESOURCE.cognitiveservices.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o-mini"
AZURE_OPENAI_API_VERSION="2025-01-01-preview"

# Azure AI Foundry
PROJECT_ENDPOINT="https://YOUR-PROJECT.cognitiveservices.azure.com/"

# Azure Search (for Lessons 5, 13)
AZURE_SEARCH_SERVICE_ENDPOINT="https://YOUR-SEARCH.search.windows.net"
AZURE_SEARCH_API_KEY="YOUR-SEARCH-KEY"
```

### Step 5: Azure Authentication

**All notebooks use Microsoft Entra ID (keyless auth):**

```python
from azure.identity import InteractiveBrowserCredential
credential = InteractiveBrowserCredential()
```

**Required Azure RBAC Role:**
- **"Cognitive Services OpenAI User"** on your Azure OpenAI resource

**If you get 403 errors**, see [TROUBLESHOOTING-AZURE.md](./TROUBLESHOOTING-AZURE.md)

---

## 📁 Trainer-Specific Files

| File | Purpose |
|------|---------|
| `TRAINER-README.md` | This file - trainer collaboration guide |
| `TROUBLESHOOTING-AZURE.md` | Azure permission issues, PIM, RBAC |
| `TRAINING-NOTES-CHAD.md` | Chad's lesson prep (Lessons 12 & 13) |
| `.env.trainer.template` | Azure-only environment template |
| `trainer-resources/` | Shared demos, scripts, backup materials |

---

## 🔧 Common Trainer Issues

### Issue: 403 AuthenticationTypeDisabled

**Cause:** Missing "Cognitive Services OpenAI User" role

**Fix:** See [TROUBLESHOOTING-AZURE.md](./TROUBLESHOOTING-AZURE.md#rbac-permissions)

### Issue: PIM Role Assignment Not Working

**Cause:** Entra ID roles ≠ Azure RBAC roles

**Fix:** Contact David Yu for Azure RBAC role assignment

### Issue: Notebooks Still Use GitHub Models

**Status:** Chad is converting all notebooks to Azure OpenAI. Check back or help convert!

---

## 🤝 Collaboration Guidelines

### Adding Your Prep Notes

Create `TRAINING-NOTES-[YOURNAME].md` with your lesson prep:

```powershell
Copy-Item TRAINING-NOTES-CHAD.md TRAINING-NOTES-YOURNAME.md
# Edit with your assigned lessons
```

### Sharing Demos or Scripts

Add to `trainer-resources/lesson-XX/`:

```powershell
mkdir trainer-resources\lesson-12
# Add your backup demos, slides, etc.
```

### Reporting Issues

Use GitHub Issues on this fork:
- Tag with `[Trainer]` prefix
- Document Azure-specific problems
- Share workarounds

### Syncing from Upstream

To get latest updates from microsoft/ai-agents-for-beginners:

```powershell
git remote add upstream https://github.com/microsoft/ai-agents-for-beginners.git
git fetch upstream
git merge upstream/main
```

---

## 📚 Training Event Structure

### Day 1: Foundation (Lessons 1-5)
- Lesson 01: Intro to AI Agents
- Lesson 02: Explore Agentic Frameworks
- Lesson 03: Agentic Design Patterns
- Lesson 04: Tool Use
- Lesson 05: Agentic RAG

### Day 2: Advanced (Lessons 6-11)
- Lesson 06: Building Trustworthy Agents
- Lesson 07: Planning Design
- Lesson 08: Multi-Agent
- Lesson 09: Metacognition
- Lesson 10: AI Agents in Production
- Lesson 11: Agentic Protocols

### Day 3: Production + Hackathon (Lessons 12-14)
- Lesson 12: Context Engineering **(Chad)**
- Lesson 13: Agent Memory **(Chad)**
- Lesson 14: Microsoft Agent Framework
- **Hackathon:** Guide teams, provide support

---

## 📝 Trainer Expectations

### Before Event
- [ ] Complete VBD accreditation for assigned lessons
- [ ] Test all code samples for assigned lessons
- [ ] Review lessons 1-11 for context
- [ ] Prepare backup demos (in case of failures)
- [ ] Join trainer Discord channel

### During Event
- **When presenting:** Deliver lessons, demos, Q&A
- **When not presenting:** 1:1 student support, troubleshooting
- **Hackathon:** Guide assigned team, provide technical support

---

## 🎯 Next Steps for New Trainers

1. **Clone this fork** and set up Python environment
2. **Create Azure resources** (OpenAI, Foundry, Search)
3. **Configure `.env`** with your resource details
4. **Test Lesson 1 notebook** to validate setup
5. **Create your training notes** (`TRAINING-NOTES-[YOURNAME].md`)
6. **Review assigned lessons** and test code samples
7. **Share issues/learnings** via GitHub Issues

---

## 📞 Contact & Support

- **Fork Owner:** Chad Toney (chad.toney@MngEnvMCAP295748.onmicrosoft.com)
- **Tenant Admin:** David Yu (for Azure permission issues)
- **General Questions:** Use Discord or GitHub Issues on this fork

---

**Last Updated:** January 6, 2026  
**Next Trainer Sync:** TBD
