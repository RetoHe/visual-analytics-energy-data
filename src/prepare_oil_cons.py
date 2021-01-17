# Import Libraries
import pandas as pd
# Import Data
oil_data = pd.read_csv("../data/raw/oil_consumption_total.csv")
# Transpose Data
oil_data = oil_data.transpose()
# Fill NA's
oil_data = oil_data.fillna(0)
# Rename first row
oil_data = oil_data.rename(columns=oil_data.iloc[0])
# Rename columns to countries
oil_cols = oil_data.columns[oil_data.dtypes.eq(object)]
oil_data[oil_cols] = oil_data[oil_cols].apply(pd.to_numeric, errors='coerce')
oil_data = oil_data.drop("country")

# Create Continental Lists
Asia = ["Azerbaijan", "Bangladesh", "China",'India',
 'Indonesia','Iran','Iraq','Israel','Japan',
 'Kazakhstan','Kuwait','Malaysia','Oman',
 'Pakistan','Philippines','Qatar','Saudi Arabia',
 'Singapore','South Korea',"Sri Lanka", "Thailand", "Vietnam",
 'Turkmenistan',"Uzbekistan",'United Arab Emirates',"Tunisia",
 "Tajikistan","North Korea","Nepal","Myanmar","Brunei", "Cambodia", "Jordan",
 "Mongolia","Kyrgyz Republic","Bahrain"]
Africa = ["Algeria","Angola","Egypt","Morocco",'South Africa',
"Zimbabwe", "Yemen", "Zambia", "Togo", "Tanzania", "Syria",
"Sudan","Senegal","Nigeria","Namibia",'Mozambique',
'Lebanon',"Libya","Kenya","Ghana",'Eritrea','Congo, Dem. Rep.',
 'Congo, Rep.',"Cote d'Ivoire","Cameroon","Benin", "Botswana","Ethiopia",
 "Gabon"]
Europe = ["Austria",'Belarus','Belgium', "Bulgaria", 'Croatia',
 'Cyprus','Czech Republic','Denmark','Estonia','Finland',
 'France','Germany','Greece','Hungary','Iceland',"Ireland",
 'Italy','Latvia','Lithuania','Luxembourg',"Netherlands",
 'North Macedonia','Norway', 'Poland',"Georgia",
 'Portugal','Romania','Russia','Slovak Republic',
 'Slovenia',"Sweden", "Spain", "Switzerland", "Ukraine",
 "United Kingdom", "Turkey",'Moldova',"Armenia","Malta",
 "Serbia", "Albania","Bosnia and Herzegovina"]
North_America = ["Canada", "Mexico","United States"]
South_America = ["Argentina", "Brazil", "Chile", "Colombia", "Ecuador",
"Peru",'Trinidad and Tobago',"Venezuela","Uruguay",'Panama',
 'Paraguay','Nicaragua','Guatemala','Haiti','Honduras','Costa Rica',
 "Jamaica", "Bolivia", "Cuba", "El Salvador","Dominican Republic"]
Oceania = ["Australia", "New Zealand"]

# Get Countries of the File
countries = []
for col in oil_data.columns:
    countries.append(col)

# Get the sum per continent and year
oil_consumption_asia = []
oil_consumption_africa = []
oil_consumption_europe = []
oil_consumption_north_america = []
oil_consumption_south_america =[]
oil_consumption_oceania = []
oil_consumption_years = []
for i in range(len(oil_data)):
    oil_consumption_ASIA = 0
    oil_consumption_AFRICA = 0
    oil_consumption_EUROPE = 0
    oil_consumption_NA = 0
    oil_consumption_SA = 0
    oil_consumption_OCEANIA = 0
    for country in countries:
        if country in Asia:
            oil_consumption_ASIA += oil_data[str(country)][i]
        elif country in Africa:
            oil_consumption_AFRICA += oil_data[str(country)][i]
        elif country in Europe:
            oil_consumption_EUROPE += oil_data[str(country)][i]
        elif country in North_America:
            oil_consumption_NA += oil_data[str(country)][i]
        elif country in South_America:
            oil_consumption_SA += oil_data[str(country)][i]
        elif country in Oceania:
            oil_consumption_OCEANIA += oil_data[str(country)][i]
        else:
            print("F*** country is missing!!!")
            print(country)
    oil_consumption_asia.append(oil_consumption_ASIA)
    oil_consumption_africa.append(oil_consumption_AFRICA)
    oil_consumption_europe.append(oil_consumption_EUROPE)
    oil_consumption_north_america.append(oil_consumption_NA)
    oil_consumption_south_america.append(oil_consumption_SA)
    oil_consumption_oceania.append(oil_consumption_OCEANIA)
    oil_consumption_years.append(oil_data.index[i])

# Add new columns to the Data
oil_cons_cleaned = oil_data
oil_cons_cleaned["Oil_Cons_Asia"] = oil_consumption_asia
oil_cons_cleaned["Oil_Cons_Africa"] = oil_consumption_africa
oil_cons_cleaned["Oil_Cons_Europe"] = oil_consumption_europe
oil_cons_cleaned["Oil_Cons_NA"] = oil_consumption_north_america
oil_cons_cleaned["Oil_Cons_SA"] = oil_consumption_south_america
oil_cons_cleaned["Oil_Cons_Oceania"] = oil_consumption_oceania

# Export new Dataframe
oil_cons_cleaned.to_csv("../data/oil_cons.csv")