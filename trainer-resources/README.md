# Trainer Resources

This directory contains trainer-specific materials not suitable for the main course repository.

## Directory Structure

```
trainer-resources/
├── README.md (this file)
├── shared-demos/          # Backup demos for live presentations
├── troubleshooting/       # Common issue resolutions
├── lesson-plans/          # Detailed lesson delivery plans
└── hackathon-guides/      # Hackathon mentoring resources
```

## Contributing Resources

### Adding Backup Demos

Create lesson-specific subdirectories:

```
trainer-resources/
└── shared-demos/
    ├── lesson-12-context/
    │   ├── backup-demo.ipynb
    │   └── demo-script.md
    └── lesson-13-memory/
        ├── backup-demo.ipynb
        └── demo-script.md
```

### Sharing Troubleshooting Solutions

Add to `troubleshooting/`:

```markdown
## Issue: [Brief Description]

**Lesson:** XX  
**Reported by:** [Trainer Name]  
**Date:** YYYY-MM-DD

**Problem:**
[Detailed description]

**Solution:**
[Step-by-step resolution]

**Prevention:**
[How to avoid this in future]
```

### Lesson Plans

Template for detailed lesson delivery plans:

```markdown
# Lesson XX: [Topic]

**Trainer:** [Name]  
**Duration:** XX minutes  
**Prerequisites:** Lessons X, Y, Z

## Learning Objectives
1. ...
2. ...

## Presentation Flow
- 00:00-05:00 - Introduction
- 05:00-15:00 - Core concepts
- ...

## Demo Checkpoints
- [ ] Demo 1: [Description]
- [ ] Demo 2: [Description]

## Common Student Questions
1. Q: ...  
   A: ...

## Backup Plan
- If demo fails: ...
- If time runs short: ...
```

---

**Guidelines:**

- Keep content trainer-focused (not student-facing)
- Update with lessons learned during training
- Share workarounds and tips
- Document "what I wish I knew" insights

---

**Last Updated:** January 6, 2026
