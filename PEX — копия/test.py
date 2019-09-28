#!/usr/local/bin/python3

import constants as const
import datetime
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Alignment, Side
import subprocess
import sys
import os


def creating_xls_file(data_set, date, bank, card):
    doc = Workbook()
    sheet = doc.active
    sheet.append(const.SHUPKA)
    total_received = 0
    total_spent = 0
    for sms in data_set:
        if const.BANKS_PHONENUMBER[bank] == sms[0]:
            operation = ''
            sum_of_operation = sms[const.INDEX_OF_SMS["sum"][bank]]
            if const.OPERATION_MEANS["received"][bank] in sms:
                operation = '+'
                total_received += float(sum_of_operation)
            elif const.OPERATION_MEANS["spent"][bank] in sms:
                operation = '-'
                total_spent += float(sum_of_operation)
            else:
                print('something wrong')
            operation_str = f'{operation}{float(sms[const.INDEX_OF_SMS["sum"][bank]])} {const.CURRENCY}'
            row = [sms[1], sms[2], const.BANKS_NAME[bank], sms[const.INDEX_OF_SMS["card"][bank]][:5], operation_str]
            sheet.append(row)
    total_sum = total_received - total_spent
    total_row_1 = [const.TOTAL, '', '', const.RECEIVED, f"{total_received} {const.CURRENCY}"]
    total_row_2 = ['', '', '', const.SPENT, f"{total_spent} {const.CURRENCY}"]
    total_row_3 = ['', '', '', const.DELTA, f"{total_sum} {const.CURRENCY}"]
    sheet.append(total_row_1)
    sheet.append(total_row_2)
    sheet.append(total_row_3)
    border = Border(left=Side(border_style='thin',
                              color='FF000000'),
                    right=Side(border_style='thin',
                               color='FF000000'),
                    top=Side(border_style='thin',
                             color='FF000000'),
                    bottom=Side(border_style='thin',
                                color='FF000000'),
                    diagonal=Side(border_style='thin',
                                  color='FF000000'),
                    diagonal_direction=0,
                    outline=Side(border_style='thin',
                                 color='FF000000'),
                    vertical=Side(border_style='thin',
                                  color='FF000000'),
                    horizontal=Side(border_style='thin',
                                    color='FF000000')
                    )
    align_center = Alignment(horizontal='center',
                             vertical='bottom',
                             text_rotation=0,
                             wrap_text=False,
                             shrink_to_fit=False,
                             indent=0)
    for cell_1 in sheet[f'A1:E{len(data_set) + 4}']:
        for cell in cell_1:
            sheet[cell.coordinate].border = border
            sheet[cell.coordinate].alignment = align_center
    dims = {}
    for row in sheet.rows:
        for cell in row:
            if cell.value:
                dims[cell.column] = max((dims.get(cell.column, 0), len(cell.value)))
    for col, value in dims.items():
        # python 3.7.2 has some problems with coordinates of excel
        if sys.version[:5] == '3.7.2':
            if col == 1:
                col = 'A'
            elif col == 2:
                col = 'B'
            elif col == 3:
                col = 'C'
            elif col == 4:
                col = 'D'
            elif col == 5:
                col = 'E'
            else:
                print('something wrong')
        sheet.column_dimensions[col].width = float(value)



creating_xls_file()