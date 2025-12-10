import React, { useState } from 'react';
import styles from './Chatbot.module.css';

function Chatbot() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [sourceReferences, setSourceReferences] = useState([]);

  const handleQueryChange = (event) => {
    setQuery(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError('');
    setResponse('');
    setSourceReferences([]); // Clear previous references

    try {
      const res = await fetch('/api/v1/chatbot/query', { // Assuming API is proxied or directly accessible
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // 'Authorization': `Bearer YOUR_AUTH_TOKEN`, // TODO: Add actual auth token
        },
        body: JSON.stringify({ query }),
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data.response);
      setSourceReferences(data.source_references || []);
    } catch (err) {
      setError('Failed to fetch response. Please try again.');
      console.error('Chatbot API error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      <h2 className={styles.chatbotHeader}>RAG Chatbot</h2>
      <form onSubmit={handleSubmit} className={styles.chatForm}>
        <input
          type="text"
          value={query}
          onChange={handleQueryChange}
          placeholder="Ask me about the book content..."
          className={styles.queryInput}
          disabled={loading}
        />
        <button type="submit" className={styles.submitButton} disabled={loading}>
          {loading ? 'Sending...' : 'Ask'}
        </button>
      </form>
      {error && <p className={styles.errorMessage}>{error}</p>}
      {response && (
        <div className={styles.responseContainer}>
          <h3>Response:</h3>
          <p>{response}</p>
          {sourceReferences.length > 0 && (
            <div className={styles.sourceReferences}>
              <h4>Source References:</h4>
              <ul>
                {sourceReferences.map((ref, index) => (
                  <li key={index}>{ref}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default Chatbot;
