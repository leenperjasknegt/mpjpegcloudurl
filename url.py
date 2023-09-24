import requests
import urllib3
from flask import Flask, render_template, request

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        credentials = (username, password)
        output_urls = get_output_urls(credentials)
        return render_template('urls.html', urls=output_urls)
    return render_template('index.html')

def get_output_urls(credentials):
    base_url = "https://127.0.0.1:7001/rest/v1"
    system_info_url = base_url + "/system/info"
    devices_url = base_url + "/devices"
    output_urls = []

    session = requests.Session()
    session.auth = credentials
    session.verify = False

    response = session.get(system_info_url)
    system_info = response.json()
    cloud_id = system_info["cloudId"]

    response = session.get(devices_url)
    devices = response.json()

    for device in devices:
        if device.get("isLicenseUsed") is True:
            device_id = device["id"]
            output_url = "https://{}.relay.vmsproxy.com/media/{}.mpjpeg".format(cloud_id, device_id.replace("{", "").replace("}", ""))
            output_urls.append(output_url)

    return output_urls

@app.route('/urls')
def urls():
    credentials = ("admin", "password")
    output_urls = get_output_urls(credentials)
    return render_template('urls.html', urls=output_urls)

@app.route('/system-info')
def system_info():
    base_url = "https://127.0.0.1:7001/rest/v1"
    system_info_url = base_url + "/system/info"
    credentials = ("admin", "password")
    session = requests.Session()
    session.auth = credentials
    session.verify = False
    response = session.get(system_info_url)
    system_info = response.json()
    return system_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
