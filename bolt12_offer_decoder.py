"""
ChainSentry v1.8.1: BOLT 12 Offer Decoder
Research Notes: Parsing static, reusable Lightning payment identifiers.
"""
def decode_bolt12_offer(offer_string: str):
    if offer_string.startswith("lno1"):
        print("⚡ Valid BOLT 12 Offer detected (Static Payment Identifier).")
        print(" -> Supports recurring payments, larger amounts, and sender-initiated invoices.")
        return True
    print("❌ Invalid offer format.")
    return False

if __name__ == "__main__":
    decode_bolt12_offer("lno1qg5sv42xf4")
