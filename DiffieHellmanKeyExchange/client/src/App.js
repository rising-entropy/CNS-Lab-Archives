import React, { useState, useEffect } from 'react';
import socketClient  from "socket.io-client";
import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";
import HomePage from './components/HomePage';
import Alice from './components/Alice';
import Bob from './components/Bob';
import Eve from './components/Eve';
const SERVER = "http://localhost:8080";


function App() {

  
  var socket = socketClient (SERVER, {
    rejectUnauthorized: false // WARN: please do not do this in production
  });

  socket.on("connect", () => {
    console.log(socket.id); // x8WIv7-mJelg7on_ALbx
  });

  return (
    <Router>
      <Routes>
          <Route exact path="/" element={<HomePage />} />
          <Route exact path="/alice" element={<Alice />} />
          <Route exact path="/bob" element={<Bob />} />
          <Route exact path="/eve" element={<Eve />} />
      </Routes>
    </Router>
  );
}

export default App;
