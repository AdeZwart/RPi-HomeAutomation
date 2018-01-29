import ConfigParser
import io

class parser:
    """Common base class for getting config settings"""

    def __init__(self):
        self.configParser = ConfigParser.RawConfigParser()
        self.configParser.read("config.ini")
    
    def getConfigSetting(self, section, setting):
        return self.configParser.get(section, setting)
