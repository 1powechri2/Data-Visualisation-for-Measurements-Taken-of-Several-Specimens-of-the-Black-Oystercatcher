import React from 'react'
import ReactDOM from 'react-dom'

function stuff() {
  return <h1>{window.stuff}</h1>;
}

const element = stuff();

ReactDOM.render(
  element,
  document.getElementById('react')
);
