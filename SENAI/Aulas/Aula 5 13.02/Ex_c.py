n1 = float(input('1° term grade: '))
n2 = float(input('2° term grade: '))
n3 = float(input('3° term grade: '))
n4 = float(input('4° term grade: '))
md = (n1 + n2 + n3 + n4) / 4

if md >= 5:
    print('GPA: {}\nApproved'.format(md)) # Grade Point Average
else:
    print('GPA: {}\nDisapproved'.format(md)) # Grade Point Average
