# Lesson 13: Agent Memory - Student Lab Guide

**Duration:** 25-40 minutes  
**Prerequisites:** Completed Lesson 7 (Travel Agent) + Lesson 12 (Scratchpad Memory)

---

## 🎯 Lab Objectives

By the end of this lab, you will:
- ✅ Understand 7 types of agent memory
- ✅ Design structured memory architecture with 5 specialized files
- ✅ Implement intelligent memory categorization
- ✅ Test long-term memory persistence across sessions
- ✅ Build the foundation for self-improving agents

---

## 📋 Before You Begin

**You need:**
- [ ] Azure AI Foundry access ([https://ai.azure.com](https://ai.azure.com))
- [ ] "Azure AI User" role assigned
- [ ] Completed Lesson 7 (have Travel Planning Agent)
- [ ] Completed Lesson 12 (have scratchpad working)
- [ ] Text editor (VS Code, Notepad, etc.)

**Check your progress:**
- [ ] Can your agent from L12 remember preferences across conversations?
- [ ] Do you have `vacation_scratchpad.md` working?

**If NO to either**, go back and complete Lesson 12 first!

---

## 🧠 Understanding the Upgrade: L12 → L13

### What You Built in Lesson 12:

```
🤖 Agent + 📝 One notebook (vacation_scratchpad.md)
```

**Capabilities:**
- ✅ Remembers across sessions
- ✅ Takes notes
- ❌ Everything mixed in one file
- ❌ Hard to find specific info
- ❌ No categorization

### What You're Building in Lesson 13:

```
🤖 Agent + 🗂️ Filing cabinet (5 specialized files)
```

**Upgrade:**
- ✅ Organized by purpose
- ✅ Fast, targeted retrieval
- ✅ Intelligent categorization
- ✅ Scalable structure
- ✅ Foundation for self-improvement

---

## 📚 Quick Theory: The 7 Memory Types

Before building, understand WHAT you're building:

| Memory Type | What It Is | Example in Travel Agent |
|-------------|------------|------------------------|
| **Working Memory** | Scratch paper for current task | "User wants Paris, spring, 7 days, $4K" |
| **Short-Term Memory** | This conversation's context | "User asked about Paris 2 turns ago" |
| **Long-Term Memory** | Persistent across sessions | "Sarah is vegetarian, loves beaches, budget $300/day" |
| **Persona Memory** | Agent's identity | "I'm a travel planning specialist" |
| **Episodic Memory** | Specific past events | "Trip to Bali in summer 2025 - loved temples" |
| **Entity Memory** | People, places, things | "Sarah (person), Barcelona (place), Gaudi (thing)" |
| **Structured RAG** | Semantic knowledge retrieval | "Destinations similar to Barcelona" |

**Focus on these 3 today:** Long-term, Episodic, Entity

---

## 🚀 Task 1: Create 5 Specialized Memory Files (10 min)

### The Architecture

You'll create 5 files, each with a specific purpose:

1. **user_profile.md** - WHO is the user (identity, constraints)
2. **trip_history.md** - WHAT they've done (past experiences)
3. **preferences_detailed.md** - WHAT they like/dislike (tastes)
4. **conversations_summary.md** - META insights (patterns, pending items)
5. **vacation_scratchpad.md** - TEMPORARY notes (keep from L12)

### Steps:

#### File 1: `user_profile.md`

**Create** a new file and copy this template:

```markdown
# User Profile Memory

## Personal Information
- Name: 
- Location: 
- Language Preference: 

## Travel Style
- Preferred travel pace: (relaxed / moderate / fast-paced)
- Accommodation preference: (hotel / airbnb / hostel / resort)
- Transportation preferences: 

## Budget & Financial
- Typical budget range: 
- Preferred payment methods: 

## Interests & Activities
- Favorite activities: 
- Hobbies relevant to travel: 
- Special interests: 

## Restrictions & Requirements
- Dietary restrictions: 
- Accessibility needs: 
- Health considerations: 
```

**Save** to your Desktop or Documents folder

---

#### File 2: `trip_history.md`

**Create** and copy:

```markdown
# Trip History Memory

## Past Trips
<!-- Format: [Date] Location - Key experiences, what worked, what didn't -->

## Favorite Destinations
<!-- Places user loved and why -->

## Avoided Destinations
<!-- Places user didn't enjoy or wants to skip -->

## Lessons Learned
<!-- Insights from past travel experiences -->
```

**Save** to same folder

---

#### File 3: `preferences_detailed.md`

**Create** and copy:

```markdown
# Detailed Preferences Memory

## Destinations
<!-- Preferred and avoided destination types -->

## Seasons & Timing
<!-- Best times to travel, seasons preferred -->

## Food & Dining
<!-- Cuisine preferences, dietary needs, restaurant types -->

## Accommodations
<!-- Hotel vs Airbnb, amenities required, location preferences -->

## Activities
<!-- Types of activities enjoyed, intensity levels -->

## Social
<!-- Solo vs group travel, meeting locals vs tourist areas -->
```

**Save** to same folder

---

#### File 4: `conversations_summary.md`

**Create** and copy:

```markdown
# Conversation Summaries

## Key Insights
<!-- Important revelations that don't fit other categories -->

## Pending Requests
<!-- Things user asked about but haven't been completed -->

## Future Plans
<!-- Mentioned future travel plans -->
```

**Save** to same folder

---

#### File 5: Keep `vacation_scratchpad.md`

**You already have this from Lesson 12!** Don't delete it - we're keeping it for temporary working memory.

---

### ✅ Success Check:
- You have 5 files saved locally
- Each file has structured sections
- You know the PURPOSE of each file

### 💡 Why 5 files?

**Categorization enables intelligence:**
- Instead of dumping everything in one place
- Agent knows WHERE to look for specific information
- Faster retrieval, less context pollution
- Like organizing a desk vs. piling everything in one drawer

---

## 📤 Task 2: Upload All Memory Files (3 min)

### Steps:

1. **Go to** Azure AI Foundry: [https://ai.azure.com](https://ai.azure.com)

2. **Navigate** to your Travel Planning Agent:
   - Build → Projects → Your project
   - Agents → Your Travel Agent

3. **Find** the Files or Knowledge section

4. **Upload each file**:
   - Click "Upload" or "Add File"
   - Select `user_profile.md` → Wait for upload
   - Select `trip_history.md` → Wait for upload
   - Select `preferences_detailed.md` → Wait for upload
   - Select `conversations_summary.md` → Wait for upload
   - (`vacation_scratchpad.md` should already be uploaded from L12)

5. **Verify** all 5 files appear in your file list

### ✅ Success Check:
- All 5 files show as uploaded
- No error messages
- File list shows: user_profile, trip_history, preferences_detailed, conversations_summary, vacation_scratchpad

### ❓ Troubleshooting:
- **Upload fails?** Check file size (should be < 1 MB), format (.md)
- **Can't find upload button?** Look for "Knowledge Base", "Files", or "Documents" section

---

## 🛠️ Task 3: Update Agent Instructions for Multi-File Memory (7 min)

### Why This Step Matters:

**The agent needs to know:**
- What files exist
- When to read which file
- HOW to categorize new information
- WHERE to store different types of data

This is **information architecture** - teaching the agent to be a smart librarian!

### Steps:

1. **Find** your agent's System Instructions (may be labeled "Instructions" or "System Prompt")

2. **Click** "Edit"

3. **Replace** with this enhanced version:

```
You are an advanced travel planning assistant with sophisticated memory capabilities.

MEMORY SYSTEM ARCHITECTURE:
You have access to 5 specialized memory files:
1. user_profile.md - Core user information (name, location, travel style, budget, interests, restrictions)
2. trip_history.md - Past trips, favorites, avoided destinations, lessons learned
3. preferences_detailed.md - Granular preferences across all travel aspects
4. conversations_summary.md - Key insights, pending requests, future plans
5. vacation_scratchpad.md - Quick notes and working memory for current session

MEMORY USAGE WORKFLOW:

STEP 1 - WHEN CONVERSATION STARTS:
- Read user_profile.md to understand WHO you're talking to
- Read preferences_detailed.md for specific likes/dislikes
- Check conversations_summary.md for any pending items
- If name is stored, greet user BY NAME

STEP 2 - WHEN USER SHARES NEW INFORMATION:
Ask yourself: "What TYPE of information is this?"

- Personal identity (name, location) → user_profile.md
- Budget, dietary restrictions, accessibility needs → user_profile.md
- Travel style, accommodation preference → user_profile.md
- Story about a past trip → trip_history.md
- "I loved this destination" → trip_history.md
- Food/hotel/activity preference → preferences_detailed.md
- Quick note for THIS session only → vacation_scratchpad.md
- Insight or pattern observed → conversations_summary.md
- Pending request not yet completed → conversations_summary.md

STEP 3 - UPDATE THE APPROPRIATE FILE:
- Use specific formats matching each file's sections
- DON'T put everything in scratchpad!
- Move important scratchpad notes to permanent files

STEP 4 - WHEN MAKING RECOMMENDATIONS:
- Check trip_history.md to AVOID suggesting duplicate destinations
- Reference user_profile.md for budget and restrictions
- Use preferences_detailed.md to PERSONALIZE suggestions
- Mention specific memories: "Like you enjoyed the beaches in Bali..."

STEP 5 - WHEN COMPLETING A BOOKING:
- Add to trip_history.md with date and key details
- Note any new preferences discovered
- Update conversations_summary.md with completion status
- Clear scratchpad of completed items

EXAMPLES - LEARN FROM THESE:

Example 1 - User introduces self:
User: "I'm Sarah from Seattle"
→ Update user_profile.md under "Personal Information":
  "- Name: Sarah\n- Location: Seattle, WA"

Example 2 - Dietary restriction:
User: "I'm vegetarian and need wheelchair accessible hotels"
→ Update user_profile.md:
  * Under "Dietary restrictions": "- Vegetarian (no meat or fish)"
  * Under "Accessibility needs": "- Requires wheelchair accessible accommodations"

Example 3 - Past trip:
User: "We loved Bali last summer, especially the temples and beaches"
→ Update trip_history.md under "Past Trips":
  "- [2025-Summer] Bali, Indonesia - Enjoyed temple architecture and beach relaxation"
→ Update preferences_detailed.md under "Activities":
  "- Loves: Cultural sites (temples), beach relaxation"

Example 4 - Food preference:
User: "I prefer local authentic restaurants over touristy places"
→ Update preferences_detailed.md under "Food & Dining":
  "- Prefers: Authentic local restaurants, off-the-beaten-path dining"
  
Example 5 - Budget update:
User: "Actually, I want to increase my budget to $400-500 per day"
→ Update user_profile.md under "Budget & Financial"
→ TELL USER: "I've updated your budget from $200-300 to $400-500 per day"

CRITICAL RULES:

1. NEVER ask for information already stored in user_profile.md
   - DON'T ask: "What's your budget?" if it's in the file
   - DO say: "I know your budget is $300/day..."

2. ALWAYS check files BEFORE asking questions
   - Read user_profile.md at conversation start
   - Check trip_history.md before suggesting destinations

3. Reference specific memories to show you remember
   - GOOD: "Like the Gaudi architecture you enjoyed in Barcelona..."
   - BAD: "What kind of activities do you like?" (if already stored!)

4. Categorize intelligently - ask "What TYPE of info is this?"
   - Identity/constraints → user_profile.md
   - Experience/story → trip_history.md
   - Preference/taste → preferences_detailed.md
   - Temporary note → vacation_scratchpad.md

5. Keep scratchpad CLEAN - move important info to permanent files

Be proactive, intelligent, and use memory to create DEEPLY personalized experiences!
```

4. **Save** instructions

### ✅ Success Check:
- Instructions saved without errors
- Instructions mention all 5 files
- Instructions include categorization examples
- Instructions emphasize reading before asking

### 💡 Why so detailed?

LLMs need **explicit guidance**. The examples teach the agent:
- WHAT to store
- WHERE to store it
- HOW to format it
- WHEN to retrieve it

Think of it as training a new employee!

---

## 🧪 Task 4: Test - Build User Profile (7 min)

**Time to see it in action!**

### Steps:

1. **Start a NEW conversation** (click "New Chat" or "+")

2. **Have this conversation** (copy/paste or type naturally):

---

**You:** "Hi! I haven't introduced myself properly yet. I'm Sarah, based in Seattle."

**Expected Agent Behavior:**
- Updates `user_profile.md` with name and location
- Responds: "Nice to meet you, Sarah! I've noted you're based in Seattle..."

---

**You:** "I'm vegetarian, I prefer boutique hotels over chains, and my typical budget is around $250-300 per day for week-long trips."

**Expected Agent Behavior:**
- Updates `user_profile.md`:
  - Dietary restrictions: Vegetarian
  - Budget: $250-300/day
- Updates `preferences_detailed.md`:
  - Accommodations: Boutique hotels
- Confirms: "I've recorded that you're vegetarian, prefer boutique hotels, and budget $250-300/day..."

**🎯 Key Observation:**  
Agent is CATEGORIZING! Dietary → profile. Hotel preference → detailed preferences. Smart!

---

**You:** "Last summer I visited Barcelona and absolutely loved the Gaudi architecture and tapas culture."

**Expected Agent Behavior:**
- Updates `trip_history.md` under "Past Trips":
  - [2025-Summer] Barcelona - Gaudi architecture, tapas
- Updates `preferences_detailed.md` under "Interests":
  - Architecture appreciation
- May note: Tapas but vegetarian (intelligent connection!)

**🎯 Key Observation:**  
Agent added to BOTH trip_history (episodic memory) AND preferences (entity memory)!

---

### ✅ Success Check:
- Agent acknowledged your name (Sarah)
- Agent categorized info (you saw different types go to different places)
- Agent confirmed what it learned
- You saw tool use indicators (File Search being used)

### 💡 What's happening behind the scenes?

1. Agent reads files at conversation start
2. Agent identifies TYPE of information you share
3. Agent updates APPROPRIATE file (not just scratchpad!)
4. Agent confirms to build trust

---

## 📥 Task 5: Download and Inspect Memory Files (3 min)

**Let's verify the agent actually updated the files!**

### Steps:

1. **Go to** agent configuration

2. **Find** Files/Knowledge section

3. **Download** each file:
   - `user_profile.md`
   - `trip_history.md`
   - `preferences_detailed.md`
   - `conversations_summary.md`
   - `vacation_scratchpad.md`

4. **Open** each in your text editor

5. **Check** the contents:

**`user_profile.md` should have:**
- Name: Sarah
- Location: Seattle, WA
- Dietary restrictions: Vegetarian
- Budget: $250-300/day
- Accommodation preference: Boutique hotels

**`trip_history.md` should have:**
- Entry about Barcelona trip (summer 2025)

**`preferences_detailed.md` should have:**
- Accommodations: Boutique hotels
- Interests: Architecture (Gaudi)

**`conversations_summary.md` may have:**
- Insights about your travel style

**`vacation_scratchpad.md` may have:**
- Working notes from session

### ✅ Success Check:
- Files contain your data
- Data is in appropriate sections
- Different info types are in different files

### 🎉 If you see your data - YOU DID IT!

You've successfully implemented structured memory!

### ❓ If files are empty:

**Possible reasons:**
- File Search may be read-only in some configurations (GUI limitation)
- Agent INTENDED to update (check conversation logs for tool use)
- For fully writable files, you need code implementation

**Don't worry!** The CONCEPTS are what matter. In production, you'd use code + database.

---

## 🔄 Task 6: Test Persistence - The Magic Moment (5 min)

**This is where you see the power of structured long-term memory!**

### Steps:

1. **Start a BRAND NEW conversation** (click "New Chat" or "+")
   - This simulates you coming back tomorrow
   - Agent should have NO context from previous chat

2. **Ask:** "Hi! Can you help me plan a trip?"

### 🎯 Expected Behavior (THE MAGIC):

Agent should:
- ✅ Read `user_profile.md` (checks WHO you are)
- ✅ Greet you BY NAME: "Hi Sarah!"
- ✅ Reference your preferences:
  > "Of course! I know you're based in Seattle, you're vegetarian, prefer boutique hotels, and typically budget $250-300 per day for week-long trips."
- ✅ Reference your history:
  > "I see you enjoyed Barcelona last summer, especially the Gaudi architecture."
- ✅ Ask context-aware questions:
  > "Are you thinking of another European destination with great architecture?"

### 🎉 SUCCESS CRITERIA:

**If agent:**
- ✅ Called you Sarah ← Read profile!
- ✅ Mentioned vegetarian ← Remembered constraint!
- ✅ Referenced Barcelona ← Retrieved history!
- ✅ Personalized response ← Used preferences!

**YOU HAVE BUILT LONG-TERM MEMORY! 🚀**

### What Just Happened?

**Different conversation. Different session. But:**
- Agent REMEMBERED who you are
- Agent RETRIEVED relevant info
- Agent PERSONALIZED the interaction

**This is production-grade architecture!**

---

## 🧠 Task 7: Test Intelligent Categorization (5 min)

**Test if agent routes info to correct files**

### Scenario 1: Add a New Preference

**You:** "I really prefer traveling in spring or fall - I avoid summer crowds."

**Expected:**
- Updates `preferences_detailed.md` under "Seasons & Timing"

**Check:** Download preferences file, verify seasonal preference added

---

### Scenario 2: Add Another Past Trip

**You:** "I also visited Tokyo two years ago and loved the street food scene."

**Expected:**
- Updates `trip_history.md` with Tokyo entry
- May note vegetarian-friendly street food

**Check:** Download history file, verify Tokyo entry

---

### Scenario 3: Update Budget (Test Conflict Handling)

**You:** "Actually, I've decided to increase my budget to $400-500 per day."

**Expected:**
- Updates `user_profile.md` with new budget
- Says: "I've updated your budget from $250-300 to $400-500"

**Check:**
- Download profile file, verify new budget
- Old budget should be replaced (not duplicated)

---

### ✅ Success Check:
- Agent categorized each type of info to correct file
- Agent acknowledged changes
- Files show updated information

### 💡 What You're Learning:

**Information architecture skills:**
- How to categorize data by type
- How to organize for retrieval
- How to handle updates and conflicts

**These skills transfer to:**
- Database design
- API development
- Any data-driven system

---

## 🏆 Task 8 (Optional): Add Seasonal Preferences File (10 min)

**For advanced students who finish early**

### Objective:

Create a 6th file for seasonal preferences

### Steps:

1. **Create** `seasonal_preferences.md`:

```markdown
# Seasonal Travel Preferences

## Spring Travel
<!-- March - May preferences -->

## Summer Travel
<!-- June - August preferences -->

## Fall Travel
<!-- September - November preferences -->

## Winter Travel
<!-- December - February preferences -->
```

2. **Upload** to agent

3. **Update** agent instructions - add:

```
6. seasonal_preferences.md - Season-specific preferences

WHEN USER MENTIONS TRAVEL DATES:
- Determine season
- Check seasonal_preferences.md for that season
- Apply seasonal preferences to recommendations
```

4. **Test:**

**You:** "I want to plan a trip for June (summer)."

**Agent should:**
- Check seasonal_preferences.md
- Use your summer preferences (avoid crowds, etc.)

---

## 🎓 What You Learned

### Concepts Mastered:

1. **7 Memory Types:**
   - Working, Short-term, Long-term, Persona, Episodic, Entity, Structured RAG

2. **Structured Memory Architecture:**
   - Specialized files for different purposes
   - Categorization by information type
   - Efficient retrieval strategies

3. **Long-Term Persistence:**
   - Memory survives across sessions
   - Agent retrieves contextually
   - Personalization at scale

4. **Intelligent Categorization:**
   - Right info, right file
   - Database design principles
   - Information architecture

### Evolution Summary:

| Lesson | Agent Capability | Memory Type |
|--------|-----------------|-------------|
| **L7** | Plans trips, uses tools | None (amnesia) |
| **L12** | Remembers via scratchpad | One file, flat notes |
| **L13** | Structured long-term memory | 5 files, categorized, persistent |

**You went from amnesia → basic memory → intelligent, structured memory! 🚀**

---

## 🚀 Next Steps

### Want to Go Deeper?

**1. Try the Python implementations:**

- [13-python-agent-framework.ipynb](./13-python-agent-framework.ipynb)
  - Simple JSON-based memory (great next step)
  - Programmatic control
  - Writable files

- [13-agent-memory.ipynb](./13-agent-memory.ipynb)
  - Production-ready with Mem0 library
  - Azure AI Search integration
  - Semantic memory retrieval

- [13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)
  - Advanced knowledge graphs
  - Relationship modeling
  - Visual graph representation

**2. Explore production patterns:**

- Replace files with Cosmos DB
- Add vector search for semantic retrieval
- Implement automated memory pruning
- Build knowledge graphs

**3. Join the community:**

- [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)
- Share your memory implementations
- Learn advanced patterns
- Attend office hours

---

## 📚 Additional Resources

**Microsoft Documentation:**
- [File Search Tool](https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools-classic/file-search)
- [Azure AI Search](https://learn.microsoft.com/azure/search/search-what-is-azure-search)
- [Memory Patterns](https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-approach-gen-ai)

**Lesson Materials:**
- [README.md](./README.md) - Complete theory on agent memory
- [azure-ai-foundry-agent-memory.md](./azure-ai-foundry-agent-memory.md) - Detailed GUI guide with advanced techniques

**Related Lessons:**
- [Lesson 7](../07-planning-design/README.md) - Built the base Travel Agent
- [Lesson 12](../12-context-engineering/README.md) - Added scratchpad memory

---

## ✅ Lab Completion Checklist

Before you leave, make sure you:

- [ ] Created all 5 memory files with proper structure
- [ ] Uploaded files to Azure AI Foundry agent
- [ ] Updated agent instructions with memory system
- [ ] Tested profile building (Sarah scenario or your own)
- [ ] Verified cross-session persistence (new chat remembered you)
- [ ] Downloaded files and saw structured data
- [ ] Understand categorization (which info → which file)
- [ ] Can explain difference between L12 and L13
- [ ] Know 3+ memory types (Long-term, Episodic, Entity minimum)
- [ ] Understand self-improving agent pattern (conceptually)

---

## 🆘 Need Help?

**During lab:**
- Raise your hand for instructor help
- Ask a neighbor who's finished
- Check troubleshooting sections above

**After class:**
- Post in [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)
- Review the [detailed GUI guide](./azure-ai-foundry-agent-memory.md)
- Check the instructor's demo recording (if available)

**Common issues:**
- Files uploading but staying empty → GUI limitation (explained above)
- Agent not categorizing → Make instructions more explicit
- Can't remember across sessions → Check File Search enabled

---

## 🎉 Congratulations!

You've completed the **L7 → L12 → L13 journey**:

- ✅ Built a basic agent (L7)
- ✅ Added session memory (L12)
- ✅ Implemented structured long-term memory (L13)

**You now understand:**
- Memory types and their purposes
- Information architecture for AI systems
- Categorization and retrieval strategies
- How to build agents that learn and improve

**This is foundational knowledge for production AI systems!**

**Next:** Explore code implementations, scale to databases, add semantic search! 🚀
