"""
ChainSentry: Chaos Fuzzer
Research Notes: Throwing corrupted and malformed hex data at our parsers to ensure they fail gracefully instead of crashing.
"""
import random

def generate_garbage_hex(length: int = 64) -> str:
    """Generates random valid hex characters that mean absolutely nothing."""
    return "".join(random.choices("0123456789abcdef", k=length))

def test_parser_resilience(hex_string: str):
    """Simulates the parser attempting to read garbage network data."""
    try:
        # Mock attempt to parse standard Bitcoin version bytes
        if len(hex_string) < 8:
            raise ValueError("Data too short")
        version = int(hex_string[:8], 16)
        return f"Parsed version: {version}"
    except Exception as e:
        return f"Graceful Failure: {e}"

if __name__ == "__main__":
    print("🔥 ChainSentry Chaos Fuzzer")
    print("-" * 65)
    
    for i in range(3):
        garbage = generate_garbage_hex(random.randint(4, 20))
        print(f"Injecting payload: {garbage}")
        print(f"Response: {test_parser_resilience(garbage)}\n")
