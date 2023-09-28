from io import BytesIO
from lxml import etree as ET
from api.gm03_validator import config
from saxonche import PySaxonProcessor

XSD = ET.parse("api/gm03_validator/schemas/iso19139.che/src/main/plugin/iso19139.che/schema.xsd")
XSD = ET.XMLSchema(XSD)

def validate(metadata: bytes) -> dict:

    tree = ET.parse(BytesIO(metadata))
    root = tree.getroot()

    # Get UUID
    if len(root.xpath("./gmd:fileIdentifier/gco:CharacterString",
                namespaces=config.NS)) > 0:
        uuid = root.xpath("./gmd:fileIdentifier/gco:CharacterString",
                    namespaces=config.NS)[0].text
    else:
        uuid = "UUID not found"

    # Get Title
    if len(root.xpath("./gmd:identificationInfo/*/gmd:citation//gmd:title/gco:CharacterString",
                namespaces=config.NS)) > 0:
        title = root.xpath("./gmd:identificationInfo/*/gmd:citation//gmd:title/gco:CharacterString",
                    namespaces=config.NS)[0].text
    else:
        title = "Title not found"

    # Initiate result
    result = {
        "uuid": uuid,
        "title": title,
        "valid": "yes",
        "errors": []
    }

    # Validate with XSD schema
    try:
        XSD.assertValid(tree)

    except Exception as error:
        result["valid"] = "no"
        result["errors"].append(str(error))

    # Validate with schematron
    with PySaxonProcessor(license=False) as proc:

        xsltproc = proc.new_xslt30_processor()
        xsltproc.set_cwd(".")
        document = proc.parse_xml(xml_text=metadata.decode("utf-8"))

        for schematron in config.SCHEMATRON:

            executable = xsltproc.compile_stylesheet(
                stylesheet_file=f"api/gm03_validator/schematron/{schematron}.xsl"
                )

            output = executable.transform_to_string(xdm_node=document)
            report = ET.fromstring(output.encode('utf-8'))

            for error in report.xpath(".//svrl:failed-assert", namespaces=config.NS):
                result["valid"] = "no"

                if "location" in error.attrib.keys():
                    location = error.attrib["location"]
                else:
                    location = ""

                try:
                    msg = error.xpath(".//svrl:text/text()",
                                      namespaces=config.NS)[0].strip()
                except IndexError:
                    msg = ""

                result["errors"].append(f"{msg} Location : {location}")

    return result
