class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name):
        self.name = name
        self.surname = surname
        self.grades = []
        self.finished_courses = []

    def __str__(self):
        avg_grades = sum(best_lecturer.grades['Python']) / 3
        some = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grades}'
        return some

some_lecturer = Lecturer('Some', 'Buddy')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some = f'Имя: {self.name}\nФамилия: {self.surname}\nСредний бал за лекции: {self.grades}'
        return some

some_reviewer = Reviewer('Some', 'Buddy')


best_lecturer = Lecturer('Ruoy', 'Eman')
best_lecturer.finished_courses += ['Python']
best_lecturer.grades['Python'] = [10, 10, 9.7]

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_attached += ['Python']

cool_student.rate_lecture(best_lecturer, 'Python', 10)
cool_student.rate_lecture(best_lecturer, 'Python', 10)
cool_student.rate_lecture(best_lecturer, 'Python', 9.7)

print(best_lecturer.grades)
print(some_reviewer)
print(some_lecturer)




