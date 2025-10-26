def fix_bug_code(user_code):
    # Example: check for common Python errors
    if "print" not in user_code:
        return user_code + "\n# Suggestion: Maybe add a print statement"
    elif "==" in user_code and "if" not in user_code:
        return user_code + "\n# Warning: comparison found outside if"
    else:
        return user_code + "\n# No obvious issues"
