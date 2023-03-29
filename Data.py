import os
import json

# Create Folder
def Folder(FolderName):
  # Convertion
  FolderName = str(FolderName)
  # Check if Folder Exist
  if os.path.exists(FolderName):
    pass
  else:
    # Create Folder
    FolderName = str(FolderName)
    os.mkdir(FolderName)
# Extension
class DataStore:
  # Create Data
  def Data(FolderLocation, FileName, DataSave):
    # Convertion
    FolderLocation = str(FolderLocation)
    DataSave = dict(DataSave)
    FileName = str(FileName)
    # Check if File Exist
    if os.path.isfile(f"{FolderLocation}/{FileName}"):
      pass
    # Create File
    elif os.path.exists(FolderLocation):
      f = open(f"{FolderLocation}/{FileName}", "x")
      f.write(json.dumps(DataSave))
    else:
      # Printing ErrorLog
      print("Folder Couldn't be Found")

  # Pull Data
  def Pull(FolderLocation, FileName):
    # Convertion
    FolderLocation = str(FolderLocation)
    FileName = str(FileName)
    # Pulling Data from Data File
    if os.path.isfile(f"{FolderLocation}/{FileName}"):
      f = open(f"{FolderLocation}/{FileName}", "rt").read()
      unloadf = json.loads(f)
      return unloadf
    else:
      # Print ErrorLog
      print("File or Dictionary Variable Couldn't be Found")

  # Change Dictionary of Data
  def ChangeDictionary(FolderLocation, FileName, DataSave):
    # Convertion
    FolderLocation = str(FolderLocation)
    FileName = str(FileName)
    DataSave = dict(DataSave)
    # Change Dictionary of Data
    if os.path.isfile(f"{FolderLocation}/{FileName}"):
      fw = open(f"{FolderLocation}/{FileName}", "w")
      fw.write(json.dumps(DataSave))
    else:
      # Print ErrorLog
      print("The File you are trying to change the Dictionary Doesn't Exist")

