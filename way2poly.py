#-*- coding: utf-8 -*-
#
# Cree un fichier polygone .poly à partir d'un numéro de way openstreetmap. La première couche de données présente dans Maperitive doit contenir le way référencé.
#
# Code fourni par JB : http://osm.org/user/JBacc1 ou jbxosmx@mailoo.org sans les x.
# Note : ce script python est fait pour être exécuté sous Maperitive et donc avec Ironpython. Certaines bibliothèques ne peuvent pas être chargées, d'où certains détours utilisés.
# Note : script fourni sans garantie, ou plutôt avec la garantie qu'il ne fonctionnera probablement pas !
# Licence : fourni sous licence FTWPL - THE FUCK THE WARRANTY PUBLIC LICENCE (You just DO WHAT THE FUCK YOU WANT TO, There is NO FUCKING WARRANTY.)
#

from maperipy import *
from maperipy.osm import *

way_number=111489599

print("Recherche d'une couche OSM")	
osm = None
layer_index=0
for layer in Map.layers:
	layer_index += 1
	if layer.layer_type == "OsmLayer":
		osm = layer.osm
		break
if osm == None:
    raise AssertionError("There are no OSM map souces.")

print("Recherche du way "+str(way_number))
way=osm.way(way_number)

with open("way_"+str(way_number)+".poly","w") as file:
	file.write("polygon\n1\n")
	for node in way.nodes:
		file.write("\t"+str(osm.node(node).location.x)+"\t"+str(osm.node(node).location.y)+"\n")
	file.write("END\nEND")