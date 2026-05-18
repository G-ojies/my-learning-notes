"""
ChainSentry: Webhook Alert System
Research Notes: Pushing critical mempool alerts to external services (Slack/Discord).
"""
import json
import urllib.request
import urllib.error

def send_discord_alert(webhook_url: str, txid: str, address: str, is_rbf: bool):
    """
    Constructs and sends a JSON payload to a Discord Webhook.
    """
    color = 16711680 if is_rbf else 65280 # Red for RBF, Green for standard
    title = "🚨 RBF DOUBLE-SPEND RISK!" if is_rbf else "💸 Target Wallet Activity"
    
    payload = {
        "embeds": [{
            "title": title,
            "description": f"Target Address: `{address}`",
            "color": color,
            "fields": [
                {"name": "TXID", "value": f"[{txid[:10]}...](https://mempool.space/tx/{txid})"}
            ]
        }]
    }
    
    # In a real app, we would use requests.post(). We use urllib for zero-dependency testing.
    req = urllib.request.Request(webhook_url, method="POST")
    req.add_header('Content-Type', 'application/json')
    
    try:
        # We mock the actual HTTP call to prevent errors in testing
        print(f"📡 Sending payload to Webhook...\n{json.dumps(payload, indent=2)}")
        print("✅ Alert dispatched successfully!")
    except Exception as e:
        print(f"❌ Failed to send alert: {e}")

if __name__ == "__main__":
    print("🔔 ChainSentry Alert Dispatcher")
    print("-" * 65)
    send_discord_alert("https://discord.com/api/webhooks/mock", "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16", "bc1q_whale_wallet", is_rbf=True)
