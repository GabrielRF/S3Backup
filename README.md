# Amazon S3 Backup

This script is used to backup files to Amazon S3.

## Installation

After cloning this repository

```
apt-get install zip
pip3 install -r requirements.txt
```

## Usage

It is recommended to use it as a cron job. Type `crontab -e` and add a line as follows:

```
0 4 * * * cd /usr/local/bin/S3Backup; /root/.virtualenvs/VirtualEnv/bin/python3 s3.py '/path/to/folder/' 'source_files.*' 'dest.zip'
```

Files are compressed as a `zip` and then uploaded to Amazon S3.
