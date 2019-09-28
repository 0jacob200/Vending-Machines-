HELLO = "Hello! This is Personal expense manager."
MAIN_MENU = "      Main menu\n"
SEPORATOR = "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
CODES_MM = "1. List of bank accounts\n2. Expenses per month\n3. Power Off"
ENTER_CODE = "Enter your code: "
INCORRECT_INPUT = "Incorrect input. Try again."
PRESS_ANY_BUTTON = "Press any button to continue."
LIST_BANK = "List of bank, count and balance\n"
TOTAL = "Total"
CURRENCY = "EUR"
ENTER_MANDY = "Enter month and year in YYYY-MM format (0 is exit): "
CHOOSE_CARD = " Choose a credit card or an option\n"
EXIT_MM = "Return to the main menu"
GOODBYE = "Goodbye and see you later.\n\nMade by Yakov Shumilov in May of 2019"
REPORT_FOR = "Report for"
RECEIVED = "Received:"
SPENT = "Spent:"
DELTA = "Delta:"
EXPORT_XLS = "Export a full report to Excel? (y or n) "
MAKING_REPORT_XLS = "Report created, opening ...\n"
SHUPKA = ["Date", "Time", "Bank", "Card", "Operation"]

# This 5 strings can be changed for adding banks:
BANKS_NAME = ["SuperBank", "GorgeousBank"]
# add bank name. Each bank has his own index in all following LISTS!
BANKS_PHONENUMBER = ["480", "720"]
# add phone number
INDEX_OF_SMS = {"operation": [3, 4], "sum": [6, 5], "card": [5, 3], "balance": [9, 8]}
# add index of information in sms of the bank
OPERATION_MEANS = {"received": ["Transfer:", "+"], "spent": ["Withdrawal:", "-"]}
# how to understand the operation
SPLIT_OPERATION_NAME = [False, True]
# Is it necessery to split operation from its sum? For example, "+10" -> "-" "10"
