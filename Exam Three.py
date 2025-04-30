import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        a1 = math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)) * 180 / math.pi
        a2 = math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)) * 180 / math.pi
        a3 = math.acos((self.s1**2 + self.s2**2 - self.s3**2) / (2 * self.s1 * self.s2)) * 180 / math.pi
        return [a1, a2, a3]

print("Type Side 1 Side 2 Side 3 Perimeter Area Angle 1 Angle 2 Angle 3")
triangle_list = []
with open("ExamThreeTriangles.txt", "r") as file:
    for line in file:
        s1, s2, s3 = map(float, line.strip().split(","))
        triangle = Triangle(s1, s2, s3)
        triangle_list.append(triangle)

for triangle in triangle_list:
    triangle_type = triangle.type()
    s1 = triangle.s1
    s2 = triangle.s2
    s3 = triangle.s3
    perimeter = triangle.perimeter()
    area = triangle.area()
    angles = triangle.angles()
    print(f"{triangle_type} {s1:.3f} {s2:.3f} {s3:.3f} {perimeter:.3f} {area:.3f} {angles[0]:.3f} {angles[1]:.3f} {angles[2]:.3f}")