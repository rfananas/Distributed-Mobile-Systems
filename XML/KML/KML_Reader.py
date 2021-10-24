# ------------------------------------------------------------------
# Name: KMLToCsv.py
#Description: Formats a XML (Export from Geo-Admin) to an nice (indentation) XML document


#Autor: Walter Rothlin

# History:
# 03-Oct-2021   Walter Rothlin      Initial Version
# ------------------------------------------------------------------
import xml.etree.ElementTree as ET

#   
def indent(elem, level=0):
    i = "\n" + level * "  "
    j = "\n" + (level - 1) * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


root = ET.parse("/Users/rfananas/Documents/HWZ/5. Semester/Distributed & Mobile Systems/Block 2/XML/Kuessnacht.kml").getroot()
indent(root)

ET.dump(root)
treeStr = ET.ElementTree(root)
treeStr.write("/Users/rfananas/Documents/HWZ/5. Semester/Distributed & Mobile Systems/Block 2/XML/Kuessnacht_nice.kml")
