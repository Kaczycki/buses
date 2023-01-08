from personal import apikey


def pintomap(zoom, lat, lon):
    """
    returns URL for opening map in OpenStreetMap.org
    example:
    # https://www.openstreetmap.org/?mlat=52.29074&mlon=20.92817#map=19/52.29074/20.92817
    # https://www.openstreetmap.org/#map=19/52.30064/20.93822
    :rtype: string
    """

    address = str('https://www.openstreetmap.org/?' +
                  'mlat=' + lat +
                  '&mlon=' + lon +
                  '#map=' + str(zoom) +
                  '/' + lat +
                  '/' + lon)
    return address


def getapiurl(linenr):
    """
    Formatting API request for Latitude and Longitude for given bus line
    API request to use on 'um.Warszawa'
    :rtype: string
    """
    apiurl = str('https://api.um.warszawa.pl/api/action/busestrams_get/?' +
                 'resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&' +
                 'apikey=' + apikey +
                 '&type=' + '1' +
                 '&line=' + linenr)
    return apiurl


def ask_for_line():
    """
    input the line number for request
    :return: int
    """
    linenr = input('Podaj numer linii autobusowej i naciśnij ENTER')
    return linenr
