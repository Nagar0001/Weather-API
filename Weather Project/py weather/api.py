import requests
import json 

url= "http://api.weatherapi.com/v1/current.json?key=feff49cb9758454bb9962819231409&q="+input("Enter Your City Name:-")

df= requests.get(url)

data=json.loads(df.content)
print(f"Temperature of {data ['location']['name']} is {data['current']['temp_c']}")

