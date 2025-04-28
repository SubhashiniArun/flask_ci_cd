from app import create_app
import logging

logging.basicConfig(level=logging.INFO)

app = create_app(config_name="development")

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=3000, debug=True) # use_reloader=False to prevent multiple instances