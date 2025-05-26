universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats():
    total_students = []
    total_tuition = []
    for university in universities:
        total_students.append(university[1])
        total_tuition.append(university[2])
    return total_students, total_tuition

def mean(numbers):
    return round((sum(numbers) / len(numbers)), 2)

def median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        num1 = numbers[n // 2 - 1]
        num2 = numbers[n // 2]
        return (num1 + num2) / 2

print(f"Total students: {sum(enrollment_stats()[0])}\n"
      f"Total tuition: ${sum(enrollment_stats()[1])}\n"
      f"\n"
      f"Student mean: {mean(enrollment_stats()[0])}\n"
      f"Student median: {median(enrollment_stats()[0])}\n"
      f"\n"
      f"Tuition mean: ${mean(enrollment_stats()[1])}\n"
      f"Tuition median: ${median(enrollment_stats()[1])}\n")
