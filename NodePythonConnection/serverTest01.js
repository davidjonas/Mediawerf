var server = require('http').createServer(),
    io = require('socket.io')(server, {'transports': ['websocket',]}),
    process = require('process');

//port to listen can be set through command line argument by running 'node server.js [port]' (it defaults to 7080)
var port = (process.argv.length >= 3) ? process.argv[2] : 8080;


function log(str){
    if(debug === true){
        console.log(str);
        if (io.sockets.clients().length > 0)
        {
            io.sockets.emit("debug", {message: str});
        }
    }
};

server.listen(port);
console.log("Server listening on port " + port);

io.sockets.on('connection', function(socket) {

	log("Connection established.");

	socket.on('windSpeedUpdate', function(data) {
        if (data)
        {
            log("Wind speed spdate: " + data['value']);
            //socket.emit("ack", {'original':'windSpeedUpdate'});
            socket.broadcast.emit("windSpeedUpdate", data);
        }
        else
        {
            log("No data received");
        }
    });

    socket.on('windDirectionUpdate', function(data) {
        if (data)
        {
            log("Wind direction update: " + data['value']);
            //socket.emit("ack", {'original':'windDirectionUpdate'});
            socket.broadcast.emit("windDirectionUpdate", data);
        }
        else
        {
            log("No data received");
        }
    });

});
