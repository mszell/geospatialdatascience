README file for Snow GIS data
-----------------------------

This zip file contains a number of GIS layers relating to John Snow's 1854 investigation of a
Cholera outbreak in London - considered by many to be the first use of geographical analysis
in an epidemiological study. More details on the history are available at
http://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak

This file contains a number of GIS layers created from Snow's original map which allow analyses to be
conducted on the data in modern GIS systems. For example, clustering of cases can be analysed and the
effect of spatial aggregation in modern anonymised health data releases. Of course, it's also just
interesting to look at the area, and how little it has changed since 1854.

Files included:
(Many of the items in the list consist of many actual files (for example .shp, .dbf etc)

* OSMap				Raster		Modern OS map of the area of the outbreak
* OSMap_Greyscale	Raster		Same as above, but in greyscale for easier visualisation
* SnowMap			Raster		Snow's original map, georeferenced and warped so that it accurately overlays the OS map
* CholeraDeaths		Vector		Points for each location of one or more deaths. Attribute value gives number of deaths at that location
* Pumps				Vector		Points for each location of a pump

Created and compiled by Robin Wilson (robin@rtwilson.com, www.rtwilson.com/academic) - Jan 2011.