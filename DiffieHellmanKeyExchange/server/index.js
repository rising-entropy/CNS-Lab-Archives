const express = require('express');
const app = express();
const cors = require("cors");
const http = require('http').createServer(app);
const PORT = 8080;
const io = require('socket.io')(http,{cors: {origin: "*"}});

app.use(cors());
app.use(require('express').json());

let p = 0;
let g = 0;

let sharedKeyOfAlice = 0
let sharedKeyOfBob = 0;


io.on("connection", (socket) => {
  console.log("Someone joined!");

  socket.on("hello", (message)=>{
    console.log(message)
  });

  socket.on("publicKeyValues", (keys)=>{
    p = keys['p'];
    g = keys['g'];
    console.log(p)
    console.log(g)
    socket.broadcast.emit("publicKeyValues", keys);
  });

  socket.on("privKeyValueAlice", (value)=>{
    sharedKeyOfAlice = value
    socket.broadcast.emit("privKeyValueAlice", sharedKeyOfAlice);
  });

  socket.on("privKeyValueBob", (value)=>{
    sharedKeyOfBob = value
    socket.broadcast.emit("privKeyValueBob", sharedKeyOfBob);
  });

});

io.listen(PORT);