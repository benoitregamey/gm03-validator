from lxml import etree as ET

NS = {
    'csw': 'http://www.opengis.net/cat/csw/2.0.2',
    'gco': 'http://www.isotc211.org/2005/gco',
    'che': 'http://www.geocat.ch/2008/che',
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'srv': 'http://www.isotc211.org/2005/srv',
    'gmx': 'http://www.isotc211.org/2005/gmx',
    'gts': 'http://www.isotc211.org/2005/gts',
    'gsr': 'http://www.isotc211.org/2005/gsr',
    'gmi': 'http://www.isotc211.org/2005/gmi',
    'gml': 'http://www.opengis.net/gml/3.2',
    'xlink': 'http://www.w3.org/1999/xlink',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'geonet': 'http://www.fao.org/geonetwork',
    'java': 'java:org.fao.geonet.util.XslUtil',
}

def validate(metadata: str) -> dict:

    root = ET.fromstring(metadata)

    uuid = root.xpath("./gmd:fileIdentifier/gco:CharacterString",
                namespaces=NS)[0].text

    title = root.xpath("./gmd:identificationInfo/*/gmd:citation//gmd:title/gco:CharacterString",
                namespaces=NS)[0].text

    return {
        "uuid": uuid,
        "title": title,
        "valid": "yes",
        "errors": []
    }
