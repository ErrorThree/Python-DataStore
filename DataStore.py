import os
import json

class Data:
  # Create Folder
  def Folder(FolderName):
    # Convertion
    FolderName = str(FolderName)
    # Check if Folder Exist
    if os.path.exists(FolderName):
      pass
    # Create Folder
    else:
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
      # Printing ErrorLog
      else:
        print("Folder Couldn't be Found")

    # Pull Data
    def Pull(FolderLocation, FileName):
      # Convertion
      FolderLocation = str(FolderLocation)
      FileName = str(FileName)
      if os.path.isfile(f"{FolderLocation}/{FileName}"):
        f = open(f"{FolderLocation}/{FileName}", "rt").read()
        unloadf = json.loads(f)
        return unloadf
      else:
        print("File or Dictionary Variable Couldn't be Found")
