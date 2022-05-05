from lxml import etree

class All_Clothes_Parser():
	def __init__(self):
		self.parse = etree.XMLParser()
		self.config_cloth = "config_all_ru/inventory/"

	def boyClothes(self):
		doc = etree.parse(self.config_cloth + "boyClothes.xml",
						  parser=self.parse)
		root = doc.getroot()
		cloth = []
		for item in root.findall(".//item"):
			cloth.append(item.attrib["id"])
		return cloth

	def girlClothes(self):
		doc = etree.parse(self.config_cloth + "girlClothes.xml",
						  parser=self.parse)
		root = doc.getroot()
		cloth = []
		for item in root.findall(".//item"):
			cloth.append(item.attrib["id"])
		return cloth
