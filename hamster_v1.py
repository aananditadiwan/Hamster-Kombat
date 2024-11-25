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


def calculate_worth(item, k=0.5):
  if item['extraProfitPerHour'] is not None and item['extraProfitPerHour'] > 0:
    cost_efficiency = item['costToUpgrade'] / item['extraProfitPerHour']
    profit_increase = item['extraProfitPerHour']
    worth = (cost_efficiency * k) + ((1 - k) * profit_increase)
    return worth
  else:
    return math.inf

CombinedList = MarketsList + PRandTeamList + LegalList + SpecialList

def calculate_metric(item, weight_profit_increase=0.5):
  worth = item['extraProfitPerHour'] / item['costToUpgrade']
  payback_time = 1 / worth  # Inverse of worth
  metric = (weight_profit_increase * item['extraProfitPerHour']) - ((1 - weight_profit_increase) * payback_time)
  item['metric'] = metric
  return item

# Apply the metric calculation
weight_profit_increase = 0.5  # Adjust this value to balance between cost and profit increase
CombinedList = [calculate_metric(item, weight_profit_increase) for item in CombinedList]

# Sort based on the calculated metric
CombinedList.sort(key=lambda x: x['metric'], reverse=True)

# Print the top 5 cards
for item in CombinedList[:5]:
    print(f"Name: {item['name']}, Cost to Upgrade: {item['costToUpgrade']}, Extra Profit Per Hour: {item['extraProfitPerHour']}, Metric: {item['metric']:.2f}")

