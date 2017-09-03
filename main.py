fileName = "fertility_Diagnosis.txt"; # name of file containing data

def main():
    openFile();
    
# open file    
def openFile():
    with open(fileName, encoding = "utf8") as inFile:
        processedFile = processFile(inFile);
        
# use file contents to build .arff file
def processFile(inFile):
    for line in inFile:
        line = line.rstrip();
        print(line);
    return inFile;
    
main();