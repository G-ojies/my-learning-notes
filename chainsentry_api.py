"""
ChainSentry: REST API Blueprint (FastAPI)
Research Notes: Exposing our SQLite database to a future frontend dashboard.
"""

def mock_api_endpoint(endpoint: str, method: str) -> dict:
    """
    Simulates routing logic for the ChainSentry API.
    """
    routes = {
        "GET /api/watchlist": "Returns all addresses currently being monitored.",
        "POST /api/watchlist": "Adds a new Bitcoin address to the database.",
        "GET /api/events/recent": "Returns the last 50 mempool zero-conf transactions.",
        "GET /api/events/{address}": "Returns activity for a specific wallet."
    }
    
    route_key = f"{method.upper()} {endpoint}"
    return {"Route": route_key, "Action": routes.get(route_key, "404 Not Found")}

if __name__ == "__main__":
    print("🌐 ChainSentry API Router Blueprint")
    print(mock_api_endpoint("/api/events/recent", "GET"))
    print(mock_api_endpoint("/api/watchlist", "POST"))
