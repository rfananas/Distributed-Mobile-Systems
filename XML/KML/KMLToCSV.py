from lxml import etree

ortschaft = 'Familie'
baseFor_XSL = '/Users/rfananas/Documents/HWZ/5. Semester/Distributed & Mobile Systems/Block 2/XML/'
baseFor_KML = '/Users/rfananas/Documents/HWZ/5. Semester/Distributed & Mobile Systems/Block 2/XML/Familie.kml'
baseFor_CSV = baseFor_KML

xsltFN = baseFor_XSL + 'transform_kml_csv.xsl'
print('reading XSLT:\n', xsltFN, '\n\n')
data = open(xsltFN)
xslt_content = data.read()
xslt_root = etree.XML(xslt_content)

kmlFN = baseFor_KML + ortschaft + '.kml'
print('reading KML:\n', kmlFN, '\n\n')
dom = etree.parse(kmlFN)

transform = etree.XSLT(xslt_root)
result = transform(dom)

csvFN = baseFor_CSV + ortschaft + '.csv'
print('writing csv:\n', csvFN, '\n\n')
f = open(csvFN, 'w')
f.write('# Converted from CSV\n')
f.write(str(result))
f.close()