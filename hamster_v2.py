# wherever k multiply by 1000
import math
from itemList import MarketsList, PRandTeamList, LegalList, SpecialList


def convert_k_values(item):
    if isinstance(item['extraProfitPerHour'], str) and 'k' in item['extraProfitPerHour']:
        item['extraProfitPerHour'] = float(item['extraProfitPerHour'].replace('k', '')) * 1000
    if isinstance(item['costToUpgrade'], str) and 'k' in item['costToUpgrade']:
        item['costToUpgrade'] = float(item['costToUpgrade'].replace('k', '')) * 1000
    return item
MarketsList = [convert_k_values(item) for item in MarketsList]
PRandTeamList = [convert_k_values(item) for item in PRandTeamList]
LegalList = [convert_k_values(item) for item in LegalList]
SpecialList = [convert_k_values(item) for item in SpecialList]



CombinedList = MarketsList + PRandTeamList + LegalList + SpecialList

for item in CombinedList :
    if item['extraProfitPerHour'] != None :
        worth = item['extraProfitPerHour']/item['costToUpgrade']
        hours = 1 / worth
        days = hours / 24
    else :
        hours = math.inf
    days = hours / 24
    item['hours']=hours
    item['days']=round(days,2)

# CombinedList.sort(key=lambda x: x['extraProfitPerHour'])
CombinedList.sort(key=lambda x: x['hours'])

# for item in CombinedList[-10:]:
for item in CombinedList[:5]:
    print(item)
