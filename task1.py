runningGlobal = True

while runningGlobal:
    running = True
    print("Введите данные в формате ИМЯ;ВОЗРАСТ;ПОЛ (Возраст в годах, пол М/F)")
    print('Введите "calc" для подсчета среднего возраста')
    print('Введите "q" для выхода')
    mCount = 0
    fCount = 0
    mAgeSum = 0
    fAgeSum = 0
    while running:

        s = input()

        if s == "q":
            runningGlobal = False
            break
        if s == "calc":
            if mCount != 0:
                print("Средний возраст мальчиков:", round(mAgeSum/mCount,3))
            if fCount != 0:
                print("Средний возраст девочек:", round(fAgeSum / fCount,3))
            if mCount == 0 and fCount == 0:
                print("Вы ничего не ввели!!!")

            break

        if s != "q" and s != "calc":
            s = s.split(';')
            if len(s) == 3:
                try:
                    age = float(s[1])
                    if s[2] == 'M':
                        mCount += 1
                        mAgeSum += age
                    if s[2] == 'F':
                        fCount += 1
                        fAgeSum += age
                except:
                    print("Вы ввели некорректное значение возраста!")
                
                if s[2] != 'F':
                    if s[2] != "M":
                        print('Вы ввели некорректный пол!')

            else:
                print("Вы не соблюли синтаксис!")
            
print('Exit OK')