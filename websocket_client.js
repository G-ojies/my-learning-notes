/**
 * ChainSentry: WebSocket Client
 * Research Notes: Listening for live RBF and transaction alerts from the FastAPI backend.
 */

function initializeStream(url) {
    const ws = new WebSocket(url);

    ws.onopen = () => {
        console.log("✅ Connected to ChainSentry WebSocket stream!");
    };

    ws.onmessage = (event) => {
        const txData = JSON.parse(event.data);
        
        if (txData.is_rbf) {
            console.error(`🚨 CRITICAL: RBF Double-Spend Attempt Detected! TXID: ${txData.txid}`);
        } else {
            console.log(`💸 New Inflow: ${txData.amount_sats} sats to ${txData.address}`);
        }
    };

    ws.onclose = () => {
        console.warn("⚠️ Stream disconnected. Attempting to reconnect in 5 seconds...");
        setTimeout(() => initializeStream(url), 5000);
    };
}

if (typeof window !== "undefined") {
    // In a browser environment, connect to our local backend
    // initializeStream("ws://localhost:8000/api/ws/mempool");
}
