"""
Unit test suite for PTLC adaptor signature generation and lock verification.
"""
import unittest
import hashlib

def generate_adaptor_lock(payment_point: str, partial_sig: str) -> dict:
    locked_sig = hashlib.sha256((payment_point + partial_sig).encode()).hexdigest()
    return {"payment_point": payment_point, "adaptor_sig": locked_sig}

class TestPTLCProtocol(unittest.TestCase):
    def test_deterministic_lock_generation(self):
        point = "02" + "a" * 62
        sig = "3045022100" + "b" * 54
        result1 = generate_adaptor_lock(point, sig)
        result2 = generate_adaptor_lock(point, sig)
        self.assertEqual(result1["adaptor_sig"], result2["adaptor_sig"])

    def test_different_points_produce_distinct_locks(self):
        sig = "3045022100" + "b" * 54
        lock1 = generate_adaptor_lock("02" + "a" * 62, sig)
        lock2 = generate_adaptor_lock("03" + "c" * 62, sig)
        self.assertNotEqual(lock1["adaptor_sig"], lock2["adaptor_sig"])

if __name__ == "__main__":
    unittest.main()
