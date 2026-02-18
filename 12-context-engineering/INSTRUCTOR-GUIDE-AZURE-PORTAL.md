# Lesson 12: Context Engineering - Instructor Guide (Azure Portal)

**Instructor:** Chad Toney  
**Duration:** 45-60 minutes (30 min lecture + 15-30 min lab)  
**Prerequisites:** Students completed Lesson 7 (Travel Planning Agent)  
**Teaching Mode:** Azure UI First, Then Code (show both approaches)

---

## 📋 Pre-Class Checklist

### Your Preparation (Before Class)

- [ ] **Azure AI Foundry Portal** open: [https://ai.azure.com](https://ai.azure.com)
- [ ] **Travel Agent from Lesson 7** ready (or create demo agent)
- [ ] **Scratchpad file** prepared locally (`vacation_scratchpad.md`)
- [ ] **Browser tabs** ready:
  - Azure AI Foundry Portal
  - Lesson 12 README.md (for reference)
  - This instructor guide
- [ ] **Test run completed** (verify everything works in your environment)
- [ ] **Permissions confirmed**: Students have "Azure AI User" role assigned

### Student Prerequisites

- [ ] Completed Lesson 7 (have Travel Planning Agent created)
- [ ] Azure AI Foundry access ([https://ai.azure.com](https://ai.azure.com))
- [ ] "Azure AI User" RBAC role assigned to their AI Foundry project
- [ ] Basic text editor (VS Code, Notepad, etc.)

---

## 🎯 Learning Objectives

By the end of this class, students will be able to:

1. **Define** context engineering and how it differs from prompt engineering
2. **Identify** the 6 types of context (Instructions, Knowledge, Tools, History, Preferences, State)
3. **Implement** agent scratchpad pattern using Azure AI Foundry UI
4. **Recognize** and mitigate 4 common context failures (Poisoning, Distraction, Confusion, Clash)
5. **Design** context management strategies for production agents

---

## 📖 Lesson Flow (60 minutes)

### Part 1: Lecture - Context Engineering Fundamentals (15 min)

#### 1.1 What is Context Engineering? (5 min)

**Key Points to Cover:**

- **Context** = ALL information available to the agent at decision time
- **Context Window** = Limited token capacity (e.g., 128K tokens for GPT-4)
- **Context Engineering** = Art of managing what goes in the window

**Teaching Script:**

> "Think about planning a vacation. If I just say 'Book me a trip,' that's basic. But if I remember you prefer beaches, have a $3000 budget, love scuba diving, and already booked hotels in Bali - now I have CONTEXT. Context engineering is how we manage all that information so the agent makes smart decisions."

**Visual Aid:**
- Draw context window as a box
- Show items going in/out
- Emphasize it's DYNAMIC (changes over time)

#### 1.2 Prompt Engineering vs Context Engineering (3 min)

**Comparison Table** (show on screen):

| Aspect | Prompt Engineering | Context Engineering |
|--------|-------------------|---------------------|
| **Focus** | Static instructions | Dynamic information |
| **Scope** | Single interaction | Multiple sessions |
| **Goal** | Clear task rules | Right info at right time |
| **Example** | "You are a travel agent" | "User prefers beach + $3K budget" |

**Key Quote:**
> "Prompt engineering tells the agent WHAT to be. Context engineering gives it the information it NEEDS."

#### 1.3 Types of Context (5 min)

**The 6 Types** (use acronym **I-K-T-H-P-S**):

1. **Instructions** - System prompt, rules, few-shot examples
2. **Knowledge** - Facts, databases, RAG-retrieved docs
3. **Tools** - Function definitions, APIs, MCP servers
4. **History** - Conversation turns (grows large quickly!)
5. **Preferences** - User likes/dislikes learned over time
6. **State** - Runtime variables (current task, subtask status)

**Real Example - Travel Agent:**
- Instructions: "You're a travel planning assistant"
- Knowledge: Flight prices, hotel availability, reviews
- Tools: `book_flight()`, `search_hotels()`, `get_weather()`
- History: "User asked about Bali, then Tokyo, then beaches"
- Preferences: "User prefers direct flights, loves seafood"
- State: "Currently searching for flights, budget=$3000, dates=TBD"

**Ask Class:**
> "Which type of context takes up the MOST tokens over time?"  
> *(Answer: History - grows with every message!)*

#### 1.4 Common Context Failures (2 min - quick overview)

Briefly introduce the 4 failures (will demo later):

1. **Poisoning** - False info gets stuck in memory
2. **Distraction** - Too much history, loses focus
3. **Confusion** - Too many tools, poor choices
4. **Clash** - Conflicting preferences

> "We'll see these in action during the demo. Each has a specific mitigation strategy."

---

### Part 2: Azure Portal Demo - Scratchpad Implementation (20 min)

**💡 Teaching Philosophy:** Show UI first, explain WHAT they're seeing, THEN show code.

#### 2.1 Navigate to Azure AI Foundry (2 min)

**Demo Steps:**

1. **Open browser**: [https://ai.azure.com](https://ai.azure.com)
2. **Point out UI elements**:
   - "Build" tab (where agents live)
   - "Projects" (your resource container)
   - "Agents" section

**Teaching Points:**
- "This is Azure AI Foundry - your one-stop shop for building AI agents"
- "Think of Projects like resource groups - they hold all your AI stuff"

3. **Select your Travel Agent** (from Lesson 7)

**Ask Students:**
> "Can everyone see their Travel Agent from Lesson 7? Raise hand if yes."  
> *(Troubleshoot if needed)*

#### 2.2 Understand Current Agent State (3 min)

**Show students the existing agent configuration:**

1. **System Instructions**: Click to view existing prompt
2. **Tools** (if any): Show what's currently enabled
3. **Model**: Point out which deployment (e.g., gpt-4o-mini)

**Teaching Point:**
> "Right now, this agent has NO memory. If I start a new conversation, it forgets everything. Let's fix that with a scratchpad."

**Quick Test** (show in playground):
- Start conversation: "I love beaches and have a $3000 budget"
- Agent responds helpfully
- **Start NEW conversation**: "What do you know about me?"
- Agent says: "I don't have any information about you"

> "See? No persistence. That's the problem we're solving."

#### 2.3 Add File Search Tool (3 min)

**Demo Steps:**

1. **Scroll to "Tools" section** in agent configuration
2. **Click "+ Add"** (or "Add Tool")
3. **Select "File Search"**
4. **Enable it**
5. **Click "Save"**

**Explain While You Click:**
- "File Search lets the agent read uploaded files"
- "We'll use this to read our scratchpad"
- "Think of it like giving the agent a notebook to check"

**If Students Ask "Why File Search?"**
> "File Search uses RAG under the hood - it searches, retrieves, and adds relevant parts to context automatically."

#### 2.4 Create the Scratchpad File (4 min)

**Demo Steps:**

1. **Open text editor** (VS Code, Notepad, whatever you prefer)
2. **Create new file**: `vacation_scratchpad.md`
3. **Type this content** (explain as you type):

```markdown
# Vacation Planning Agent Scratchpad

## User Preferences
<!-- Agent will record what the user likes/needs here -->

## Completed Tasks
<!-- Agent logs finished work here -->

## Notes
<!-- Agent's working notes go here -->
```

**Explain Each Section:**
- **User Preferences**: "Budget, destinations, activities - the user's constraints"
- **Completed Tasks**: "What has the agent already done? Prevents duplication"
- **Notes**: "Agent's 'thinking space' - like rough draft notes"

4. **Save the file** to Desktop or known location

**Why Markdown?**
> "Markdown is human-readable AND structured. Agents parse it well. Plus, we can open it and check what the agent wrote!"

#### 2.5 Upload Scratchpad to Agent (2 min)

**Demo Steps:**

1. **In agent UI**, find **"Files"** or **"Knowledge"** section
   - *(May be called "Vector Store" or "File Search" depending on UI version)*
2. **Click "Upload"**
3. **Select** `vacation_scratchpad.md`
4. **Wait for processing** (usually 5-10 seconds)
5. **Verify** file appears in list

**Teaching Point:**
> "This file now lives in the agent's knowledge base. When we enabled File Search, the agent can now read this file during conversations."

#### 2.6 Update Agent Instructions to Use Scratchpad (6 min)

**This is the CRITICAL step** - take time here!

**Demo Steps:**

1. **Click "Edit" on System Instructions**
2. **Add this to the BEGINNING** of the existing instructions:

```
SCRATCHPAD MANAGEMENT (CRITICAL - DO THIS FIRST):
1. At the START of EVERY conversation, read vacation_scratchpad.md
2. When user mentions preferences (budget, dates, destinations, activities):
   - ADD them to the "User Preferences" section
   - Use bullet format: "- Budget: $3000 per person"
3. When you COMPLETE a task (create itinerary, find flights, etc.):
   - ADD it to "Completed Tasks" with timestamp
   - Format: "- [2026-02-15] Created 7-day Bali beach itinerary"
4. BEFORE making recommendations:
   - CHECK the scratchpad for existing preferences
   - PERSONALIZE responses based on what you learned

SCRATCHPAD UPDATE EXAMPLES:
User says: "I love beach destinations with warm weather"
→ Add: "- Destination preference: Beach destinations, warm weather"

User says: "Budget is $3000 per person for one week"
→ Add: "- Budget: $3000 per person for 7-day trip"

You create an itinerary:
→ Add: "- [2026-02-15] Created detailed Bali itinerary with snorkeling, beach resorts, and cultural sites"

Be PROACTIVE about checking and updating the scratchpad!
```

3. **Keep existing Travel Agent instructions below this**

**Explain While You Type:**
- "Notice the emphasis: CRITICAL, FIRST, EVERY - agents need explicit instructions"
- "We give EXAMPLES so the agent knows exactly what format to use"
- "Timestamps help track when things happened"

4. **Click "Save"**

**Ask Students:**
> "Why do we need to be SO explicit with instructions?"  
> *(Answer: LLMs are creative but not mind-readers - specificity matters)*

---

### Part 3: Live Testing - See Context in Action (10 min)

**This is where it gets exciting!**

#### 3.1 First Conversation - Check Scratchpad Works (5 min)

**Demo Conversation:**

1. **Start NEW conversation** in Playground

**You:** "Hi! I'm planning a vacation. Can you help?"

**Expected Agent Behavior:**
- Checks scratchpad (you might see tool use indicator)
- Responds: "I'd be happy to help! Can you tell me about your preferences?"

**You:** "I love beach destinations with warm weather, and my budget is around $3000 per person for a week-long trip."

**Expected Agent Behavior:**
- Acknowledges preferences
- *Ideally* says something like "I'll make note of that" (indicating scratchpad update)

**You:** "Great! Can you create a detailed itinerary for Bali?"

**Expected Agent Behavior:**
- Creates itinerary
- Should mention adding it to completed tasks

**Teaching Points During Demo:**
- **Point out tool use icons**: "See that? The agent is accessing File Search"
- **Highlight personalization**: "Notice how it remembered my budget"
- **Explain background work**: "The agent is updating the scratchpad now - we'll check it after"

#### 3.2 Download and Inspect Scratchpad (2 min)

**Demo Steps:**

1. **Go back to agent configuration**
2. **Find uploaded files**
3. **Download** `vacation_scratchpad.md`
4. **Open in text editor**

**Show Students:**
- Preferences section - should have beach, budget entries
- Completed Tasks - should have Bali itinerary entry with timestamp
- Notes - may have additional context

**Celebrate if it worked!**
> "Look at that! The agent IS taking notes! This is persistence in action."

**If it DIDN'T work:**
> "Sometimes agents need reminders. Let's make the instructions even more explicit..." (adjust instructions, retry)

#### 3.3 Second Conversation - Prove Persistence (3 min)

**This is the money shot!**

1. **Start BRAND NEW conversation** (hit "New Chat" or "+" button)

**You:** "Hi! Can you help me plan a trip?"

**Expected Agent Behavior:**
- Checks scratchpad
- Says something like: "Of course! I see you prefer beach destinations and have a budget of $3000 per person for a week. Would you like to continue planning your Bali trip, or explore other destinations?"

**Pause for effect. Let students see this.**

**Teaching Point:**
> "THIS is context engineering! Different conversation, but the agent REMEMBERS. The scratchpad persisted across sessions. That's what makes agents useful in production."

**Ask Class:**
> "How did the agent remember across conversations?"  
> *(Answer: Read the scratchpad file at the start - it's in the knowledge base)*

---

### Part 4: Code Alternative (Optional - 5 min)

**If time permits, show the Python notebook briefly:**

1. **Open** `12-python-agent-framework.ipynb`
2. **Show key sections**:
   - Scratchpad file creation (markdown)
   - Read scratchpad function
   - Write to scratchpad function
   - Agent instructions (similar to GUI)

**Comparison Points:**

| Aspect | GUI Approach | Code Approach |
|--------|--------------|---------------|
| Setup | 10 minutes | 30+ minutes |
| Customization | Limited | Unlimited |
| Best For | Demos, PoCs | Production apps |
| Debugging | Chat interface | Logs, print statements |

**Key Message:**
> "Same concepts, different implementation. GUI is great for learning and quick PoCs. Code gives you full control for production systems."

---

### Part 5: Context Failures & Mitigations (10 min)

**Bring it back to theory with real examples.**

#### 5.1 Context Poisoning (2 min)

**Definition:** False information gets into memory and spreads.

**Travel Agent Example:**
> "Agent hallucinates a direct flight from your small local airport to Tokyo. This fake flight gets saved in the scratchpad. Now every search tries to find this impossible flight."

**Solution:** **Context Validation + Quarantine**
- Validate info before saving to scratchpad
- "Is this flight real? Check with API before recording it."
- If questionable, mark as "unverified" or don't save

**Show in Scratchpad:**
```markdown
## Verified Bookings
- [2026-02-15] ✅ CONFIRMED: Flight ABC123 to Bali

## Unverified Notes
- [2026-02-15] ⚠️ NEEDS CHECK: User mentioned direct flight from small airport
```

#### 5.2 Context Distraction (2 min)

**Definition:** Too much history → agent loses focus on current task.

**Travel Agent Example:**
> "You've been chatting about dream destinations for 30 messages. Finally you ask 'Find me a cheap flight next month' but the agent keeps asking about your backpacking trip from 2 years ago."

**Solution:** **Context Summarization**
- Periodically compress old history
- Keep only relevant recent turns
- "After 20 messages, summarize everything into 3 key points"

**Code Pattern (show briefly):**
```python
if conversation_length > 20:
    summary = summarize_conversation(history)
    new_context = [summary] + recent_messages[-5:]
```

#### 5.3 Context Confusion (2 min)

**Definition:** Too many tools → agent calls wrong ones.

**Travel Agent Example:**
> "Agent has 50 tools: book_flight, book_hotel, rent_car, weather_forecast, currency_converter, etc. You ask 'What's the best way to get around Paris?' Agent calls book_flight WITHIN Paris instead of public_transport_info."

**Solution:** **Tool Loadout Management (RAG over tools)**
- Store tool descriptions in vector DB
- Retrieve only relevant tools per query
- Limit to < 30 tools per call (research-backed number)

**Show Concept:**
```
User Query: "How do I get around Paris?"
↓
Vector Search over Tool Descriptions
↓
Retrieved Tools: [public_transport_info, rent_car, taxi_booking]
→ ONLY give these to agent
```

#### 5.4 Context Clash (2 min)

**Definition:** Conflicting info in context → inconsistent agent behavior.

**Travel Agent Example:**
> "First you say 'I want economy class.' Later: 'Actually, let's do business class.' Both instructions stay in context. Agent gets confused about which to use."

**Solution:** **Context Pruning + Scratchpad**
- Remove outdated preferences when new ones arrive
- Or explicitly mark "OUTDATED" in scratchpad

**Show in Scratchpad:**
```markdown
## User Preferences
- ~~Flight class: Economy~~ UPDATED
- Flight class: Business (as of 2026-02-15)
```

#### 5.5 Summary - The 4 Failures (2 min)

**Quick Review Table** (show on screen):

| Failure | Problem | Solution |
|---------|---------|----------|
| **Poisoning** | False info spreads | Validate before saving |
| **Distraction** | Too much history | Summarize periodically |
| **Confusion** | Too many tools | RAG over tools |
| **Clash** | Conflicting info | Prune/override outdated |

**Ask Class:**
> "Which failure would you hit first in a long-running customer service agent?"  
> *(Answer: Likely Distraction - history grows fast!)*

---

## 🧪 Student Lab Time (15-30 min)

**Lab Instructions** (give to students):

### Task 1: Implement Scratchpad (15 min)

1. **Navigate** to your Travel Agent from Lesson 7
2. **Enable** File Search tool
3. **Create** `vacation_scratchpad.md` with 3 sections (Preferences, Tasks, Notes)
4. **Upload** file to agent
5. **Update** agent instructions to use scratchpad (use template from demo)
6. **Test** with two conversations:
   - Conversation 1: Give preferences, ask for itinerary
   - Conversation 2 (NEW chat): Ask "What do you know about me?"
7. **Download** scratchpad and verify it has content

**Success Criteria:**
- ✅ New conversation remembers your preferences
- ✅ Scratchpad file contains your data
- ✅ Agent references scratchpad in responses

### Task 2: Test Context Failure (Optional - 10 min)

**Create a Context Clash scenario:**

1. Tell agent: "I want budget hotels under $100/night"
2. Later in same conversation: "Actually, I want luxury 5-star resorts"
3. Observe: Does agent get confused? Does it update scratchpad correctly?
4. Download scratchpad: Which preference is recorded?

**Experiment:**
- Modify instructions to handle conflicts (e.g., "Always use LATEST preference")
- Re-test

### Task 3: Advanced - Multiple Scratchpads (Extra Credit - 10 min)

Create TWO scratchpad files:
- `preferences_scratchpad.md` - User preferences only
- `bookings_scratchpad.md` - Completed bookings only

Update instructions to:
- Check BOTH files at conversation start
- Update appropriate file based on content type

---

## 🎓 Instructor Tips & Troubleshooting

### Common Student Issues

**Issue 1: "File Search tool not available"**

**Cause:** Wrong project type or permissions.

**Fix:**
- Verify student has "Azure AI User" role
- Check they're in correct AI Foundry project
- Worst case: Use their neighbor's screen share

**Issue 2: "Agent doesn't update scratchpad"**

**Cause:** Instructions not explicit enough.

**Fix:**
- Make instructions MORE directive: "You MUST update scratchpad BEFORE responding"
- Add examples of exact format
- Remind agent: "After updating, confirm to user: 'I've made note of that.'"

**Issue 3: "Downloaded scratchpad is empty"**

**Cause:** Agent isn't actually writing to file (File Search is read-only by default in some configurations).

**Fix:**
- **Explain limitation**: "In GUI-only mode, File Search reads files but doesn't write updates in real-time. For writable scratchpads, we need code (which we'll see in the Python notebook)."
- **Alternative**: Show that agent INTENDS to update (check conversation logs for tool use)
- **Future solution**: Point to Lesson 13 for database-backed memory

**Issue 4: "New conversation doesn't remember anything"**

**Cause:** 
- Scratchpad not uploaded correctly
- File Search not enabled
- Agent instructions missing the "check scratchpad first" step

**Fix (Debugging checklist):**
1. Verify File Search tool shows as "Enabled"
2. Check Files section - is scratchpad listed?
3. Review agent instructions - do they mention scratchpad explicitly?
4. Test by asking: "Can you read the vacation_scratchpad.md file?" (Direct test)

### Time Management

**If running SHORT on time:**
- Skip Part 4 (Code Alternative) - focus on GUI
- Shorten Part 5 (Context Failures) to 5 min - just give examples, skip details
- Reduce lab time to 15 min (just Task 1)

**If running LONG on time:**
- Add deep dive into File Search tool configuration
- Show Azure OpenAI Studio view of the same agent
- Discuss cost implications (tokens used by File Search)
- Show advanced scratchpad templates

### Engagement Strategies

**Keep students engaged:**

1. **Ask questions frequently**:
   - "Why do you think the agent needs explicit instructions?"
   - "What happens if we don't check the scratchpad at conversation start?"
   - "In your project, what would you put in the scratchpad?"

2. **Use real-world scenarios**:
   - "Imagine you're building a customer support agent for 10,000 users..."
   - "Your CEO asks if the agent can remember past issues - what do you say?"

3. **Show failures, not just success**:
   - Intentionally skip a step, show it breaks
   - Recover and explain WHY it broke

4. **Relate to previous lessons**:
   - "In Lesson 7, we built the basic agent - now we're making it SMART"
   - "In Lesson 13, we'll replace this file with a database - even more powerful"

---

## 📚 Post-Class Resources

**Share with students:**

1. **Lesson Materials:**
   - [README.md](./README.md) - Full theory
   - [azure-ai-foundry-context-engineering.md](./azure-ai-foundry-context-engineering.md) - GUI guide
   - [12-python-agent-framework.ipynb](./code_samples/12-python-agent-framework.ipynb) - Code implementation

2. **Microsoft Docs:**
   - [File Search Tool](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools-classic/file-search)
   - [Agent Quickstart](https://learn.microsoft.com/azure/ai-foundry/agents/quickstart)
   - [Context Engineering Best Practices](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai)

3. **Next Steps:**
   - Complete Lesson 13 (Agent Memory) - builds on this!
   - Join [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for Q&A

---

## 🎬 Closing (5 min)

### Key Takeaways

**Summarize for students:**

> "Today we covered:
> 
> 1. **Context engineering** is managing dynamic information, not just static prompts
> 2. **6 types of context**: Instructions, Knowledge, Tools, History, Preferences, State
> 3. **Scratchpad pattern**: Agent's notebook for persistent memory
> 4. **4 context failures**: Poisoning, Distraction, Confusion, Clash - each has specific mitigation
> 5. **GUI vs Code**: Same concepts, different tools for different use cases
> 
> You now have a foundation for building agents that REMEMBER and LEARN from interactions!"

### Preview Next Lesson

> "In **Lesson 13 (Agent Memory)**, we'll take this scratchpad concept and supercharge it:
> - Replace markdown files with **Cosmos DB**
> - Add **vector search** over memories
> - Implement **semantic retrieval** - agent finds relevant memories automatically
> - Build true **long-term memory** with conversation summaries
> 
> Same Travel Agent, even smarter!"

### Q&A

**Open floor for questions.**

**Likely questions:**

**Q:** "Can I use this in production?"

**A:** "GUI approach is great for PoCs and small-scale use. For production with thousands of users, use the code approach + database (Lesson 13). File-based scratchpads don't scale well."

**Q:** "How much does File Search cost?"

**A:** "File Search uses vector search under the hood - costs are based on index size and queries. For small scratchpads (< 1MB), negligible. Check Azure OpenAI pricing for details."

**Q:** "What if I want to share scratchpad across multiple agents?"

**A:** "Upload the same file to multiple agents, OR use shared storage (blob storage, Cosmos DB) with code-based approach."

---

## ✅ Instructor Self-Assessment

**After class, check:**

- [ ] Students successfully created scratchpad agents (> 80% success rate)
- [ ] Students can explain context engineering vs prompt engineering
- [ ] Students tested persistence across conversations
- [ ] Students understand at least 2 context failures
- [ ] Lab time was sufficient (adjust for next session if not)
- [ ] Students know how to access Lesson 13 materials

**Continuous Improvement:**
- Note which concepts needed more explanation
- Record timing - did you rush/drag anywhere?
- Capture student questions for FAQ updates
- Test all demos again before next class (Azure UI changes!)

---

**Good luck, and have fun teaching!** 🚀

Remember: **Show the UI first, explain what's happening, THEN show code.** Students learn best when they see architecture before implementation.
