var socketId;

// Handle the "onReceive" event.
var onReceive = function(info) {
  if (info.socketId !== socketId)
    return;
  console.log(info.data);
  console.log("Received data");
};

// Create the Socket
chrome.sockets.udp.create({}, function(socketInfo) {
  console.log("Binding socket.");
  socketId = socketInfo.socketId;
  // Setup event handler and bind socket.
  chrome.sockets.udp.onReceive.addListener(onReceive);
  chrome.sockets.udp.bind(socketId,
    "0.0.0.0", 1337, function(result) {
      if (result < 0) {
        console.log("Error binding socket.");
        return;
      }
  });
});
