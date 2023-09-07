# master commit
# dsjgjdjfgdjgjdfg
# develop commit
# some information

# develop commit

n1 = int(input("введите первую цифру "))
n2 = int(input("введите вторую цифру "))
n3 = int(input("введите третью цифру "))

user_choice = int(input("введите 1, чтобы узнать максимальную цифру\n2, чтобы узнать минимальную цифру\n3, чтобы узнать среднее арифметическое чисел\n"))

if user_choice == 1:
    if n1 >= n2 >= n3:
        print(n1)
    elif n2 >= n1 >= n3:
        print(n2)
    else:
        print(n3)
elif user_choice == 2:
    if n1 <= n2 <= n3:
        print(n1)
    elif n2 <= n1 <= n3:
        print(n2)
    else:
        print(n3)
elif user_choice == 3:
    print((n1 + n2 + n3) / 3)
else:
    print("Неверный выбор")
    
# ############################
# ############################
