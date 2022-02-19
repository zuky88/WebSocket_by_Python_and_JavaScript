'use strict';

{
    const Start = document.getElementById("Start")
    const Clear = document.getElementById("Clear")
    const End = document.getElementById("End")
    const ADDRESS = '127.0.0.1'
    const PORT = 60000
    const URI = 'ws://' + ADDRESS + ':' + String(PORT)
    var SndMsgList = document.getElementById("SndMsg")
    var RcvMsgList = document.getElementById("RcvMsg")
    var data = 0;
    var connection = "";

    function clearArea(){
      SndMsgList.value = '';
      RcvMsgList.value = '';
    }
    Start.addEventListener('click', () =>{
        clearArea();
        connection = new WebSocket(URI);
        connection.onopen = () => {
          console.log("Connected.");
        };
        connection.onerror = () => {
          console.log("Error");
        };
        connection.onmessage = (e) => {
          let msg = e.data;
          let now = new Date()
          RcvMsgList.value = "[Client]Recv:" + String(msg) + "[" + now + "]\n" + RcvMsgList.value;
        };
        connection.onclose = () => {
          console.log("End connection");
        };
    });
    Clear.addEventListener('click', () =>{
        clearArea();
    });
    End.addEventListener('click', () => {
        connection.close();
    });
    function clientMain(){
      if (connection.readyState == WebSocket.OPEN){
        data += 1;
        connection.send(data);
        let now = new Date()
        SndMsgList.value = "[Client]Send:" + String(data) + "[" + now + "]\n" + SndMsgList.value;
      }
      const timeoutId = setTimeout(clientMain, 100);
    }
    clientMain();
}