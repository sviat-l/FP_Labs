"""
Lab 1.2 Create Map with film locations
"""

import argparse
import math
import re
from functools import lru_cache
from random import uniform, choice
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


parser = argparse.ArgumentParser()
parser.add_argument("latitute", type=float)
parser.add_argument("longitude", type=float)
parser.add_argument("year", type=int)
parser.add_argument("path", type=str)
ARGS = parser.parse_args()

# ARGS = (50, 50, 2014,'data/short_locations.list')
COLORS = ('red', 'blue', 'green', 'purple', 'orange', 'darkred',
          'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple',
          'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray')
MAP_PATH = 'examples/Film_map.html'



def create_dataset(path: str) -> pd.DataFrame:
    """
    Create pandas dataframe with film information:
        Name('name')        Year('year')        Location('location')
      "LawstinWoods"              '2013'	    "Erin, New York, USA"
    """
    df = pd.DataFrame(columns=["name", "year", "location"])

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                # get and procced film name
                name = re.search(r'^.*? \(', line).group()[:-2]
                name = name.replace('"', '').strip()
                # get and procced year
                year = re.search(r'\(\d{4}\)', line).group()
                year = year[1:-1]
                # get and procces location info
                location = line.split('\t')
                if location[-1].startswith('('):
                    location.pop()
                location = location[-1].strip()
            except AttributeError:
                continue
            row = pd.DataFrame({"name": [name], "year": [year], "location": [location]})
            df =  pd.concat([df, row], ignore_index = True)
    return df


def haversine(point1:tuple[float], point2: tuple[float]) -> float:
    """
    Calculate and return the haversin in radians
    from stated spherical coordinatess
    """
    if point1 is None or point2 is None:
        return math.inf
    lon1, lat1 = map(math.radians, point1)
    lon2, lat2 = map(math.radians, point2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    tmp = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    return 2 * math.asin(math.sqrt(tmp))


@lru_cache(100000)
def coordinates(place_all: str) -> tuple[float]:
    """
    Return coordinates (latitude, longitude) of the location
    """
    place_all = place_all.split(',')
    for place in place_all:
        try:
            geolocator = Nominatim(user_agent="Film location")
            # to handle time limits
            geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
            # get geolocation information
            location = geocode(place.strip())
            return location.latitude, location.longitude
        except AttributeError:
            continue
    return None, None


def get_clothest(df: pd.DataFrame, lon: float, lat: float, year:int) -> dict:
    """
    Find and return dict ('name':(lon, lat)} with 10
    clothest film locations from pandas database to stated point
    """
    year_df = df.loc[df["year"] == str(year)]
    # dm it. lets simply sort
    year_df['coords'] = year_df.apply(lambda row: coordinates(row['location']), axis=1)
    year_df['distance'] = year_df.apply(lambda row: haversine((lon, lat),
                        coordinates(row['location'])), axis=1)
    year_df.sort_values(by=['distance'], inplace=True)
    result = []
    for _, row in year_df.iterrows():
        result.append( (row['name'], row['coords']))
        if len(result) == 10:
            break
    return result


def create_map(latitute:float, longitude:float, year:int, path:str):
    """
    Create map of 10 closest location to stated one, for stated year
    """
    mapa = folium.Map(control_scale=True, location=[
                      longitude, latitute], zoom_start=3)

    folium.CircleMarker(location=[longitude, latitute],
                                                radius=4).add_to(mapa)

    films_dataframe = create_dataset(path)
    clothest_dct = get_clothest(films_dataframe,
                                longitude, latitute, year)

    locations = folium.FeatureGroup(name=f"Movie Locations for {year}")

    for film_name, (lat, lot) in clothest_dct:
        locations.add_child(folium.Marker(location=
                [lat + uniform(-0.001, 0.001), lot + uniform(-0.001, 0.001)],
                tooltip=film_name, icon=folium.Icon(choice(COLORS),
                            icon_color=choice(COLORS), icon='cloud')))

    mapa.add_child(locations)
    folium.TileLayer('cartodbdark_matter').add_to(mapa)
    folium.TileLayer('Stamen Terrain').add_to(mapa)
    mapa.add_child(folium.LayerControl())
    mapa.save(MAP_PATH)

if __name__ == '__main__':
    create_map(ARGS.latitute, ARGS.longitude, ARGS.year, ARGS.path)
