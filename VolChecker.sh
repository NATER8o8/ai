```bash
#!/bin/bash
# This script uses the aws cli to check which volume attached to an ec2 instance is the root volume, and then mounts the other volume

# Get the instance id from the metadata service
instance_id=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)

# Get the root device name from the describe-instances command
root_device=$(aws ec2 describe-instances --instance-ids $instance_id --query "Reservations[0].Instances[0].RootDeviceName" --output text)

# Get the list of attached volumes from the describe-volumes command
attached_volumes=$(aws ec2 describe-volumes --filters Name=attachment.instance-id,Values=$instance_id --query "Volumes[*].Attachments[*].Device" --output text)

# Loop through the attached volumes and find the one that is not the root device
for volume in $attached_volumes; do
  if [ "$volume" != "$root_device" ]; then
    # This is the non-root volume, mount it to /mnt
    echo "Mounting $volume to /mnt"
    sudo mount $volume /mnt
    # Exit the loop
    break
  fi
done

# Check if the mount was successful
if [ $? -eq 0 ]; then
  echo "Mount successful"
else
  echo "Mount failed"
fi

```

#Source: Conversation with Bing, 4/27/2023
#(1) Amazon EC2 instance root device volume. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html.
#(2) attach-volume — AWS CLI 1.27.119 Command Reference. https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-volume.html.
#(3) how to get volume id attached to instance from AWS CLI. https://serverfault.com/questions/888199/how-to-get-volume-id-attached-to-instance-from-aws-cli.
#(4) Mount EBS volume to a running AWS instance with a script. https://stackoverflow.com/questions/41351457/mount-ebs-volume-to-a-running-aws-instance-with-a-script.
#(5) BASH - Check if a volume is attached to instance without AWS CLI tools. https://stackoverflow.com/questions/31992396/bash-check-if-a-volume-is-attached-to-instance-without-aws-cli-tools.
