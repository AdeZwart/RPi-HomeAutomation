import ConfigParser
import io

def getConfigSetting(section, setting):
    return config.get(section, setting)

with open("config.ini") as f:
    config_file = f.read()
        
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(config_file))
