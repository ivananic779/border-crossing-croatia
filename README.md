# Script to get tourist and domestic ins and outs from the country of Croatia

## Requirements:
'''
pip install pandas
pip install requests
'''
The script (main.py) also requires the file excel_template to be in the same directory as main.py

excel_template is a template for column names which I was lazy to do by hand so I wrote a terrible script which got the job done poorly, if you make it better please submit a pull request.

Variable "days_look_back" in main.py tells the script how many days into the past from today you want to look.
For example, setting it to 500 would transfer the last 500 days into a new excel file

ulazi_izlazi is an actual example of 02.09.2021 - 500 days back
