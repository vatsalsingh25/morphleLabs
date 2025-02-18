from flask import Flask
import subprocess
import datetime
import pytz

app = Flask(__name__)

def get_system_info():

    username = subprocess.getoutput('whoami')
    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    top_output = subprocess.getoutput('top -b -n 1')
    
    return username, server_time, top_output

@app.route('/htop')
def htop():
    username, server_time, top_output = get_system_info()
    
    html_content = f"""
    <pre>
Name: VATSAL_SINGH
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
    </pre>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)