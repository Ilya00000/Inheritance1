def rate_lecturer(lecturer, course, grade):
    if course in lecturer.courses_attached:
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def review_homework(self, student, course, grade):
        if course in self.courses_attached:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached.append('Python')

cool_reviewer.review_homework(best_student, 'Python', 10)
cool_reviewer.review_homework(best_student, 'Python', 9)

print(f"Оценки студента {best_student.name} {best_student.surname}: {best_student.grades}")