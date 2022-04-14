import javabridge
import bioformats
import re

javabridge.start_vm(class_path=bioformats.JARS)

path = "./3377A8.ome.tif"

# with bioformats.ImageReader(path) as reader:
# 	print(reader.read())

xml = bioformats.get_omexml_metadata(path)

# (?# matches = re.search(r'Channel Color="" ID="Channel:0:0" Name="DNA (DAPI)"(.+?)"', xml))
matches = re.findall(r'Name="(.+?)"', xml)
for match in matches:
	print(match)

#print(xml)

javabridge.kill_vm()
