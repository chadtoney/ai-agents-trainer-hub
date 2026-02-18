# Lesson 12 Quick Reference - Instructor Cheat Sheet

**⏱️ Total Time:** 60 minutes  
**👤 Instructor:** Chad Toney

---

## ⚡ Pre-Demo Checklist (3 min before class)

- [ ] Azure AI Foundry open: https://ai.azure.com
- [ ] Travel Agent from Lesson 7 visible
- [ ] `vacation_scratchpad.md` file created on Desktop
- [ ] This cheat sheet + main guide open
- [ ] Students confirmed to have Azure AI User role

---

## 📊 Lesson Timeline

| Time | Section | Key Action |
|------|---------|------------|
| 0-15 | Lecture | Context fundamentals, 6 types, 4 failures |
| 15-35 | Demo | Azure Portal scratchpad implementation |
| 35-45 | Context Failures | Live examples + mitigations |
| 45-60 | Lab | Students implement scratchpad |

---

## 🎯 Key Definitions (Slide 1)

**Context Engineering** = Managing dynamic information in agent's decision window

**Context Window** = Limited token capacity (e.g., 128K tokens)

**Prompt Engineering vs Context Engineering:**
- Prompt = Static "rules for the agent"
- Context = Dynamic "information the agent needs"

---

## 📝 The 6 Types of Context (Slide 2)

**I-K-T-H-P-S** (acronym for memory)

1. **Instructions** - System prompt, rules
2. **Knowledge** - Facts, RAG data
3. **Tools** - Function definitions
4. **History** - Conversation turns ⚠️ (grows fastest!)
5. **Preferences** - User likes/dislikes
6. **State** - Runtime variables

**Travel Agent Example:**
- Instructions: "You're a travel planner"
- Knowledge: Flight prices, hotels
- Tools: `book_flight()`, `search_hotels()`
- History: Chat messages
- Preferences: "User loves beaches"
- State: "Currently searching flights, budget=$3K"

---

## 🚨 The 4 Context Failures (Slide 3)

| Failure | Problem | Solution |
|---------|---------|----------|
| **Poisoning** | False info spreads | Validate before saving |
| **Distraction** | Too much history | Summarize periodically |
| **Confusion** | Too many tools (>30) | RAG over tool descriptions |
| **Clash** | Conflicting preferences | Prune/override old info |

---

## 🖥️ Azure Portal Demo Steps (15-20 min)

### Step 1: Navigate (2 min)
1. Go to https://ai.azure.com
2. Build tab → Projects → Select project
3. Agents → Select Travel Agent

### Step 2: Add File Search (2 min)
1. Tools section → Click "+ Add"
2. Select "File Search"
3. Enable → Save

**Explain:** "File Search = agent can read uploaded files (uses RAG)"

### Step 3: Create Scratchpad (3 min)
1. Open text editor
2. Create `vacation_scratchpad.md`:

```markdown
# Vacation Planning Agent Scratchpad

## User Preferences
<!-- Budget, destinations, activities -->

## Completed Tasks
<!-- What agent has done -->

## Notes
<!-- Agent's working thoughts -->
```

3. Save to Desktop

**Explain sections** as you type!

### Step 4: Upload File (2 min)
1. In agent UI → Files/Knowledge section
2. Upload `vacation_scratchpad.md`
3. Wait for processing (~10 sec)
4. Verify appears in file list

### Step 5: Update Instructions (6 min) ⚠️ CRITICAL STEP

Add to TOP of system instructions:

```
SCRATCHPAD MANAGEMENT (CRITICAL - DO THIS FIRST):
1. At the START of EVERY conversation, read vacation_scratchpad.md
2. When user mentions preferences (budget, dates, destinations):
   - ADD to "User Preferences" section
   - Format: "- Budget: $3000 per person"
3. When you COMPLETE a task:
   - ADD to "Completed Tasks" with timestamp
   - Format: "- [2026-02-15] Created Bali itinerary"
4. BEFORE recommendations, CHECK scratchpad for context

EXAMPLES:
User: "I love beach destinations"
→ Add: "- Destination preference: Beach, warm weather"

User: "Budget is $3000 per person"
→ Add: "- Budget: $3000/person for 7-day trip"

You create itinerary:
→ Add: "- [2026-02-15] Created Bali itinerary with snorkeling"
```

