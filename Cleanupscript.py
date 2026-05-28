import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')

def delete_old_snapshots(days=7):
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])

    cutoff = datetime.now() - timedelta(days=days)

    for snap in snapshots['Snapshots']:
        start_time = snap['StartTime'].replace(tzinfo=None)

        if start_time < cutoff:
            ec2.delete_snapshot(SnapshotId=snap['SnapshotId'])
            print("Deleted:", snap['SnapshotId'])

if __name__ == "__main__":
    delete_old_snapshots()