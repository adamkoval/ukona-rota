from api_resources import sheets_api
from hours_resources import find_totals
import argparse

date_range = input("Prosim zadajte datumy (napr. 1.4.2021-1.5.2021): ").split('-')
cred_json = "credentials_service.json"
spreadsheet_id = open("sheet_id.txt", 'r').readlines()[0][:-1]
read_tab_name = "rota"
write_tab_name = "hours"

api = sheets_api(cred_json, spreadsheet_id)
values = api.read(read_tab_name)

totals, formatted_totals = find_totals(values, date_range)

api.write("hours", formatted_totals)
