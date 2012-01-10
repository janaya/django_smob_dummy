

    $(document).ready(function(){
            var conn = {},
            serverUri,
            publish     = document.getElementById('publish'),
            form        = publish.form;
            
          var rss_url = "http://localhost:8000/person/post/rssrdf";
          var callback_url = "http://localhost:8000/callback";
          var publisher_url = "http://smob.rhizomatik.net/me/rss";
          var foaf_url = "http://xmppwebid.github.com/xmppwebid/julia";
          
            function startConnection() {
                var host = "localhost",
                port = 8080;
                serverUri = "ws://"+host+":"+port;
                openConnection();
            }

            function openConnection() {
                if ( !conn.readyState || conn.readyState > 1 ) {

                    conn = new WebSocket( serverUri );

                    conn.onopen = function () {
                      console.debug("Socket opened");
                    };

                    conn.onmessage = function( event ) {
                        var string = event.data;
                        var code = format_xml(string).replace(/></,'').replace(/\&/g,'&'+'amp;').replace(/</g,'&'+'lt;').replace(/>/g,'&'+'gt;').replace(/\'/g,'&'+'apos;').replace(/\"/g,'&'+'quot;')
                        $('#messages').prepend("<pre class='sh_xml'><code>"+ code + "</code></pre>");
                        sh_highlightDocument(); 
                        if($('#messages').children().size() > 5) {
                            $('#messages pre:last-child').remove();
                        }
                    };

                    conn.onclose = function( event ) {
                      console.debug("Socket closed");
                    };
                }
            }

            if (!window.WebSocket) {
                console.debug("Sockets not supported");
            } else {
                form.addEventListener("submit", function (e) {
                    e.preventDefault();

                    // if web socket connected
                    if (conn.readyState === 1) {
                        var connection =  {"hub.mode":"subscribe","hub.verify":"async","hub.callback":callback_url,"hub.topic": publisher_url};
                        conn.send(JSON.stringify(connection));
                        publish.value = "";
                    }
                }, false);

                startConnection();
            }

        
    });
