"""
ChainSentry v1.2.0: LN Gossip Topology Mapping
Research Notes: Building a local graph of the Lightning Network to optimize routing paths.
"""
class LightningGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {} # channel_id -> routing_policy

    def add_channel(self, node_a, node_b, capacity, fee_rate):
        self.nodes.update([node_a, node_b])
        self.edges[f"{node_a}-{node_b}"] = {"capacity": capacity, "fee": fee_rate}
        print(f"🔗 Channel added: {node_a[:8]} <-> {node_b[:8]} | Cap: {capacity} sats")

if __name__ == "__main__":
    graph = LightningGraph()
    graph.add_channel("03abc123", "02def456", 5000000, 10)
