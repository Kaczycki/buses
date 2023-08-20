from main import getapiurl

def test_api():
    assert getapiurl(str(150)) == \
         'https://api.um.warszawa.pl/api/action/busestrams_get/?' \
         'resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&' \
         'apikey=8f6792f1-0ad3-4159-ab79-bd3ceaae46f7&' \
         'type=1&' \
         'line=150'


