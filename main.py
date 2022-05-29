import re
import subprocess
from wsgiref.simple_server import server_version


def get_internet_speed():
    try:
        response = subprocess.Popen('/usr/bin/speedtest --accept-license --accept-gdpr', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    except:
        pass
    return response

def prep_recieved_values(response):
    values = {}

    ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
    download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
    upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
    jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)
    server_name = re.search('Server:', response, re.MULTILINE)
    server_version = re.search('id', response, re.MULTILINE)

    values["ping"] = ping.group(1)
    values["download"] = download.group(1)
    values["upload"] = upload.group(1)
    values["jitter"] = jitter.group(1)

    return values

def main():
    current = get_internet_speed()
    internet_values = prep_recieved_values(current)
    print(internet_values)

if __name__ == "__main__":
    main()