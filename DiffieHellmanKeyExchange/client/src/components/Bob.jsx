import React, {useState, useEffect} from 'react'
import socketClient  from "socket.io-client";
const SERVER = "http://localhost:8080";

export default function Bob() {

  var socket = socketClient (SERVER, {
    rejectUnauthorized: false // WARN: please do not do this in production
  });

  socket.on("connect", () => {
      console.log(socket.id); // x8WIv7-mJelg7on_ALbx
      socket.emit('hello', "Hello from Bob!")
  });

  const [arePublicKeysDeclared, setArePublicKeysDeclared] = useState(false);
  const [areKeysExchanged, setAreKeysExchanged] = useState(false);
  const [hasSharedKey, setHasSharedKey] = useState(false)
  const [hasIncomingKeyReceived, setHasIncomingKeyReceived] = useState(false)

  const [p, setP] = useState(0);
  const [g, setG] = useState(0);
  const [privKey, setPrivKey] = useState(0);
  const [keyToExchange, setKeyToExchange] = useState(0);
  const [incomingSharedKey, setIncomingSharedKey] = useState(0)
  const [finalKey, setFinalKey] = useState(-1)

  socket.on("publicKeyValues", (keys)=>{
    setP(keys['p'])
    setG(keys['g'])
    setArePublicKeysDeclared(true);
  });

  const keysExchangeSubmitHandler = (e) => {
    e.preventDefault();
    let theValueToExchange = Math.pow(g, privKey);
    console.log(theValueToExchange);
    console.log("Aaaaaaa")
    theValueToExchange %= p;
    setKeyToExchange(theValueToExchange)
    socket.emit("privKeyValueBob", theValueToExchange);
    setAreKeysExchanged(true);
  }

  socket.on("privKeyValueAlice", (value)=>{
    setIncomingSharedKey(value);
    setHasSharedKey(true);
    setHasIncomingKeyReceived(true)
  })

  const computeFinalKey = () => {
    let finalKeyValue = Math.pow(incomingSharedKey, privKey);
    finalKeyValue %= p;
    setFinalKey(finalKeyValue)
  }

  if(finalKey === -1){
    if(areKeysExchanged&&hasIncomingKeyReceived){
        computeFinalKey()
    }
  }

  return (
    <div className='container container-fluid'>
        <h2 style={{textAlign: 'center', marginBottom: '1rem'}}>Bob 👦</h2>
        {!arePublicKeysDeclared ? <p>Waiting for declaration of Public Keys...</p> : <div className='container container-fluid'>
          <h6>Public Keys:</h6>
          <h6>P: {p}</h6>
          <h6>G: {g}</h6>
          </div>}
        {arePublicKeysDeclared && !areKeysExchanged ? <>
        <div>
          <h6>Selection of Private Key and Exchange</h6>
          <form className='privKey' onSubmit={keysExchangeSubmitHandler} >
            <div className="form-group">
              <label htmlFor="privKey">Enter Private Key</label>
              <input onChange={(e)=>setPrivKey(parseInt(e.target.value))} type="number" className="form-control" id="privKey" placeholder="Private Key" required />
            </div>
            <button style={{margin: '1rem auto'}} type="submit" class="btn btn-primary">Submit</button>
        </form>
        </div>
        </> : <></>}
        {areKeysExchanged && !hasSharedKey ? <>
        <div>
          <h6>Key Shared on Public Channel - {keyToExchange}</h6>
          <h6>Waiting for Key to be shared from Alice...</h6>
        </div>
        </> : <></>}
        {areKeysExchanged&&hasIncomingKeyReceived ? <>
        <div className='container container-fluid'>
            <h6>Key Shared on Public Channel - {keyToExchange}</h6>
            <h6>Incoming Key - {incomingSharedKey}</h6>
        </div>
        <div className='container container-fluid'>
            <h6>We get final common key as: {finalKey}</h6>
        </div>
        </> : <></>}
    </div>
  )
}
