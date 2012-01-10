
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

function send_or_ask_cookie(conn) {
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

