================================================================================
STAGE 1 & 2 EXECUTION GUIDE - WINDOWS
Kartik's Real-Time Walkthrough
================================================================================

You have your folder on Desktop with all files.
Let's execute STAGE 1 (Understanding) and STAGE 2 (Setup) RIGHT NOW.

================================================================================
STAGE 1: UNDERSTAND (30 MINUTES) - DO THIS FIRST
================================================================================

⏱️ TIMER: 30 minutes

STEP 1: Read README_FIRST.txt (5 minutes)
├─ Location: Desktop/project1/README_FIRST.txt
├─ Open with: Any text editor (Notepad, Word, VS Code)
├─ Why: It tells you what to read
└─ Focus on: The timeline and reading order

STEP 2: Read YOU_START_HERE.txt (10 minutes)
├─ Location: Desktop/project1/YOU_START_HERE.txt
├─ This is your overview document
├─ Why: Explains everything in simple terms
└─ Focus on: Understanding the 5 stages and why each matters

STEP 3: Read TODAY_ROADMAP.md (5 minutes)
├─ Location: Desktop/project1/TODAY_ROADMAP.md
├─ This is YOUR plan for today
├─ Why: Shows exact timing and what you'll accomplish
└─ Focus on: The 5-stage timeline (4 hours 20 minutes)

