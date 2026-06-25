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


# Loop a fixed number of times (one per allowed attempt),
# instead of looping over a pre-existing collection.
while failed_attempts < MAX_ATTEMPTS and not account_locked:

    # Call input() freshly on EACH loop iteration —
    # this is what actually gives the user a new chance to type.
    attempt = input("Enter your password: ")

    if attempt == correct_password:
        print("Access Granted ✅")
        break  # Stop the loop immediately — no need to keep asking
    else:
        failed_attempts += 1
        if failed_attempts >= MAX_ATTEMPTS:
            account_locked = True
            print("Account LOCKED 🔒 Too many failed attempts.")
        else:
            print(f"Access Denied ❌ ({failed_attempts}/{MAX_ATTEMPTS} failed attempts)")