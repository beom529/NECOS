#from NECOS import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #username
    #password
    #passwordLength
    #birthday
    #SoSDate
    #EoSDate
    #rank
    #name
    #permissionID
    #creationDate
    #modificationDate
    
# class Permission(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
    
#     #readUserManager
#     #writeUserManager
#     #readChangeLog
#     #writeChangeLog
#     #readVirusLog
#     #writeVirusLog
    
    
    
    
#     pass

# class PolicyChangeLog(db.Model):
#     #id
    
#     #date
#     #firewallType
#     #policyChangeID
#     #modificationRequestor
#     #modificationPerformer
#     #action
#     #addressType
#     #address
#     #country
#     #supplementalAddress
#     #reason
#     #note
#     #blockReason
#     #cooperationName
#     pass

# class VirusLog(db.Model):
#     #id
    
#     #detectionDate
#     #infectionDate
#     #networkType
#     #infectionBase
#     #address
#     #isSampleFile
#     #malwareName
#     #infectionFileHash
#     #infectionFileCrationDate
#     #diagnosticRequestDate
#     #diagnositcResult
#     #isFalsePositive
#     #isSARequired
#     #isInvasionReponseReportRequired
#     #diagnosticProgress
#     #isComfirmed
#     #notes
#     #i
    
#     pass