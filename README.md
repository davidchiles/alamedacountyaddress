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
