import React, {useState, useEffect} from 'react'
import socketClient  from "socket.io-client";
const SERVER = "http://localhost:8080";

export default function Eve() {

  var socket = socketClient (SERVER, {
    rejectUnauthorized: false // WARN: please do not do this in production
  });

  const [arePublicKeysReceived, setArePublicKeysReceived] = useState(false);
  const [p, setP] = useState(0)
  const [g, setG] = useState(0)
  const [isKeySharedByAlice, setIsKeySharedByAlice] = useState(false)
  const [keySharedByAlice, setKeySharedByAlice] = useState(0)
  const [isKeySharedByBob, setIsKeySharedByBob] = useState(false)
  const [keySharedByBob, setKeySharedByBob] = useState(0)


  socket.on("connect", () => {
      console.log(socket.id); // x8WIv7-mJelg7on_ALbx
      socket.emit('hello', "Hello from Eve!")
  });

  socket.on("publicKeyValues", (keys)=>{
    setP(keys['p']);
    setG(keys['g']);
    setArePublicKeysReceived(true);
  });

  socket.on("privKeyValueAlice", (value)=>{
    setKeySharedByAlice(value);
    setIsKeySharedByAlice(true);
  });

  socket.on("privKeyValueBob", (value)=>{
    setKeySharedByBob(value);
    setIsKeySharedByBob(true);
  });

  return (
    <div className='container container-fluid'>
        <h2 style={{textAlign: 'center', marginBottom: '2rem'}}>Eve 😈</h2>
        <div className='container container-fluid'>
          <h6>Public Key P: {arePublicKeysReceived ? p : 'Waiting for it...'}</h6>
          <h6>Public Key G: {arePublicKeysReceived ? g : 'Waiting for it...'}</h6>
          <h6>Key Shared By Alice: {isKeySharedByAlice ? keySharedByAlice : 'Waiting for it...'}</h6>
          <h6>Key Shared By Bob: {isKeySharedByBob ? keySharedByBob : 'Waiting for it...'}</h6>
        </div>
    </div>
  )
}
