class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        progress_courses = ','.join(self.courses_in_progress)
        finish_courses = ', '.join(self.finished_courses)
        grade_count = 0

        for i in self.grades:
            grade_count += len(self.grades[i])

        self.average_rating = sum(map(sum, self.grades.values())) / grade_count

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
              f'{self.average_rating}\n' \
              f'Курсы в процессе изучения: {progress_courses}\nЗавершенные курсы: {finish_courses}'
        return res

    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Сравнение невозможно')
            return
        return self.average_rating < other.average_rating


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grade_count = 0
        for i in self.grades:
            grade_count += len(self.grades[i])

        self.average_rating = sum(map(sum, self.grades.values())) / grade_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Сравнение невозможно')
            return
        return self.average_rating < other.average_rating


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lector_1 = Lecturer('Reed', 'Richards')
lector_1.courses_attached += ['Python']

lector_2 = Lecturer('Tony', 'Stark')
lector_2.courses_attached += ['JavaScript']

reviewer_1 = Reviewer('Bruce', 'Banner')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['JavaScript']

reviewer_2 = Reviewer('Stephen', 'Strange')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['JavaScript']

student_1 = Student('Peter', 'Parker')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['GIT', 'Введение в программирование']

student_2 = Student('Clint', 'Barton')
student_2.courses_in_progress += ['JavaScript']
student_2.finished_courses += ['GIT', 'Введение в программирование']

student_1.rate_hw(lector_1, 'Python', 10)
student_1.rate_hw(lector_1, 'Python', 8)

student_2.rate_hw(lector_2, 'JavaScript', 7)
student_2.rate_hw(lector_2, 'JavaScript', 9)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'JavaScript', 7)
reviewer_1.rate_hw(student_2, 'JavaScript', 5)

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 8)

reviewer_2.rate_hw(student_2, 'JavaScript', 6)
reviewer_2.rate_hw(student_2, 'JavaScript', 5)

print(student_1, student_2, sep='\n\n')
print()
print(lector_1, lector_2, sep='\n\n')
print()
print(student_1 < student_2)
print()
print(lector_1 < lector_2)
print()
students = [student_1, student_2]
lectors = [lector_1, lector_2]


def students_rating(students, courses):
    summ = 0
    count = 0
    for student in students:
        if student.courses_in_progress == [courses]:
            summ += student.average_rating
            count += 1
    average_homeworks = summ / count
    return average_homeworks


def lectors_rating(lectors, courses):
    summ = 0
    count = 0
    for lec in lectors:
        if lec.courses_attached == [courses]:
            summ += lec.average_rating
            count += 1
    average_lecture = summ / count
    return average_lecture


print(f"Средняя оценка студентов за д/з в рамках курса {'Python'}: {students_rating(students, 'Python')}")
print(f"Средняя оценка студентов за д/з в рамках курса {'JavaScript'}: {students_rating(students, 'JavaScript')}")
print()
print(f"Средняя оценка лекторов за лекции в рамках курса {'Python'}: {lectors_rating(lectors, 'Python')}")
print(f"Средняя оценка лекторов за лекции в рамках курса {'JavaScript'}: {lectors_rating(lectors, 'JavaScript')}")
