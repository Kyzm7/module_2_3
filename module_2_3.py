my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while (my_list[a]) > 0 or (my_list[a]) == 0:
    if (my_list[a]) == 0:
        if a < len(my_list):
            a=a+1
            continue
    else:
        print (my_list[a])
        if a < len(my_list):
           a=a+1


