# Rename this file to secrets.py and fill in your details

# WiFi Credentials
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASS = "YOUR_WIFI_PASSWORD"

# MQTT Broker Configuration
MQTT_SERVER = "your-endpoint.iot.region.amazonaws.com"
MQTT_PORT = 8883
MQTT_SSL = True

# AWS Certificate Paths
CERT_FILE = "/config/certificate.pem.crt"
KEY_FILE = "/config/private.pem.key"
# MQTT Certificate & Credentials
MQTT_CERT = 'AmazonRootCA.pem'   # CA Certificate (Required for AWS)
MQTT_CLIENT_CERT = 'device.pem.crt' # Device Certificate (Required for AWS)
MQTT_CLIENT_KEY = 'private.pem.key' # Device Private Key (Required for AWS)
MQTT_USER = None # AWS often ignores User/Pass, but keep None or empty
MQTT_PASS = None

# Device Security
# SHA-256 hashed password for Setup Mode. 
SETUP_PASSWORD_HASH = "2f1b3754105485376249057c979341536acc7777548332168800343712051122" # Example for "SET_UP_PASSWORD"
