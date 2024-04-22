import csv

officer_forms = './csv/OfficerOnboarding.csv'

print('>>>>>>>>>>>>>>>>>>>>> OFFICER FORMS <<<<<<<<<<<<<<<<<<<<<<<<')

with open(officer_forms, newline='') as csvfile:
    officer_reader = csv.reader(csvfile, dialect='excel')

    next(officer_reader)
    next(officer_reader)
    headers = next(officer_reader)
    status_index = headers.index('Status')


    for row in officer_reader:
        if row[status_index] == 'Pending':
            if row[15].strip() == '' and row[17].strip() == '':
                print('[DENY]',row[2], row[22], row[21], 'Neither incoming SEO and Finance Officer were selected')
            elif row[15].strip() != '' and row[17].strip() != '':
                if row[22] == row[21]:
                    print('[DENY]',row[2], row[22], row[21], 'Both incoming SEO and Finance Officer were selected for the same RSO')
                else:
                    print('[MULTIPLE ORGS]', row[2], 'SEO for :' + row[22], 'FO for :' + row[21], row[15], row[17])
            elif row[40].lower() != 'yes' or row[40].lower() == row[32].lower():
                print('[DENY]','Did not agree with statment.', row[2], row[22], row[21], row[15], row[17])
            else:
                print(row[2], row[22], row[21], row[15], row[17])
            print('-------------------------------')
            

# TODO Group same orgs together in output
# TODO Clean up output for better viewing
# TODO Error handling when no file exist