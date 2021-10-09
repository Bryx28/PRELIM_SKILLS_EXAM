import json
import csv
from os import write

#Opening JSON File
json_path = '/home/devasc/Quebral_PrelimSkillsExam/covid_cases.json'
with open(json_path) as file_input:
    COVID_cases = json.loads(file_input.read())

csv_path = '/home/devasc/Quebral_PrelimSkillsExam/COVIDcases_JSON.csv'
with open(csv_path, 'w') as file_output:
    writer = csv.writer(file_output)
    writer.writerow(['Date Reported', 'Countries and Territories', 'Cases', 'Deaths'])

    for record in COVID_cases['records']:
        writer.writerow([record['dateRep'],
                         record['countriesAndTerritories'],
                         record['cases'],
                         record['deaths']])

    