class Parser:

    def __init__(self, seafar_json_object):
        self.type = seafar_json_object["type"]
        self.geometry_type = seafar_json_object["geometry"]["type"]
        self.latitude = seafar_json_object["geometry"]["coordinates"][1]
        self.longitude = seafar_json_object["geometry"]["coordinates"][0]
        self.sogKph = seafar_json_object["properties"]["sogKph"]
        self.headingTrueDegrees = seafar_json_object["properties"]["headingTrueDegrees"]
        self.epochSeconds = seafar_json_object["properties"]["epochSeconds"]

