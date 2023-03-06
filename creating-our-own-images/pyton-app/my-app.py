import calendar

print('Добро пожаловать в календарь\n')

year = int(input('Введите год:'))
mount = int(input('Введите месяц:'))

print(calendar.monthcalendar(year, mount))

print('Good bye!')
