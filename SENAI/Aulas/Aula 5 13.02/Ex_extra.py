n1 = float(input('1° grade: '))
n2 = float(input('2° grade: '))
n3 = float(input('3° grade: '))
n4 = float(input('4° grade: '))
md = (n1 + n2 + n3 + n4) / 4

if md >= 7:
    print('GPA: {}\nApproved'.format(md)) # Grade Point Average
elif md >= 5 and md < 7:
    print('GPA: {}\nSummer School'.format(md)) # Grade Point Average
else:
    print('GPA: {}\nDisapproved'.format(md)) # Grade Point Average