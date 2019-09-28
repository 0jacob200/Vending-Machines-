# MAIN MENU

# WARNING: This code works correctly only in terminal!

import os
import copy
import important_information as i_i
import prints as pr
import iteam_print as it_pr
from inserting_banknotes import while_insert as inserting
from service_menu import service_code as ser
from buying_code import buy
from getting_change import changer as change
import checker

cust_code = 0
list_num_prdct = copy.deepcopy(i_i.LIST_DEFAULT_NUM_PRDCT)
list_num_cn = copy.deepcopy(i_i.LIST_DEFAULT_NUM_CN)
list_ins_bn = copy.deepcopy(i_i.LIST_INSERTED_BN_DEFAULT)
credit_cust = 0
while True:
    os.system('cls||clear')
    print(pr.SEPORATOR)
    print(pr.HELLO_PRINT)
    while True:
        # Menu level
        print(pr.SEPORATOR)
        print(pr.CREDIT + str(credit_cust))
        print(pr.SEPORATOR)
        print(pr.MENU)
        for print_code in pr.MENU_CODE:
            print(print_code)
        print(pr.SEPORATOR)
        cust_code = input(pr.ENTER_CODE)
        os.system('cls||clear')
        if cust_code == "1":
            # Inserting banknote
            credit_cust, list_ins_bn = inserting(credit_cust, list_num_cn, list_num_prdct, list_ins_bn)
            os.system('cls||clear')
        elif cust_code == "2":
            # List of products
            it_pr.func_prdct(credit_cust, list_num_prdct)
            os.system('cls||clear')
        elif cust_code == "3":
            # Choosing an item
            credit_cust, list_num_prdct = buy(credit_cust, list_num_prdct, list_num_cn)
            os.system('cls||clear')
        elif cust_code == "4":
            # Getting a change
            credit_cust, list_num_cn = change(credit_cust, list_num_cn)
            break
        elif cust_code == "srvop17":
            # Service Menu
            list_num_prdct, list_num_cn, credit_cust, list_ins_bn = ser(list_num_prdct, list_num_cn,
                                                                        credit_cust, list_ins_bn)
            os.system('cls||clear')
        elif cust_code == chr(70):
            it_pr.print_of_print()
            os.system('cls||clear')
        elif cust_code == "OFF":
            # For power off the machine
            os.system('cls||clear')
            quit()
        else:
            it_pr.error_line()
    print(pr.SEPORATOR)
    print(pr.GOODBYE)
    input_line = input(pr.CNT)
    os.system('cls||clear')
    list_num_prdct, list_num_cn, credit_cust, list_ins_bn = checker.close_menu_zero(list_num_prdct, list_num_cn,
                                                                                    credit_cust, list_ins_bn)
