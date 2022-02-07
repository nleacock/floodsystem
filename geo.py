# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from distutils.command import build
from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from .stationdata import build_station_list
from haversine import haversine, Unit
def stations_by_distance(stations, p):
    stations_distance_list = []
    for i in stations:
        distance = haversine(i.coord, p)
        t = (i.name, i.town, distance)
        stations_distance_list.append(t)
    sortedlist = sorted_by_key(stations_distance_list, 2)
    return sortedlist

def stations_within_radius(stations, centre, r):
    """""This function returns a list of all stations within radius r
    of a geographical coordinate x"""
    #create empty list of stations
    within_radius_list = []
    #calculate distance of station from x
    for i in stations:
        dist = haversine(i.coord, centre)
        #if distance to x is less than r, add station name to the list
        if dist <= r:
            within_radius_list.append(i.name)
    
    return within_radius_list
        
rivers = set()
def rivers_with_stations(stations):
    #runs through every river and adds them to a list
    for i in stations:
        rivers.add(i.river)
    return rivers

def stations_by_river(stations):
    dictionary = {}
    #for each river in the list of rivers
    for i in rivers:
        stationsonriver = []
        #test every station for the selected river
        for j in stations:
            #check if selected station is on the river of the selected river - add station to the list if yes
            if j.river == i:
                #adds station to the list of stations that lie on selected river
                stationsonriver.append(j.name)
            else:
                #nothing happens and returns to the loop for the next stations
                arbitrary = 0
        #adds the river and its corresponding stations to the dictionary
        stationsonriver.sort()
        dictionary[i] = stationsonriver
    return dictionary