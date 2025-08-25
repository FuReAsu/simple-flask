import os

port = os.getenv('APP_PORT', '8765')

bind = f'0.0.0.0:{port}'
workers = 1
accesslog = '-'
errorlog = '-'
