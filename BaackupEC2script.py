import boto3
from datetime import datetime

ec2 = boto3.client('ec2')

def create_ec2_snapshot(instance_id):
    volumes = ec2.describe_volumes(
        Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}]
    )

    for volume in volumes['Volumes']:
        snapshot = ec2.create_snapshot(
            VolumeId=volume['VolumeId'],
            Description=f"Auto backup {datetime.now()}"
        )
        print("Snapshot created:", snapshot['SnapshotId'])

if __name__ == "__main__":
    create_ec2_snapshot("i-0123456789abcdef0")