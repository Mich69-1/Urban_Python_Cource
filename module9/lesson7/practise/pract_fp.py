animal = 'мишка'
animals = ['зайка', 'котейка', 'хуейка']

def gen_repeat(n):

    def repeat(animal):

        return (animal[:2] + '-') * n + animal

    return repeat


teste1 = gen_repeat(4)
teste2 = gen_repeat(2)

repetitions = [gen_repeat(n) for n in range(1, 4)]

result = [func(animal) for func in repetitions]
print(result)


usezv = [[func(x) for x in animals for func in repetitions], [func(x) for func in repetitions for x in animals]]
print(usezv)

print([x**2 for x in range(5)])