SERVER_HOST="localhost"
SERVER_PORT=8443
SERVER_CONFIG="./config/nixpass.conf"
SSL_CERT_FILE="./certs/certificate.crt"
SSL_KEY_FILE="./certs/certificate.key"

export SERVER_CONFIG=$SERVER_CONFIG
.venv/bin/uvicorn nixpass.server:nixpass_server --host $SERVER_HOST --port $SERVER_PORT --ssl-certfile=$SSL_CERT_FILE --ssl-keyfile=$SSL_KEY_FILE
