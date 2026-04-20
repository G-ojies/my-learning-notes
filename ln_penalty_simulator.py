"""
Lightning Network: Justice / Penalty Transaction Simulator
Research Notes: How LN prevents cheating using revocation secrets.
"""
def check_cheat_attempt(broadcasted_state: int, current_state: int) -> str:
    if broadcasted_state < current_state:
        return "🚨 CHEAT DETECTED! Old state broadcasted. Justice transaction triggered. All funds swept to honest party."
    return "✅ State is valid and current."

if __name__ == "__main__":
    print(check_cheat_attempt(broadcasted_state=5, current_state=12))
