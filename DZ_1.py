
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
    def rate_hw(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        counter = 0
        for i in self.grades:
            counter += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / counter  # можно использовать for, но с функцией map() будет короче

        finished_courses_unpacked = ', '.join(self.finished_courses)
        courses_in_progress_unpacked = ', '.join(self.courses_in_progress)

        res = f'Имя: {self.name} \nФамилия: {self.surname} ' \
               f'\nСредняя оценка за домашние задания: {self.average_rating}' \
               f'\nКурсы в процессе изучения: {finished_courses_unpacked} ' \
               f'\nЗавершенные курсы: {courses_in_progress_unpacked}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating
#--------------------------------------------------------------------------

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

#-----------------------------------------------------------------------------
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = float()


    def __str__(self):
        counter = 0
        for i in self.grades:
            counter += len(self.grades[i])
        self.average_rating = sum(map(sum, self.grades.values())) / counter

        res = f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname} ' \
               f'\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нельзя сравнить')
            return
        return self.average_rating < other.average_rating
#-------------------------------------------------------------------------------

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
        res = f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname}'
        return res

# создаем лекторов

best_lecturer_1 = Lecturer('Ivan', 'Petrov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Sergey', 'Trou')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Olga', 'Trovina')
best_lecturer_3.courses_attached += ['Python']

# создаем проверяющих и ставим курсы

cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Anastasia', 'Drow')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']

cool_reviewer_3 = Reviewer('Oleg', 'Mone')
cool_reviewer_3.courses_attached += ['Python']
cool_reviewer_3.courses_attached += ['Java']

# пишем студентов и добавляем изучаемые и завершенные курсы

best_student_1 = Student('Ruoy', 'Eman', 'your_gender')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.finished_courses = ['Введение в программирование']

best_student_2 = Student('Alina', 'Zdravina', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.finished_courses = ['Введение в программирование']

best_student_3 = Student('Roman', 'Zvagin', 'your_gender')
best_student_3.courses_in_progress += ['Java']
best_student_3.finished_courses = ['Введение в программирование']

# ставим оценки студентам за домашнее задание

cool_reviewer_1.rate_hw(best_student_1, 'Python', 5)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 7)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 3)
cool_reviewer_2.rate_hw(best_student_2, 'Python', 7)

cool_reviewer_1.rate_hw(best_student_3, 'Java', 5)
cool_reviewer_1.rate_hw(best_student_3, 'Java', 10)
cool_reviewer_1.rate_hw(best_student_3, 'Java', 4)

cool_reviewer_2.rate_hw(best_student_3, 'Java', 9)
cool_reviewer_2.rate_hw(best_student_3, 'Java', 6)
cool_reviewer_2.rate_hw(best_student_3, 'Java', 10)
cool_reviewer_2.rate_hw(best_student_3, 'Java', 5)

# ставим оценки лекторам за их лекции

best_student_1.rate_hw(best_lecturer_1, 'Python', 9)
best_student_1.rate_hw(best_lecturer_1, 'Python', 7)
best_student_1.rate_hw(best_lecturer_1, 'Python', 6)

best_student_3.rate_hw(best_lecturer_2, 'Java', 7)
best_student_3.rate_hw(best_lecturer_2, 'Java', 7)
best_student_3.rate_hw(best_lecturer_2, 'Java', 7)

best_student_2.rate_hw(best_lecturer_3, 'Python', 8)
best_student_2.rate_hw(best_lecturer_3, 'Python', 5)
best_student_2.rate_hw(best_lecturer_3, 'Python', 8)

# Выводим карточку студента со всей информацией
print(f'Карточки студентов: \n\n{best_student_1} \n\n{best_student_2} \n\n{best_student_3}')
print()

# Выводим карточку лекторов со всей информацией
print(f'Карточки лекторов: \n\n{best_lecturer_1} \n\n{best_lecturer_2} \n\n{best_lecturer_3}')
print()

# Сравнение студентов
print(f'Вывод сравнения студентов по средней оценке за лекции: '
      f'\n{best_student_1.name} {best_student_1.surname} < {best_student_3.name} {best_student_3.surname} = {best_student_1 < best_student_3}')
print()
print(f'Вывод сравнения студентов по средней оценке за лекции: '
      f'\n{best_student_2.name} {best_student_2.surname} < {best_student_3.name} {best_student_3.surname} = {best_student_2 < best_student_3}')
print()

# Сравнение лекторов
print(f'Вывод сравнения лекторов по средней оценке за лекции: '
      f'\n{best_lecturer_1.name} {best_lecturer_1.surname} > {best_lecturer_3.name} {best_lecturer_3.surname} = {best_lecturer_1 > best_lecturer_3}')
print()
print(f'Вывод сравнения лекторов по средней оценке за лекции: '
      f'\n{best_lecturer_2.name} {best_lecturer_2.surname} < {best_lecturer_1.name} {best_lecturer_1.surname} = {best_lecturer_2 < best_lecturer_1}')

student_list = [best_student_1, best_student_2, best_student_3]

def total_count_student(student_list, name_course):
    sum = 0
    counter = 0

    for stud in student_list:
        if stud.courses_in_progress == [name_course]:
            sum += stud.average_rating
            counter += 1
    average_all = sum / counter
    return average_all

lector_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def total_count_lector(lector_list, name_course):
    sum = 0
    counter = 0

    for stud in lector_list:
        if stud.courses_attached == [name_course]:
            sum += stud.average_rating
            counter += 1
    average_all = sum / counter
    return average_all

print(f'Общая средняя оценка по курсу Python среди студентов: {total_count_student(student_list, "Python")}')
print()
print(f'Общая средняя оценка по курсу Java среди лекторов: {total_count_lector(lector_list, "Java")}')

s