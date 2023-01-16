import boto3

def lambda_handler(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Define the bucket name and file name
    bucket_name = 'paulahakeem-bucket'
    file_name = 'original.txt'

    # Create a new file in the bucket with some text
    s3.put_object(Bucket=bucket_name, Key=file_name, Body='Hello, how area you today?!')

    # Define the new file name for the copy
    new_file_name = 'copy.txt'

    # Copy the file to the new location
    s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': file_name}, Key=new_file_name)