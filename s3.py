import boto3
import configparser
from datetime import datetime
from datetime import timedelta
import magic
import os
import requests
import sys

config = configparser.ConfigParser()
config.sections()
config.read('/usr/local/bin/S3Backup/backup.conf')

path = sys.argv[1]
source = sys.argv[2]
dest = sys.argv[3]

# AMAZON S3
ACCESS_KEY_ID = config['AMAZON']['ACCESS_KEY_ID']
SECRET_ACCESS_KEY = config['AMAZON']['SECRET_ACCESS_KEY']
BUCKET = config['AMAZON']['BUCKET']

def send_s3(FILE):
    length = len(FILE.split('/'))
    NAME = FILE.split('/')[length-1]
    NAME = NAME + ' ' + str(datetime.now()) + '.zip'
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)
    b = s3.Bucket(name=BUCKET)
    data = open(FILE, 'rb')
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(FILE)
    b.put_object(Key=NAME, Body=data, ACL='public-read', ContentType=file_type)
    s3.Object(bucket_name='bkp.grf.xyz', key=FILE)

def zip_folder(path, source, dest):
    os.chdir(path)
    os.system('zip ' + dest + ' ' + source)
    return(path + dest)

if __name__ == '__main__':
    bkp_file = zip_folder(path, source, dest)
    print(bkp_file)
    send_s3(bkp_file)
