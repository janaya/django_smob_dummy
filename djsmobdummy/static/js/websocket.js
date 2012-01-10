
///////////////////////////////////////////////////////////////////////////////
// Helper functions
// TODO: move to another file
///////////////////////////////////////////////////////////////////////////////

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}    
function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function send_or_ask_cookie() {
  // CHECK WHETHER COOKIE IN BROWSER
  var clientId= readCookie('ClientId');
  if (clientId) {
    console.debug("found cookie");
    console.debug(clientId);
    // SEND COOKIE TO WEB SOCKET SERVER
    conn.send({ClientId: clientId});
    console.debug("sent cookie");
  } else {
    // ASK FOR A COOKIE TO WEB SOCKET SERVER
    console.debug("no cookie");
    conn.send({ClientId: 0});
  }
}

function subscribe() {
  if (conn.connected) {
    console.debug("going to ask subscription for ");
    var connection = {"hub.mode":"subscribe","hub.verify":"async","hub.callback":"http://localhost:8000/callback","hub.topic": "http://smob.rhizomatik.net/me/rss"};
    conn.send(JSON.stringify(connection));
  }
}
function followings() {
  if (conn.connected) {
    console.debug("going to ask followings");
    //conn.send(JSON.stringify({"GET":"followings"}))
    var connection = {"GET":"followings"};
    conn.send(JSON.stringify(connection));
  }
}
///////////////////////////////////////////////////////////////////////////////
// Socket code
// TODO: move to a function?
///////////////////////////////////////////////////////////////////////////////

      var conn = {};
      var host = "localhost",
          port = 8080;
      var serverUri = "ws://"+host+":"+port;

      // CHECK WHETHER SOCKETS SUPPORTED    
      if (!window.WebSocket) {
        console.debug("sockets not supported");
        // TODO: advice sockets not supported
        // BUT, socket.io is going to use long-pooling if not supported?
        // if behind a firewall:
        //   advice it can not subscribe nor get updates
        // else:
        //   if want to subscribe (in add/following/x):
        //     call php function
      } else {
        console.debug("sockets supported");
        
        // CREATE NEW SOCKET
        //conn = new WebSocket( serverUri );
        var conn = new io.Socket(host,{port: port});
        //var socket = io.connectWithSession(host,{port: port});
        conn.connect(); 
        
        // ON SOCKET STABLISHED
        conn.on('connect',function() {
          console.debug("Socket opened");
          send_or_ask_cookie();
          
        });

        // ON MESSAGE RECEIVED
        conn.on('message',function(data) {
          var string = data;
          console.debug("mesage received");
          //}
          console.debug(string);
          
          try {
            // MESSAGE IS JSON
            json = JSON.parse(string);
            console.debug(json);
            if ( json.ClientId ) {
              console.debug(json.ClientId);
              createCookie("ClientId",json.ClientId);
              console.debug("stored cookie");
            };
          } catch(err) {
            // MESSAGE IS NOT JSON
            console.debug("no json", err);
            
            // message is the new post
            // real time page refresh
            //$('#messages').prepend("<pre class='sh_xml'><code>"+ code + "</code></pre>");
            //sh_highlightDocument(); 
            //if($('#messages').children().size() > 5) {
            //    $('#messages pre:last-child').remove();
          }
          
        });

        // DISCONNECT 
        conn.on('disconnect',function() {
          console.debug("socket closed");
        });    
      
      }  
      
//      $(document).ready(function(){    
//        $.ajax({
//            type: "GET",
//            url: "/client/subscribe_form.html",
//            //data: "dataType=ini",
//            success: function(msg)
//            {
//              //var subscribe_form = eval(msg);
//              $('#subscribediv').append(msg); 
//            }
//        });
//      });  
