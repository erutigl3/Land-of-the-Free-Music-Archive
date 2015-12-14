# Land-of-the-Free-Music-Archive
A network graph of the Free Music Archive by Eugene Rutigliano
This is a repository of scripts and data used to make a Gephi network graph of artists on the Free Music Archive (http://www.freemusicarchive.com).  The network is based on related artist assignments produced by EchoNest acoustical analysis.  The data in the csv files was retrieved in mid November 2015.  FMA adds artists regularly, so the network graph is likely to change over time.
Scripts run in this order
1. req_FMA_artistid.py - query FMA API for artist ids >  generates fma_ids.json 
2. req_EchoNest_artistrel.py - requires fma_ids.json > query EchoNest API with FMA ids > get normalized artist name data > query EchoNest API for related info > generates echo_related_network.csv (warning: >16,000 requests; may require about 4 hours and additional permissions from EchoNest API)
3. req_FMA_artistnodes.py - FMA API query for id, name, favorites > generates fma_nodes_network_fav.csv
Importing csv to Gephi may require some additional memory allocation.  Any suggestions about to make all of these connections legible in a network graph are appreciated!

