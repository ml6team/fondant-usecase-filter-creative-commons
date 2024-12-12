import logging

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import boto3
import botocore

logger = logging.getLogger(__name__)

COMMONCRAWL_BASE_URL = "https://data.commoncrawl.org/"


def download_warc_file(warc_file: str, retries: int = 10,):
    """
    Downloads a WARC file from the Common Crawl S3 bucket.

    Args:
        warc_file (str): The name of the WARC file to download from the S3 bucket.
        retries (int, optional): The number of retry attempts for the download. Defaults to 10.

    Returns:
        a zipped binary file: The body of the response containing the WARC file content.
    """
    retry_config = botocore.config.Config(
        retries={"max_attempts": retries, "mode": "standard"}
    )

    s3_client = boto3.client("s3", config=retry_config)
    bucket_name = "commoncrawl"
    response = s3_client.get_object(Bucket=bucket_name, Key=warc_file)
    return response["Body"]
