import configparser
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

config = configparser.ConfigParser()
config.read(os.path.abspath(dname + '/../config.ini'))