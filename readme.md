#OpenStreetMap Alameda County Address Import

Just getting started

##Data

https://data.acgov.org/Government/Alameda-County-Secondary-Addresses/8e4s-7f4v

What are 'Secondary Addresses'?

##Translation

| OSM TAG           | SHP                                       |
| ------------------|:-----------------------------------------:|
| `addr:housenumber`| `ST_NUM`        					        |
| `addr:unit`       | `UNIT`                                    |
| `addr:street`     | `DIRPRE` +  `FEANME` + `FEATYP` + `DIRSUF`|
| `addr:postcode`   | `ZIPCODE`                                 |
| `addr:city`       | `CITY`         					        |

The following will be expanded `FEATYP`, `DIRPRE`, `DIRSUF`.

What's the best way to handle capitalization?

##Usage

`git clone git@github.com:davidchiles/alamedacountyaddress.git --recursive`

First unzip `data/Alameda_County_Secondary_Addresses.zip`

###Translate to OSM file

`cd lib/ogr2osm/`

`python ogr2osm.py ../../data/Alameda_County_Secondary_Addresses/SPAD.shp  -o ../../acaddress.osm -t acaddress`

###Split
Split the large county osm file into smaller manageable city osm files

`python split.py`

###Merge
