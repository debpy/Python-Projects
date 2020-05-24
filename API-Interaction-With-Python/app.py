from libs.openexchange import OpenExchangeClient
import time

#Implementing a currency exchange library using Python
'''
import requests
ENDPOINT="https://openexchangerates.org/api/latest.json"
'''
APP_ID="**********************"
client = OpenExchangeClient(APP_ID)
usd_amount=1000

start_time=time.time()
inr_amount=client.convert(usd_amount, "USD", "INR")
print(f"First call takes {time.time()-start_time:.2f} seconds to complete")

start_time=time.time()
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
inr_amount=client.convert(usd_amount, "USD", "INR")
print(f"After 10 calls took {time.time()-start_time} seconds to complete")

print(f"USD {usd_amount:.2f} is INR {inr_amount:.2f}")

gbp_amount=1000
inr_amount=client.convert(usd_amount, "GBP", "INR")
print(f"GBP {usd_amount:.2f} is INR {inr_amount:.2f}")

#response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
#usd_amount=1
#inr_amount=usd_amount * response.json()['rates']['INR']

