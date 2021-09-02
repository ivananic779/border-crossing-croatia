import pandas as pd
from openpyxl import workbook
from openpyxl import load_workbook
import datetime
import time
import json

url = r'https://granica.mup.hr/default.inc.aspx?ajaxq=PrometPoDatumu&odDat='

wb = load_workbook('template_ulazi_izlazi.xlsx')
sheet = wb.active

excel_row_number = 2
excel_column_number = 1

def data_to_excel(_data, _date):
    global excel_column_number
    global excel_row_number

    for key, value in _data.items():
        if excel_column_number == 1:
            sheet.cell(row=excel_row_number,column=excel_column_number).value = _date
            excel_column_number += 1
        elif (key != '0'):
            sheet.cell(row=excel_row_number,column=excel_column_number).value = value
            excel_column_number += 1

if __name__ == '__main__':
    base = datetime.datetime.today()
    days_look_back = 500
    date_list = [base - datetime.timedelta(days=x) for x in range(days_look_back)]

    i = 0

    for date in date_list:

        # Sometimes the request fails, so we need to retry it
        try:
            tables_ulazi_izlazi = pd.read_html(url + date.strftime('%d.%m.20%y.'))
        except:
            tables_ulazi_izlazi = pd.read_html(url + date.strftime('%d.%m.20%y.'))
            continue

        i += 1
        print('ulazi i izlazi procitani ' + str(i))

        json_putnici = json.loads(json.dumps(tables_ulazi_izlazi[0].to_dict(orient='records'), indent=4))
        
        for row in json_putnici[3:9]:
            data_to_excel(row, date.strftime('%d.%m.20%y.'))

        for row in json_putnici[12:]:
            data_to_excel(row, date.strftime('%d.%m.20%y.'))

        # reset for each new date
        excel_row_number += 1
        excel_column_number = 1

        # print(json_putnici[1]['1'])

        # df_json = pd.read_json(json_putnici)
        # df_json.to_excel('file.xlsx')

    wb.save('ulazi_izlazi.xlsx')
