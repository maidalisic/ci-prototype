import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputs, setInputs] = useState({ a: 0, b: 0 });
  const [result, setResult] = useState(null);

  const handleChange = (event) => {
    setInputs({ ...inputs, [event.target.name]: parseInt(event.target.value, 10) });
  };

  const handleAdd = async () => {
    const response = await fetch('/api/add', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(inputs)
    });
    const data = await response.json();
    setResult(data.result);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Add Two Numbers</h1>
        <input type="number" name="a" value={inputs.a} onChange={handleChange} />
        <input type="number" name="b" value={inputs.b} onChange={handleChange} />
        <button onClick={handleAdd}>Add</button>
        <h2>Result: {result}</h2>
      </header>
    </div>
  );
}

export default App;
