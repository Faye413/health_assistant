def process_user_data(user_data):
    # Simulate data analysis (e.g., averages, summaries)
    return {
        "average_sleep_quality": sum(user_data['sleep_quality']) / len(user_data['sleep_quality']),
        "activity_summary": f"User's average step count: {sum(user_data['steps']) / len(user_data['steps'])}",
        "heart_rate_analysis": f"Average heart rate is {sum(user_data['heart_rate']) / len(user_data['heart_rate'])} bpm"
    }
