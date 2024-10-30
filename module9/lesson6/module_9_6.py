# Домашнее задание по теме "Генераторы"


def all_variants(text):
    cnt = 2                                         # Счетчик длин подпоследовательностей
    while cnt <= len(text)+1:
        cnt1 = cnt-1                                # Счетчик подпоследовательностей длины cnt-1 символов
        while cnt1 <= len(text):
            yield text[cnt1-(cnt-1):cnt1]           # Возврат подпоследовательнрости длины cnt-1
            cnt1 += 1
        cnt += 1


a = all_variants("abc")
for i in a:
    print(i)
