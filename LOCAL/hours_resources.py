import numpy as np
import re
import datetime

def get_hours(timerange_str):
    def minutes_to_frac(minutes):
        return minutes/60

    def get_time(time_str):
        hrs, mins = time_str.split(":")
        mins = minutes_to_frac(int(mins))
        return int(hrs) + mins

    try:
        time0, time1 = timerange_str.split('-')
        time0 = get_time(time0)
        time1 = get_time(time1)
        return time1 - time0
    except:
        print("there was an error in calculating: {}".format(timerange_str))
        return np.nan

def check_date(date_str, date_range):
    date = convert_date(date_str)
    min_date = convert_date(date_range[0])
    max_date = convert_date(date_range[1])

    if date >= min_date and date <= max_date:
        return True
    else:
        return False

def convert_date(date_str):
    day, month, year = [int(i) for i in date_str.split(".")]
    date = datetime.datetime(year, month, day, 0, 0, 0)
    return date

def find_totals(sheet_array, date_range):
    """Finds total hours worked from rota sheet array (2d array) in the given date range (1x2 array, e.g.: ["1.4.2021, "1.6.2021"]
    """
    lines = sheet_array
    days_in_range = convert_date(date_range[1]) - convert_date(date_range[0])
    days_in_range = days_in_range.days

    doch_dct_main = {}
    people = ["Adam", "Monika", "Paula", "Viki"]
    totals = {"Meno":[],
            "Hodiny_total": [],
            "Hodiny_prac. tyzden":[],
            "Hodiny_Sobota":[],
            "Hodiny_Nedela":[],
            "Hodiny_tyzdenny priemer":[]}

    for person in people:
        doch_dct_sub = {"date":[], "day":[], "name":[], "tot_hrs":[], "wk_hrs":[], "sat_hrs":[], "sun_hrs":[], "euros":[]}
        for line in lines:
            if line[3] == person:
                date, day, name, hours = line[0], line[2], line[3], get_hours(line[4])
                if check_date(date, date_range):
                    doch_dct_sub["date"].append(date)
                    doch_dct_sub["day"].append(day)
                    doch_dct_sub["name"].append(name)
                    if re.match(day[:2], "So"):
                        doch_dct_sub["sat_hrs"].append(hours)
                        doch_dct_sub["euros"].append(hours * 6)
                    elif re.match(day[:2], "Ne"):
                        doch_dct_sub["sun_hrs"].append(hours)
                        doch_dct_sub["euros"].append(hours * 8)
                    else:
                        doch_dct_sub["wk_hrs"].append(hours)
                        doch_dct_sub["euros"].append(hours * 4)
                    doch_dct_sub["tot_hrs"].append(hours)
                else:
                    pass
        doch_dct_main[person] = doch_dct_sub

        totals["Meno"].append(person)
        totals["Hodiny_total"].append(np.sum(doch_dct_main[person]["tot_hrs"]))
        totals["Hodiny_prac. tyzden"].append(np.sum(doch_dct_main[person]["wk_hrs"]))
        totals["Hodiny_Sobota"].append(np.sum(doch_dct_main[person]["sat_hrs"]))
        totals["Hodiny_Nedela"].append(np.sum(doch_dct_main[person]["sun_hrs"]))
        #totals["tot_euros"].append(np.sum(doch_dct_main[person]["euros"]))
        totals["Hodiny_tyzdenny priemer"].append(np.sum(doch_dct_main[person]["tot_hrs"]) / days_in_range * 7)

    formatted_totals = []
    formatted_totals.append(["Datum {}-{}".format(*date_range)])
    for key in totals:
        formatted_line = []
        formatted_line.append(key)
        [formatted_line.append(item) for item in totals[key]]
        formatted_totals.append(formatted_line)
    return totals, formatted_totals
