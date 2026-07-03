"""
ChainSentry v1.2.0: PayJoin (Stowaway) Detector
Research Notes: Preventing false volume alerts by identifying collaborative spends.
"""
def is_likely_payjoin(inputs: list, outputs: list) -> bool:
    """
    PayJoins break the common-input ownership heuristic.
    If a transaction has no obvious change output and inputs belong to different entities.
    """
    # Simplified heuristic: No change output and exactly 2 inputs
    if len(inputs) == 2 and len(outputs) == 1:
        return True
    return False
