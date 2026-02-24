"""
Bitcoin OP_RETURN Payload Decoder
Research Notes on extracting arbitrary data from transactions.
"""

def decode_op_return(hex_script: str):
    """
    Extracts and decodes the hidden payload inside an OP_RETURN script.
    
    Structure:
    [OP_RETURN (6a)] + [Push Data Opcode / Length] + [Raw Hex Payload]
    """
    if not hex_script.startswith('6a'):
        return "Not an OP_RETURN script."
        
    try:
        # Strip the '6a' (OP_RETURN opcode)
        payload_section = hex_script[2:]
        
        # For simplicity in this research script, we assume a direct push (0x01-0x4b)
        # where the next byte is the length of the data.
        length_hex = payload_section[:2]
        length_bytes = int(length_hex, 16)
        
        # Extract the actual data payload
        data_hex = payload_section[2:2 + (length_bytes * 2)]
        
        # Check for known protocols
        protocol = "Unknown Text"
        if data_hex.startswith('6f6d6e69'):
            protocol = "Omni Layer Protocol"
        elif data_hex.startswith('0109f91102'):
            protocol = "OpenTimestamps"
            
        # Decode the hex into a readable UTF-8 string
        raw_bytes = bytes.fromhex(data_hex)
        readable_text = raw_bytes.decode('utf-8', errors='replace')
        
        return {
            "Raw Hex": data_hex,
            "Protocol": protocol,
            "Decoded Message": readable_text
        }
        
    except Exception as e:
        return f"Decoding error: {e}"

if __name__ == "__main__":
    print("🕵️  Decoding OP_RETURN Blockchain Messages:")
    print("-" * 50)
    
    # Example: "sob-2026" embedded in hex
    example_script = "6a08736f622d32303236"
    
    result = decode_op_return(example_script)
    for key, value in result.items():
        print(f"{key}: {value}")
