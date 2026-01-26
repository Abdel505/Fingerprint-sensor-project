# Rename this file to secrets.py and fill in your details

# WiFi Credentials
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASS = "YOUR_WIFI_PASSWORD"

# MQTT Broker Configuration
MQTT_SERVER = "your-cluster-url.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_SSL = True

# MQTT Certificate & Credentials
MQTT_CERT = 'AmazonRootCA.pem'   # CA Certificate (Required for AWS)
MQTT_CLIENT_CERT = 'device.pem.crt' # Device Certificate (Required for AWS)
MQTT_CLIENT_KEY = 'private.pem.key' # Device Private Key (Required for AWS)
MQTT_USER = None # AWS often ignores User/Pass, but keep None or empty
MQTT_PASS = None

# Device Security
SETUP_PASSWORD = "SET_UP_PASSWORD" # Password for Setup Mode
