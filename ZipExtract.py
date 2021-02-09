
# Importing os module
import os

# Importing Zip Module
from zipfile import ZipFile

# A function to extract zip file 
def extract(zipFilePath):

    # We can skip the special characters using '\' 
    # So it adds \\ to the path
    path=zipFilePath.replace('\\','\\\\')

    # removes the quote from both the end
    path=path.strip('"')

    # Below block of code creates a breakpoint 
    # And seperates filepath and filename
    lengthOfPath=len(path)-1
    breakPoint=0
    for i in range(lengthOfPath,0,-1):
        if path[i]=='\\':
            breakPoint=i
            break
    file=path[breakPoint+1:]
    path=path[:breakPoint+1]

    # Changes the path of the current directory
    # to the path where zip exists
    os.chdir(path)

    # opens the zip and extracts it to the same path
    with ZipFile(file) as zip:
        print("Extracting...")
        zip.extractall()
        print("Done.")

    # Exits    
    input("\nEnter to Exit.")
    


if __name__=='__main__':

      # Welcome Note
      print("Welcome to ZIP extractor by MRPNH !!")
      print("Drag and Drop Your Zip file Here")

      # Take the file path input including zip file name
      zipFilePath=input()
      print("File Path:",zipFilePath)
      
      # Calls the extract function
      extract(zipFilePath)
