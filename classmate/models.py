from django.db import models
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
  student_name = models.CharField(max_length=255)

  def __str__(self):
    return self.student_name


class Class(models.Model):
  class_name = models.CharField(max_length=255)

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
  

class SeatingAssignment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE,
                              related_name='seating_assignments_as_student')
  partner = models.ForeignKey(Student, on_delete=models.CASCADE, 
                              blank=True, null=True,
                              related_name='seating_assignments_as_partner')
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.CASCADE, )
  class_name = models.ForeignKey(Class, on_delete=models.CASCADE, )
  desk_num = models.IntegerField()

  def __str__(self):
    return f'{self.student} : {self.partner}'
  

class ClassAssignment(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE, )
  class_name = models.ForeignKey(Class, on_delete=models.CASCADE, )
  week_commencing = models.ForeignKey(TermPeriod, on_delete=models.CASCADE,
                                      blank=True, null=True,
                                      related_name='date_as_week_commencing')
  week_until = models.ForeignKey(TermPeriod, on_delete=models.CASCADE, 
                                 blank=True, null=True,
                                 related_name='date_as_week_until')

  def __str__(self):
    return f'{self.student} : {self.week_commencing}'
