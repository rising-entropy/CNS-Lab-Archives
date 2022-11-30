import React, {useState, useEffect} from 'react'
import socketClient  from "socket.io-client";
const SERVER = "http://localhost:8080";

function gcd(x, y) {
    if ((typeof x !== 'number') || (typeof y !== 'number')) 
      return false;
    x = Math.abs(x);
    y = Math.abs(y);
    while(y) {
      var t = y;
      y = x % y;
      x = t;
    }
    return x;
}

const checkIfPrimitiveRoot = (p, g) => {
    if(g<0 || gcd(p,g)!=1 || g>=p){
        alert("g<0 || gcd(p,g)!=1 || g>=p")
        return false;
    }
    let solutionsList = [];
    for(let i=1; i<p; i++){
        let value = Math.pow(g, i);
        value %= p
        if(solutionsList.includes(value)){
            alert(solutionsList)
            alert(value)
            return false;
        }
        solutionsList.push(value);
    }
    return true;
}

export default function Alice() {
    var socket = socketClient (SERVER, {
        rejectUnauthorized: false // WARN: please do not do this in production
    });
    
    socket.on("connect", () => {
        console.log(socket.id); // x8WIv7-mJelg7on_ALbx
        socket.emit('hello', "Hello from Alice!")
    });

    const [arePublicKeysDeclared, setArePublicKeysDeclared] = useState(false);
    const [areKeysExchanged, setAreKeysExchanged] = useState(false);
    const [hasSharedKey, setHasSharedKey] = useState(false);
    const [hasIncomingKeyReceived, setHasIncomingKeyReceived] = useState(false)

    const [p, setP] = useState(0);
    const [g, setG] = useState(0);
    const [privKey, setPrivKey] = useState(0);
    const [keyToExchange, setKeyToExchange] = useState(0);
    const [incomingSharedKey, setIncomingSharedKey] = useState(0);
    const [finalKey, setFinalKey] = useState(-1)

    const publicKeysSubmitHandler = (e) => {
        e.preventDefault();
        if(!checkIfPrimitiveRoot(p, g)){
            alert('Invalid Value of Primitive Root.');
            return;
        }
        socket.emit("publicKeyValues", {
            p, g
        });
        setArePublicKeysDeclared(true);
    }

    const keysExchangeSubmitHandler = (e) => {
        e.preventDefault();
        let theValueToExchange = Math.pow(g, privKey);
        theValueToExchange %= p;
        setKeyToExchange(theValueToExchange)
        socket.emit("privKeyValueAlice", theValueToExchange);
        setAreKeysExchanged(true);
    }

    socket.on("privKeyValueBob", (value)=>{
        setIncomingSharedKey(value);
        setHasSharedKey(true);
        setHasIncomingKeyReceived(true)
    });

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
        <h2 style={{textAlign: 'center', marginBottom: '1rem'}}>Alice 👧</h2>
        {!arePublicKeysDeclared ? <></> : <div className='container container-fluid'>
          <h6>Public Keys:</h6>
          <h6>P: {p}</h6>
          <h6>G: {g}</h6>
          </div>}
        {!arePublicKeysDeclared ? <form className='PandG' onSubmit={publicKeysSubmitHandler} >
            <div className="form-group">
                <label htmlFor="p">Enter Public Key P</label>
                <input onChange={(e)=>setP(parseInt(e.target.value))} type="number" className="form-control" id="p" placeholder="P" required />
            </div>
            <div className="form-group">
                <label htmlFor="g">Enter Public Key G</label>
                <input onChange={(e)=>setG(parseInt(e.target.value))} type="number" className="form-control" id="g" placeholder="G - Primitive Root of P" required />
            </div>
            <button style={{margin: '1rem auto'}} type="submit" class="btn btn-primary">Submit</button>
        </form> : <></>}
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
          <h6>Waiting for Key to be shared from Bob...</h6>
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
