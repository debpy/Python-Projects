import boto
import datetime
import dateutil
from dateutil import parser
import boto3
from  connect import *

conn=ec2_connect()

def delete_unused_snapshots():
    ebsAllSnapshots=conn.describe_snapshots()
    #days=arg['days']
#Get the 30 days old date
    timeLimit=datetime.datetime.now() - datetime.timedelta(days=30)

    for snapshot in ebsAllSnapshots:
        if parser.parse(snapshot.start_time).date() <= timeLimit.date():
            print(" Deleting Snapshot %s  %s "  %(snapshot.id,snapshot.tags))
            #connection.delete_snapshot(snapshot.id)
        else:
            # this section will have all snapshots which is created before 30 days
            print("Only Deleting Snapshots which is 30 days old")
delete_unused_snapshots()
