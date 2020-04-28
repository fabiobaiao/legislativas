import requests

parties = set()
resultsByTerritory = {}
subscribedVotersByTerritory = {}

def territory(territoryKey):
    params = {"territoryKey": "LOCAL-{}".format(territoryKey), "electionId": "AR"}
    results = requests.get("https://www.legislativas2019.mai.gov.pt/frontend/data/TerritoryResults", params = params).json()

    currentResults = results["currentResults"]
    subscribedVotersByTerritory[code] = currentResults["subscribedVoters"]
    for resultsParty in currentResults["resultsParty"]:
        party = resultsParty["acronym"]

        parties.add(party)

        territoryResults = resultsByTerritory.setdefault(code, {})
        territoryResults[party] = resultsParty["votes"]


for code in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "30", "40", "50"]:
    territoryKey = "{}0000".format(code)
    territory(territoryKey)

for code in open("concelhos.txt").read().splitlines():
    territoryKey = "{}00".format(code)
    territory(territoryKey)

for code in open("freguesias.txt").read().splitlines():
    territoryKey = "{}".format(code)
    territory(territoryKey)



sortedParties = sorted(parties)
print(",", end = "")
for party in sortedParties:
    print(",{}".format(party), end = "")
print()

for code in resultsByTerritory.keys():
    print("{},{}".format(code, subscribedVotersByTerritory[code]), end = "")
    territoryResults = resultsByTerritory[code]
    for party in sortedParties:
        print(",{}".format(territoryResults.get(party, "")), end = "")
    print()
