import constants as const
import core
import os

"""
WARNING: Works correctly in terminal.

The dataset should be in chronological order from the oldest sms to the newest one.
A telephone number is the first place, date and time in format YYYY-MM-DD hh:mm is the second one
and text of sms is the last place.

The openpyxl is sheet. It has some problems with last version of Python (3.7.2)

This code has few piece:
1. CORE  - main logic and the most number of calculation
2. INTERFACE
3. CONSTANTS  - strings and some arguments to change for adding new bank
4. SMS_data - SMS for data processing
"""


def endless_cycle():
    os.system("cls||clear")
    print(const.SEPORATOR)
    print(const.HELLO)
    while True:
        print(const.SEPORATOR)
        print(const.MAIN_MENU)
        print(const.CODES_MM)
        print(const.SEPORATOR)
        cust_code = input(const.ENTER_CODE)
        os.system("cls||clear")
        if cust_code == "1":
            list_bank_accounts()
        elif cust_code == "2":
            expenses_per_month()
        elif cust_code == "3":
            print(const.SEPORATOR)
            input(const.GOODBYE)
            os.system("cls||clear")
            quit()
        elif cust_code == "off":
            quit()
        else:
            print_incorrect_input()
        os.system("cls||clear")


def list_bank_accounts():
    os.system("cls||clear")
    print(const.SEPORATOR)
    print(const.LIST_BANK)
    counter1 = 0
    total_balance = 0
    card_in_print_num = 1
    while counter1 != len(const.BANKS_NAME):
        card_list, balance_list = core.take_card_and_balance(counter1)
        counter1_2 = 0
        while counter1_2 != len(card_list):
            print(f"{card_in_print_num}. {const.BANKS_NAME[counter1]} {card_list[counter1_2]} balance:"
                  f" {balance_list[counter1_2]} {const.CURRENCY}")
            total_balance += float(balance_list[counter1_2])
            counter1_2 += 1
            card_in_print_num += 1
        counter1 += 1
    print(const.SEPORATOR)
    print(f"{const.TOTAL}: {total_balance} {const.CURRENCY}\n")
    code = input(const.PRESS_ANY_BUTTON)
    if code == "off":
        os.system("cls||clear")
        quit()


def expenses_per_month():
    while True:
        os.system("cls||clear")
        print(const.SEPORATOR)
        month_and_year = input(const.ENTER_MANDY)
        if month_and_year == "off":
            os.system("cls||clear")
            quit()
        elif month_and_year == "0" or month_and_year == '':
            return
        month_and_year = core.make_date_format(month_and_year)
        if month_and_year is False:
            print_incorrect_input()
        else:
            break
    while True:
        print(const.SEPORATOR)
        print(const.CHOOSE_CARD)
        print("1. " + const.EXIT_MM)
        print("2. " + const.TOTAL)
        counter2 = 0
        all_cards_list = []
        point_print_for_card = 3
        while counter2 != len(const.BANKS_NAME):
            counter2_1 = 0
            cards, balances = core.take_card_and_balance(counter2)
            all_cards_list.append(cards)
            while counter2_1 != len(cards):
                print(f"{point_print_for_card}. {const.BANKS_NAME[counter2]} ({cards[counter2_1]})")
                counter2_1 += 1
                point_print_for_card += 1
            counter2 += 1
        print(const.SEPORATOR)
        cust_code_1 = input(const.ENTER_CODE)
        os.system("cls||clear")
        if cust_code_1 == "off":
            quit()
        else:
            try:
                cust_code_1 = int(cust_code_1)
            except ValueError:
                print_incorrect_input()
            else:
                if cust_code_1 == 1:
                    return
                elif cust_code_1 == 2:
                    received_total, spent_total, delta_total = \
                        core.total_per_month(month_and_year, all_cards_list)
                    print(const.SEPORATOR)
                    print(f"{const.REPORT_FOR} {month_and_year} of all cards\n")
                    print(f"{const.RECEIVED} {received_total} {const.CURRENCY}")
                    print(f"   {const.SPENT} {spent_total} {const.CURRENCY}")
                    print(f"   {const.DELTA} {delta_total} {const.CURRENCY}")
                    print(const.SEPORATOR)
                    export_to_xls = input(const.EXPORT_XLS)
                    if export_to_xls == "y":
                        print(const.SEPORATOR)
                        print(const.MAKING_REPORT_XLS)
                        bank_all = []
                        for num in range(len(const.BANKS_NAME)):
                            bank_all.append(num)
                        core.creating_xl_for_all(month_and_year)
                        input(const.PRESS_ANY_BUTTON)
                    elif export_to_xls == "n":
                        os.system("cls||clear")
                    elif export_to_xls == "off":
                        os.system("cls||clear")
                        quit()
                    else:
                        print_incorrect_input()
                    os.system("cls||clear")
                elif 2 < cust_code_1 < point_print_for_card:
                    number_card_in_menu = cust_code_1 - 2
                    sum_of_list_len_before = 0
                    bank = 0
                    card = 0
                    while bank != len(all_cards_list):
                        cards_of_bank = all_cards_list[bank]
                        if (number_card_in_menu - sum_of_list_len_before) <= len(cards_of_bank):
                            card = cards_of_bank.pop(number_card_in_menu - sum_of_list_len_before - 1)
                            break
                        else:
                            sum_of_list_len_before += len(cards_of_bank)
                            bank += 1
                    print_expanse_bank(bank, card, month_and_year)
                else:
                    print_incorrect_input()
            os.system("cls||clear")


def print_expanse_bank(bank_index, card,  date_cust):
    data_sms, received, spent, delta = core.income_and_outcome_calculation(bank_index, card, date_cust)
    while True:
        print(const.SEPORATOR)
        print(f"{const.REPORT_FOR} {date_cust} card {card} {const.BANKS_NAME[bank_index]}\n")
        print(f"{const.RECEIVED} {received} {const.CURRENCY}")
        print(f"   {const.SPENT} {spent} {const.CURRENCY}")
        print(f"   {const.DELTA} {delta} {const.CURRENCY}")
        print(const.SEPORATOR)
        export_to_xls = input(const.EXPORT_XLS)
        if export_to_xls == "y":
            print(const.SEPORATOR)
            print(const.MAKING_REPORT_XLS)
            core.creating_xls_file(data_sms, date_cust, bank_index, card)
            input(const.PRESS_ANY_BUTTON)
            break
        elif export_to_xls == "n":
            os.system("cls||clear")
            break
        elif export_to_xls == "off":
            os.system("cls||clear")
            quit()
        else:
            print_incorrect_input()
        os.system("cls||clear")


def print_incorrect_input():
    os.system("cls||clear")
    print(const.SEPORATOR)
    print(f"{const.INCORRECT_INPUT}\n")
    code = input(const.PRESS_ANY_BUTTON)
    if code == "off":
        os.system("cls||clear")
        quit()
    os.system("cls||clear")


endless_cycle()
