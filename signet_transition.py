"""
ChainSentry: Signet Network Configuration
Research Notes: Moving from local Regtest to the global Signet testing network.
"""

def generate_signet_conf() -> str:
    """
    Generates the bitcoin.conf required to connect ChainSentry's node 
    to the official Bitcoin Signet (BIP 325) for global testing.
    """
    return """# Bitcoin Core Signet Configuration
signet=1

[signet]
server=1
txindex=1
rpcuser=chainsentry
rpcpassword=localdev

# Connect to official signet seed nodes
addnode=178.128.221.177
addnode=2a01:7c8:d005:390::5
addnode=v7f6bptoedwnt34hwjqruvwyy5j2rnj5e4rrcqffn4cwjldkhy23r4qd.onion:38333
"""

if __name__ == "__main__":
    print("🌍 Preparing ChainSentry for Global Signet Transition")
    print("-" * 65)
    print("Writing to ~/.bitcoin/bitcoin.conf...")
    print(generate_signet_conf())
    print("-" * 65)
    print("Signet provides a reliable, globally distributed test environment without the unreliability of Testnet3!")
