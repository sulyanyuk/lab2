print('Вводите время заплывов по очереди, "print" для вывода наименьшего, "q" для выхода')
globalRun = True
while globalRun:
    while True:
        try:
            inp = input()
            if inp == "q":
                globalRun = False
                break
            if inp == "print":
                print("Введите хотя-бы одно число!")
            else:
                top = round(float(inp),3)
                break
        except ValueError:
            print("Введите хотя-бы одно число!")

    if not globalRun:
        break

    while True:
        mostRecent = input()
        if mostRecent == 'print': 
            print('Лучшее время: ',top)
            break
        elif mostRecent == 'q':
            break
        else:
            try:
                mostRecent = round(float(mostRecent),3)
                if mostRecent < top:
                    top = mostRecent
            except:
                print("Вы ввели не число!")
    
print('Exit OK')
