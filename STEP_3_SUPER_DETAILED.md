================================================================================
STEP 3: CONFIGURE GIT ON WINDOWS
SUPER DETAILED - LIKE YOU'RE A COMPLETE BEGINNER
================================================================================

We're going to:
1. Open Command Prompt (the black window where you type)
2. Type 2 commands
3. Verify it worked

That's it. Very simple.

Let's go step by step.

================================================================================
PART A: OPEN COMMAND PROMPT
================================================================================

⏱️ Time: 1 minute

CLICK 1: Open Command Prompt
├─ Look at your Windows desktop
├─ Find the Windows logo button (bottom left corner of screen)
│  └─ It looks like 4 squares: ⊞
├─ Click it once
└─ You'll see a menu appear

If you can't find it:
├─ Look at the TASKBAR (bottom of your screen)
├─ The Windows logo should be there on the left side
└─ Click it

WHAT IT LOOKS LIKE:
┌─────────────────────────────────────────┐
│  Windows Menu appears with lots of apps │
│  and a search box at top                 │
└─────────────────────────────────────────┘

CLICK 2: Type "cmd" in the search box
├─ Look at the top of the menu
├─ There's a white box that says "Type here to search"
├─ Click in that box
└─ A cursor will appear (blinking line)

WHAT IT LOOKS LIKE:
┌────────────────────────────────────────┐
│ [Type here to search]  ← Click here    │
│                                         │
│ Results will appear below               │
└────────────────────────────────────────┘

CLICK 3: Type "cmd"
├─ Your keyboard is now ready to type
├─ Type the letters: c m d
├─ You should see "cmd" appear in the search box
└─ Don't press anything yet, just type

WHAT IT LOOKS LIKE:
┌────────────────────────────────────────┐
│ [cmd]  ← The letters appear here       │
│                                         │
│ Command Prompt appears below            │
│ (black icon)                            │
└────────────────────────────────────────┘

CLICK 4: Click "Command Prompt"
├─ Below the search box, you'll see a result
├─ It says "Command Prompt" with a black icon
├─ Click on it
└─ A BLACK WINDOW will open

WHAT IT LOOKS LIKE:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │ ← Blinking cursor here
│ _                                       │
│                                         │
│ (empty black window)                    │
│                                         │
└─────────────────────────────────────────┘

✅ YOU NOW HAVE: Command Prompt open (black window)

The > symbol means it's ready for you to type commands.

================================================================================
PART B: TYPE COMMAND #1
================================================================================

⏱️ Time: 1 minute

Now you have a black window open. This is Command Prompt.

COMMAND #1: Configure Git Name

You're going to type ONE line that tells Git who you are.

COPY THIS EXACTLY (it's long):

git config --global user.name "Kartik Sawant"

Here's how:

OPTION 1: Copy-Paste (EASIEST - I RECOMMEND THIS)
├─ Select the entire text above: git config --global user.name "Kartik Sawant"
├─ Right-click it
├─ Choose "Copy"
├─ Click in the black Command Prompt window
├─ Right-click
├─ Choose "Paste"
├─ The text appears in the black window
└─ Press Enter (big key on keyboard)

OPTION 2: Type it manually
├─ Click in the black window
├─ Type exactly: git config --global user.name "Kartik Sawant"
│  └─ Be careful with spaces and quotes!
├─ Press Enter

WHAT IT LOOKS LIKE AFTER YOU PASTE AND PRESS ENTER:

BEFORE:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ _                                       │
└─────────────────────────────────────────┘

AFTER YOU PASTE:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ git config --global user.name "Kartik S │
│ awant"                                  │
│ _                                       │
└─────────────────────────────────────────┘

AFTER YOU PRESS ENTER:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ git config --global user.name "Kartik S │
│ awant"                                  │
│ C:\Users\YourName>                      │ ← New line, ready for next command
│ _                                       │
└─────────────────────────────────────────┘

✅ NOTICE: No error message = SUCCESS!
✅ You see a new prompt (C:\Users\YourName>) = It worked!

If you see something like "command not found", it means Git isn't installed.
Go back and install Git first.

================================================================================
PART C: TYPE COMMAND #2
================================================================================

⏱️ Time: 1 minute

Now you're going to type the SECOND command.

COPY THIS EXACTLY:

git config --global user.email "kartiksawant31@gmail.com"

STEPS (same as Command #1):

OPTION 1: Copy-Paste (EASIEST)
├─ Select the text: git config --global user.email "kartiksawant31@gmail.com"
├─ Right-click → Copy
├─ Click in black window
├─ Right-click → Paste
├─ Press Enter

OPTION 2: Type manually
├─ Type: git config --global user.email "kartiksawant31@gmail.com"
├─ Be careful with spaces and quotes
├─ Press Enter

WHAT IT LOOKS LIKE:

BEFORE:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ _                                       │
└─────────────────────────────────────────┘

AFTER BOTH COMMANDS:
┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ git config --global user.name "Kartik S │
│ awant"                                  │
│ C:\Users\YourName>                      │
│ git config --global user.email "kartik  │
│ sawant31@gmail.com"                     │
│ C:\Users\YourName>                      │
│ _                                       │
└─────────────────────────────────────────┘

✅ SUCCESS: No errors = Git is configured!

================================================================================
PART D: VERIFY IT WORKED (OPTIONAL BUT GOOD TO CHECK)
================================================================================

⏱️ Time: 1 minute

Let's verify Git knows your name.

TYPE THIS COMMAND:

git config --global user.name

HOW:
├─ Copy: git config --global user.name
├─ Paste in black window
├─ Press Enter

WHAT SHOULD HAPPEN:

┌─────────────────────────────────────────┐
│ C:\Users\YourName>                      │
│ git config --global user.name           │
│ Kartik Sawant                           │ ← This should appear!
│ C:\Users\YourName>                      │
│ _                                       │
└─────────────────────────────────────────┘

If you see "Kartik Sawant" = ✅ PERFECT!
It means Git knows your name.

================================================================================
SUMMARY OF WHAT YOU JUST DID
================================================================================

You typed 2 commands in Command Prompt:

COMMAND 1: git config --global user.name "Kartik Sawant"
└─ This tells Git: "Your name is Kartik Sawant"

COMMAND 2: git config --global user.email "kartiksawant31@gmail.com"
└─ This tells Git: "Your email is kartiksawant31@gmail.com"

Now Git knows WHO YOU ARE.

When you push code to GitHub later, Git will say: "This code is from Kartik Sawant"

================================================================================
NEXT STEPS
================================================================================

✅ STEP 3 COMPLETE: Git is configured!

You can close the black Command Prompt window now:
├─ Type: exit
├─ Press Enter
└─ The window closes

Or just click the X button.

NEXT: STEP 4 (Create GitHub Token)
└─ Tell me when you're ready and I'll guide you through it!

================================================================================
CHECKLIST - STEP 3
================================================================================

□ Opened Command Prompt (black window)
□ Typed Command #1 (git config --global user.name "Kartik Sawant")
□ Pressed Enter
□ Typed Command #2 (git config --global user.email "kartiksawant31@gmail.com")
□ Pressed Enter
□ Verified with: git config --global user.name
□ Saw "Kartik Sawant" appear
□ Closed Command Prompt (optional)

================================================================================
YOU'RE DONE WITH STEP 3!
================================================================================

Great job! You just configured Git.

Tell me: "✅ STEP 3 COMPLETE"

Then I'll guide you through STEP 4 (Creating GitHub Token) with the same detail.

================================================================================
