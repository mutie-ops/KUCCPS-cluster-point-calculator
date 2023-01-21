# calculating cluster points
from math import sqrt

GRADE_POINTS = {'A': 12, 'A-': 11, 'B+': 10, 'B': 9, 'B-': 8, 'C+': 7, 'C': 6, 'C-': 5,
                'D+': 4, 'D': 3, 'D-': 2, 'E': 1}

CLUSTER_SUBJECTS = ['MATHEMATICS', 'ENGLISH', 'SWAHILI', 'BIOLOGY',
                    'PHYSICS', 'CHEMISTRY', 'CRE', 'COMPUTER']

print('COLLECTIVE GRADE')
print('.......................')
t = input('YOUR GRADE POINTS: ')
R = 48  # maximum performance of relevant subjects
T = 84  # maximum performance of relevant subjects 7 or 8 subjects //spi


# calculate r = sum of cluster subjects

# choose cluster subjects

def inputs():
    print('INPUT SUBJECTS')
    print('.............................')

    subject_1 = input("enter subject 1: ").upper()
    print(subject_1)
    subject_2 = input("enter subject 2: ").upper()
    print(subject_2)
    subject_3 = input("enter subject 3: ").upper()
    print(subject_3)
    subject_4 = input("enter subject 4: ").upper()
    print(subject_4)

    # input grade
    print('INPUT GRADE')
    print('.............................')

    SUBJ = input(subject_1 + ': ').upper()
    if SUBJ in GRADE_POINTS:
        SUBJ_1 = GRADE_POINTS[SUBJ]
        print(str(SUBJ_1))

    SUBJ1 = input(subject_2 + ': ').upper()
    if SUBJ1 in GRADE_POINTS:
        SUBJ_2 = GRADE_POINTS[SUBJ1]
        print(str(SUBJ_2))

    SUBJ2 = input(subject_3 + ': ').upper()
    if SUBJ2 in GRADE_POINTS:
        SUBJ_3 = GRADE_POINTS[SUBJ2]
        print(str(SUBJ_3))

    SUBJ3 = input(subject_4 + ': ').upper()
    if SUBJ3 in GRADE_POINTS:
        SUBJ_4 = GRADE_POINTS[SUBJ3]
        print(str(SUBJ_4))

    r = int(SUBJ_1 + SUBJ_2 + SUBJ_3 + SUBJ_4)  # RAW cluster points

    return r


def cluster_points_():
    ASM = int(inputs()) / R
    # print('ASM:',ASM)

    SMI = int(t) / T
    # print('SMI:',SMI)

    multiplication = ASM * SMI
    ROOT = sqrt(multiplication)
    # print('square_root',ROOT)

    cluster_points = ROOT * 48
    print('your cluster points is: ', cluster_points)


cluster_points_()
