# Get Border crossing for Croatia - historical information divided into various categories as excel sheets

Running main.py will transfer data from https://granica.mup.hr/default.inc.aspx?ajaxq=PrometPoDatumu&odDat= to an
excel file for each day from today to days_look_back days ago.

### template_ulazi _izlazi contains sheets for each of the border crossing categories, it needs to be in the same folder as main.py

The other xlsx file beside the template is a mined dataset from the date in the filename - 3500 days ago.

Requered imports:
pip install requests
pip install pandas

### missing_dates.txt contains the list of all dates that are missing from the dataset


### The functions in main.py were almost completly written by github copilot based on the comments.

