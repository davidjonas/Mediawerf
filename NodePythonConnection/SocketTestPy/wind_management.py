from socketIO_client import SocketIO
import sys


port = 8080
host = "localhost"
interval = 1


#read port from commandline python wind_managment.py host 8080
if len(sys.argv) >= 4:
    try:
        port = int(sys.argv[3])
        host = sys.argv[2]
    except:
        print("Argument error, Usage: python wind_managment.py host port")


def logACK(data):
    print("Acknoledgement received for %s"%data['original'])

if __name__ == "__main__":
    socketIO = SocketIO(host, port)
    socketIO.on("ack", logACK)

    while True:
        try:
            socketIO.emit('windSpeedUpdate', {'value': 200})
            socketIO.emit('windDirectionUpdate', {'value': 45})
            socketIO.wait(interval)
        except:
            break



