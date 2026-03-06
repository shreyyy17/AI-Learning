from InteractingWithApis.libs.openexchange import OpenExchange

APP_ID = "142cf2dc6da84fc4b01460160da933bb"

usd_amount = 1
client = OpenExchange(APP_ID)

gbp_amount = client.convert(usd_amount,"USD","INR")

print(f"USD {usd_amount} is GBP {gbp_amount}")

# exchange_rates = response.json()['rates']
#
#
# usd_amount = 1000
# gbp_amount = usd_amount * exchange_rates['GBP']
#
# print(f"USD {usd_amount} is GBP {gbp_amount}")

