def grade(total_reward):
    if total_reward > 5:
        return "Excellent"
    elif total_reward > 2:
        return "Good"
    return "Needs Improvement"
