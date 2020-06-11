# Resource Monitor

A project for getting system host resource data.

## Installing and Running

Installing:
```
pip3 install virtualenv && /
virtualenv venv && /
pip3 install -r requirements.txt
```

Running:
```
python server.py
```

## Usage

### Document Retrieval

```bash
curl -X GET http://localhost:5002/resource
```

## Docker

Create image:
```
sudo docker build -t resource-monitor .
```

Run container:
```
sudo docker run -d -p 5002:5002 --name resource-monitor resource-monitor
```

## API Reference

A Swagger reference is available in swagger.yml.
