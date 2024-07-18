import converter
import sys


data = converter.read(sys.argv[1])

xml_data = converter.convert(data)

converter.write(sys.argv[2], xml_data)
