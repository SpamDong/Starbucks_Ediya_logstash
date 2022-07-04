# Jupyter
## Installation
`pip install jupyter`
- jupyter Python API

## Exec
`jupyter notebook`

# Logstash
## Installation
`pip install logstash`
`pip install python-logstash`

- Logstash Python API

## Command

### Connection
```python
host = 'Logstash host'

test_logger = logging.getLogger('python-logstash-logger')

test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))
test_logger.addHandler(StreamHandler())
```

### Send
`test_logger.info('커피', extra=data)`
<br><br><br>
