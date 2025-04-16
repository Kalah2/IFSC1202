import csv
from typing import List

class Student:
    def __init__(self, firstname: str, lastname: str, tnumber: str, scores: List[str]):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = [float(score) if score else 0.0 for score in scores]

    def RunningAverage(self) -> float:
        valid_scores = [score for score in self.Grades if score > 0]
        return sum(valid_scores) / len(valid_scores) if valid_scores else 0.0

    def TotalAverage(self) -> float:
        return sum(self.Grades) / len(self.Grades)

    def LetterGrade(self) -> str:
        average = self.TotalAverage()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

students = []
with open('10.ProjectStudentScores.txt', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        firstname, lastname, tnumber, *scores = row
        student = Student(firstname, lastname, tnumber, scores)
        students.append(student)

for student in students:
    print(f'{student.FirstName} {student.LastName} - Running Average: {student.RunningAverage():.4f}, Total Average: {student.TotalAverage():.2f}, Letter Grade: {student.LetterGrade()}')