import csv

advisor_form = './csv/AdvisorForm.csv'
elibility_sheet = './csv/AdvisorEligibility.csv'

print('>>>>>>>>>>>>>>>>>>>>> ADVISOR FORMS <<<<<<<<<<<<<<<<<<<<<<<<')


eligibile_advisors_username = set()
with open(elibility_sheet, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        eligibile_advisors_username.add(row[0])

eligibile_advisors_email = set()
with open(elibility_sheet, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for row in reader:
        eligibile_advisors_email.add(row[3])

# TODO ^ Check if this worked


with open(advisor_form, newline='', encoding='utf-8') as csvfile:
    advisor_reader = csv.reader(csvfile, dialect='excel')

    next(advisor_reader)
    next(advisor_reader)
    headers = next(advisor_reader)
    status_index = headers.index('Status')

    for row in advisor_reader:
        if row[status_index] == 'Pending':
            if row[2] in eligibile_advisors_username or row[3] in eligibile_advisors_username:
                print(row[2], row[3], row[4])
            else:
                print('[CHECK]', row[2], row[3], row[4])
            print('-------------------------------')
            


# TODO Group same orgs together in output
# TODO Clean up output for better viewing
