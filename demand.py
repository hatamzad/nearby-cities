import requests
import json
import uszipcode

miles = input('Enter Miles: ')
city = input('Enter City: ').capitalize()
state = input('Enter State: ').upper()
country = input('Country: ').title()

api_call = 'http://getnearbycities.geobytes.com/GetNearbyCities?callback=?&radius=' + miles + '&locationcode=' + city + ', ' + state + ', ' +country 
response = requests.get(api_call)

def drawNbcTable(response):
    print ('Miles | City | State | Country')

    response = response.replace('?(', '').replace(');', '')
    response = json.loads(response)
    for i in range(0, len(response)):
        # zipcodes = mylib.getZipcodeFOrCity(response[i][1])
        print ( response[i][11] + ' | ' + response[i][1] + ' | ' + response[i][2] + ' | ' + response[i][3] + ' | ' + response[i][8] + ' | ' + response[i][10])
        # for zipcode in zipcodes:
        #     print (zipcode)
    
print (drawNbcTable(response.text))
