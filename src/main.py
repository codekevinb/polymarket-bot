import yaml
import json

# Load configuration
try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print("Error: config.yaml not found.")
    config = None
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")
    config = None

if config is None:
    # Handle the case where the configuration could not be loaded
    exit(1)

# Use the loaded configuration
# Your bot logic here...