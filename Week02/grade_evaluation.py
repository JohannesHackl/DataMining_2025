import bisect

score = input("Enter a score between 0 and 100.\n")
score = int(score)

if score < 0 or score > 100:
    print("FAIL")

boundaries = [50, 62.5, 75, 87.5, 101]  # Upper bounds
grades = ["F", "D", "C", "B", "A"]

index = bisect.bisect(boundaries, score)
grade = grades[index] if 0 <= score <= 100 else "Invalid score"

print(f"Score = {score}\nGrade = {grade}")

