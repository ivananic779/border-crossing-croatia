import pandas as pd
import datetime
import json

url = r'https://granica.mup.hr/default.inc.aspx?ajaxq=PrometPoDatumu&odDat='

base = datetime.datetime.today()
days_look_back = 1
date_list = [base - datetime.timedelta(days=x) for x in range(days_look_back)]

for date in date_list:
    tables_ulazi_izlazi = pd.read_html(url + date.strftime('%d.%m.20%y.'))

    print("PUTNICI")
    print(json.dumps(tables_ulazi_izlazi[0].to_dict(orient='records'), indent=4))

    print("ULAZI")
    print(json.dumps(tables_ulazi_izlazi[1].to_dict(orient='records'), indent=4))

    print("IZLAZI")
    print(json.dumps(tables_ulazi_izlazi[2].to_dict(orient='records'), indent=4))

    print("SVEUKUPNO")
    print(json.dumps(tables_ulazi_izlazi[3].to_dict(orient='records'), indent=4))
