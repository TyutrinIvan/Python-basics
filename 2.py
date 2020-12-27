time_sec = int(input('Введите количество прошедших секунд за текущий день - '))
while time_sec > 86400:
    print('Пожалуйста, введите количество секунд, прошедших с начала ДАННОГО дня!')
    time_sec = int(input('Введите количество прошедших секунд за текущий день - '))
hours = time_sec // 3600
mins = (time_sec // 60) - (hours * 60)
secs = time_sec - ((mins * 60) + (hours * 3600))
print(f"Настоящее время - {hours:02}:{mins:02}:{secs:02} ")

