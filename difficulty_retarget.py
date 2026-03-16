"""
Bitcoin Difficulty Retargeting
Research Notes: Calculating the 2016 block adjustment window.
"""
def calculate_new_target(old_target: int, actual_timespan_seconds: int) -> int:
    EXPECTED_TIMESPAN = 2016 * 10 * 60 # 14 days in seconds
    
    # Satoshi's limits: Adjustments cannot be more than 4x or less than 0.25x
    clamped_timespan = max(EXPECTED_TIMESPAN // 4, min(actual_timespan_seconds, EXPECTED_TIMESPAN * 4))
    
    return (old_target * clamped_timespan) // EXPECTED_TIMESPAN
