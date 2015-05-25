var app = require('./app');

var server = app.listen(3000, function () {
	
	//report status http server
 	var host = server.address().address
  	var port = server.address().port
  	console.log('Server app listening at http://%s:%s', host, port)
})

// SOCKETS

var io = require( "socket.io" )( server );

var sala1 = io.of('/devroom');
sala1.on('connection', function(socket){
  console.log("new socket connected in devroom")
  socket.on('chat message', function(msg){
    msg.date = new Date();
    sala1.emit('chat message', msg);
  });

});

io.on("connection", function(socket){
  console.log("nueva conexion en socket general")

  socket.on('newroom', function(msg){
    console.log("nueva sala: " + msg)
    io.of("/" + msg).on('connection', function(socket){
      console.log("nueva conexion en nueva sala");
      socket.on('chat message', function(msg){
        msg.date = new Date();
        io.of(this.nsp.name).emit('chat message', msg);
      })
    })
  })

  socket.on('closeroom', function(msg){
    delete io.nsps['/' + msg];
    console.log("sala borrada: + msg")
  })
})
