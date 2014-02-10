bind = "127.0.0.1:8001" # Direccion donde accedera Nginx
logfile = "/var/www/logs/misitio/gunicorn.log" # Direccion donde estaran los logs
workers = 1 # Dependera en medida de la carga de trabajo
loglevel = 'info' # Tipo de logging
