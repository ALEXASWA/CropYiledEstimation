import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Dynamically fetch host, port, and debug settings
    host = os.getenv('FLASK_HOST', '127.0.0.1')  # Defalt: localhost
    port = int(os.getenv('FLASK_PORT', 5000))    # Default: port 5000
    debug = os.getenv('FLASK_DEBUG', 'true').lower() == 'true'  # Default: debug mode on

    print(f"Starting Flask app on {host}:{port} with debug={debug}")  # Debug log
    app.run(host=host, port=port, debug=debug)
