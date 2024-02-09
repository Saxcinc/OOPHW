class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def estimation(self, lecturer,course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def average_grade(self):
        for course, estimation in self.grades.items():
            res = sum(estimation) / len(estimation)
        return res

    def __str__(self):
        return f"Имя: {self.name}\nФамилия:{self.surname}\nСредняя оценка за домашнее задание: {self.average_grade():.2f}\n"\
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def average_grade(self):
        for course, estimation in self.grades.items():
            res = sum(estimation) / len(estimation)
        return res

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade():.2f}"
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()


class Rewiever(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def estimation(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def student_rating(list_, course_name):
    sum_all = 0
    count_all = 0
    for stud in list_:
        if course_name in stud.courses_in_progress:
            sum_all += stud.average_grade()
            count_all += 1
        else:
            return
    average_for_all = sum_all / count_all
    return f"Средняя оценка для всех студентов на курсе {course_name}: {average_for_all:.2f}"

def lecturer_rating(list_, course_name):
    sum_all = 0
    count_all = 0
    for lect in list_:
        if course_name in lect.courses_attached:
            sum_all += lect.average_grade()
            count_all += 1
        else:
            return
    average_for_all = sum_all / count_all
    return f"Средняя оценка для всех лекторов по курсу {course_name}: {average_for_all:.2f}"


jordan = Student("Jordan", "Belfort", "Man")
jordan.courses_in_progress += ["Python"]
jordan.courses_in_progress += ["JavaScript"]
jordan.finished_courses += ["Git"]

emi = Student("Emilia", "Clarke", "Woman")
emi.courses_in_progress += ["Python"]
emi.courses_in_progress += ["Git"]
emi.finished_courses += ["PHP"]

stephen = Lecturer("Stephen", "Wozniak")
stephen.courses_attached += ["Python"]

mark = Lecturer("Mark", "Zuckerberg")
mark.courses_attached += ["Python"]

pavel = Rewiever("Pavel", "Durov")
pavel.courses_attached += ["Python"]

jeffrey = Rewiever("Jeffrey", "Bezos")
jeffrey.courses_attached += ["Python"]

study_list = [jordan, emi]
lector_list = [stephen, mark]

pavel.estimation(jordan, "Python", 8)
pavel.estimation(jordan, "Python", 7)
pavel.estimation(jordan, "Python", 10)

jeffrey.estimation(emi, "Python", 10)
jeffrey.estimation(emi, "Python", 9)
jeffrey.estimation(emi, "Python", 10)

jordan.estimation(stephen, "Python", 10)
jordan.estimation(stephen, "Python", 10)
jordan.estimation(stephen, "Python", 10)

emi.estimation(mark, "Python", 9)
emi.estimation(mark, "Python", 10)
emi.estimation(mark, "Python", 9)

print(jordan, "\n")
print(emi, "\n")
print(stephen, "\n")
print(mark, "\n")
print(pavel, "\n")
print(jeffrey, "\n")
print(jordan < emi, "\n")
print(stephen == mark,"\n")
print(student_rating(study_list, "Python"), "\n" )
print(lecturer_rating(lector_list, "Python"), "\n")