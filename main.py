from DataStore import Data

Data.Folder("Test")
Data.DataStore.Data("Test", "E", {"Name":"E","Money":0})
print(Data.DataStore.Pull("Test", "E"))