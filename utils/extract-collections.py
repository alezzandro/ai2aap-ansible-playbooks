#!/bin/python

import yaml

yamlfile = yaml.safe_load(open("./ee-supported-rhel8-collections.yaml",'r'))

print("---")
print("collections: ")
for collection in yamlfile["collections"]:
  print("  - name: "+collection["name"])
  print("    version: "+collection["version"])


