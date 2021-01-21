# Import Libraries
import pandas as pd
# Import Data
oil_data = pd.read_csv("data/raw/hydro_power_generation_per_person.csv")
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
 "Serbia", "Albania","Bosnia and Herzegovina","Montenegro"]
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
COUNTRIES_ASIA = []
COUNTRIES_AFRICA = []
COUNTRIES_EUROPE = []
COUNTRIES_NA = []
COUNTRIES_SA = []
COUNTRIES_OCEANIA = []

for i in range(len(oil_data)):
    oil_consumption_ASIA = 0
    oil_consumption_AFRICA = 0
    oil_consumption_EUROPE = 0
    oil_consumption_NA = 0
    oil_consumption_SA = 0
    oil_consumption_OCEANIA = 0
    countries_asia = 0
    countries_africa = 0
    countries_europe = 0
    countries_na = 0
    countries_sa = 0
    countries_oceania = 0
    for country in countries:
        if country in Asia:
            oil_consumption_ASIA += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_asia += 1
            else:
                pass
        elif country in Africa:
            oil_consumption_AFRICA += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_africa += 1
            else:
                pass
        elif country in Europe:
            oil_consumption_EUROPE += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_europe += 1
            else:
                pass
        elif country in North_America:
            oil_consumption_NA += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_na += 1
            else:
                pass
        elif country in South_America:
            oil_consumption_SA += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_sa += 1
            else:
                pass
        elif country in Oceania:
            oil_consumption_OCEANIA += oil_data[str(country)][i]
            if oil_data[str(country)][i] != 0:
                countries_oceania += 1
            else:
                pass
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
    COUNTRIES_ASIA.append(countries_asia)
    COUNTRIES_AFRICA.append(countries_africa)
    COUNTRIES_EUROPE.append(countries_europe)
    COUNTRIES_NA.append(countries_na)
    COUNTRIES_SA.append(countries_sa)
    COUNTRIES_OCEANIA.append(countries_oceania)
# Add new columns to the Data
oil_cons_cleaned = oil_data
oil_cons_cleaned["Hydro_Asia_pp"] = oil_consumption_asia
oil_cons_cleaned["Hydro_Africa_pp"] = oil_consumption_africa
oil_cons_cleaned["Hydro_Europe_pp"] = oil_consumption_europe
oil_cons_cleaned["Hydro_NA_pp"] = oil_consumption_north_america
oil_cons_cleaned["Hydro_SA_pp"] = oil_consumption_south_america
oil_cons_cleaned["Hydro_Oceania_pp"] = oil_consumption_oceania
oil_cons_cleaned["People_Asia"] = COUNTRIES_ASIA
oil_cons_cleaned["People_Africa"] = COUNTRIES_AFRICA
oil_cons_cleaned["People_Europe"] = COUNTRIES_EUROPE
oil_cons_cleaned["People_NA"] = COUNTRIES_NA
oil_cons_cleaned["Peolpe_SA"] = COUNTRIES_SA
oil_cons_cleaned["People_Oceania"] = COUNTRIES_OCEANIA

oil_cons_cleaned["avg_ASIA"] = oil_cons_cleaned["Hydro_Asia_pp"]/oil_cons_cleaned["People_Asia"]
oil_cons_cleaned["avg_AFRICA"] = oil_cons_cleaned["Hydro_Africa_pp"]/oil_cons_cleaned["People_Africa"]
oil_cons_cleaned["avg_EUROPE"] = oil_cons_cleaned["Hydro_Europe_pp"]/oil_cons_cleaned["People_Europe"]
oil_cons_cleaned["avg_NA"] = oil_cons_cleaned["Hydro_NA_pp"]/oil_cons_cleaned["People_NA"]
oil_cons_cleaned["avg_SA"] = oil_cons_cleaned["Hydro_SA_pp"]/oil_cons_cleaned["Peolpe_SA"]
oil_cons_cleaned["avg_OCEANIA"] = oil_cons_cleaned["Hydro_Oceania_pp"]/oil_cons_cleaned["People_Oceania"]


# Export new Dataframe
oil_cons_cleaned.to_csv("data/hydro_per_person.csv")