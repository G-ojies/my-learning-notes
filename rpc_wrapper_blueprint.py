"""
Bitcoin JSON-RPC Client Blueprint
Research Notes: Standardizing calls to bitcoind.
"""
import json

def format_rpc_request(method: str, params: list = []) -> str:
    payload = {
        "jsonrpc": "1.0",
        "id": "research_client",
        "method": method,
        "params": params
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    print(format_rpc_request("getblockchaininfo"))
