# This file has a function of inserting banknotes

import os
import important_information as i_i
import prints as pr
from iteam_print import error_line as error
import checker


def while_insert(credit, list_cn, list_pr, list_bn):
    while True:
        print(pr.SEPORATOR)
        print(pr.CREDIT + str(credit))
        print(pr.SEPORATOR)
        print(pr.INSERT_BN)
        print(pr.SUP_BN)
        print(i_i.LIST_RIGHT_BN)
        print(pr.STOP_INSERT)
        try:
            banknote = int(input(pr.CUST_INSERT))
            if banknote == 0:
                break
            if banknote in i_i.LIST_RIGHT_BN:
                credit += banknote
                flag = checker.find_prdct_with_change(credit, list_cn, list_pr)
                if flag is False:
                    credit -= banknote
                else:
                    index = i_i.LIST_RIGHT_BN.index(banknote)
                    list_bn[index] += 1
            else:
                print(pr.SEPORATOR)
                print(pr.ERROR_WR + pr.ERROR_IN_BN)
                print()
                contin = input(pr.CNT)
                os.system('cls||clear')
            os.system('cls||clear')
        except ValueError:
            error()
    return credit, list_bn


# next lines just for check
# cr = 0
# cr = while_insert(cr, i_i.LIST_DEFAULT_NUM_PRDCT, i_i.LIST_DEFAULT_NUM_PRDCT)
# print(i_i.LIST_INSERTED_BN)
# print(pr.CREDIT + str(cr))
