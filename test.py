
result = {'items':
              [
                  {'title': 'Việt Nam', 'id': 'here:cm:namedplace:23824718', 'resultType': 'administrativeArea', 'administrativeAreaType': 'country',
                   'address': {'label': 'Việt Nam', 'countryCode': 'VNM', 'countryName': 'Việt Nam'},
                   'position': {'lat': 21.02888, 'lng': 105.85464}, 'mapView': {'west': 102.14459, 'south': 8.38129, 'east': 109.4693, 'north': 23.39274}, 'scoring': {'queryScore': 1.0, 'fieldScore': {'country': 1.0}}}]}


if __name__ == '__main__':
   print(result['items'][0]['position']['lat'])