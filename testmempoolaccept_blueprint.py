"""
ChainSentry: testmempoolaccept RPC Blueprint
Research Notes: Safely validating raw transactions without broadcasting them.
"""
import json

def construct_testmempoolaccept(raw_tx_hex: str) -> str:
    payload = {
        "method": "testmempoolaccept",
        "params": [[raw_tx_hex]]
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    print("Pre-flight check for raw transaction:")
    print(construct_testmempoolaccept("0200000001..."))
