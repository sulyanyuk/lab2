while True:
    try:
        n = int(input('Введите кол-во учащихся: '))
        break
    except ValueError:
        print("Вы ввели некорректное число студентов!",end=' ')

print('Вводите отметки в формате "ОЦ1,ОЦ2,ОЦ3,ОЦ4" ')

failed = 0
total = 0
for s in range(1, n + 1):
    correctInput = False
    while not correctInput:
        try:
            marks = input(f'Оценки учащегося {s}: ').split(',')
            if len(marks) == 4:
                countedFailure = False
                totalScore = 0
                for mark in marks:
                    if (float(mark) <= 2.0) and not countedFailure:
                        failed += 1
                        countedFailure = True
                    totalScore += float(mark)
                correctInput = True
            else:
                print("Вы неверно ввели оценки!")
        except ValueError:
            print("Вы неверно ввели оценки!")
    total += totalScore
avg = total/(4*n)
print(f"Failed: {failed}, avg: {avg}")