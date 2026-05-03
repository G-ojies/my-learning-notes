"""
ChainSentry: Strict Address Validator
Research Notes: Preventing bad data from entering the database using regex.
"""
import re

def is_valid_bitcoin_address(address: str) -> bool:
    """
    Basic sanity checks for Bitcoin address formats before database insertion.
    """
    # Legacy (P2PKH) or Nested SegWit (P2SH)
    if re.match(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", address):
        return True
    
    # Native SegWit (v0) or Taproot (v1)
    if re.match(r"^bc1[a-z0-9]{39,59}$", address):
        return True
        
    return False

if __name__ == "__main__":
    print("🛂 ChainSentry Address Validator")
    good_addr = "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"
    bad_addr = "bc1q_this_is_fake_and_invalid"
    
    print(f"{good_addr}: {'Valid' if is_valid_bitcoin_address(good_addr) else 'Invalid'}")
    print(f"{bad_addr}: {'Valid' if is_valid_bitcoin_address(bad_addr) else 'Invalid'}")
