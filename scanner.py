from flask import Flask, render_template, request, jsonify
import socket

app = Flask(__name__)

# Ye function ports scan karega
def scan_logic(target):
    open_ports = []
    for port in range(1, 101): # 1 se 100 ports tak scan
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target_ip = request.form.get('ip')
    found_ports = scan_logic(target_ip)
    return jsonify({'ports': found_ports, 'target': target_ip})

if __name__ == '__main__':
    app.run(debug=True) # Localhost start karne ke liye
