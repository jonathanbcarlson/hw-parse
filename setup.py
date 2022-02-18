#!/usr/bin/env python3
import configparser
from pathlib import Path

default_cfg = {}
default_cfg['preamblepath'] = '/path/to/preamble'
default_cfg['authorname'] = 'First Last'
default_cfg['config_file_path'] = f'{Path.home()}/.config/hw-parse/hw-parse.cfg'
def config():
  config = configparser.ConfigParser()
  config['DEFAULT'] = {
      'PreamblePath': default_cfg['preamblepath'],
      'AuthorName': default_cfg['authorname'],
      }
  with open(default_cfg['config_file_path'], 'w') as configfile:
    config.write(configfile)
# https://stackoverflow.com/questions/6523791/why-is-python-running-my-module-when-i-import-it-and-how-do-i-stop-it
# only overwrite config during setup
if __name__ == "__main__":
  config()
