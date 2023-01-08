import json
import webbrowser
import requests

from netlib import *


if __name__ == '__main__':

    linenr = ask_for_line()
    # print complete API request
    print(getapiurl(str(linenr)))
    # loads API response to "response" object
    response = requests.get(getapiurl(str(linenr)))
    # loads JSON {result:lista} to "lista" object
    lista = dict(response.json()).values()
    # iterate through "lista" (one item: list))
    for i in lista:
        # iterates list items which are dictionaries for specific buses
        for bus in i:
            # opens a map with bus pinned for each bus on the route
            webbrowser.open(pintomap(16, str(bus['Lat']), str(bus['Lon'])))

