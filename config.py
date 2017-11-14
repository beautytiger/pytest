# -*- coding: utf8 -*-

import ConfigParser

parser = ConfigParser.ConfigParser()
parser.read("sample.conf")

name = parser.get("tester", "username")
pwd = parser.get("tester", "password")
sec = parser.get("tester", "newsec")
url = parser.get("tester", "url")

print name, pwd, sec, url
