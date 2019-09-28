import prints as pr
import os
import important_information as i_i
import iteam_print as i_p
from service_menu import service_code as se_cd


def close_menu_zero(listpr, listcn, credit, listbn):
    sum_coin = 0
    for coins in listcn:
        sum_coin += coins
    prdct_num = 0
    for prdct in listcn:
        prdct_num += prdct
    if sum_coin == 0 or prdct_num == 0:
        while True:
            print(pr.NO_COIN)
            cus_code = input(pr.ENTER_CODE)
            if cus_code == "srvop17":
                os.system('cls||clear')
                listpr, listcn, credit, listbn = se_cd(listpr, listcn, credit, listbn)
                if listpr == i_i.LIST_DEFAULT_NUM_PRDCT:
                    return listpr, listcn, credit, listbn
                else:
                    print(pr.UPDATED)
                    print()
                    contin = input(pr.CNT)
            else:
                i_p.error_line()
    else:
        return listpr, listcn, credit, listbn


def check_for_buying_menu(credit, product, listcn):
    price_buy_prdct = i_i.LIST_PRICE[product - 1]
    sum_coin = 0
    for index in range(0, len(listcn) - 1):
        sum_coin += i_i.LIST_RIGHT_CN[index] * listcn[index]
    if credit - price_buy_prdct > sum_coin:
        flag_not_change = True
        return flag_not_change
    else:
        flag_not_change = False
        return flag_not_change


def find_prdct_with_change(credit, list_cn, list_pr):
    counter = 0
    flag_product_buy_with_change = False
    for product in range(0, len(i_i.LIST_PRICE) - 1):
        if list_pr[product] > 0:
            flag_product_buy_with_change = check_for_buying_menu(credit, product, list_cn)
            if flag_product_buy_with_change is True:
                return flag_product_buy_with_change
            else:
                counter += 1
                if counter == len(i_i.LIST_PRICE):
                    print(pr.ERORR_NO_CHANGE_BN)
                    print()
                    contin = input(pr.CNT)
                    return flag_product_buy_with_change

# next lines just for check
# perem = input()
# check_for_int(perem)
# list = []
# list2 = []
# close_menu_zero(list, list2)
