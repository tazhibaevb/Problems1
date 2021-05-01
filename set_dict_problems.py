# # Problem 0:
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# a = 6
# dates_of_birth.discard(a)
# print(dates_of_birth)


# # Problem 1:
# a = {1}
# b = {2}
# c = a.union(b)
# print(c)


# # Problem 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_2.difference(farm_1)
# print(a)


# # Problem 3:
# a = {1,2,3,4,5}
# b = 6
# a.add(b)
# a.pop()
# print(a)


# # Problem 10:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['Coca-Cola', 'Sprite', 'Fanta'] = 'drinks'
# print(menu)


# # Problem 020:
# a = {'add("*")', '.remove("*")', '.clear()', '.difference("*")', '.update("*")',
#      '.discard("*")', '.intersection("*")', '.intersection_update(*)', '.pop()'}
# b = {'.clear()', '.keys()', '.items()', '.get("*")', '.values()', '.update("*")'}
# c = a.intersection(b)
# print(c)


# # Problem 31:
# a = { }
# for x in range(3):
#     name = input('логин: ')
#     password = input('пароль: ')
#     a[name] = password
# print(a)


# Problem 27:
# name = ['baha', 'almaz', 'beka', 'cate', 'irvin']
# prof = ['gamer', 'driver', 'doctor', 'banker', 'surgeon']
# a = { }
# for x in range(len(name)):
#     print(f'Здравствуйте {name[x]}. Прекрасная профессия - {prof[x]}')


# # Problem 22:
# a = set()
# for x in range(10):
#     b = input('цифра? ')
#     a.add(b)
# x = frozenset(a)
# print(x)


# # Problem 99:
# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['besh_bermak'] = 130
# print(menu)
# menu['besh_bermak'] = 135
# print(menu)
# menu.pop('borsh')
# print(menu)


# # Problem 11:
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana',
#                             'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# s_a_countries = list(set(south_american_countries))
# print(s_a_countries)


# # Problem 101:
# suitcase = []
# suitcase.append(1)
# suitcase.append(2)
# suitcase.append(3)
# suitcase.append(4)
# suitcase.append(5)
# suitcase.pop(-1)
# print(suitcase)


# # Problem 001:
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# a = farm_1 & farm_2
# print(farm_1 & farm_2)
# b = farm_1 - farm_2
# print(b)
