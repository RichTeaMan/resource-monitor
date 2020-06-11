import os
import psutil
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from json import dumps
from datetime import datetime, timezone

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return 'Resource monitor', 200

class Monitor(Resource):

    def get(self):
        print('Resource monitor requested.')

        cpu = psutil.cpu_times()
        cpuStats = psutil.cpu_stats();
        mem = psutil.virtual_memory()

        result = {
            'cpu': {
                'user': cpu.user,
                'nice': cpu.nice,
                'system': cpu.system,
                'idle': cpu.idle,
                'iowait': cpu.iowait,
                'irq': cpu.irq,
                'softirq': cpu.softirq,
                'steal': cpu.steal,
                'guest': cpu.guest
            },
            'memory': {
                'total':mem.total,
                'available':mem.available,
                'percent':mem.percent,
                'used':mem.used,
                'free':mem.free,
                'active':mem.active,
                'inactive':mem.inactive,
                'buffers':mem.buffers,
                'cached':mem.cached,
                'shared':mem.shared
            }
        }

        print(result)
        return result

api.add_resource(Home, '/')
api.add_resource(Monitor, '/resource')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5002')
