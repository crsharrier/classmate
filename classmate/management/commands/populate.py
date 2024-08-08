from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from classmate.models import Class, Student, ClassAssignment, TermPeriod

import pandas as pd
from datetime import datetime, timedelta

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

# def populate_dates():
#     start_date = timezone.datetime(2020, 1, 1)  # Start from January 1, 2020
#     end_date = timezone.datetime(2030, 12, 31)  # End at December 31, 2030
#     current_date = start_date

#     while current_date <= end_date:
#         # Ensure the date is the Monday of the week
#         week_commencing = current_date - timedelta(days=current_date.weekday())

#         # Create DateDim object and save
#         DateDim.objects.create(week_commencing=week_commencing)

#         # Move to the next Monday (start of next week)
#         current_date += timedelta(days=7)


def populate_class_assignments():
    maths_class = Class.objects.get(class_name='Maths')
    english_class = Class.objects.get(class_name='English')
    whole_class = Class.objects.get(class_name='Whole Class')

    maths_students = students[:20]
    english_students = students[20:40]
    whole_class_students = students[:30]

    september_date = TermPeriod.objects.get_or_create(week_commencing=date(2024, 9, 9))[0]
    january_date = TermPeriod.objects.get_or_create(week_commencing=date(2025, 1, 6))[0]

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

def populate_term_periods():
    df = pd.read_csv('data/term_periods.csv')
    for _, row in df.iterrows():
        wc = datetime.strptime(row['week_commencing'], '%d/%m/%y')

        tp = TermPeriod(
            week_commencing = wc,
            week_name = row['week_name'],
            period_name = row['period_name'],
            period_type = row['period_type'],
        )
        tp.save()

class Command(BaseCommand):
    help = 'Populate db with data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help="Populate all models with data"
        )

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

        parser.add_argument(
            '--term-periods',
            action='store_true',
            help="Populate 'ClassAssignment' model with data"
        )

        # parser.add_argument(
        #     '--dates',
        #     action='store_true',
        #     help="Populate 'ClassAssignment' model with data"
        # )

    def handle(self, *args, **options):
        if options.get('all'):
            populate_term_periods()
            populate_classes()
            populate_students()
            populate_class_assignments()
            self.stdout.write(self.style.SUCCESS("All entities populated successfully"))

        if options.get('classes'):
            populate_classes()
            self.stdout.write(self.style.SUCCESS("'Class' populated successfully"))

        if options.get('students'):
            populate_students()
            self.stdout.write(self.style.SUCCESS("'Student' populated successfully"))

        if options.get('class_assignments'):
            populate_class_assignments()
            self.stdout.write(self.style.SUCCESS("'ClassAssignments' populated successfully"))

        if options.get('term_periods'):
            populate_term_periods()
            self.stdout.write(self.style.SUCCESS("'TermPeriods' populated successfully"))

        # if options.get('dates'):
        #     populate_dates()
        #     self.stdout.write(self.style.SUCCESS("'DateDim' populated successfully"))

        if not any(options.get(key) for key in ['all', 'classes', 'students', 'class_assignments', 'term_periods']):
            self.stdout.write(self.style.WARNING(
                "No arguments provided. Please use one of the following options:\n"
                "--classes to populate 'Class' model\n"
                "--students to populate 'Student' model\n"
                "--class-assignments to populate 'ClassAssignment' model"
            ))