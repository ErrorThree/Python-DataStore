from DataStore import Data
from random import randint

username = input("Name: ")
Template = {"Username": username, "Money": 0, "Test":0}
Data.Folder("Saved_Data")

Data.DataStore.Data("Saved_Data", username.lower() + "_Data", Template)

def runcommand():
  command = input("Command: ")
  if command.lower() == "add":
    Money = Data.DataStore.Pull("Saved_Data", username.lower() + "_Data")
    number = randint(1,10)
    Money["Money"] = Money["Money"]+number
    Data.DataStore.ChangeDictionary("Saved_Data", username.lower() + "_Data", Money)
    print(f'Added {username} ${number} | You have ${Money["Money"]}')
  runcommand()
runcommand()