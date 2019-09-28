# Service menu

import os
import copy
import prints as pr
import important_information as i_i
from iteam_print import error_line as error


def service_code(list_pr, list_cn, credit, list_bn):
    print(pr.HELLO_SER)
    index_bn = len(list_bn)
    while True:
        # service menu
        print(pr.SEPORATOR)
        print(pr.MENU_SER)
        for code in pr.MENU_SER_CODE:
            print(code)
        print(pr.SEPORATOR)
        ser_code = input(pr.ENTER_CODE)
        os.system('cls||clear')
        if ser_code == "1":
            # Power off
            quit()
        elif ser_code == "2":
            # Return to main menu
            os.system('cls||clear')
            return list_pr, list_cn, credit, list_bn
        elif ser_code == "3":
            # Service operation
            if credit == 0:
                print(pr.SEPORATOR)
                print(pr.ABOUT_PRODUCT_AND_COIN_NUM)
                print(list_pr)
                print(list_cn)
                list_pr = copy.deepcopy(i_i.LIST_DEFAULT_NUM_PRDCT)
                list_cn = copy.deepcopy(i_i.LIST_DEFAULT_NUM_CN)
                print(pr.SEPORATOR)
                while index_bn != 0:
                    print(pr.VALUE_BN + str(i_i.LIST_RIGHT_BN[index_bn - 1]))
                    print(pr.NUM + str(list_bn[index_bn - 1]))
                    print()
                    index_bn -= 1
                print(pr.SEPORATOR)
                list_bn = copy.deepcopy(i_i.LIST_INSERTED_BN_DEFAULT)
                contin = input(pr.CNT)
                return list_pr, list_cn, credit, list_bn
            else:
                print(pr.CREDIT_0)
                print()
                contin = input(pr.CNT)
            os.system('cls||clear')
        elif ser_code == "4":
            # Show information
            print(pr.SEPORATOR)
            print(pr.SHOW_INFO)
            print(list_bn)
            print(list_cn)
            print(list_pr)
            print(pr.SEPORATOR)
            print()
            input_line = input(pr.CNT)
            os.system('cls||clear')
        else:
            error()


# next line just for check
# service_code()
