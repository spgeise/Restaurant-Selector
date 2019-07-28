from Files import ziplist, latlist, lnglist
import requests, time


class RestaurantList:

    csi_lat = '27.320079'
    csi_lng = '-82.445405'
    api_key = 'key=AIzaSyDn8AOP3ZgLA9WpdoEbg-qqUeWGyQEVaWM'
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    radius = '&rankby=distance'
    type = '&type=restaurant'
    results = []

    def __init__(self, zipcode):
        self.zipcode = str(zipcode)                                 # Convert zip code to string
        self.coordinates()
        self.latlong = self.lat + ',' + self.lng
        self.query = RestaurantList.url + 'location=' + self.latlong + RestaurantList.radius + \
                     RestaurantList.type + '&' + RestaurantList.api_key
        self.next = None
        self.n = None
        self.y = None

    def coordinates(self):
        if self.zipcode == 'csi':                                   # Check if entry is 'csi' and use built in lat/lng
            self.lat = RestaurantList.csi_lat
            self.lng = RestaurantList.csi_lng
            return self.lat, self.lng
        else:                                                       # Get lat/lng for zip code
            index = ziplist.zipcode_list.index(self.zipcode)
            self.lat = str(latlist.lat_list[index])
            self.lng = str(lnglist.lng_list[index])
            return self.lat, self.lng

    def get_request(self, query):
        r = requests.get(query)                                      # Send request
        x = r.json()                                                 # Return json results
        self.y = x['results']
        time.sleep(1.25)
        try:                                                         # Check for Next Page Token and return it
            self.n = x['next_page_token']
            return self.n, self.y
        except KeyError:
            return self.y

    def next_page(self, n):
        self.next = RestaurantList.url + RestaurantList.api_key + '&pagetoken=' + n
        return self.next

    def build_list(self, y):
        for i in range(len(y)):                                       # Add items to results list
            item = str(y[i]['name'])
            RestaurantList.results.append(' '.join(item.split()[:5]))
