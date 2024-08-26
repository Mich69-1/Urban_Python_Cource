def get_password(num):
    if num > 20 or num < 3:
        print("Похоже Вы плохо рассмотрели число!")
        return "Ошибка!"
    result = ""
    for i in range(1, num):
        for j in range(i+1, num):
            if num % (i + j) == 0:
                result += str(i) + str(j)
    return result


print("Ваш пароль:", get_password(int(input("Число на камне?"))))

