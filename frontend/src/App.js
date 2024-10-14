import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [form, setForm] = useState({ sender: '', recipient: '', amount: '' });
  const [message, setMessage] = useState('');
  const [chain, setChain] = useState([]);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/transaction', form);
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Error submitting transaction');
    }
  };

  // Fetch Blockchain
  const fetchChain = async () => {
    const response = await axios.get('http://localhost:5000/chain');
    setChain(response.data.chain);
  };

  return (
    <div className="App">
      <h1>Crypto Bank</h1>

      <form onSubmit={handleSubmit}>
        <label>Sender:</label>
        <input
          type="text"
          value={form.sender}
          onChange={(e) => setForm({ ...form, sender: e.target.value })}
          required
        />

        <label>Recipient:</label>
        <input
          type="text"
          value={form.recipient}
          onChange={(e) => setForm({ ...form, recipient: e.target.value })}
          required
        />

        <label>Amount:</label>
        <input
          type="number"
          value={form.amount}
          onChange={(e) => setForm({ ...form, amount: e.target.value })}
          required
        />

        <button type="submit">Send Transaction</button>
      </form>

      {message && <p>{message}</p>}

      <button onClick={fetchChain}>Get Blockchain</button>
      {chain.length > 0 && (
        <div>
          <h2>Blockchain:</h2>
          <pre>{JSON.stringify(chain, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
