import React from 'react';
import './App.css';

import Alert from '../Alert/Alert';

function App() {
  return (
    <div className='wrapper'>
      <Alert title='Items Not Added' type='error' />
      <div>your items are out of stock.</div>
    </div>
  )
}

export default App;
