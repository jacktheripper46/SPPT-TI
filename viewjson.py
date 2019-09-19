from flask import Flask
import json

with open('orang.json') as f:
  data = json.load(f)

print(data)
