from collections import ChainMap


default_settings = {'mode': 'eco', 'power_level': 7}
user_settings = {}

settings = ChainMap(user_settings, default_settings)

print(settings["mode"])