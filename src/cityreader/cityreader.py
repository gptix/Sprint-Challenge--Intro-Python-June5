# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
import os

datafile_name = 'cities.csv'
dir_path = os.path.dirname(os.path.realpath(__file__))
path_name = dir_path + '/' + datafile_name

class City():
    def __init__(self, name, lat, lon):
        """Store the name, latitude, and longitude
        for a city.
        Input is received as three strings.  The 
        lat and log values are converted to floats."""
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)
        
    def __str__(self):
        """Print out strings in (City): (lat, long) format."""
        return f'{self.name}: ({self.lat}, {self.lon})'

def get_required_data(row):
    """Index 0: city name
    Index 3: latitude
    Index 4: longitude"""
    return [row[0]]+row[3:5]
    
def cityreader(cities=[]):
    """Read a CSV file, and create, collect, and return 
    a list of 'City' objects."""
    # Open the file, expected to be in the same directory.
    with open(path_name) as f:
        # Instantiate a reader object
        rowreader = csv.reader(f)
        # iterate past the header row, which is not ueful.
        rowreader.__next__()
        # Iterate over remaining rows, 
        for row in rowreader:
            # creating a City object for each, and collecting
            # in the list 'cities'
            cities.append(City(*(get_required_data(row))))
    # 'with' structure automatically closes file.        
    return cities


def __main__():
    cities = cityreader()
    for c in cities:
        print(c)
    
    
    
    

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.    
    
# 

# # In[9]:


# # get west longitude (more negative)
# # get east longitude (less negative)
# # get north latitide (bigger)
# # get south latitude (smaller)

# def in_box(lat1, lon1, lat2, lon2, city):
#     """Report whether a city's lat/lon is within a box 
#     defined by north and south latitudes, and east and west
#     longitude."""
#     lat = city.lat
#     lon = city.lon
    
# #     return (lat, lon)
# #     return type(lat)
#     return (n > lat > s)
# #             and (w > lon > e))

# # test
# my_city = cities[0]
# my_lat_lon = (my_city.lat, my_city.lon)
# my_lat_lon

# in_box(90, -130, my_city)


# # In[7]:


