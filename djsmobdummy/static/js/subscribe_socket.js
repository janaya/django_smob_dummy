
(function (window) {

  function subscription(host, port, callback_url, publisher_url) {
    var socket = new io.Socket(host, {port: port});

    button.onclick = function (e) {
      var params = {"hub.mode":"subscribe","hub.verify":"async","hub.callback":callback_url,"hub.topic": publisher_url};
      socket.send(JSON.stringify(params));
    }

    socket.on('connect', function(){
      console.debug("Socket opened");
      send_or_ask_cookie();
    });
    
    socket.on('disconnect', function(){
    });

    socket.connect();
  }
})(window);

