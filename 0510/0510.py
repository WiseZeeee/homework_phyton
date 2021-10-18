import random
def random_name(names, surnames, ser_names, numb):
    i = 0
    while i < numb:
        yield (random.choice(names) + ' ' + random.choice(surnames) + ' ' + random.choice(ser_names))
        i+=1
f1 = ['Камиль', 'Никита', 'Денис', 'Влад', 'Сергей']
f2 = ['Дроздов', 'Березов', 'Иванов', 'Орлов', 'Осипов']
f3 = ['Дммитриевич', 'Олегович', 'Романович', 'Макисмович', 'Алексеевич']
for i in random_name(f1,f2,f3,3):
    print(i)