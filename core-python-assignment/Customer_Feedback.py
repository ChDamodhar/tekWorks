def feedback(ratings):
    if not ratings:
        return "No ratings available."

    positive_count = sum(1 for r in ratings if r >= 4) 
    percentage = (positive_count / len(ratings)) * 100
    return f"Positive Feedback: {round(percentage, 2)}%"
ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(feedback(ratings))