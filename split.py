import xml.etree.ElementTree as ET


files = dict()

tree = ET.parse('acaddress.osm')
root = tree.getroot()

for child in root:
	for tag in child:
		if tag.attrib['k'] == 'addr:city':
			cityName = tag.attrib['v']
			if cityName not in files.keys():
				files[cityName] = list(child)
			else:
				files[cityName].append(child)

for cityName in files.keys():
	root = ET.Element("osm")
	root.set("version", '0.6')
	root 
	for node in files[cityName]:
		root.append(node)

	tree = ET.ElementTree(root)
	filename = './cities/'+cityName+'.osm'
	tree.write(filename)