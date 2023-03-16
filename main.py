import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = {}

    def __str__(self):
        res = f'Name = {self.name}\nSurname = {self.surname}\nGrades = {self.grades}\nAVG grade = {self.avg_grade}\nCourses in progress = {self.courses_in_progress}\nFinished courses = {self.finished_courses}\n'
        return res

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade_st(self, student, course_name):
        if isinstance(student, Student) and course_name in student.courses_in_progress:
            student.avg_grade[course_name] = statistics.mean(student.grades[course_name])
        else:
            print('Такого курса нет')
            return 'Ошибка_2'

    # def __lt__(self, course, other):
    #     if not isinstance(other, Student):
    #         print('Not a Student')
    #         return
    #     else:
    #         return self.avg_grade[self.courses_in_progress] > other.avg_grade[other.courses_in_progress]



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __str__(self):
        res = f'Name = {self.name}\nSurname = {self.surname}\n'
        return res


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# [] - список; {} - словарь
class Lecturer(Mentor):
    grades = {}
    avg_grade = {}
    def __str__(self):
        res = f'Name = {self.name}\nSurname = {self.surname}\nGrades = {self.grades}\nAvg Grades = {self.avg_grade}\n'
        return res


    def avg_grade_lec(self, lecturer, course_name):
        if isinstance(lecturer, Lecturer) and course_name in lecturer.courses_attached:
            lecturer.avg_grade[course_name] = statistics.mean(lecturer.grades[course_name])

            #print(statistics.mean(lecturer.grades[course_name]))
        else:
            print('Лектор не закреплен за таким курсом')
            return 'Ошибка_2'


# Добавляем 1й экземпляр класса Student
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['C++']
# Добавляем 2й экземпляр класса Student
student_2 = Student('Serg', 'Blanc', 'male')
student_2.courses_in_progress += ['Python']

# Добавляем экземпляр класса Reviewer
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']

# Добавляем оценки студенту-1 и студенту-2 по имеющимся курсам
cool_mentor.rate_hw(student_1, 'Python', 10)
cool_mentor.rate_hw(student_1, 'Python', 9)
cool_mentor.rate_hw(student_1, 'Python', 5)
cool_mentor.rate_hw(student_1, 'C++', 5)
cool_mentor.rate_hw(student_1, 'C++', 7)
cool_mentor.rate_hw(student_2, 'Python', 9)
cool_mentor.rate_hw(student_2, 'Python', 5)

# Добавляем экземпляр класса Lecturer
mentor_2 = Lecturer('Brilliant', 'Lecturer')
mentor_2.courses_attached += ['Python']

# Добавляем оценки лектору
student_1.rate_lecturer(mentor_2, 'Python', 9)
student_2.rate_lecturer(mentor_2, 'Python', 7)

# Рассчитываем средние оценки студентов по пройденным курсам
student_1.avg_grade_st(student_1, 'Python')
student_1.avg_grade_st(student_1, 'C++')
student_2.avg_grade_st(student_2, 'Python')

# Рассчитываем средние оценки лекторов по прикрепленным курсам
mentor_2.avg_grade_lec(mentor_2, 'Python')

student_1.add_courses('Start of programming')
student_2.add_courses('Start of programming')

# выводим обновленные __str__ для всех экземпляров классов
print(student_1.__str__())
print(student_2.__str__())
print(mentor_2.__str__())
print(cool_mentor.__str__())
print(student_1.avg_grade['Python'] > student_2.avg_grade['Python'])
#print(student_1.__lt__(['Python'], student_2['Python']))