fileName = "fertility_Diagnosis.txt";

def main():
    openFile();
    
def openFile():
    with open(fileName, encoding = "utf8") as inFile:
        processedFile = processFile(inFile);
        
def processFile(inFile):
    for line in inFile:
        line = line.rstrip();
        print(line);
    return inFile;
    
main();