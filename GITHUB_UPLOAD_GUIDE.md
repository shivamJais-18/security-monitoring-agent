# GitHub Upload Guide

## Step-by-Step Instructions to Upload Your Project

### Prerequisites
- GitHub account (create one at https://github.com if needed)
- Git installed on your computer (download from https://git-scm.com)
- Administrator access to your system

### Step 1: Install Git

If Git is not installed:
1. Visit https://git-scm.com/download/win (for Windows)
2. Download the installer
3. Run it and follow the installation wizard
4. Select "Use Git from the command line" during installation
5. Restart your terminal/PowerShell after installation

### Step 2: Configure Git (First Time Only)

Open PowerShell and run:
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Example:
```powershell
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
```

### Step 3: Create a GitHub Repository

1. Go to https://github.com/new
2. Create a new repository:
   - **Repository name**: `security-monitoring-platform` (or your preferred name)
   - **Description**: "A comprehensive security monitoring and threat detection system with real-time dashboard"
   - **Public** or **Private** (choose based on preference)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click **"Create repository"**
4. Copy the HTTPS URL (looks like: `https://github.com/YOUR_USERNAME/security-monitoring-platform.git`)

### Step 4: Initialize Git in Your Project

Open PowerShell and navigate to your project:
```powershell
cd d:\Coding\Pj
```

Initialize git:
```powershell
git init
```

### Step 5: Add Files to Git

Add all files:
```powershell
git add .
```

Verify files are staged:
```powershell
git status
```

You should see a list of files ready to commit (in green).

### Step 6: Create Initial Commit

```powershell
git commit -m "Initial commit: Security monitoring platform with threat detection and dashboard"
```

### Step 7: Connect to GitHub Repository

Replace the URL with your repository URL from Step 3:
```powershell
git remote add origin https://github.com/YOUR_USERNAME/security-monitoring-platform.git
```

Example:
```powershell
git remote add origin https://github.com/johndoe/security-monitoring-platform.git
```

Verify the connection:
```powershell
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/security-monitoring-platform.git (fetch)
origin  https://github.com/YOUR_USERNAME/security-monitoring-platform.git (push)
```

### Step 8: Push to GitHub

First, rename the default branch to `main` (GitHub standard):
```powershell
git branch -M main
```

Push your code:
```powershell
git push -u origin main
```

This will prompt for authentication. Follow the GitHub authentication flow:

#### Option A: Personal Access Token (Recommended)
1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Select `repo` scope
4. Copy the token
5. When prompted in terminal, paste the token as password

#### Option B: GitHub CLI
If using GitHub CLI, you can authenticate with:
```powershell
gh auth login
```

### Step 9: Verify Upload

1. Go to your GitHub repository: `https://github.com/YOUR_USERNAME/security-monitoring-platform`
2. Verify all files are there
3. Check that README.md is displayed

---

## Complete Command List (Quick Reference)

```powershell
# Navigate to project
cd d:\Coding\Pj

# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init

# Check status
git status

# Stage all files
git add .

# Create commit
git commit -m "Initial commit: Security monitoring platform"

# Add remote (replace URL)
git remote add origin https://github.com/YOUR_USERNAME/security-monitoring-platform.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## After Initial Upload: Making Updates

To update your code on GitHub after initial upload:

```powershell
# Check what changed
git status

# Stage changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

---

## Common Git Commands

### Check Status
```powershell
git status          # See which files changed
git log             # View commit history
git diff            # Show exactly what changed
```

### Undo Changes
```powershell
git restore .       # Undo all unstaged changes
git reset --hard    # Discard all local changes
```

### Branches
```powershell
git branch          # List branches
git branch feature  # Create new branch
git checkout feature # Switch to branch
git merge feature    # Merge branch to main
```

### Working with Remote
```powershell
git pull            # Download latest from GitHub
git push            # Upload your changes
git remote show origin # See remote details
```

---

## Troubleshooting

### Issue: "fatal: not a git repository"
**Solution:**
```powershell
cd d:\Coding\Pj
git init
```

### Issue: "fatal: 'origin' does not appear to be a 'git' repository"
**Solution:**
```powershell
# Check if remote exists
git remote -v

# If not, add it
git remote add origin YOUR_REPO_URL

# Or if it exists but wrong URL, update it
git remote set-url origin YOUR_REPO_URL
```

### Issue: Authentication Failed
**Solution:**
1. Check your GitHub username and email match:
   ```powershell
   git config --global user.name
   git config --global user.email
   ```
2. For HTTPS, use a Personal Access Token (not your password)
3. Or use SSH keys (more advanced)

### Issue: Changes not being pushed
**Solution:**
```powershell
# Make sure you committed
git status

# If files are unstaged, add them
git add .

# Then commit
git commit -m "Your message"

# Then push
git push origin main
```

### Issue: Large files being rejected
**Solution:** The `.gitignore` we created should prevent this. Verify:
```powershell
git status

# Remove files from git index if accidentally added
git rm --cached data/raw_logs/*.json
git commit -m "Remove large log files"
git push
```

---

## Project Structure on GitHub

Your repository will contain:
```
security-monitoring-platform/
├── .gitignore                   # Files to ignore
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
├── api_server.py               # Flask backend
├── run_pipeline.py             # Security pipeline
├── data_injector.py            # CLI tool
├── agents/                     # AI agents
├── data/                       # Data (logs excluded by .gitignore)
├── security-ui/                # Vue.js frontend
├── utils/                      # Utilities
├── MANUAL_DATA_GUIDE.md        # Data injection guide
└── CUSTOM_DATA_PANEL_GUIDE.md  # Dashboard guide
```

---

## Next Steps

After uploading to GitHub:

1. **Share the link**: Send `https://github.com/YOUR_USERNAME/security-monitoring-platform` to others
2. **Collaborators**: Go to Settings → Collaborators to add team members
3. **Issues**: Use GitHub Issues tab to track bugs and features
4. **Releases**: Create releases for stable versions
5. **GitHub Pages**: Optional - host documentation
6. **Actions**: Optional - set up CI/CD pipeline

---

## GitHub Best Practices

✅ **DO:**
- Commit frequently with clear messages
- Use `.gitignore` to exclude large files
- Write descriptive README
- Use branches for features
- Write good commit messages

❌ **DON'T:**
- Commit API keys or passwords
- Commit large binary files
- Push work-in-progress without commits
- Use unclear commit messages like "fix stuff"
- Store secrets in code

---

## Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [GitHub CLI](https://cli.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

---

## Summary

After following these steps:
✅ Your project will be on GitHub
✅ You can share it with others
✅ Version control is set up
✅ You can collaborate with team members
✅ You have a backup of your code

**Good luck! 🚀**
