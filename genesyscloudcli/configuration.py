import configparser

class Configuration:
    output_type= 'json'

    def __init__ ():
        config_file_name = 'config'
        home = os.path.expanduser('~')
        config_file_path = os.path.join(home, '.genesyscloud', config_file_name)

        config = configparser.ConfigParser()
        
        # Get the current users home directory and check the ~/.aws/config file exists
        if not os.path.isfile(config_file_path):
            return 

        config.read(config_file_path)

        output_type = get_property(config._defaults, 'output_type', json)

    def get_property(defaults,prop, default):
        if prop in defaults:
            return defaults[prop]
        
        return default
