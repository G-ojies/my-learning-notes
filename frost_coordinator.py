"""
ChainSentry v1.9.1: FROST Multi-Party Coordinator
Research Notes: Managing round timeouts and abort conditions when a signer drops out.
"""
def manage_frost_round(participants: list, nonces_received: int):
    print("📋 FROST Coordinator Active: Managing signature rounds.")
    if nonces_received < len(participants):
        print("⚠️ Warning: Round 1 timeout detected. Missing participant nonce.")
        print(" -> Aborting round and triggering disqualification protocol.")
        return False
    print("✅ All participant nonces accounted for. Proceeding to Round 2.")
    return True

if __name__ == "__main__":
    manage_frost_round(["signer_1", "signer_2", "signer_3"], 2)
