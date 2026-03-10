"""
Bitcoin BIP32 Child Key Derivation
Research Notes: Normal vs. Hardened derivation paths.
"""
def explain_derivation(index: int):
    HARDENED_OFFSET = 0x80000000
    if index >= HARDENED_OFFSET:
        return f"Index {index}: Hardened Child (Cannot be derived from parent xpub)"
    return f"Index {index}: Normal Child (Can be derived from parent xpub)"

if __name__ == "__main__":
    print("🌳 BIP32 Child Key Concepts")
    print(explain_derivation(0))
    print(explain_derivation(0x80000000)) # Index 0' (Hardened)
