n1 = float(input('1° term grade: '))
n2 = float(input('2° term grade: '))
n3 = float(input('3° term grade: '))
n4 = float(input('4° term grade: '))
md1 = (n1 + n2 + n3 + n4) / 4

if md1 >= 7:
    print('GPA: {}\nApproved'.format(md1)) # Grade Point Average
else:
    ne = float(input('Exam grade: '))
    md2 = (md1 + ne) / 2
    
    if md2 >= 5: 
        print('GPA: {}\nApproved in exam'.format(md2)) # Grade Point Average
    else:
        print('GPA: {}\nDisapproved'.format(md2)) # Grade Point Average









    