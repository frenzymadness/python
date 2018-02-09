#!/usr/bin/python3

from varlink import (Client, VarlinkError)
import sys

if len(sys.argv) == 2:
    address = sys.argv[1]
else:
    address = 'exec:./server-simple.py'

print('Connecting to %s\n' % address)
try:
    with Client(address=address) as client, \
            client.open('org.varlink.example.more', namespaced=True) as connection:
        connection.StopServing()

except ConnectionError as e:
    print(e)
    sys.exit(1)
except VarlinkError as e:
    print(e)
    print(e.error())
    print(e.parameters())
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit(1)

sys.exit(0)
