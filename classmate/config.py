# Excel templates 
DATA_FOLDER = 'data/'
TEMPLATE_PATH = 'data/class_admin.xlsx'
HOMEWORK_TRACKER_PATH = 'data/homework_tracker.xlsx'
NUM_DESKS = 30

class SeatingPlanCellReferences:
    title = 'B4'
    orig_range = 'B4:M15'
    titles = ['B4', 'B22', 'O4', 'O22']
    save_toggles = ['G4', 'G22', 'T4', 'T22']
    period = 'K1'
    commencing = 'K2'
    height = 19
    desks = {
        'Swift': [
            (1, 'C8'),
            (2, 'C9'),
            (3, 'D8'),
            (4, 'D9'),
            (5, 'C10'),
            (6, 'D10'),
            ],
        'Blackbird': [
            (7, 'I9'),
            (8, 'J9'),
            (9, 'K9'),
            (10, 'L9'),
        ],
        'Greenfinch': [
            (11, 'F11'),
            (12, 'F12'),
            (13, 'G11'),
            (14, 'G12'),
            (15, 'F13'),
            (16, 'G13'),
        ],
        'Robin': [
            (17, 'K12'),
            (18, 'K13'),
            (19, 'L12'),
            (20, 'L13'),
            (21, 'K14'),
            (22, 'L14'),
        ],
        'Wagtail': [
            (23, 'C14'),
            (24, 'C15'),
            (25, 'C16'),
            (26, 'D16'),
        ],
        'Starling': [
            (27, 'I17'),
            (28, 'J17'),
            (29, 'K17'),
            (30, 'L17'),
        ]
    }

class LiningUpCellReferences:
    period = 'K1'
    commencing = 'K2'

    title_row = 4
    start_row = 5
    
    cols = [3, 6, 9, 12]