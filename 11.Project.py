class Student:
    def __init__(self, firstname, lastname, tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = []

    def RunningAverage(self):
        """Calculates the running average of non-blank scores."""
        valid_grades = [float(grade) for grade in self.Grades if grade]
        if valid_grades:
            return sum(valid_grades) / len(valid_grades)
        else:
            return 0.0

    def TotalAverage(self):
        """Calculates the average of scores, treating missing as zero."""
        total_sum = sum(float(grade) if grade else 0 for grade in self.Grades)
        return total_sum / len(self.Grades)

    def LetterGrade(self):
        """Returns the letter grade based on the TotalAverage."""
        total_average = self.TotalAverage()
        if total_average >= 90:
            return "A"
        elif total_average >= 80:
            return "B"
        elif total_average >= 70:
            return "C"
        elif total_average >= 60:
            return "D"
        else:
            return "F"


class StudentList:
    def __init__(self):
        self.Studentlist = []

    def add_student(self, firstname, lastname, tnumber):
        """Creates a Student object and appends it to the list."""
        student = Student(firstname, lastname, tnumber)
        self.Studentlist.append(student)

    def find_student(self, tnumber):
        """Finds a student by TNumber and returns the index, -1 if not found."""
        for i, student in enumerate(self.Studentlist):
            if student.TNumber == tnumber:
                return i
        return -1

    def print_student_list(self):
        """Prints the attributes of each Student object in the list."""
        print("First Last ID Running Semester Letter")
        print("Name Name Number Average Average Grade")
        print("------------ ------------ ------------ ------------ ------------ ------------")
        for student in self.Studentlist:
            print(
                f"{student.FirstName} {student.LastName} {student.TNumber} {student.RunningAverage():.2f} {student.TotalAverage():.2f} {student.LetterGrade()}"
            )

    def add_student_from_file(self, filename):
        """Reads student data from a file and adds students to the list."""
        with open("11.ProjectStudents.txt", "r") as file:
            for line in file:
                firstname, lastname, tnumber = line.strip().split(",")
                self.add_student(firstname, lastname, tnumber)

    def add_scores_from_file(self, filename):
        """Reads scores from a file and adds them to the appropriate student."""
        with open("11.ProjectScores.txt", "r") as file:
            for line in file:
                tnumber, score = line.strip().split(",")
                index = self.find_student(tnumber)
                if index != -1:
                    self.Studentlist[index].Grades.append(score)


# Main Program
student_list = StudentList()

# Add students from file
student_list.add_student_from_file("11.Project Students.txt")

# Add scores from file
student_list.add_scores_from_file("11.Project Scores.txt")

# Print the student list
student_list.print_student_list()