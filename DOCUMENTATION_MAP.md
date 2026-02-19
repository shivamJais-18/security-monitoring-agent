# 📚 Documentation Map

Find the right guide for your needs in 30 seconds!

---

## 🎯 Choose Your Path

```
Are you NEW to this project?
        ↓
        YES → Read QUICK_REFERENCE.md (5 min)
        ↓
        Read ADD_AND_MONITOR_DATA_GUIDE.md (10 min)
        ↓
        You're ready! Start testing

Are you using the DASHBOARD UI?
        ↓
        YES → Read CUSTOM_DATA_PANEL_GUIDE.md
        ↓
        Go to http://localhost:5174 → Click "🎯 Custom Data"

Prefer COMMAND LINE?
        ↓
        YES → Read MANUAL_DATA_GUIDE.md
        ↓
        Run: python data_injector.py add-preset sql_injection

Want to create CUSTOM DATASETS?
        ↓
        YES → Read data/raw_logs/DATASET_README.md
        ↓
        Run: python data/raw_logs/generate_logs.py

Want to DEPLOY to GitHub?
        ↓
        YES → Read GITHUB_UPLOAD_GUIDE.md
        ↓
        Follow git workflow

Want to SHARE on LinkedIn?
        ↓
        YES → Read LINKEDIN_GUIDE.md
        ↓
        Use post templates + hashtags

Need COMPLETE WORKFLOW?
        ↓
        YES → Read ADD_AND_MONITOR_DATA_GUIDE.md (full guide)
        ↓
        Complete all 4 test scenarios
```

---

## 📖 Guide Matrix

| **Guide** | **Time** | **For Whom** | **Key Topics** |
|-----------|----------|------------|----------------|
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | 5 min | Everyone starting fresh | Setup, quick commands, event types, threat levels |
| [ADD_AND_MONITOR_DATA_GUIDE.md](ADD_AND_MONITOR_DATA_GUIDE.md) | 15 min | Users wanting full workflow | Both UI + CLI, test scenarios, troubleshooting |
| [CUSTOM_DATA_PANEL_GUIDE.md](CUSTOM_DATA_PANEL_GUIDE.md) | 10 min | Dashboard users | Form fields, tabs, auto-refresh, live monitoring |
| [MANUAL_DATA_GUIDE.md](MANUAL_DATA_GUIDE.md) | 8 min | CLI users | Commands, presets, custom threats, incidents |
| [DATASET_README.md](data/raw_logs/DATASET_README.md) | 10 min | Data engineers | Generators, scenarios, dataset analysis |
| [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md) | 5 min | Deployment | Git setup, push, repository |
| [LINKEDIN_GUIDE.md](LINKEDIN_GUIDE.md) | 5 min | Promotion | Templates, hashtags, engagement |
| README.md | 20 min | Project overview | Architecture, features, troubleshooting |

---

## 🚀 Quick Links

### Start Your Journey (Do These First)
1. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ← Start here (5 min)
2. **[ADD_AND_MONITOR_DATA_GUIDE.md](ADD_AND_MONITOR_DATA_GUIDE.md)** ← Then here (10 min)

### Now Pick Your Method
- **Dashboard? →** [CUSTOM_DATA_PANEL_GUIDE.md](CUSTOM_DATA_PANEL_GUIDE.md)
- **Command Line? →** [MANUAL_DATA_GUIDE.md](MANUAL_DATA_GUIDE.md)

### Ready to Share?
- **GitHub? →** [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)
- **LinkedIn? →** [LINKEDIN_GUIDE.md](LINKEDIN_GUIDE.md)

### Deep Dives
- **Datasets? →** [DATASET_README.md](data/raw_logs/DATASET_README.md)
- **Everything? →** [README.md](README.md)

---

## 💡 Common Scenarios

### "I want to add a threat right now!"
```
1. Read QUICK_REFERENCE.md (2 min)
2. Start servers (1 min)
3. Go to http://localhost:5174
4. Click "🎯 Custom Data" → "Add Threat" tab
5. Fill form and click "Add Threat"
Total: 5 minutes
```

### "I want to understand everything"
```
1. Read QUICK_REFERENCE.md (5 min)
2. Read ADD_AND_MONITOR_DATA_GUIDE.md (10 min)
3. Read CUSTOM_DATA_PANEL_GUIDE.md (10 min)
4. Run through all 4 test scenarios (15 min)
Total: 40 minutes
```

### "I prefer command line"
```
1. Read QUICK_REFERENCE.md (5 min)
2. Read MANUAL_DATA_GUIDE.md (8 min)
3. Try commands from QUICK_REFERENCE.md (5 min)
Total: 18 minutes
```

### "I want to post this on GitHub"
```
1. Make sure you have the code working
2. Read GITHUB_UPLOAD_GUIDE.md (5 min)
3. Follow the git workflow (10 min)
4. Verify push succeeded
Total: 15 minutes
```

