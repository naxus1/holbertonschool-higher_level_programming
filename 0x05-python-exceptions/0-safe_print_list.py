#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cont = 0
        for value in range(x):
            print("{}".format(my_list[value]), end="")
            cont += 1
    except:
        pass
    print()
    return(cont)
