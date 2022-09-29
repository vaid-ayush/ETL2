from boto3.session import Session
import boto3
from botocore.exceptions import NoCredentialsError

def downloadingFile(bucket, key, filename):
    s3 = boto3.client("s3")
    try:
        s3.download_file(bucket, key, filename)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


downloaded = downloadingFile('staging-for-load', 'adobe_analytics/dtm_data/commercial/01-decommercialresponsive_2021-01-05.tsv.gz', '01-decommercialresponsive_2021-01-05.tsv.gz')
