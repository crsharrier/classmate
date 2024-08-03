from django.core.management.base import BaseCommand
from datetime import date
from classmate.models import Class, Student, ClassAssignment, DateDim

students = [
        'Saara', 'Ayyub', 'Sara', 'Afsana', 'Adyan', 'Sufyan', 'Ayat', 
        'Mukhtar', 'Yahya', 'Dawud', 'Felix', 'Ocean', 'Inaya', 'Ayline', 
        'Suha', 'Madiha', 'Rahat', 'Alexander', 'Yassin', 'Sameeha', 
        'Charlotte', 'Ayaan', 'Zarah', 'Anastasiia', 'Tanisha', 'Amira', 
        'Armaan', 'Khairah', 'Aaliyah', 'Sarosh', 'Pavit', 'Aneesah', 
        'Rumaysa', 'Zahiya', 'Jannat', 'Daniyyal', 'Adiv', 'Arissa', 
        'Fateha', 'Hanifa', 'Issa', 'Odrika', 'Torshan', 'Ismail', 'Rahma',
        'Maimuna', 'Aneeshah', 'Shahir'
        ]

def populate_class_assignments():
    maths_class = Class.objects.get(class_name='Maths')
    english_class = Class.objects.get(class_name='English')
    whole_class = Class.objects.get(class_name='Whole Class')

    maths_students = students[:20]
    english_students = students[20:40]
    whole_class_students = students[:30]

    september_date = DateDim.objects.get_or_create(week_commencing=date(2024, 9, 1))[0]
    january_date = DateDim.objects.get_or_create(week_commencing=date(2025, 1, 1))[0]

    # Create class assignments for September
    for student_name in maths_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=maths_class, week_commencing=september_date)
    
    for student_name in english_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=english_class, week_commencing=september_date)

    for student_name in whole_class_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=whole_class, week_commencing=september_date)

    # Create class assignments for January
    for student_name in maths_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=maths_class, week_commencing=january_date)
    
    for student_name in english_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=english_class, week_commencing=january_date)

    for student_name in whole_class_students:
        student = Student.objects.get(student_name=student_name)
        ClassAssignment.objects.create(
            student=student, class_name=whole_class, week_commencing=january_date)
            

def populate_classes():
    classes = ['Whole Class', 'Maths', 'English']
    for cl in classes:
        Class.objects.create(class_name=cl)

def populate_students():
    for st in students:
        Student.objects.create(student_name=st)


class Command(BaseCommand):
    help = 'Populate db with data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--classes',
            action='store_true',
            help="Populate 'Class' model with data"
        )

        parser.add_argument(
            '--students',
            action='store_true',
            help="Populate 'Student' model with data"
        )

        parser.add_argument(
            '--class-assignments',
            action='store_true',
            help="Populate 'ClassAssignment' model with data"
        )

    def handle(self, *args, **options):
        if options.get('classes'):
            populate_classes()
            self.stdout.write(self.style.SUCCESS("'Class' populated successfully"))

        if options.get('students'):
            populate_students()
            self.stdout.write(self.style.SUCCESS("'Student' populated successfully"))

        if options.get('class_assignments'):
            populate_class_assignments()
            self.stdout.write(self.style.SUCCESS("'ClassAssignments' populated successfully"))

        if not any(options.get(key) for key in ['classes', 'students', 'class_assignments']):
            self.stdout.write(self.style.WARNING(
                "No arguments provided. Please use one of the following options:\n"
                "--classes to populate 'Class' model\n"
                "--students to populate 'Student' model\n"
                "--class-assignments to populate 'ClassAssignment' model"
            ))