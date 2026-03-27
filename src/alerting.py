import configparser

# Load credentials from the config file
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['DEFAULT']['API_KEY']
USERNAME = config['DEFAULT']['USERNAME']
