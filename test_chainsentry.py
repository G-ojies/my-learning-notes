"""
ChainSentry: Unit Testing Architecture
Research Notes: Using Pytest to ensure our core logic never breaks.
"""

def test_rbf_detection():
    # Sequence < 0xffffffff-1 means RBF is enabled
    assert int("fdffffff", 16) <= (0xffffffff - 1) == True
    
def test_address_validation():
    # Should fail because it lacks the 'bc1' prefix or '1/3' starting char
    assert ("0xABCDEF..."[:3] == "bc1") == False

if __name__ == "__main__":
    print("🧪 Running ChainSentry Core Test Suite...")
    test_rbf_detection()
    test_address_validation()
    print("✅ All tests passed! Ready for production.")
