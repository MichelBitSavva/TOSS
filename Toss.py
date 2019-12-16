import itertools
import pprint

# Первые места своих групп
PSG = {"Name": 'PSG', "Country": 'France', "Group": 'A'}
Bayern = {"Name": 'Bayern', "Country": 'Germany', "Group": 'B'}
Man_city = {"Name": 'Man_city', "Country": 'England', "Group": 'C'}
Juventus = {"Name": 'Juventus', "Country": 'Italy', "Group": 'D'}
Liverpool = {"Name": 'Liverpool', "Country": 'England', "Group": 'E'}
# Barcelona = {"Name": 'Barcelona', "Country": 'Spain', "Group": 'F'}
# Leipzig = {"Name": 'Leipzig', "Country": 'Germany', "Group": 'G'}
# Valencia = {"Name": 'Valencia', "Country": 'Spain', "Group": 'H'}

# Вторые места своих групп
Real = {"Name": 'Real', "Country": 'Spain', "Group": 'A'}
Totenhem = {"Name": 'Totenhem', "Country": 'England', "Group": 'B'}
# Atalanta = {"Name": 'Atalanta', "Country": 'Italy', "Group": 'C'}
Atletico = {"Name": 'Atletico', "Country": 'Spain', "Group": 'D'}
Napoli = {"Name": 'Napoli', "Country": 'Italy', "Group": 'E'}
# Borussia = {"Name": 'Borussia', "Country": 'Germany', "Group": 'F'}
# Lyon = {"Name": 'Lyon', "Country": 'France', "Group": 'G'}
Chelsea = {"Name": 'Chelsea', "Country": 'England', "Group": 'H'}

# Корзины жеребьевки
pool_a = [PSG, Bayern, Man_city, Juventus, Liverpool]
pool_b = [Real, Totenhem, Napoli, Chelsea, Atletico]

perm_a = itertools.permutations(pool_a)
perm_b = itertools.permutations(pool_b)
pp = pprint.PrettyPrinter(indent=4)

counter = 0
array_team = []
array_Man_city = []
counter_real = 0
counter_Napoli = 0

list_b = list(perm_b)
list_a = list(perm_a)

for a in list_a:
    assert isinstance(list_b, object)
    for b in list_b:
        for index, team_a in enumerate(a):
            team_b = b[index]
            if team_a["Country"] != team_b["Country"] and team_a["Group"] != team_b["Group"]:
                array_team.append(team_a["Name"] + team_b["Name"])
            if team_a["Name"] == 'Man_city' and team_a["Country"] != team_b["Country"] and team_a["Group"] != team_b["Group"]:
                array_Man_city.append(team_a["Name"])
            if team_a["Name"] == 'Man_city' and team_b["Name"] == 'Real':
                counter_real += 1
            if team_a["Name"] == 'Man_city' and team_b["Name"] == 'Napoli':
                counter_Napoli += 1

print('Всего возможных вариантов пар' + " " + format(len(array_team)))
print('_______________________________________________________________')
print('Всего вариантов с Манчестер Сити' + " " + format(len(array_Man_city)))
print('_______________________________________________________________')
print('Всего вариантов  Манчестер Сити - Реал' + " " + format(counter_real))
print('Вероятность выпадения варианта Манчестер Сити - Реал равна' + " " + format(counter_real / len(array_Man_city) * 100))
print('_______________________________________________________________')
print('Всего вариантов  Манчестер Сити - Наполи' + " " + format(counter_Napoli))
print('Вероятность выпадения варианта Манчестер Сити - Наполи равна' + " " + format(counter_Napoli / len(array_Man_city) * 100))