# Function to buy a product

import important_information as i_i
import prints as pr
import iteam_print as i_p
import os
import checker


def buy(credit, list_pr, list_cn):
    print(pr.SEPORATOR)
    print(pr.CREDIT + str(credit))
    print(pr.SEPORATOR)
    try:
        product = int(input(pr.CHOOSE_IT))
        # flag = checker.check_for_buying_menu(credit, product, list_cn)
        # if flag is True:
        #     print(pr.NO_CHAHGE)
        #     print()
        #     contin = input(pr.CNT)
        #     return credit, list_pr
        if 0 < product < len(list_pr):
            if i_i.LIST_PRICE[product - 1] <= credit:
                if list_pr[product - 1] > 0:
                    credit -= i_i.LIST_PRICE[product - 1]
                    list_pr[product - 1] -= 1
                else:
                    print(pr.NO_PRDCT)
                    print()
                    input_line = input(pr.CNT)
                    return credit, list_pr
            else:
                print(pr.CANT_BUY)
                print()
                input_line = input(pr.CNT)
                return credit, list_pr
        else:
            i_p.error_line()
            return credit, list_pr
        print(pr.CUST_PRDCT)
        i_p.print_itm(product, list_pr)
        input_line = input(pr.CNT)
        return credit, list_pr
    except ValueError:
        i_p.error_line()
        return credit, list_pr


# next line for check
# cr = int(input())
# # buy(cr)
