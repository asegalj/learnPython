import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename',  help='the first number of lines to read')
args = parser.parse_args()
filename = args.filename
try:
    f = open(filename, 'r')
except FileNotFoundError as err:
    print(f"Error: {err}")
else:
    print(f.read())
file=f
document=file.read()
loaded = yaml.load(document)
loaded['b']['version'] = '2.3.0.0'
dumped = yaml.dump(loaded)
file.close()
file=open('document2.yaml', 'w')
file.write(dumped)
file.close()