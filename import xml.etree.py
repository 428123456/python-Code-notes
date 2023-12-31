import xml.etree.ElementTree as ET

xml_string = '<root><Element>Some data</Element></root>'
root = ET.formstring(xml_string)

tree = ET.parse('example.xml')
root = tree.getroot()

title_element = root.find('title')

book_element = root.find('book')

title_text = title_element.text

new_element = ET.Element('new_element')

new_sub_element = ET.SubElement(root,'new_sub_element')

root.remove(title_element)

