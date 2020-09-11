import boto3


def get_prefix_s3(bucket="fedex-case", prefix=""):
    client = boto3.client("s3")
    result = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter="/")
    result = result.get("CommonPrefixes")
    return result


def delete_by_prefix(prefix: str, bucket_name: str = "fedex-case"):
    if prefix[-1] == "/":
        prefix = prefix[:-1]
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    bucket.objects.filter(Prefix=f"{prefix}/").delete()


def delete_old_data(remove_prefixes: list):
    any(map(delete_by_prefix, remove_prefixes))
