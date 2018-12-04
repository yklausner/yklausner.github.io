from json import load
from sys import argv

def loc(nb):
    cells = load(open(nb))['cells']
    #return sum(len(c['source']) for c in cells if c['cell_type'] == 'code')
    sum = 0 
    for c in cells:
        if c['cell_type'] == 'code':
            for line in c['source']:
                if str.lstrip(line[0]) != '#':
                    sum += 1
    return sum 

def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)

if __name__ == '__main__':
    print(run(argv[1:]))