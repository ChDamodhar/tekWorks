students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

def cal_averages(students):
    return {name: round(sum(marks) / len(marks), 2) for name, marks in students.items()}

averages = cal_averages(students)
top_performer = max(averages, key=averages.get)

print("Average Marks:", averages)
print("Top Performer:", top_performer)
