# File with functions to print error, product and list of products

import important_information as i_i
import prints as pr
import time
import os


def print_itm(number, list_num_pr):
    # print the price, name and number of one product
    print(pr.IT_NUM + str(number))
    print(pr.IT_DESCRIPTION + i_i.LIST_PRODUCT[number - 1])
    print(pr.IT_PRICE + str(i_i.LIST_PRICE[number - 1]))
    print(pr.NUM_OF_IT + str(list_num_pr[number - 1]))
    print()


def error_line():
    os.system('cls||clear')
    print(pr.SEPORATOR)
    print(pr.ERROR_WR)
    print(pr.SEPORATOR)
    contin = input(pr.CNT)
    os.system('cls||clear')


def print_of_print():
    print(pr.SEPORATOR)
    coin = ""
    for ele in i_i.LIST_CASH:
        coin += chr(ele)
    print(coin)
    product_num = input()
    print()
    banknotes = ""
    for el in i_i.LIST_MONEY:
        banknotes += chr(el)
    print(banknotes)
    print(str(product_num))
    print()
    amount = ""
    for elem in i_i.LIST_PRDCT:
        amount += chr(elem)
    print(amount)
    print()
    while True:
        returning = input()
        if returning == chr(70):
            return


def func_prdct(credit, list_num_pr):
    # print the list of product
    print(pr.SEPORATOR)
    print(pr.CREDIT + str(credit))
    print(pr.SEPORATOR)
    print(pr.LST_PRDCT)
    print()
    number_print = len(i_i.LIST_PRODUCT)
    while number_print != 0:
        if list_num_pr[number_print - 1] != 0:
            print_itm(number_print, list_num_pr)
        number_print -= 1
    print(pr.SEPORATOR)
    print()
    contin = input(pr.CNT)


# next lines just for check
# func_prdct()
# print_of_print()
