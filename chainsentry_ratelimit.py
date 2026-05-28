"""
ChainSentry: API Rate Limiting (Redis Blueprint)
Research Notes: Protecting our public endpoints from DDoS and spam after the v1.0 launch.
"""
import time

def check_rate_limit(ip_address: str, max_requests: int = 5, window_seconds: int = 1) -> dict:
    """
    Simulates a Token Bucket rate limiting algorithm.
    In production, this would be backed by an in-memory Redis datastore.
    """
    # Mocking the validation
    allowed = True 
    
    if not allowed:
        return {"status": 429, "message": "Too Many Requests", "retry_after": window_seconds}
        
    return {"status": 200, "message": "Request Allowed", "ip": ip_address}

if __name__ == "__main__":
    print("🛡️ ChainSentry API Rate Limiter")
    print("-" * 65)
    print(f"Evaluating inbound request from 192.168.1.105...")
    result = check_rate_limit("192.168.1.105")
    print(f"Result: {result['status']} - {result['message']}")
