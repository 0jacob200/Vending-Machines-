# Function to get change

import important_information as i_i
import prints as pr


def changer(credit, list_cn):
    print(pr.SEPORATOR)
    print(pr.TAKE_CHANGE)
    print(pr.SEPORATOR)
    for r_coin in i_i.LIST_RIGHT_CN:
        index = i_i.LIST_RIGHT_CN.index(r_coin)
        if list_cn[index] > 0:
            num_coin = credit // r_coin
            if num_coin > list_cn[index]:
                print(pr.VALUE_CN + str(r_coin))
                print(pr.NUM + str(0))
                print()
            else:
                print(pr.VALUE_CN + str(r_coin))
                print(pr.NUM + str(num_coin))
                print()
                credit -= r_coin * num_coin
                list_cn[index] -= num_coin
        else:
            print(pr.VALUE_CN + str(r_coin))
            print(pr.NUM + str(0))
            print()
    return credit, list_cn


# def give_change(credit, list_cn):
#     print(pr.SEPORATOR)
#     print(pr.TAKE_CHANGE)
#     print(pr.SEPORATOR)
#     for r_coin in range(0, len(i_i.LIST_RIGHT_CN))
#         if list_cn[r_coin] > 0:
#


# next lines just for check
# cr = int(input())
# changer(cr)
# print(i_i.LIST_NUM_CN)
