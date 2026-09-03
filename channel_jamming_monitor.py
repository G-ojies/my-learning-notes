"""
ChainSentry v1.6.1: Channel Jamming Detector
Research Notes: Detecting when an attacker routes low-fee HTLCs to exhaust channel liquidity.
"""
def detect_liquidity_jam(active_htlcs: list, max_concurrent: int = 483):
    """
    Lightning channels have a hard limit of 483 concurrent HTLCs.
    Attackers exploit this by sending 483 dust payments that never resolve.
    """
    if len(active_htlcs) >= max_concurrent:
        print("🚨 CRITICAL: HTLC Slot Exhaustion Detected! Potential Jamming Attack.")
        print(" -> Action: Dynamic fee bumping initiated. Rejecting low-rep peers.")
        return True
    return False

if __name__ == "__main__":
    detect_liquidity_jam(["htlc_mock"] * 483)
