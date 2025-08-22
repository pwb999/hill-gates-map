**ThunderForest - Outdoors Map using Mapbox and PMtile**     

**Layers**    
So far:-     
--Gates      
--Stiles      
--Kissing_Gates   
--Walls     

**Process**     
1. Copy the KMZ from Mac/Organic Maps application.   
In BBEdit extract just the Name, Lon and Lat.    
Add a Line Number   
**Headers** -- ID, Name, Lon, Lat   

2. Convert this csv into a GeoJson file using python script .py   

3. Generate PMtiles using **-- TippeCanoe** to create the **pmtiles**   

4. Update the **index.html** and push this to **S3** to serve up the ThunderForest map and point/polyline data tiles.   

5. ALL these files should be uploaded to my S3 Bucket ensuring public access to these files as its a website.   

----Sunday 17th August 2025 19:21

The final version is now see https://s3.eu-west-2.amazonaws.com/www.libre-maps.com/cumbria/index.html   
Works very well. 

Index25.html is the Vector 2 version which renders its own set of walls in a dashed line format.    
EACH Feature can has its own theme/colour/style so its more versatile than the default Outdoors and Landscaper rasters.    

Slight difference in OSM mode between stiles points and OSM Stiles. Gates seem ok..

It may be possible to make this OFFLINE completely if the tiles were in pmtiles format too.

---Future issues---           
Look at how to ADD a point ie stile/gate etc directly.
How can it be printed easily.    
Scale bar.    
GRID Overlay    
Marginalia

--Thursday 21st August 2025
**Ideas for development**   
Main issue is the cost of tiles from End Provider.    
The only cost free source is OSM where NO API required.     
Or perhaps OS Open Source tiles.    
**Raster vs Vector**   
Clearly vector is better as you can style EACH Feature to your own choice.    

OFFLINE - Can I build an offline map and data tile set in iphone format for FREE ????    
=====================================================================================





