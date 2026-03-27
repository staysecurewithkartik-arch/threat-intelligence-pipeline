================================================================================
EXACT COMMANDS TO RUN - COPY & PASTE READY
================================================================================

Kartik, these are the EXACT commands you'll run. Just copy and paste them.
No typing needed. Follow in order.

================================================================================
PREREQUISITES (Do These First Once)
================================================================================

STEP 1: Create GitHub Account
├─ Open browser: https://github.com/signup
├─ Fill form:
│  ├─ Username: kartiksawant31 (or your preferred name)
│  ├─ Email: kartiksawant31@gmail.com
│  ├─ Password: Strong password (8+ chars, mix of letters/numbers/symbols)
│  └─ Agree to terms
├─ Verify email
└─ DONE - You now have GitHub account

STEP 2: Install Git (If Not Already Installed)
├─ Check if installed:
│  Open terminal/command prompt and run:
│  
│  git --version
│
├─ If you see "git version 2.x.x" → SKIP TO STEP 3
├─ If error or not found → Download and install:
│  └─ Windows: https://git-scm.com/downloads
│  └─ Mac: brew install git (or https://git-scm.com/downloads)
│  └─ Linux: sudo apt install git
│
└─ Verify after install: git --version

STEP 3: Configure Git (First Time Only)
├─ Open terminal/command prompt
├─ Run this command (replace with YOUR name):
│
│  git config --global user.name "Kartik Sawant"
│
├─ Run this command (replace with YOUR email):
│
│  git config --global user.email "kartiksawant31@gmail.com"
│
└─ These tell Git who you are

STEP 4: Create GitHub Personal Access Token
├─ Why? GitHub now requires tokens instead of passwords for Git operations
├─ Go to: https://github.com/settings/tokens/new
├─ Settings:
│  ├─ Token name: "threat-intel-pipeline"
│  ├─ Expiration: 90 days
│  ├─ Scopes: Check "repo" (full control of private repositories)
│  └─ Click "Generate token"
├─ COPY the token (you'll use it in Step 8)
├─ IMPORTANT: Save it somewhere safe - you won't see it again!
└─ DONE

================================================================================
MAIN DEPLOYMENT (These Are The Real Steps)
================================================================================

STEP 5: Prepare Local Folder
├─ Open terminal/command prompt
├─ Navigate to your Downloads (or preferred location):
│
│  cd ~/Downloads
│  (or: cd Desktop)
│  (or: cd Documents)
│
├─ Create project folder:
│
│  mkdir threat-intel-pipeline
│
├─ Navigate into it:
│
│  cd threat-intel-pipeline
│
├─ Put all the project files here:
│  ├─ threat_intel_pipeline.py
│  ├─ threat_intel_pipeline_demo.py
│  ├─ sample_firewall_logs.txt
│  ├─ sample_email_headers.txt
│  ├─ sample_siem_alerts.txt
│  ├─ requirements.txt
│  ├─ README.md
│  ├─ GITHUB_SETUP.md
│  └─ All other files
│
└─ DONE - Folder ready

STEP 6: Create GitHub Repository (Online)
├─ Go to: https://github.com/new
├─ Fill in:
│  ├─ Repository name: threat-intelligence-pipeline
│  ├─ Description: "AI-powered threat intelligence automation with Claude. Ingests firewall logs, email headers, and SIEM alerts → correlates IOCs → generates risk-scored incident reports with MITRE ATT&CK mapping."
│  ├─ Visibility: PUBLIC ⚠️ MUST BE PUBLIC!
│  ├─ Initialize: None (don't check "Add README" - you have one)
│  └─ Click "Create repository"
│
├─ You'll see this on the next page:
│  "Quick setup - if you've done this kind of thing before"
│
└─ DONE - Empty repo created

STEP 7: Initialize Local Git Repository
├─ In your terminal, you should still be in ~/threat-intel-pipeline/
├─ Run:
│
│  git init
│
├─ Output: "Initialized empty Git repository in /path/to/threat-intel-pipeline/.git"
└─ DONE

STEP 8: Add Your Files to Git
├─ Run:
│
│  git add .
│
├─ This stages all files for commit
├─ The dot (.) means "all files in current folder"
└─ DONE (no output usually means success)

STEP 9: Create First Commit
├─ Run:
│
│  git commit -m "Initial commit: Threat Intelligence Pipeline with Claude AI"
│
├─ Output will show:
│  - Files changed: X files
│  - Insertions: +X
│  └─ This is normal!
│
└─ DONE

STEP 10: Add GitHub as Remote
├─ Go back to GitHub (https://github.com/new after you created repo)
├─ Look for: "…or push an existing repository from the command line"
├─ You'll see something like:
│
│  git remote add origin https://github.com/YOUR_USERNAME/threat-intelligence-pipeline.git
│
├─ Copy that line (with YOUR actual username)
├─ Paste it in terminal:
│
│  git remote add origin https://github.com/kartiksawant31/threat-intelligence-pipeline.git
│
│  (Replace kartiksawant31 with your GitHub username)
│
└─ DONE

STEP 11: Rename Branch to Main (First Time Only)
├─ Run:
│
│  git branch -M main
│
├─ This renames your default branch to 'main' (GitHub standard)
└─ DONE

STEP 12: Push Code to GitHub (The Big Moment!)
├─ Run:
│
│  git push -u origin main
│
├─ First time, it will ask for authentication:
│  ├─ Username: your GitHub username (kartiksawant31)
│  ├─ Password: paste your Personal Access Token (from Step 4)
│  └─ (The token is your "password" now)
│
├─ Wait for it to finish
├─ Output will show something like:
│  "Branch 'main' set up to track remote branch 'main' from 'origin'."
│
└─ DONE - Your code is on GitHub!

================================================================================
VERIFY IT WORKED
================================================================================

STEP 13: Check GitHub (Visual Confirmation)
├─ Open browser
├─ Go to: https://github.com/YOUR_USERNAME/threat-intelligence-pipeline
│  (Replace YOUR_USERNAME with your actual username)
│
├─ You should see:
│  ├─ All your files listed
│  ├─ README.md rendered (nice formatting)
│  ├─ "threat_intel_pipeline.py" visible
│  ├─ "sample_*.txt" files visible
│  └─ Green "Code" button
│
└─ SUCCESS! Project is public on GitHub

STEP 14: Test the Code Works
├─ Back in terminal (in ~/threat-intel-pipeline/)
├─ Test demo version (no API needed):
│
│  python threat_intel_pipeline_demo.py
│
├─ Should output:
│  - "THREAT INTELLIGENCE PIPELINE - DEMO"
│  - "Generating demo incident report..."
│  - "Risk Score: 95/100"
│  - Files saved: INC-*.json and INC-*.md
│
└─ DONE - Code works!

================================================================================
FUTURE UPDATES (After Initial Push)
================================================================================

When you make changes (test with real data, customize code, etc.):

STEP A: Check What Changed
├─ Run:
│
│  git status
│
├─ Shows files that changed
└─ DONE

STEP B: Stage Changes
├─ Run:
│
│  git add .
│
└─ DONE

STEP C: Commit Changes
├─ Run (replace message with your actual change):
│
│  git commit -m "Add real Sophos logs, test with production data"
│
├─ Or:
│
│  git commit -m "Customize risk scoring logic"
│
└─ DONE

STEP D: Push to GitHub
├─ Run:
│
│  git push
│
├─ Your changes now visible on GitHub
└─ DONE

Repeat A-D whenever you update the project.

================================================================================
TROUBLESHOOTING (If Something Goes Wrong)
================================================================================

Problem 1: "fatal: not a git repository"
├─ You're not in the project folder
├─ Fix: cd ~/threat-intel-pipeline/ (or wherever you put it)

Problem 2: "git: command not found"
├─ Git not installed
├─ Fix: Install Git (see Step 2 above)

Problem 3: "Permission denied (publickey)" when pushing
├─ SSH key issue (advanced)
├─ Fix: Use HTTPS token instead (we're using that, so skip this)

Problem 4: Authentication keeps failing
├─ Wrong username or token
├─ Fix: 
│  ├─ Verify GitHub username (look at profile URL)
│  ├─ Verify token is from Step 4 (not old password)
│  └─ Try: git config --global credential.helper wincred (Windows)

Problem 5: Files not showing on GitHub
├─ Didn't push successfully
├─ Fix: Run: git push (try again)
├─ Or check: git status (to see what's not pushed)

Problem 6: README.md not rendering nicely
├─ GitHub can take 30 seconds to refresh
├─ Fix: Refresh browser (F5 or Cmd+R)

Problem 7: "origin" already exists
├─ You ran "git remote add origin" twice
├─ Fix: Run: git remote remove origin
│       Then run: git remote add origin https://... again

================================================================================
MINIMAL COMMANDS (Just Copy & Paste These)
================================================================================

If you just want the bare minimum:

1. Create GitHub account: https://github.com/signup

2. Install Git: https://git-scm.com/downloads

3. In terminal:
   
   git config --global user.name "Kartik Sawant"
   git config --global user.email "kartiksawant31@gmail.com"

4. Create repo online: https://github.com/new
   Name: threat-intelligence-pipeline
   Visibility: PUBLIC
   Initialize: None

5. In terminal (replace kartiksawant31 with YOUR username):
   
   cd ~/Downloads/threat-intel-pipeline
   git init
   git add .
   git commit -m "Initial commit: Threat Intelligence Pipeline with Claude AI"
   git remote add origin https://github.com/kartiksawant31/threat-intelligence-pipeline.git
   git branch -M main
   git push -u origin main

6. When it asks for password: paste your GitHub token (from https://github.com/settings/tokens/new)

7. Check: https://github.com/kartiksawant31/threat-intelligence-pipeline

Done!

================================================================================
WHAT HAPPENS AFTER YOU PUSH
================================================================================

Your GitHub repo now has:
✓ All project files visible
✓ README.md showing project description
✓ Code readable to anyone
✓ Can share link: github.com/YOUR_USERNAME/threat-intelligence-pipeline
✓ Can clone it: git clone https://github.com/YOUR_USERNAME/threat-intelligence-pipeline.git

Recruiters can now:
✓ See your code
✓ Check code quality
✓ Verify it's a real project
✓ See it's production-ready

This is your proof.

================================================================================
NEXT STEPS AFTER DEPLOYING
================================================================================

1. Test with Your Data
   ├─ Get your Sophos logs
   ├─ Get Claude API key (console.anthropic.com)
   ├─ Run: export ANTHROPIC_API_KEY="sk-ant-..."
   ├─ Run: python threat_intel_pipeline.py (with your data)
   └─ Commit results: git add . && git commit -m "..."

2. Add to LinkedIn
   ├─ LinkedIn profile → Add "Projects" section
   ├─ Title: "Threat Intelligence Pipeline with Claude AI"
   ├─ Link to GitHub
   ├─ Add description and screenshot of report

3. Reference in Job Applications
   ├─ Resume: Add "Projects" section with GitHub link
   ├─ Cover letter: "I've built a threat intelligence pipeline..."
   ├─ Application: Include GitHub link

4. Practice Interview Explanation
   ├─ 30-second version
   ├─ 2-minute version
   ├─ Ask yourself questions and answer them

5. Keep Improving
   ├─ Add features
   ├─ Integrate threat feeds
   ├─ Build dashboard
   ├─ Each change = new commit = proof of ongoing work

================================================================================
YOU'RE READY
================================================================================

You now have:
✓ Complete commands to run
✓ Exact steps in order
✓ Troubleshooting guide
✓ Verification steps

Next: Do Phase 2 (Setup) and Phase 3 (Deploy)

It takes 30 minutes.

Then your project is on GitHub.

Then you tell recruiters about it.

Then you get called for interviews.

Then you explain it and get the job.

That's the path.

Ready? Start with creating your GitHub account.

Then come back and run the commands above.

✅ You've got this, Kartik.

================================================================================
