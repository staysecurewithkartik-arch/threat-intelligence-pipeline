================================================================================
WINDOWS VM - QUICK EXECUTION GUIDE
Download Files → Configure Git → Push to GitHub
Time: 30 minutes total
================================================================================

You have:
✅ GitHub repo created (threat-intelligence-pipeline)
✅ Git installed on VM
✅ Currently in VM browser

You need:
1. Download all files to VM
2. Configure git on VM (1 minute)
3. Push code to GitHub (5 minutes)

Let's GO!

================================================================================
STEP 1: DOWNLOAD ALL FILES TO VM (5 MINUTES)
================================================================================

You're in a browser right now looking at the outputs folder I created.

METHOD: Download as ZIP (Fastest)

WHAT YOU SEE IN BROWSER:
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
└─ All other files

STEPS TO DOWNLOAD:

1. In your browser, look for a DOWNLOAD button or ZIP option
   └─ Usually at top of file list

2. If you see a "Download All" button:
   ├─ Click it
   ├─ Choose location: Downloads folder
   └─ Wait for download to complete

3. If no download button, manually select files:
   ├─ Open File Explorer in VM
   ├─ Go to Downloads (or where you want files)
   ├─ Create new folder: threat-intel-pipeline
   ├─ Go back to browser
   ├─ Open EACH file in browser
   ├─ Right-click → Save As
   ├─ Save to: C:\Users\YourName\Downloads\threat-intel-pipeline\

   Files to download (21 total):
   - threat_intel_pipeline.py
   - threat_intel_pipeline_demo.py
   - sample_firewall_logs.txt
   - sample_email_headers.txt
   - sample_siem_alerts.txt
   - requirements.txt
   - README.md
   - GITHUB_SETUP.md
   - COMPLETE_PORTFOLIO_PROCESS.md
   - EXACT_COMMANDS.md
   - YOU_START_HERE.txt
   - PROJECT_HEADLINES.txt
   - TODAY_ROADMAP.md
   - _FILES_MANIFEST.txt
   - STAGE_1_2_WINDOWS_GUIDE.md
   - STEP_3_SUPER_DETAILED.md
   - README_FIRST.txt
   - INC-20260323072520_report.md
   - INC-20260323072520_report.json
   - And any other .md or .txt files you see

VERIFY DOWNLOAD:
├─ Open File Explorer
├─ Go to Downloads folder
├─ You should see all files there
└─ ✅ All files downloaded!

================================================================================
STEP 2: OPEN COMMAND PROMPT IN VM (1 MINUTE)
================================================================================

You need to navigate to your project folder and run git commands.

STEPS:

1. Press: Windows Key + R (opens Run dialog)
2. Type: cmd
3. Press: Enter
4. Black Command Prompt window opens

YOU SEE:
C:\Users\YourName>
_

5. Navigate to your files folder. Type:

   cd Downloads\threat-intel-pipeline

6. Press: Enter

YOU SHOULD SEE:
C:\Users\YourName\Downloads\threat-intel-pipeline>
_

VERIFY FILES ARE HERE:
7. Type: dir
8. Press: Enter
9. You should see all your files listed:
   - threat_intel_pipeline.py
   - sample_firewall_logs.txt
   - etc.

✅ YOU'RE IN THE RIGHT FOLDER!

================================================================================
STEP 3: CONFIGURE GIT (1 MINUTE) - QUICK VERSION
================================================================================

Two commands. Copy-paste each one.

COMMAND 1:
git config --global user.name "Kartik Sawant"

HOW:
1. Copy the command above
2. Right-click in Command Prompt
3. Paste
4. Press Enter

COMMAND 2:
git config --global user.email "kartiksawant31@gmail.com"

HOW:
1. Copy the command above
2. Right-click in Command Prompt
3. Paste
4. Press Enter

✅ GIT IS CONFIGURED!

================================================================================
STEP 4: INITIALIZE GIT IN YOUR FOLDER (1 MINUTE)
================================================================================

Now you're going to tell Git to track your files.

COMMAND:
git init

HOW:
1. Copy: git init
2. Right-click in Command Prompt
3. Paste
4. Press Enter

YOU SEE:
Initialized empty Git repository in C:\Users\YourName\Downloads\threat-intel-pipeline\.git

✅ GIT IS TRACKING YOUR FOLDER!

================================================================================
STEP 5: ADD ALL FILES TO GIT (1 MINUTE)
================================================================================

COMMAND:
git add .

