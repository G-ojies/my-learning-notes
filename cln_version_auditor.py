"""
ChainSentry: Core Lightning Vulnerability Auditor
Research Notes: Flagging nodes running deprecated versions (like 26.04) before the emergency patch.
"""
def audit_cln_nodes(node_list: list):
    print("🔍 Scanning Lightning Network topology for vulnerable Core Lightning versions...")
    for node in node_list:
        if node['version'] == '26.04' or node['version'] < '26.06.6':
            print(f"🚨 WARNING: Node {node['id']} is running vulnerable CLN version {node['version']}!")
            print(" -> Recommendation: Upgrade to signed emergency binaries or take offline immediately.")

if __name__ == "__main__":
    mock_nodes = [{"id": "03abc123", "version": "26.04"}, {"id": "02def456", "version": "26.06.6"}]
    audit_cln_nodes(mock_nodes)
