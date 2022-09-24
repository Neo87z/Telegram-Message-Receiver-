from flask import  Flask

from flask import *
from flask_ngrok import run_with_ngrok
from pymongo import MongoClient

app= Flask(__name__)


def GetAllMessages():
    try:
        connection_string = "mongodb+srv://admin:admin@cluster0.vhzg812.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        test_db = client.FirstDB
        collectionName = test_db.Names
        Data = collectionName.find()
        AllData = []
        for mes in Data:
            data = {
                "MessageID": mes['MessageID'],
                "Sender": mes['Sender'],
                "Message": mes['Message']
            }
            AllData.append(data)

        FinalData = {
            "FianlData": AllData
        }

        return FinalData

    except Exception as eB:
        print(eB)


def GetAllBetsData():
    try:
        connection_string = "mongodb+srv://admin:admin@cluster0.vhzg812.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        test_db = client.FirstDB
        collectionName = test_db.Bets
        Data = collectionName.find()
        AllData = []
        for mes in Data:
            test_document = {
                "BetName": mes['BetName'],
                "ImageURL": mes['ImageURL'],
                "Team1": mes['Team1'],
                "Team2": mes['Team2'],
                "BetID": mes['BetID'],
                "Team1Logo": mes['Team1Logo'],
                "Team2Logo": mes['Team2Logo'],
                "Team1Score": mes['Team1Score'],
                "Team2Score": mes['Team2Score']
            }

            AllData.append(test_document)

        FinalData = {
            "FianlData": AllData
        }
        return FinalData

    except Exception as eB:
        print(eB)

from flask_cors import CORS
app=Flask(__name__)
cors = CORS(app)

@app.route("/GetALlMessage2s22222222",methods=['GET'])
def TransformVerb2222222s():
  dataa=GetAllMessages()
  print(type(dataa))
  return dataa


@app.route("/GetAllBets22",methods=['GET'])
def GetAllBet22s():
  dataa=GetAllBetsData()
  print(type(dataa))
  return dataa

@app.route('/')
def hello():
    return 'Hel;lo'


if __name__ == '__main__':
    app.run()
