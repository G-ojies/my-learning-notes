"""
ChainSentry: Genesis Day Consensus Retarget Simulator
Research Notes: Commemorating the Jan 3, 2009 Genesis Block. Simulating the 2016-block difficulty retarget cycle.
"""
TARGET_TIMESPAN = 14 * 24 * 60 * 60  # 2 weeks in seconds (1,209,600s)

def calculate_next_work_required(actual_timespan: int, current_target: int) -> int:
    # Dampen adjustment by maximum factor of 4 to prevent wild swings
    if actual_timespan < TARGET_TIMESPAN // 4:
        actual_timespan = TARGET_TIMESPAN // 4
    if actual_timespan > TARGET_TIMESPAN * 4:
        actual_timespan = TARGET_TIMESPAN * 4

    new_target = (current_target * actual_timespan) // TARGET_TIMESPAN
    print(f"⛏️ Genesis Protocol Check | Adjusted timespan: {actual_timespan}s")
    print(f" -> Next difficulty target calculated: {hex(new_target)}")
    return new_target

if __name__ == "__main__":
    calculate_next_work_required(1000000, 0x00000000FFFF0000000000000000000000000000000000000000000000000000)
