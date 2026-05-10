# 🛡️ ChainSentry

ChainSentry is a real-time Bitcoin mempool monitor and wallet surveillance tool designed to detect zero-conf transactions, flag RBF (Replace-By-Fee) double-spend risks, and log activity to a local SQLite database.

## Architecture
- **Mempool Monitor**: Streams zero-conf transactions via ZMQ/RPC.
- **RBF Analyzer**: Inspects `sequence` flags to warn of BIP125 replacements.
- **Database**: SQLite schema to persistently log target wallet inflows/outflows.
- **API**: FastAPI blueprints for dashboard integration.

## Testing
Run the pytest suite to verify cryptographic and network logic:
`pytest test_chainsentry.py`
