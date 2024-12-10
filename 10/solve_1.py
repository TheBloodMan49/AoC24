

def main(file: str):
    with open(file) as f:
        data = [[int(x) for x in line.strip().split()] for line in f.readlines()]
        
