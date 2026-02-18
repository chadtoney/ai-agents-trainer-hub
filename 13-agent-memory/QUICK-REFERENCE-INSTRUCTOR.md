# Lesson 13 Quick Reference - Instructor Cheat Sheet

**⏱️ Total Time:** 60-75 minutes  
**👤 Instructor:** Chad Toney  
**Prerequisites:** Students completed L7 (Travel Agent) + L12 (Scratchpad)

---

## ⚡ Pre-Demo Checklist (5 min before class)

- [ ] Azure AI Foundry open: https://ai.azure.com
- [ ] Travel Agent with L12 scratchpad ready
- [ ] 5 memory files created on Desktop
- [ ] This cheat sheet + main guide open
- [ ] Whiteboard ready for memory diagrams

---

## 📊 Lesson Timeline

| Time | Section | Key Action |
|------|---------|------------|
| 0-10 | Evolution Story | L7 → L12 → L13 progression |
| 10-25 | Theory | 7 memory types + examples |
| 25-50 | Demo | Create 5-file system in Azure Portal |
| 50-55 | Self-Improvement | Knowledge agent pattern |
| 55-60 | Production | Scaling considerations |
| 60-75+ | Lab | Students implement 5-file memory |

---

## 🎯 The Evolution Narrative (First 3 min)

**Opening script:**

> "Our journey:
> - **L7**: Agent with tools, but amnesia 🤖
> - **L12**: Added 1 notebook (scratchpad) 🤖📝
> - **L13**: Upgraded to filing cabinet (5 specialized files) 🤖🗂️
> 
> Today: One scratchpad → Structured memory architecture"

**Draw on board:**
```
L7: 🤖 (forgets)
L12: 🤖 + 📝 (1 file)
L13: 🤖 + 🗂️ (5 files, organized)
```

---

## 📝 The 5-File Architecture (Slide)

```
Memory System:
├── user_profile.md       → WHO (identity, constraints)
├── trip_history.md       → WHAT done (experiences)
├── preferences_detailed.md → WHAT likes (tastes)
├── conversations_summary.md → META (insights, pending)
└── vacation_scratchpad.md   → TEMP (session notes)
```

**Purpose of each:**
- **Profile**: "Name, budget, dietary, accessibility"
- **History**: "Past trips, favorites, avoided"
- **Preferences**: "Food, hotels, activities, social"
- **Summary**: "Key insights, pending requests"
- **Scratchpad**: "Temporary working memory"

---

## 🧠 The 7 Memory Types (Quick Ref)

| Type | Analogy | Example | File |
|------|---------|---------|------|
| **Working** | Doing math in head | "Paris, spring, 7 days, $4K" | Scratchpad |
| **Short-term** | This meeting's context | "User asked about Paris 2 turns ago" | Auto history |
| **Long-term** | Friend's birthday | "Sarah is vegetarian, loves beaches" | Profile + Prefs |
| **Persona** | "I'm a doctor" | "I'm a travel specialist" | Instructions |
| **Episodic** | High school graduation | "Trip to Bali, summer 2025" | History |
| **Entity** | Rolodex | "Sarah → loves → Barcelona" | Preferences |
| **Structured RAG** | Smart librarian | "Relaxing + culture → Bali" | Azure AI Search |

**Teach these 3 DEEPLY:** Long-term, Episodic, Entity (skip others if time short!)

---

## 🖥️ Azure Portal Demo Steps (25 min)

### Step 1: Show Current State (2 min)
1. Open Travel Agent from L12
2. Show existing scratchpad file
3. Test: "One file for everything - limited!"

### Step 2: Create 5 Files (8 min - create LIVE)

**user_profile.md (2 min):**
```markdown
# User Profile Memory

## Personal Information
- Name: 
- Location: 

## Travel Style
- Preferred travel pace: 

## Budget & Financial
- Typical budget range: 

## Interests & Activities

## Restrictions & Requirements
- Dietary restrictions: 
- Accessibility needs: 
```

**trip_history.md (2 min):**
```markdown
# Trip History Memory

## Past Trips

## Favorite Destinations

## Avoided Destinations

## Lessons Learned
```

**preferences_detailed.md (2 min):**
```markdown
# Detailed Preferences Memory

## Destinations

## Food & Dining

## Accommodations

## Activities

## Social
```

**conversations_summary.md (1 min):**
```markdown
# Conversation Summaries

## Key Insights

## Pending Requests

## Future Plans
```

**Keep `vacation_scratchpad.md` from L12 (1 min)**

### Step 3: Upload All Files (3 min)
1. Go to Files/Knowledge section
2. Upload all 5 files
3. Wait for processing
4. Verify in file list

### Step 4: Update Instructions (8 min) ⚠️ CRITICAL

**Add to agent instructions:**

```
MEMORY SYSTEM ARCHITECTURE:
5 specialized files:
1. user_profile.md - Core info (name, budget, restrictions)
2. trip_history.md - Past trips, lessons learned
3. preferences_detailed.md - Granular preferences
4. conversations_summary.md - Insights, pending items
5. vacation_scratchpad.md - Session working memory

WORKFLOW:

CONVERSATION START:
- Read user_profile.md (WHO)
- Read preferences_detailed.md (WHAT they like)
- Check conversations_summary.md (pending items)

NEW INFORMATION - CATEGORIZE:
Ask: "What TYPE is this?"
- Identity/budget/dietary → user_profile.md
- Past trip story → trip_history.md
- Food/hotel/activity preference → preferences_detailed.md
- Session note → vacation_scratchpad.md
- Insight → conversations_summary.md

MAKING RECOMMENDATIONS:
- Check trip_history.md (avoid duplicates)
- Use user_profile.md (budget, restrictions)
- Apply preferences_detailed.md (personalize)
- Reference: "Like you enjoyed in Barcelona..."

EXAMPLES:

User: "I'm Sarah from Seattle, vegetarian"
→ user_profile.md: Name, Location, Dietary

User: "Loved Bali's beaches"
→ trip_history.md: Past trip
→ preferences_detailed.md: Beach preference

User: "Budget $200-300/day"
→ user_profile.md: Budget

NEVER ask what's in profile!
Be intelligent about file selection!
```

