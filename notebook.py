from datetime import date
import os 
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classmate.settings')
django.setup()

from classmate.models import Class, Student, TermPeriod
from classmate.excel_backend import (
    generate_seating_plan, print_seating_plans, generate_lining_up_order, 
    print_lining_up_orders
    )
from openpyxl import load_workbook
from classmate.config import *

wb = load_workbook(TEMPLATE_PATH, keep_vba=True)
period = TermPeriod.objects.get(week_commencing=date(2024, 9, 2))

classes_seating = {}
for name in ('Reading', 'Writing', 'Maths', 'Whole Class'):
    cls = Class.objects.get(class_name=name)
    desk_details = generate_seating_plan(cls)
    classes_seating[cls] = desk_details
print_seating_plans(wb, classes_seating, period)

lining_up_orders = {}
for cl in ['Whole Class', 'Maths', 'Reading', 'Writing']: 
    lining_up_orders[cl] = generate_lining_up_order(cl)

print_lining_up_orders(wb, lining_up_orders, period)

output_path =f'{DATA_FOLDER}Class Admin {period.period_name}.xlsx'
wb.save(output_path)
