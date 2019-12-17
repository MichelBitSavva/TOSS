import itertools
import pprint

# Первые места своих групп
PSG = {"Name": 'PSG', "Country": 'France', "Group": 'A'}
Bayern = {"Name": 'Bayern', "Country": 'Germany', "Group": 'B'}
Man_city = {"Name": 'Man_city', "Country": 'England', "Group": 'C'}
Juventus = {"Name": 'Juventus', "Country": 'Italy', "Group": 'D'}
Liverpool = {"Name": 'Liverpool', "Country": 'England', "Group": 'E'}
Barcelona = {"Name": 'Barcelona', "Country": 'Spain', "Group": 'F'}
Leipzig = {"Name": 'Leipzig', "Country": 'Germany', "Group": 'G'}
Valencia = {"Name": 'Valencia', "Country": 'Spain', "Group": 'H'}

# Вторые места своих групп
Real = {"Name": 'Real', "Country": 'Spain', "Group": 'A'}
Totenhem = {"Name": 'Totenhem', "Country": 'England', "Group": 'B'}
Atalanta = {"Name": 'Atalanta', "Country": 'Italy', "Group": 'C'}
Atletico = {"Name": 'Atletico', "Country": 'Spain', "Group": 'D'}
Napoli = {"Name": 'Napoli', "Country": 'Italy', "Group": 'E'}
Borussia = {"Name": 'Borussia', "Country": 'Germany', "Group": 'F'}
Lyon = {"Name": 'Lyon', "Country": 'France', "Group": 'G'}
Chelsea = {"Name": 'Chelsea', "Country": 'England', "Group": 'H'}

# Корзины жеребьевки
pool_a = [PSG, Bayern, Man_city, Juventus, Liverpool, Barcelona, Leipzig, Valencia]
pool_b = [Real, Totenhem, Atalanta, Atletico, Napoli, Borussia, Lyon, Chelsea]

perm_a = itertools.permutations(pool_a)
perm_b = itertools.permutations(pool_b)
pp = pprint.PrettyPrinter(indent=4)

list_b = list(perm_b)
list_a = list(perm_a)

x = []
counter = 0
counter_PSG = 0
counter_PSG_Totenhem = 0
counter_PSG_Atalanta = 0
counter_PSG_Atletico = 0
counter_PSG_Napoli = 0
counter_PSG_Borussia = 0
counter_PSG_Chelsea = 0

for a in list_a:
    assert isinstance(list_b, object)
    for b in list_b:
        for index, team_a in enumerate(a):
            team_b = b[index]
            x.append(team_a)
            x.append(team_b)
            if len(x) >= 15:
                for t in x:
                    if ((x[0]["Country"]) == (x[1]["Country"])) or ((x[0]["Group"]) == (x[1]["Group"])) or (
                            (x[2]["Country"]) == (x[3]["Country"])) or ((x[2]["Group"]) == (x[3]["Group"])) or (
                            (x[4]["Country"]) == (x[5]["Country"])) or ((x[4]["Group"]) == (x[5]["Group"])) or (
                            (x[6]["Country"]) == (x[7]["Country"])) or ((x[6]["Group"]) == (x[7]["Group"])) or (
                            (x[8]["Country"]) == (x[9]["Country"])) or ((x[8]["Group"]) == (x[9]["Group"])) or (
                            (x[10]["Country"]) == (x[11]["Country"])) or ((x[10]["Group"]) == (x[11]["Group"])) or (
                            (x[12]["Country"]) == (x[13]["Country"])) or ((x[12]["Group"]) == (x[13]["Group"]))or (
                            (x[14]["Country"]) == (x[15]["Country"])) or ((x[14]["Group"]) == (x[15]["Group"])):
                        x.clear()

                    else:
                        for el in x:
                            if el["Name"] == 'PSG':
                                counter_PSG +=1
                                index = x.index(el) + 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Totenhem':
                                counter_PSG_Totenhem += 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Atalanta':
                                counter_PSG_Atalanta += 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Atletico':
                                counter_PSG_Atletico += 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Napoli':
                                counter_PSG_Napoli += 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Borussia':
                                counter_PSG_Borussia += 1
                            if el["Name"] == 'PSG' and x[index]["Name"] == 'Chelsea':
                                counter_PSG_Chelsea += 1
                        print(counter_PSG)
                        x.clear()
print(counter_PSG)
print('-------------------------')
print(counter_PSG_Totenhem)
print(counter_PSG_Atalanta)
print(counter_PSG_Atletico)
print(counter_PSG_Napoli)
print(counter_PSG_Borussia)
print(counter_PSG_Chelsea)
print('-------------------------')
print('Вероятность выпадения варианта PSG - Totenhem равна' + " " + format(counter_PSG_Totenhem / counter_PSG * 100))
print('Вероятность выпадения варианта PSG - Atalanta равна' + " " + format(counter_PSG_Atalanta / counter_PSG * 100))
print('Вероятность выпадения варианта PSG - Atletico равна' + " " + format(counter_PSG_Atletico / counter_PSG * 100))
print('Вероятность выпадения варианта PSG - Napoli равна' + " " + format(counter_PSG_Napoli / counter_PSG * 100))
print('Вероятность выпадения варианта PSG - Borussia равна' + " " + format(counter_PSG_Borussia / counter_PSG * 100))
print('Вероятность выпадения варианта PSG - Borussia равна' + " " + format(counter_PSG_Chelsea / counter_PSG * 100))
