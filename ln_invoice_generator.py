"""
ChainSentry: Premium Lightning Network Billing
Research Notes: Generating BOLT11 invoices via LND for premium SMS alerts.
"""
import json

def construct_ln_invoice_request(memo: str, value_sats: int) -> str:
    """
    Constructs the JSON payload required to ask an LND node to generate a BOLT11 invoice.
    """
    payload = {
        "memo": memo,
        "value": value_sats,
        "expiry": 3600 # 1 hour
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    print("⚡ ChainSentry Premium: Lightning Invoice Generator")
    print("-" * 65)
    
    # 5,000 sats for 1 month of premium SMS RBF alerts
    req = construct_ln_invoice_request(memo="ChainSentry Premium: 1 Month", value_sats=5000)
    
    print("POST /v1/invoices payload:")
    print(req)
    print("-" * 65)
    print("Once paid, the backend will upgrade the user's account via Webhook!")
