import xml.etree.ElementTree as ET

#定义一个XML字符串
xml_string = '''
<bookstrore>
    <book>
        <title>Introduction to python</title>
        <author>John Doe</author>
        <price>29.99</price>
    </book>
    <book>
        <title>Data Science with python</title>
        <author>Jane Smith</author>
        <price>39.95</price>
    </book>
</bookstrore>
'''

#使用ElementTree解析XML字符串
root = ET.fromstring(xml_string)

#遍历XML树
for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    price = book.find('price').text  # Corrected variable name from 'prtin' to 'price'
    print(f'Title:{title}, Author:{author}, Price: {price}')  # Corrected variable name from 'prtin' to 'price'
