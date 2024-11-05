from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import RegexValidator

# class DateDim(models.Model):
#   week_commencing = models.DateField(primary_key=True)

class TermPeriod(models.Model):
  week_commencing = models.DateField(primary_key=True)
  week_name = models.CharField(max_length=255)
  period_name = models.CharField(max_length=255)
  period_type = models.CharField(max_length=255, validators=[RegexValidator(r'^term_time|holiday$')])
  

class Job(models.Model):
  job_name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.job_name
  

class Student(models.Model):
  student_name = models.CharField(unique=True, max_length=255)

  def __str__(self):
    return self.student_name


class Class(models.Model):
  class_name = models.CharField(unique=True, max_length=255)

  def __str__(self):
    return self.class_name
  

class JobAssignment(models.Model):
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.CASCADE, )
  job_name = models.ForeignKey(Job, on_delete=models.CASCADE, )
  student_name = models.ForeignKey(Student, on_delete=models.CASCADE, )

  def __str__(self):
    return f'{self.job_name} : {self.student_name}'
  
  
class PlaceInLine(models.Model):
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.CASCADE, )
  student_name = models.ForeignKey(Student, on_delete=models.CASCADE, )
  rank = models.IntegerField()

  def __str__(self):
    return f'{self.week_commencing} : {self.student_name}'
  

class ClassAssignment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, )
  the_class = models.ForeignKey(Class, db_column='class_name', on_delete=models.CASCADE, )
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.CASCADE,
                                      blank=True, null=True,
                                      related_name='date_as_week_commencing')
  week_until = models.ForeignKey(TermPeriod, on_delete=models.CASCADE, 
                                 blank=True, null=True,
                                 related_name='date_as_week_until')
  is_current = models.BooleanField(default=True)

  class Meta:
        constraints = [
            UniqueConstraint(fields=['student', 'the_class', 'week_commencing'], name='unique_student_class_week')
        ]

  def __str__(self):
    return f'{self.student} : {self.week_commencing}'
  

class SeatingAssignment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='seating_assignments_as_student')
  partner = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='seating_assignments_as_partner')
  # seating_layout = models.ForeignKey(SeatingLayout, on_delete=models.DO_NOTHING)
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.DO_NOTHING)
  the_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
  seat_num = models.IntegerField()
  desk_name = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.student} : {self.partner}'



class FloorPlan(models.Model):
  layout = models.JSONField()
  nickname = models.CharField(max_length=1024)
  
  
class SeatingLayout(models.Model):
  floorplan = models.ForeignKey(FloorPlan, on_delete=models.DO_NOTHING)
  the_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING)
  period = models.ForeignKey(TermPeriod, on_delete=models.DO_NOTHING)

  
models_dict = {
  'seating_layout': SeatingLayout,
  'class': Class,
  'term_period': TermPeriod,
  'job': Job,
  'student': Student,
  'job_assignment': JobAssignment,
  'place_in_line': PlaceInLine
}