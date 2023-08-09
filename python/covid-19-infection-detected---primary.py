# BHF CVD COVID UK Consortium, 2023.

import sys, csv, re

codes = [{"code":"1321541000000108","system":"snomedct"},{"code":"1321551000000106","system":"snomedct"},{"code":"1321761000000103","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('covid-19-infection-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["covid-19-infection-detected---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["covid-19-infection-detected---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["covid-19-infection-detected---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)