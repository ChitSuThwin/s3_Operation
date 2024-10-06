import boto3

def s3_client():
    s3=boto3.client()
    """:type : pyboto3.s3"""
    return s3