data = pd.read_csv("election_area_data/Befolkning.csv", sep=";")

data.replace("-", 0, inplace=True)

origins = [
    "Danmark",
    "Nordiske lande",
    "Tyrkiet",
    "Tidligere Jugoslavien",
    "Gamle EU-lande",
    "Nye EU-lande",
    "Øvrige Europa",
    "Afrika",
    "Nordamerika",
    "Syd- og Mellemamerika",
    "Asien og Oceanien",
    "Uoplyst",
]

cols = data.columns.to_list()
for o in origins:

    sel_cols = [c for c in cols if c.endswith(o)]

    for s in sel_cols:
        data[s] = data[s].astype(str)
        data[s] = data[s].apply(lambda x: x.replace(",", "."))
        data[s] = data[s].astype(float)

    data[o] = data[sel_cols].sum(axis=1)

data["total_population"] = data[origins].sum(axis=1)


income_cols = [
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Under 100.000 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Under 100.000 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_100.000 - 149.999 kr",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_150.000 - 199.999 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_200.000 - 299.999 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_300.000 - 399.999 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_400.000 - 499.999 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_500.000 - 749.999 kr.",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_750.000 kr.-",
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt",
]

for i in income_cols:

    data[i] = data[i].astype(str)
    data[i] = data[i].apply(lambda x: x.replace(",", "."))

    data[i] = data[i].astype(float)

data["households_share_income_under100k"] = (
    data["FV2022 - Husstandsindkomster fordelt på afstemningsområder_Under 100.000 kr."]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_100-149.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_100.000 - 149.999 kr"
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_150-199.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_150.000 - 199.999 kr."
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_200-299.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_200.000 - 299.999 kr."
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_300-399.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_300.000 - 399.999 kr."
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_400-499.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_400.000 - 499.999 kr."
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_500-749.9k"] = (
    data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_500.000 - 749.999 kr."
    ]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)
data["households_share_income_750-k"] = (
    data["FV2022 - Husstandsindkomster fordelt på afstemningsområder_750.000 kr.-"]
    / data[
        "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
    ]
)


data["total_households"] = data[
    "FV2022 - Husstandsindkomster fordelt på afstemningsområder_Antal husstande i alt"
]


car_cols = ['FV2022 - Husstandes bilrådighed fordelt på afstemningsområder_Husstande med 1 bil',
 'FV2022 - Husstandes bilrådighed fordelt på afstemningsområder_Husstande med 2 eller flere biler',
 'FV2022 - Husstandes bilrådighed fordelt på afstemningsområder_Husstande uden bil']

for c in car_cols:
    data[c] = data[c].astype(str)
    data[c] = data[c].apply(lambda x: x.replace(',','.'))

    data[c] = data[c].astype(float)


new_car_cols = ['share_households_1car','share_households_2pluscar','share_households_nocar']

for c,n in zip(car_cols,new_car_cols):
    data[n] = data[c]/data['total_households']


cols = ['Gruppe',
 'ValgstedId',
 'KredsNr',
 'StorKredsNr',
 'LandsdelsNr',
 'total_population',
 'Danmark',
 'Nordiske lande',
 'Tyrkiet',
 'Tidligere Jugoslavien',
 'Gamle EU-lande',
 'Nye EU-lande',
 'Øvrige Europa',
 'Afrika',
 'Nordamerika',
 'Syd- og Mellemamerika',
 'Asien og Oceanien',
 'Uoplyst',
 'households_share_income_under100k',
 'households_share_income_100-149.9k',
 'households_share_income_150-199.9k',
 'households_share_income_200-299.9k',
 'households_share_income_300-399.9k',
 'households_share_income_400-499.9k',
 'households_share_income_500-749.9k',
 'households_share_income_750-k',
 'total_households',
 'share_households_1car',
 'share_households_2pluscar',
 'share_households_nocar'
 ]

data = data[cols]

data.to_csv('data/socio_economic_data.csv',index=False)


dict = {101: "København",
147: "Frederiksberg",
155: "Dragør",
185: "Tårnby",
165: "Albertslund",
151: "Ballerup",
153: "Brøndby",
157:" Gentofte",
159: "Gladsaxe",
161: "Glostrup",
163: "Herlev",
167: "Hvidovre",
169: "Høje-Taastrup",
183: "Ishøj",
173: "Lyngby-Taarbæk",
175: "Rødovre",
187: "Vallensbæk",
201: "Allerød",
240: "Egedal",
210: "Fredensborg",
250: "Frederikssund",
190: "Furesø",
270: "Gribskov",
260: "Halsnæs",
217: "Helsingør",
219: "Hillerød",
223: "Hørsholm",
230: "Rudersdal"}

dict.keys()