STEP 4: Skim EXACT_COMMANDS.md (10 minutes)
├─ Location: Desktop/project1/EXACT_COMMANDS.md
├─ Don't memorize, just familiarize yourself
├─ Why: See what commands are coming
└─ Focus on: The structure (you'll follow this next)

✅ AFTER READING STAGE 1:
You will know:
├─ Why you're building this (CTI portfolio)
├─ What each stage does
├─ How GitHub works
├─ Why this matters for your career
└─ Complete roadmap for today

================================================================================
STAGE 2: SETUP (20 MINUTES) - DO THIS NOW
================================================================================

⏱️ TIMER: 20 minutes

You'll:
1. Create GitHub account (online)
2. Install Git on Windows
3. Configure Git
4. Create API token
5. Organize your files

---

STEP 1: CREATE GITHUB ACCOUNT (2 minutes)
══════════════════════════════════════════

1. Open browser (Chrome, Edge, Firefox)
2. Go to: https://github.com/signup
3. Fill in:
   ├─ Username: kartiksawant31
   ├─ Email: kartiksawant31@gmail.com
   ├─ Password: Choose something strong!
   │  └─ Example: Th!sMust8BeStr0ng2024
   └─ Agree to terms
4. Click "Create account"
5. Verify your email (check inbox)

✅ YOU NOW HAVE: GitHub account

---

STEP 2: INSTALL GIT ON WINDOWS (10 minutes)
════════════════════════════════════════════

OPTION A: Quick Check (1 minute)
├─ Press: Windows Key + R
├─ Type: cmd
├─ Click OK (opens Command Prompt)
├─ Type: git --version
├─ If you see "git version 2.x.x" → SKIP TO STEP 3
└─ If error → Continue to Option B

OPTION B: Install Git (10 minutes if needed)
├─ Go to: https://git-scm.com/downloads
├─ Click: Windows (blue button)
├─ Download starts automatically
├─ Find downloaded file (usually in Downloads folder)
├─ Double-click the .exe file
├─ Click "Run" if prompted
├─ Click "Next" multiple times (all defaults are fine)
├─ Click "Install"
├─ Click "Finish"
├─ Wait for installation to complete

VERIFY GIT IS INSTALLED:
├─ Press: Windows Key + R
├─ Type: cmd
├─ Click OK
├─ Type: git --version
├─ You should see: "git version 2.x.x"
└─ ✅ Git is installed!

✅ YOU NOW HAVE: Git installed on Windows

---

STEP 3: CONFIGURE GIT (1 minute)
════════════════════════════════

1. Press: Windows Key + R
2. Type: cmd
3. Click OK (opens Command Prompt)
4. Copy and paste this (replace with YOUR info):

   git config --global user.name "Kartik Sawant"

5. Press Enter
6. Copy and paste this:

   git config --global user.email "kartiksawant31@gmail.com"

7. Press Enter
8. Type: git config --global user.name
9. Press Enter
10. You should see: "Kartik Sawant"

✅ GIT KNOWS WHO YOU ARE

---

STEP 4: CREATE GITHUB PERSONAL ACCESS TOKEN (5 minutes)
═══════════════════════════════════════════════════════

This is like a password for Git to talk to GitHub.

1. Go to browser
2. Go to: https://github.com/settings/tokens/new
3. Login if prompted
4. Fill in:
   ├─ Token name: threat-intel-pipeline
   ├─ Expiration: 90 days
   ├─ Scopes: Click checkbox for "repo"
   └─ Click "Generate token"
5. YOU'LL SEE A LONG CODE (like: ghp_abc123xyz...)
6. COPY THIS CODE (very important!)
7. Paste it in a notepad file for now:
   ├─ Press Windows Key
   ├─ Type: notepad
   ├─ Click Notepad
   ├─ Paste the token
   ├─ Save as: github_token.txt on Desktop
   └─ Keep this file safe!

⚠️ IMPORTANT: You won't see this token again!

✅ YOU NOW HAVE: GitHub authentication token

---

STEP 5: ORGANIZE YOUR FOLDER (2 minutes)
═════════════════════════════════════════

Your folder should have these files:

Desktop/project1/
├─ threat_intel_pipeline.py
├─ threat_intel_pipeline_demo.py
├─ sample_firewall_logs.txt
├─ sample_email_headers.txt
├─ sample_siem_alerts.txt
├─ requirements.txt
├─ README.md
├─ GITHUB_SETUP.md
├─ COMPLETE_PORTFOLIO_PROCESS.md
├─ EXACT_COMMANDS.md
├─ YOU_START_HERE.txt
└─ README_FIRST.txt

If missing any files, download them from outputs again.

✅ STAGE 2 IS COMPLETE!

================================================================================
AFTER STAGE 2: YOU HAVE EVERYTHING READY
================================================================================

✅ GitHub account created
✅ Git installed on Windows
✅ Git configured with your name/email
✅ GitHub token created and saved
✅ Project files organized
✅ You're ready for STAGE 3

================================================================================
NEXT: STAGE 3 (DEPLOY TO GITHUB)
================================================================================

Time: 15 minutes

You will:
1. Create GitHub repository online
2. Open Command Prompt in your project folder
3. Run Git commands to push your code to GitHub
4. Verify it's live

Tell me when STAGE 2 is complete, and I'll give you STAGE 3 commands.

================================================================================
QUICK CHECKLIST - STAGE 2
================================================================================

□ Read README_FIRST.txt
□ Read YOU_START_HERE.txt
□ Read TODAY_ROADMAP.md
□ Skim EXACT_COMMANDS.md
□ Created GitHub account (github.com/signup)
□ Installed Git on Windows
□ Configured Git (git config commands)
□ Created GitHub personal access token
□ Saved token in notepad file
□ Organized project folder

================================================================================
YOU'RE ALMOST READY!
================================================================================

You've now:
✓ Understood the full vision (STAGE 1)
✓ Set up everything on your computer (STAGE 2)

Next:
✓ Push code to GitHub (STAGE 3)
✓ Test with data (STAGE 4)
✓ Tell recruiters (STAGE 5)

All happening TODAY.

================================================================================
TELL ME WHEN YOU'RE DONE WITH STAGE 2
================================================================================

Once you complete all the checkboxes above, tell me:

"✅ STAGE 2 COMPLETE - Ready for STAGE 3"

Then I'll give you the exact STAGE 3 commands to push your code to GitHub.

Your project will be LIVE within 15 minutes after that.

Let's go! 🚀

================================================================================
