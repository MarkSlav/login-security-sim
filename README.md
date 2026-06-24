
Create a beginner-friendly Python example that demonstrates the combined use of:

Boolean variables
Boolean conditional statements
Compound Boolean expressions (and, or, not)
Comparison operators (==, !=, >, <, >=, <=)
The if, elif, and else decision structure

Example:

if grade >= 70:
    print("Passed")
elif grade >= 50:
    print("Recovery")
else:
    print("Failed")

You may use a different example if it better demonstrates the concepts.


Step 1: Real-World Scenario

The problem: Security Operations Centers (SOCs) constantly monitor login attempts to detect potential brute-force attacks or unauthorized access. A simple but real defense mechanism is login attempt monitoring with lockout logic — if someone fails to log in too many times, the system locks the account and flags it as suspicious.
Why it matters: Attackers often try thousands of password guesses per second (a "brute-force attack"). Without a lockout system, an attacker could eventually guess the right password. This is one of the most fundamental access-control concepts in cybersecurity.
How the program helps: We'll build a simplified login simulator that checks a password, tracks failed attempts, and uses Boolean logic to decide whether to grant access, warn the user, or lock the account — exactly the kind of logic real authentication systems use (just much more simplified).
Step 2: Fully Commented Python Code

====================================================

# === Simple Login Security Simulator ===
# This program simulates a basic login system with lockout protection,
# similar in concept to what's used in real authentication systems.

# Store the "correct" password as a string.
# In a real system, this would be a hashed password stored in a database,
# never plain text like this.
correct_password = "CyberSafe123"

# Track how many times the user has failed to log in.
# We initialize this as an integer (int), starting at zero.
failed_attempts = 0

# Set the maximum number of allowed failed attempts before lockout.
# This is a constant — a value that shouldn't change during execution.
MAX_ATTEMPTS = 3

# A Boolean variable representing whether the account is currently locked.
# Booleans only ever hold True or False.
account_locked = False

# We simulate three login attempts using a list of guessed passwords.
# In a real program, this would come from live user input instead.
login_attempts = ["wrongpass", "CyberSafe123", "anotherwrong"]

# Loop through each attempted password one at a time.
for attempt in login_attempts:

    # 'not' reverses a Boolean value. This reads as:
    # "if the account is NOT locked, continue checking the login."
    if not account_locked:

        # Compound Boolean expression using 'and':
        # Both conditions must be True for access to be granted.
        if attempt == correct_password and failed_attempts < MAX_ATTEMPTS:
            print(f"Attempt '{attempt}': Access Granted ✅")
            # Once granted, we could break out of the loop entirely,
            # since there's no need to keep checking further attempts.
            break

        # 'elif' checks an alternative condition only if the first failed.
        # Here we check if the password is wrong AND attempts remain available.
        elif attempt != correct_password and failed_attempts < MAX_ATTEMPTS - 1:
            failed_attempts += 1  # Increase the failed attempt counter by 1
            print(f"Attempt '{attempt}': Access Denied ❌ "
                  f"({failed_attempts}/{MAX_ATTEMPTS} failed attempts)")

        # 'else' catches every remaining case —
        # this means the password was wrong AND attempts are exhausted.
        else:
            failed_attempts += 1
            account_locked = True  # Lock the account using Boolean True
            print(f"Attempt '{attempt}': Account LOCKED 🔒 "
                  f"Too many failed attempts.")

    # If the account is already locked, skip all further checks.
    else:
        print(f"Attempt '{attempt}': Ignored — account is locked.")

# Final status report using a Boolean check
if account_locked:
    print("\nFinal Status: Account is locked. Contact security admin.")
else:
    print("\nFinal Status: Account is active.")


============================================================
