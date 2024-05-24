import React, { useState } from 'react';
import './App.css';

function App() {
    const [expression, setExpression] = useState('');
    const [result, setResult] = useState('');

    const handleInputChange = (event) => {
        setExpression(event.target.value);
    };

    const handleCalculate = async () => {
        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ expression })
            });
            const data = await response.json();
            setResult(data.result || data.error);
        } catch (error) {
            setResult('Error: ' + error.message);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Calculator</h1>
                <input
                    type="text"
                    value={expression}
                    onChange={handleInputChange}
                    placeholder="Type an expression"
                />
                <button onClick={handleCalculate}>Calculate</button>
                <h2>Result: {result}</h2>
            </header>
        </div>
    );
}

export default App;
