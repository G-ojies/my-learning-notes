# 🗺️ ChainSentry v1.1.0 Architecture Roadmap

The next iteration of ChainSentry moves beyond passive observation into active anomaly classification and Layer 2 awareness.

## Planned Features
1. **The Heuristic Engine:** Integration of the Whale Alert and Dust Attack detection algorithms directly into the WebSocket stream.
2. **Dynamic Fee Thresholds:** Automatically adjusting RBF warning severity based on the current 2-block `estimatesmartfee` network average.
3. **Lightning Node Integration:** Querying local LND channels to verify Submarine Swap outpoints in real-time.
4. **Enhanced UI:** Dedicated dashboard panels for Mempool Congestion visualizers.
