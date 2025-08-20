**ThunderForest - Outdoors Map using Mapbox and PMtile**
see https://s3.eu-west-2.amazonaws.com/www.libre-maps.com/cumbria/index.html   
**Layers**    
So far:-   
--Gates   
--Stiles   
--Kissing_Gates   
--Walls   

**Process**     
Copy the KMZ from Mac/Organic Maps application.   

In BBEdit extract just the Name, Lon and Lat.    
Add a Line Number   
**Headers** -- ID, Name, Lon, Lat   

id, name, lon, lat   
 
2. Convert this csv into a GeoJson file using python script .py   

3. Generate PMtiles using **-- TippeCanoe** to create the **pmtiles**   

4. Update the **index.html** and push this to **S3** to serve up the ThunderForest map and point/polyline data tiles.   

5. ALL these files should be uploaded to my S3 Bucket ensuring public access to these files as its a website.   

----Sunday 17th August 2025 19:21
