import React from 'react'
import ReactDOM from 'react-dom'

var dude = "dude"
function Welcome(name) {
  return <h1>Hello, {name}</h1>;
}

const element = Welcome(dude);
ReactDOM.render(
  element,
  document.getElementById('react')
);
