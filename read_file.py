#Rread file and convert to list
def read_file(filename: str) -> list:
    """
    Reads a file and returns a list of lines.
    
    Args:
        filename (str): The name of the file to read.
    
    Returns:
        data (list): A list of lines from the file.
    """
    s=g.split(',')
    i=0
    while i<len(s):
        s[i] = int(s[i])
        i+=1
    return s
f=open('data.txt', mode='r')
g=f.read()
print(read_file('data.txt'))