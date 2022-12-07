num_list = [11,12,13,14,15]
g_comp = (num for num in num_list if num % 5 == 0)
for num in g_comp:
    print(num)