**Save instructions**

### Step 5: Test - Build Profile (4 min)

**Conversation:**

```
User: "I'm Sarah from Seattle"
Agent: (updates profile) "Nice to meet you, Sarah!"

User: "I'm vegetarian, prefer boutique hotels, budget $250-300/day"
Agent: (categorizes to profile + preferences) "Recorded..."

User: "Loved Barcelona last summer - Gaudi architecture"
Agent: (adds to history + preferences) "I'll remember that..."
```

**Point out:** Agent categorizing to different files!

### Step 6: Test Persistence (3 min)

**NEW conversation:**

```
User: "Hi! Can help me plan a trip?"
Agent: "Hi Sarah! I know you're vegetarian, prefer boutique 
        hotels, budget $250-300/day. I see you loved Barcelona's
        architecture. Thinking another European city?"
```

**PAUSE - emphasize:** "NEW chat, but agent KNOWS Sarah! Long-term memory!"

### Step 7: Download Files (2 min)
- Download all 5 files
- Show structured data in appropriate files
- Compare to L12 (everything in one file)

---

## 💡 Teaching Tips

### Key Questions to Ask

**Every 5 minutes ask:**
- "Where would 'user loves beaches' go? Which file?"
- "What's the difference between history and preferences?"
- "Why not one big file?"

### Show Progression Often

**Constantly reference:**
- L7: Stateless (forgets everything)
- L12: One scratchpad (basic memory)
- L13: 5 files (structured, intelligent)

### Celebrate Wins

**When persistence works:**
> "See that?! NEW conversation, agent remembers Sarah! 🎉"

---

## 🆘 Troubleshooting Quick Fixes

### "Agent puts everything in scratchpad"
→ Make instructions MORE explicit with WRONG/RIGHT examples
→ "WRONG: Dietary in scratchpad ❌ RIGHT: Dietary in profile ✅"

### "Agent doesn't check profile before asking"
→ Emphasize: "FIRST STEP ALWAYS: Read user_profile.md"
→ "NEVER ask for name/budget if stored!"

### "Files stay empty"
→ **Explain:** File Search may be read-only (GUI limitation)
→ Agent INTENDS to update (check logs)
→ For writable: Use code (Python notebooks)

### "Too slow - reads all files"
→ **Optimize instructions:**
```
ALWAYS read: user_profile.md
READ IF RELEVANT: trip_history (discussing trips),
                  preferences (making recommendations)
```

---

## 🧪 Lab Instructions (Give to Students)

**Task 1: 5-File Memory System (20 min)**

1. Create 5 files (use templates)
2. Upload to agent
3. Update instructions (use template)
4. Test: Introduce yourself, share preferences
5. NEW chat: Agent should remember you
6. Download files, verify data

**Success = Agent remembers across conversations ✓**

**Task 2 (Optional): Memory Conflicts (10 min)**

1. Say: "Budget $200/day"
2. Later: "Change to $400/day"
3. Check: Did agent update? Acknowledge change?

---

## 🎓 Self-Improving Pattern (5 min)

**Draw diagram:**

```
User ←→ Primary Agent
           ↓ (watches)
    Knowledge Agent
           ↓
    Memory Files
```

**Explain:**
1. Primary Agent talks to user
2. Knowledge Agent observes
3. Knowledge Agent asks: "Worth saving?"
4. Extracts, categorizes, stores
5. Next time: Primary retrieves, uses

**Analogy:** Executive + assistant + filing cabinet

---

## 🏭 Production Considerations (5 min)

**GUI → Code → Production:**

| Stage | Storage | Use Case |
|-------|---------|----------|
| L12 GUI | 1 markdown file | Learning |
| L13 GUI | 5 markdown files | Prototypes |
| L13 Code | JSON files | Small apps |
| Production | Cosmos DB + AI Search | Enterprise |

**Key message:**
> "GUI = learning concepts ✅  
> Production = code + database ✅  
> But ARCHITECTURE (5 memory types) = SAME!"

---

## 🎬 Closing Summary (5 min)

**The trilogy:**

> "Journey complete!
> - L7: Basic agent 🛠️
> - L12: Session memory 📝
> - L13: Structured long-term memory 🗂️
> 
> You built a **stateful, learning agent** 🚀"

**Key Takeaways:**
1. Memory types matter
2. Structure enables intelligence
3. Categorization is key
4. Persistence creates value
5. Self-improvement is a pattern

**Q&A**

---

## 📱 Emergency Backup

**If Azure down:** Use screenshots/recording  
**If students stuck:** Pair programming, screen share  
**If totally broken:** Theory/whiteboard, assign reading

---

## ✅ Post-Class Checklist

- [ ] >80% implemented 5-file system
- [ ] Students explain 3+ memory types
- [ ] Tested cross-session persistence
- [ ] Understand categorization
- [ ] See L7→L12→L13 evolution
- [ ] Know code implementations exist

---

## 🎯 Remember

**Teaching approach:**
1. Show progression (L7 → L12 → L13)
2. Emphasize categorization ("What TYPE of info?")
3. Celebrate persistence working
4. Connect GUI to production patterns

**Core message:**
> "One scratchpad → Organized filing system = Smarter agent!"

**Good luck! 🚀**