---

## 🎬 Learning Path by Role

### Security Analyst
1. README.md - Understand architecture
2. QUICK_REFERENCE.md - Get up to speed
3. ADD_AND_MONITOR_DATA_GUIDE.md - Learn workflow
4. CUSTOM_DATA_PANEL_GUIDE.md - Master dashboard

### DevOps/Platform Engineer
1. QUICK_REFERENCE.md - Overview
2. README.md - Full architecture
3. DATASET_README.md - Understand data
4. GITHUB_UPLOAD_GUIDE.md - Deployment

### Data Scientist
1. README.md - Architecture section
2. DATASET_README.md - Data generation
3. Code files: agents/threat_detector.py
4. Experiment with custom datasets

### Project Manager
1. README.md - Overview section
2. QUICK_REFERENCE.md - Features summary
3. LINKEDIN_GUIDE.md - Promotion materials

---

## 📊 File Structure Guide

```
d:\Coding\Pj\
│
├── README.md                          ← Main project documentation
├── QUICK_REFERENCE.md                 ← Cheat sheet (start here!)
├── ADD_AND_MONITOR_DATA_GUIDE.md      ← Complete workflow guide
├── CUSTOM_DATA_PANEL_GUIDE.md         ← Dashboard features
├── MANUAL_DATA_GUIDE.md               ← CLI tool reference
├── GITHUB_UPLOAD_GUIDE.md             ← GitHub deployment
├── LINKEDIN_GUIDE.md                  ← Sharing on social media
├── DOCUMENTATION_MAP.md               ← This file (guide to guides!)
│
├── api_server.py                      ← Flask backend
├── data_injector.py                   ← CLI tool for data injection
├── run_pipeline.py                    ← Security pipeline
│
├── data/
│   └── raw_logs/
│       └── DATASET_README.md          ← Data generation guide
│
└── security-ui/                       ← Vue.js dashboard
    └── src/
        └── components/
            └── CustomDataPanel.vue    ← Data injection UI
```

---

## ✨ Pro Tips

1. **Just starting?** → Open QUICK_REFERENCE.md in one tab, README.md in another
2. **Need both UI and CLI?** → Read both guides but start with UI (easier)
3. **Stuck?** → Check "Troubleshooting" in ADD_AND_MONITOR_DATA_GUIDE.md
4. **Want examples?** → Look at test scenarios in ADD_AND_MONITOR_DATA_GUIDE.md
5. **Sharing project?** → Use LINKEDIN_GUIDE.md templates

---

## 🎯 Recommended Reading Order

```
Week 1: Getting Started
  Mon: QUICK_REFERENCE.md (5 min)
  Tue: ADD_AND_MONITOR_DATA_GUIDE.md (10 min)
  Wed: CUSTOM_DATA_PANEL_GUIDE.md (10 min)
  Thu: MANUAL_DATA_GUIDE.md (8 min)
  Fri: Run all test scenarios (30 min)
       Total: 1 hour

Week 2: Deep Dive
  Mon-Wed: README.md (30 min) + Study agents/ code (1 hour)
  Thu: DATASET_README.md (10 min)
  Fri: Create custom dataset (30 min)
       Total: 2.5 hours

Week 3: Sharing
  GITHUB_UPLOAD_GUIDE.md → Push to GitHub (15 min)
  LINKEDIN_GUIDE.md → Share your success (15 min)
  Total: 30 minutes
```

---

## 📞 If You Get Stuck...

1. **"How do I start?"** → QUICK_REFERENCE.md
2. **"Where's the dashboard?"** → CUSTOM_DATA_PANEL_GUIDE.md
3. **"What commands can I run?"** → MANUAL_DATA_GUIDE.md + QUICK_REFERENCE.md
4. **"Nothing's working"** → Check Troubleshooting in ADD_AND_MONITOR_DATA_GUIDE.md
5. **"How do I share this?"** → GITHUB_UPLOAD_GUIDE.md or LINKEDIN_GUIDE.md
6. **"Tell me everything"** → README.md

---

## 🏆 Success Checklist

After reading guides, you should be able to:

- [ ] Start the Flask backend (port 8000)
- [ ] Start the Vue.js frontend (port 5174)
- [ ] Add a threat via the dashboard
- [ ] Add a threat via CLI
- [ ] See threats appear in Live Monitor
- [ ] Create an incident
- [ ] Understand the 5-stage pipeline
- [ ] Explain threat levels (CRITICAL, HIGH, MEDIUM)
- [ ] Run all 4 test scenarios
- [ ] Deploy to GitHub (optional)

If you can do all of these, you've mastered the platform! 🎉

---

**Happy learning! 🚀**

**Read QUICK_REFERENCE.md next →**