(That's "git add" + SPACE + DOT)

HOW:
1. Copy: git add .
2. Right-click in Command Prompt
3. Paste
4. Press Enter

YOU SEE:
(Nothing appears - that's normal, no output means success)

✅ ALL FILES ARE STAGED!

================================================================================
STEP 6: CREATE FIRST COMMIT (1 MINUTE)
================================================================================

COMMAND:
git commit -m "Initial commit: Threat Intelligence Pipeline with Claude AI"

HOW:
1. Copy the command above
2. Right-click in Command Prompt
3. Paste
4. Press Enter

YOU SEE:
[main (root-commit) abc1234] Initial commit: Threat Intelligence Pipeline with Claude AI
 XX files changed, XXXX insertions(+)
 create mode 100644 threat_intel_pipeline.py
 etc...

✅ COMMIT IS CREATED!

================================================================================
STEP 7: CONNECT TO GITHUB (2 MINUTES)
================================================================================

Now you connect your LOCAL folder to your GITHUB repo.

COMMAND (REPLACE YOUR_USERNAME):

git remote add origin https://github.com/YOUR_USERNAME/threat-intelligence-pipeline.git

EXAMPLE (if your username is "kartiksawant31"):

git remote add origin https://github.com/kartiksawant31/threat-intelligence-pipeline.git

HOW:
1. Replace YOUR_USERNAME with your actual GitHub username
2. Copy the full command
3. Right-click in Command Prompt
4. Paste
5. Press Enter

YOU SEE:
(Nothing appears - that's normal, no output means success)

✅ CONNECTED TO GITHUB!

================================================================================
STEP 8: RENAME BRANCH (1 MINUTE)
================================================================================

COMMAND:
git branch -M main

HOW:
1. Copy: git branch -M main
2. Right-click in Command Prompt
3. Paste
4. Press Enter

YOU SEE:
(Nothing appears - that's normal)

✅ BRANCH RENAMED!

================================================================================
STEP 9: PUSH TO GITHUB (THE BIG MOMENT!) (5 MINUTES)
================================================================================

This uploads your code to GitHub!

COMMAND:
git push -u origin main

HOW:
1. Copy: git push -u origin main
2. Right-click in Command Prompt
3. Paste
4. Press Enter

IT WILL ASK FOR CREDENTIALS:

You'll see:
username for 'https://github.com': 

TYPE YOUR GITHUB USERNAME:
kartiksawant31
(Press Enter)

Then it asks:
password for 'https://kartiksawant31@github.com': 

PASTE YOUR GITHUB TOKEN (you saved in notepad earlier):
The long code like: ghp_abc123xyz...
(Right-click to paste)
(Press Enter)

WAIT... it uploads...

YOU'LL SEE:
Enumerating objects: XX, done.
Counting objects: XX%, done.
Writing objects: XX%, done.
Total XX (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/kartiksawant31/threat-intelligence-pipeline.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.

✅ YOUR CODE IS ON GITHUB!!!

================================================================================
STEP 10: VERIFY ON GITHUB (1 MINUTE)
================================================================================

Open browser and go to:
https://github.com/YOUR_USERNAME/threat-intelligence-pipeline

(Replace YOUR_USERNAME)

EXAMPLE:
https://github.com/kartiksawant31/threat-intelligence-pipeline

YOU SHOULD SEE:
✅ All your files listed
✅ README.md rendered nicely
✅ Your description at top
✅ Green "Code" button

✅ YOUR PROJECT IS LIVE AND PUBLIC!

================================================================================
FINAL CHECKLIST
================================================================================

□ Downloaded all files to VM
□ Opened Command Prompt in VM
□ Navigated to project folder
□ Configured git (user.name and user.email)
□ Ran: git init
□ Ran: git add .
□ Ran: git commit -m "..."
□ Ran: git remote add origin
□ Ran: git branch -M main
□ Ran: git push -u origin main
□ Verified on GitHub (opened in browser)

================================================================================
YOU'RE DONE WITH STAGES 1-3! 🎉
================================================================================

What you accomplished:
✅ Downloaded files to VM
✅ Configured Git
✅ Pushed code to GitHub
✅ Project is LIVE and PUBLIC

Next: STAGE 4 (Test with real data)

Tell me: "✅ STAGES 1-3 COMPLETE - Code is on GitHub"

Then I'll guide you through STAGE 4 (running the pipeline with your data).

================================================================================
TOTAL TIME: 30 minutes
RESULT: Production-ready project on public GitHub

You're KILLING IT, Kartik! 🚀

================================================================================