**Save instructions**

### Step 6: Test - First Conversation (4 min)

**Conversation 1 (New chat):**

```
User: "Hi! I'm planning a vacation. Can you help?"
Agent: (checks scratchpad) "Sure! Tell me your preferences..."

User: "I love beaches, budget $3000 per person for a week"
Agent: (acknowledges, updates scratchpad)

User: "Create a detailed Bali itinerary"
Agent: (creates itinerary, marks task complete)
```

**Point out:**
- Tool use indicators (File Search in action)
- Agent mentions "making note" or "I'll remember"

### Step 7: Download Scratchpad (2 min)
1. Go to Files section
2. Download `vacation_scratchpad.md`
3. Open in editor
4. **Show students** the preferences and tasks

**Celebrate if it worked!** 🎉

### Step 8: Test Persistence (3 min)

**Conversation 2 (NEW chat - this is the money shot!):**

```
User: "Hi! Can you help me plan a trip?"
Agent: "Of course! I see you prefer beach destinations and 
       have a budget of $3000 per person. Would you like to 
       continue with Bali or explore other options?"
```

**PAUSE. Let students absorb this.**

> "Different conversation. Agent REMEMBERS. That's context engineering!"

---

## 💡 Teaching Tips

### Keep Students Engaged

**Ask questions every 5 minutes:**
- "Why do agents need explicit instructions?"
- "What happens if we skip checking the scratchpad?"
- "In YOUR project, what would go in the scratchpad?"

### Show Failures Too

- Intentionally skip scratchpad check in instructions → breaks
- Show recovery: "See? Without explicit instructions, it forgets!"

### Connect to Real World

- "Imagine 10,000 customer support conversations..."
- "Your CEO asks 'Can it remember past issues?' - what do you say?"

---

## 🆘 Troubleshooting Quick Fixes

### "File Search not available"
→ Check Azure AI User role, verify project type

### "Agent doesn't update scratchpad"
→ Make instructions MORE explicit, add examples, use CAPS

### "Downloaded scratchpad is empty"
→ **Explain**: GUI File Search is read-only in some configs
→ Point to code notebook for writable version

### "New chat doesn't remember"
→ Debug checklist:
1. File Search enabled? ✓
2. File uploaded? ✓
3. Instructions mention scratchpad? ✓
4. Test: Ask "Can you read vacation_scratchpad.md?"

---

## 🧪 Lab Instructions (Give to Students)

**Task 1: Implement Scratchpad (15 min)**

1. Enable File Search on your Travel Agent
2. Create `vacation_scratchpad.md` (3 sections)
3. Upload file
4. Update instructions (use template from demo)
5. Test with 2 conversations:
   - Conv 1: Give preferences, get itinerary
   - Conv 2 (NEW): Ask "What do you know about me?"
6. Download scratchpad, verify contents

**Success = New conversation remembers you! ✓**

---

## 🎬 Closing Summary (5 min)

**Key Takeaways:**
1. Context engineering = managing dynamic info
2. 6 types: I-K-T-H-P-S
3. Scratchpad = agent's notebook
4. 4 failures: Poisoning, Distraction, Confusion, Clash
5. GUI vs Code = same concepts, different tools

**Next Lesson:**
"Lesson 13 = Replace scratchpad with Cosmos DB + vector search!"

**Q&A**

---

## 📱 Emergency Contact

**If Azure is down:** Use screenshots/recorded demo  
**If students blocked:** Pair programming, share screens  
**If totally stuck:** Move to theory/whiteboard, assign homework

---

## ✅ Post-Class Checklist

- [ ] >80% students successfully implemented scratchpad
- [ ] Students can explain context vs prompt engineering
- [ ] Students tested persistence
- [ ] Lab time sufficient? (adjust next time)
- [ ] Capture questions for FAQ

---

**🎯 Remember:** Show UI → Explain → Then Code  
**🎯 Remember:** Celebrate small wins!  
**🎯 Remember:** It's okay if things break - that's learning!

**Good luck! 🚀**
