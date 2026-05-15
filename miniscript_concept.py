"""
ChainSentry: Miniscript Policy Simulator
Research Notes: Translating human-readable policy to Bitcoin Script.
"""
def compile_simple_policy(policy: str) -> str:
    """
    Mock compiler for a simple 'and(pk(A),older(10))' policy.
    Meaning: Requires Signature A AND the UTXO must be 10 blocks old.
    """
    if policy == "and(pk(A),older(10))":
        return "<10> OP_CHECKSEQUENCEVERIFY OP_DROP <PubKey_A> OP_CHECKSIG"
    return "Unsupported policy."

if __name__ == "__main__":
    print("🧠 Miniscript to Bitcoin Script")
    policy = "and(pk(A),older(10))"
    print(f"Policy: {policy}\nScript: {compile_simple_policy(policy)}")
