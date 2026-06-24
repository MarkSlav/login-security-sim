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
# here you can test a variaty Attempts....I can test:
#login_attempts = ["wrong1", "wrong2", "wrong3", "wrong4"]
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