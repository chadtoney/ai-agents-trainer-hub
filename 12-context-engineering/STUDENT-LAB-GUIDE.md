# Lesson 12: Context Engineering - Student Lab Guide

**Duration:** 15-30 minutes  
**Prerequisites:** Completed Lesson 7 (Travel Planning Agent)

---

## 🎯 Lab Objectives

By the end of this lab, you will:
- ✅ Understand context engineering vs prompt engineering
- ✅ Implement agent scratchpad for persistent memory
- ✅ Test memory persistence across conversations
- ✅ Observe context management in action

---

## 📋 Before You Begin

**You need:**
- [ ] Azure AI Foundry access ([https://ai.azure.com](https://ai.azure.com))
- [ ] "Azure AI User" role assigned to your AI Foundry project
- [ ] Travel Planning Agent from Lesson 7 (or any agent)
- [ ] Text editor (VS Code, Notepad, etc.)

**If you don't have the Travel Agent from Lesson 7:**
- You can create a new basic agent
- Or ask your instructor for a starter agent

---

## 🚀 Task 1: Enable File Search Tool (3 min)

### Steps:

1. **Navigate to your agent:**
   - Go to [https://ai.azure.com](https://ai.azure.com)
   - Select **Build** → **Projects** → Your project
   - Click **Agents** → Select your **Travel Planning Agent**

2. **Add File Search tool:**
   - Scroll to **Tools** section
   - Click **"+ Add"** or **"Add Tool"**
   - Select **"File Search"**
   - Enable the tool
   - Click **"Save"**

### ✅ Success Check:
- You should see "File Search" listed as an enabled tool

### ❓ Troubleshooting:
- **Can't find File Search?** Ask instructor to verify your permissions
- **Tool grayed out?** Make sure you saved the agent first

---

## 📝 Task 2: Create Scratchpad File (5 min)

### Steps:

1. **Open your text editor** (VS Code, Notepad, etc.)

2. **Create a new file** named `vacation_scratchpad.md`

3. **Copy this template:**

```markdown
# Vacation Planning Agent Scratchpad

## User Preferences
<!-- Agent will record user preferences here -->
<!-- Examples: Budget, destinations, activities, travel dates, dietary restrictions -->

## Completed Tasks  
<!-- Agent logs finished work here with timestamps -->
<!-- Format: - [YYYY-MM-DD] Description of completed task -->

## Notes
<!-- Agent's working notes and observations -->
<!-- Context that doesn't fit other categories -->
```

4. **Save the file** to your Desktop or Documents folder (remember where!)

### ✅ Success Check:
- File saved as `vacation_scratchpad.md`
- Contains all 3 sections (Preferences, Tasks, Notes)

### 💡 Why Markdown?
Markdown is:
- ✅ Human-readable (you can check what the agent wrote)
- ✅ Structured (sections and bullet points)
- ✅ Easy for LLMs to parse and update

---

## 📤 Task 3: Upload Scratchpad to Agent (3 min)

### Steps:

1. **In your agent's interface**, find the **Files** or **Knowledge** section
   - May also be called "Vector Store" or "File Search" depending on UI

2. **Click "Upload"** or "Add File"

3. **Select your** `vacation_scratchpad.md` file

4. **Wait for upload** (usually 5-10 seconds)

5. **Verify** the file appears in your file list

### ✅ Success Check:
- File shows as uploaded in the agent's knowledge base
- No error messages

### ❓ Troubleshooting:
- **Upload fails?** Check file size (should be < 1 MB), file format (should be .md)
- **Can't find upload button?** Look for "Knowledge Base", "Files", or "Documents" tab

---

## 🛠️ Task 4: Update Agent Instructions (7 min)

### Steps:

1. **Find your agent's System Instructions** (usually labeled "Instructions" or "System Prompt")

2. **Click "Edit"**

3. **Add the following to the BEGINNING** of your existing instructions:

```
SCRATCHPAD MANAGEMENT (CRITICAL - READ THIS FIRST):

1. At the START of EVERY conversation, read the vacation_scratchpad.md file
2. When the user mentions preferences (budget, destinations, activities, dates):
   - ADD them to the "User Preferences" section
   - Use bullet format: "- Budget: $3000 per person for 7 days"
3. When you COMPLETE a task (create itinerary, find flights, research hotels):
   - ADD it to the "Completed Tasks" section with today's date
   - Format: "- [2026-02-15] Created detailed 7-day Bali beach itinerary"
4. BEFORE making recommendations:
   - CHECK the scratchpad for existing preferences
   - PERSONALIZE your response based on what the user told you before

SCRATCHPAD UPDATE EXAMPLES:

User says: "I love beach destinations with warm weather"
→ You add: "- Destination preference: Beach destinations, warm/tropical climate"

User says: "My budget is around $3000 per person for a week-long trip"
→ You add: "- Budget: $3000 per person for 7-day vacation"

You create an itinerary for the user:
→ You add: "- [2026-02-15] Created 7-day Bali itinerary including snorkeling, beach resorts, and temple visits"

Be PROACTIVE about checking and updating the scratchpad!
```

4. **Keep your existing Travel Agent instructions below this**

5. **Click "Save"**

### ✅ Success Check:
- Instructions saved without errors
- Scratchpad management section is at the TOP

### 💡 Why so specific?
Large Language Models need **explicit instructions**. Words like "CRITICAL", "FIRST", "EVERY" emphasize importance. Examples show the agent exactly what format to use.

---

## 🧪 Task 5: Test - First Conversation (5 min)

### Steps:

1. **Start a NEW conversation** in the Playground (click "New Chat" or "+" button)

2. **Have this conversation:**

**You:** "Hi! I'm planning a vacation. Can you help?"

**Expected:** Agent should acknowledge and ask about your preferences

---

**You:** "I love beach destinations with warm weather, and my budget is around $3000 per person for a week-long trip."

**Expected:** Agent should:
- Acknowledge your preferences
- May say something like "I'll make note of that" or "I'm recording your preferences"
- Ask follow-up questions

---

**You:** "Great! Can you create a detailed itinerary for Bali, Indonesia?"

**Expected:** Agent should:
- Create a detailed Bali itinerary
- Use your budget constraint ($3000)
- Focus on beach activities (since you love beaches)
- May mention adding the task to completed list

---

### ✅ Success Check:
- Agent asked relevant questions
- Agent created personalized itinerary based on your budget and beach preference
- You see tool use indicators (File Search being used)

### 💡 What's happening behind the scenes?
- Agent reads scratchpad at conversation start
- Agent updates scratchpad with your preferences
- Agent checks scratchpad before responding
- Agent records completed task (itinerary creation)

---

## 📥 Task 6: Download and Inspect Scratchpad (3 min)

### Steps:

1. **Go back to your agent's configuration page**

2. **Find the Files/Knowledge section**

3. **Download** the `vacation_scratchpad.md` file

4. **Open it in your text editor**

5. **Check the contents:**
   - **User Preferences** section should have:
     - Your beach destination preference
     - Your $3000 budget
   - **Completed Tasks** section should have:
     - Entry about creating Bali itinerary with today's date
   - **Notes** section may have additional context

### ✅ Success Check:
- Scratchpad contains data from your conversation
- Preferences are formatted as bullet points
- Tasks have timestamps

### 🎉 Celebrate!
If you see your data in the scratchpad, **you've successfully implemented context engineering!**

### ❓ If scratchpad is empty:
- Agent may not have updated it (File Search is read-only in some configurations)
- Check if agent mentioned "making note" during conversation
- Ask instructor - this is a known limitation of GUI-only approach
- Full writeable scratchpad requires code (see Python notebook)

---

## 🔄 Task 7: Test Persistence - Second Conversation (5 min)

**This is where the magic happens!**

### Steps:

1. **Start a BRAND NEW conversation** (click "New Chat" or "+")
   - This simulates a user coming back tomorrow
   - The agent should have NO context from your previous chat

2. **Ask:** "Hi! Can you help me plan a trip?"

### 🎯 Expected Behavior:

The agent should:
- ✅ Check the scratchpad (you may see File Search tool indicator)
- ✅ **Remember your preferences** from the previous conversation
- ✅ Say something like:
  > "Of course! I see you prefer beach destinations with warm weather and have a budget of $3000 per person for a week. Would you like to continue planning your Bali trip, or explore other beach destinations?"

### ✅ Success Check:
- **Agent mentions your budget ✓**
- **Agent mentions your beach preference ✓**
- **Agent references Bali from previous conversation ✓**

### 🎉 If this worked - YOU DID IT!

**This proves:**
- Memory persists across different conversations
- Scratchpad acts as long-term context storage
- Agent can retrieve and use past information

### ❓ If agent doesn't remember:

**Debugging checklist:**
1. Is File Search enabled? (Check tools section)
2. Is scratchpad file uploaded? (Check files section)
3. Do instructions say to "read vacation_scratchpad.md at START of conversation"?
4. Try asking directly: "Can you read the vacation_scratchpad.md file and tell me what it says?"

**If still stuck:** Ask instructor for help!

---

## 🏆 Task 8 (Optional): Test Context Clash (10 min)

**For advanced students who finish early**

### Objective:
Create a **Context Clash** scenario (conflicting preferences) and see how the agent handles it.

### Steps:

1. **In the SAME conversation**, tell the agent:

**You:** "I want budget hotels under $100 per night."

**Expected:** Agent acknowledges

---

2. **A few messages later, contradict yourself:**

**You:** "Actually, for this trip I want luxury 5-star resorts with ocean views."

**Expected:** Agent should recognize the change

---

3. **Now test the agent:**

**You:** "Based on my preferences, recommend a hotel in Bali."

### 🤔 Observe:
- Does agent use budget or luxury preference?
- Does agent ask which one you want?
- Does agent update scratchpad to override old preference?

4. **Download scratchpad again**
   - Which preference is saved?
   - Did agent mark old preference as outdated?

### 💡 Experiment:
Modify your agent instructions to handle conflicts better:

**Add this to instructions:**
```
HANDLING CONFLICTING PREFERENCES:
- When user changes their mind, UPDATE the scratchpad
- Mark old preference as "OUTDATED" or "REPLACED"
- Always use the LATEST preference
- Confirm with user: "I've updated your preference from [old] to [new]"
```

**Re-test** and see if agent handles conflicts better!

---

## 🎓 What You Learned

### Concepts Applied:

1. **Persistent Memory**: Information stored beyond a single conversation
2. **Context Retrieval**: Agent reads scratchpad before responding
3. **Context Writing**: Agent updates scratchpad with new info
4. **Task Tracking**: Completed work is recorded
5. **Personalization**: Agent tailors responses to user preferences

### Context Engineering vs Prompt Engineering:

| Aspect | Prompt Engineering | Context Engineering |
|--------|-------------------|---------------------|
| **Focus** | Static rules | Dynamic information |
| **Scope** | Single conversation | Multiple sessions |
| **Example** | "You are a travel agent" | "User prefers beaches, budget $3K" |

### Real-World Use Cases:

This pattern works for:
- ✅ Customer support agents (remember past issues)
- ✅ Personal assistants (learn user preferences)
- ✅ Research assistants (track findings across sessions)
- ✅ Project management agents (remember task status)

---

## 🚀 Next Steps

### Want to go deeper?

1. **Try the Python implementation:**
   - Open [12-python-agent-framework.ipynb](./code_samples/12-python-agent-framework.ipynb)
   - Same concepts, but with full programmatic control
   - Writeable scratchpad + unlimited customization

2. **Move to Lesson 13 (Agent Memory):**
   - Replace file-based scratchpad with **Cosmos DB**
   - Add **vector search** over memories
   - Implement **semantic retrieval** (find relevant memories automatically)
   - Build **conversation summarization** for long-term memory

3. **Join the community:**
   - [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)
   - Ask questions, share your scratchpad implementations
   - Attend office hours for advanced topics

---

## 📚 Additional Resources

**Microsoft Documentation:**
- [File Search Tool Guide](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools-classic/file-search)
- [Azure AI Agents Quickstart](https://learn.microsoft.com/azure/ai-foundry/agents/quickstart)
- [Context Best Practices](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai)

**Lesson Materials:**
- [README.md](./README.md) - Full theory on context engineering
- [azure-ai-foundry-context-engineering.md](./azure-ai-foundry-context-engineering.md) - Detailed GUI guide
- [12-python-agent-framework.ipynb](./code_samples/12-python-agent-framework.ipynb) - Code implementation

---

## ✅ Lab Completion Checklist

Before you leave, make sure you:

- [ ] Enabled File Search tool on your agent
- [ ] Created and uploaded `vacation_scratchpad.md`
- [ ] Updated agent instructions with scratchpad management
- [ ] Tested first conversation (gave preferences, got itinerary)
- [ ] Downloaded scratchpad and verified it contains data
- [ ] Tested second conversation (new chat remembered you)
- [ ] Understand difference between context and prompt engineering
- [ ] Know how to troubleshoot scratchpad issues

---

## 🆘 Need Help?

**During lab:**
- Raise your hand
- Ask your neighbor
- Check the troubleshooting sections above

**After class:**
- Post in [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)
- Review the instructor's demo recording (if available)
- Check the detailed [azure-ai-foundry-context-engineering.md](./azure-ai-foundry-context-engineering.md) guide

---

**🎉 Congratulations on completing Lesson 12!**

You now understand how to build agents that **remember, learn, and personalize** interactions across conversations. This is a foundational skill for production AI systems!

**Next:** Lesson 13 - Agent Memory (database-backed memory + vector search)
