import urllib.parse


def handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    print(f"uploaded file name is {key}")
    return {'status': 'success', 'key': key}
