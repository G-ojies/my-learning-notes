"""
Bitcoin RPC Block Parser
Research Notes: Parsing the JSON response from `getblock` into local data structures.
"""
import json

def parse_rpc_block(rpc_json: str) -> dict:
    data = json.loads(rpc_json)
    return {
        "Hash": data.get("hash"),
        "Confirmations": data.get("confirmations"),
        "Size (Bytes)": data.get("size"),
        "Weight (WU)": data.get("weight"),
        "Tx Count": len(data.get("tx", [])),
        "Difficulty": data.get("difficulty")
    }
