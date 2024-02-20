# Open the .csv file and read it
with open('data/raw/worldbank_immunization.csv') as f:
  for line in f:
    print(line)

# Check headers
f = open("data/raw/worldbank_immunization.csv")

headers = f.readline().split(',')
# Here .strip() is unnecesary since the header titles do not have any unneccesary spaces
print(headers)

f.close()

# Check which variable corresponds to which column number
for index, headers in enumerate(headers):
  print(index, headers)
# Country_code variable is at number 3 and Immunization variable is at number 7

# Create an empty list
data = []

# Open the .csv file and iterate though each row in this data file.
# Then, split each line into a list using the split(',') function. Use strip() function to get rif of potenatial unneccesary spaces.
# Then, append this list to the empty data list.
# Thus, the data list now contains all the rows of the .csv file as a list.
with open("data/raw/worldbank_immunization.csv") as f:
  for line in f:
    data.append(list(line.strip().split(',')))

print(data) # This prints the whole .csv file as list.
print(data[0]) # This prints the first row of the .csv file, i.e., the headers.
print(data[1:]) # This prints everything starting from the second row, i.e., eveyrhing except the headers.

# But I do not need all rows for counting the percentage of vaccinated children in each country in 2017. So, I should calculate where the row 2017 starts. To do this, I subtract number of unique country codes (uniqe countries) from overall number of rows.

# Calculating number of overall rows:
number_rows = len(data)
print(f"Overall number of rows: {number_rows}") # 3808 rows

# Calculating number of unique country codes:
unique_country_codes = set()
for row in data:
    country_code = row[3]
    unique_country_codes.add(country_code)

number_unique_country_codes = len(unique_country_codes)

print(f"Number of unique country codes: {number_unique_country_codes}") # 190 unique countries

# Calculating from which row year 2017 starts:
print(3808-190) # Year 2017 starts from row 3618. Given that indexing starts from 0, it is row 3617.

print(data[3617:]) # This prints data only for 2017 for each country.

# Now, I display the percentage of children vaccintaed against measles in each country in 2017.
percentage_vaccinated = {}

for row in data[3617:]:
    countrycode = row[3]
    imm = row[7]
    percentage_vaccinated[countrycode] = imm

print(percentage_vaccinated)