# # Problem 1:
# lang1 = 'Rust'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for x in languages:
#     if x == 'Rust':
#         print('this language is in list')
#     else:
#         pass


# # Problem 2:
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for x in languages:
#     print(x)
#     if x == 'php':
#         break


# # Problem 3:
# i = 3
# factorial = 7
# txt = 7
# while i <= txt:
#     factorial *= 7
#     print(factorial)
#     i += 1


# # Problem 4:
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# i = 0
# x = 0
# while i < len(languages):
#     print(x, languages[i])
#     i += 1
#     x += 1


# # Problem 5:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for x in a:
#     print(x)


# # Problem 6:
# names = ['Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек',
#          'Дастан', 'Бекмамат', 'Аслан']
# for x in range(len(names)):
#     if x % 2 == 0:
#         print(names[x])


# # Problem 7:
# names = ['Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек', 'Эрмек',
#           'Дастан', 'Бекмамат', 'Аслан']
# for x in range(len(names)):
#     if x % 2 == 0:
#         print(names[x])

# # Problem 8:
# a = int(input('введите число: '))
# if a >= 100:
#     print('число трехзначное')
# else:
#     print('число не трехзначное')
# if a > 0 and a % 2 == 0:
#     print('число положительное и четное')
# else:
#     print('число не положительное или не четное')
# if a // 31 == 0:
#     print('делится на 31 без остатка')
# else:
#     print('не делится на 31 без остатка')
# if a > 100 and a % 17 == 0:
#     print('число больше 100 и оно делится на 17 без остатка')
# else:
#     print('число не больше 100 и оно не делится на 17 без остатка')
# if a > 150 and a == (13**2):
#     print(a)



# # Problem 9:
# a = [i**2 for i in range(-100,100) if i % 2 == 0 and i % 13 == 0 ]
# print(a)
# b = [i for i in range(-100,100,7) if i % 2 == 1]
# print(b)
# print(len(a))
# print(len(b))