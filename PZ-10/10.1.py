c = 0

voyage = {'mexico', 'canada', 'israel', 'italy', 'usa'}
reyna_tour = {'england', 'japan', 'canada', 'sar'}
rainbow = {'usa', 'spain', 'scotland', 'australia', 'italy', 'canada'}

a = {'italy', 'canada'}
penis = [voyage, reyna_tour, rainbow]
penis_2_0 = ['voyage', 'reyna_tour', 'rainbow']

# в каких турагенствах туры в италию и канаду
for i in penis:
    b = i & a
    if b == a:
        print(f'В туре {penis_2_0[c]}')
    c = +1

# добавление страны в турагенство
reyna_tour.update(['india'])
print(reyna_tour)

# список всех туров
print(f'список всех туров: {voyage|reyna_tour|rainbow}')


