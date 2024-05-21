import datetime as dt

# Укажите дату и время начала прохождения курса
start_moment = dt.datetime(2022, 10, 1, 9, 0, 0)  # ГГГГ, ММ, ДД, ЧЧ, ММ, СС

# Укажите текущую дату и время
current_moment = dt.datetime.now()

# Вычислите разницу между моментами времени
total_time = current_moment - start_moment

print(total_time)