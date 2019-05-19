import yaml
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
loaded = yaml.load(document)
print(loaded['a']['c'])
loaded['a']['c'] = 2
dumped = yaml.dump(loaded)
print(dumped)