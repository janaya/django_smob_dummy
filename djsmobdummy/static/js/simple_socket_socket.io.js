

    $(document).ready(function(){
        function initConnection() {
        
          var host = "localhost",
              port = 8080;

          var rss_url = "http://localhost:8000/person/post/rssrdf";
          var callback_url = "http://localhost:8000/callback";
          var publisher_url = "http://smob.rhizomatik.net/me/rss";
          var foaf_url = "http://xmppwebid.github.com/xmppwebid/julia";

          var socket = new io.Socket(host, {port: port});


          socket.on('connect', function(){
            console.debug("Socket opened");
            send_or_ask_cookie(socket);
          });
          
          socket.on('disconnect', function(){
          });

          socket.connect();
        }

        $("#publish-form").bind('submit',function (e) {
          e.preventDefault();
          if (socket.connected == true) {
            var params = {"hub.mode":"subscribe","hub.verify":"async","hub.callback":callback_url,"hub.topic": publisher_url};
            socket.send(JSON.stringify(params));
          }
        }, false);
        
//      $('#publish-button').click(function(e) {
//        e.preventDefault();
//        subscription(host, port, callback_url, publisher_url);
//      });
        initConnection();

    });
