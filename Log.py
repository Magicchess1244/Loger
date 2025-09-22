from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    # Get user's IP address
    user_ip = request.remote_addr
    
    # Store IP in file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("user.txt", "a") as file:
        file.write(f"{timestamp} - {user_ip}\n")
    
    return "Finished"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
