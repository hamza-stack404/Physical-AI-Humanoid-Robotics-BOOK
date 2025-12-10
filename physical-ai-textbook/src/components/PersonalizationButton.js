import React, { useState } from 'react';
import styles from './PersonalizationButton.module.css'; // Assuming you'll create this CSS module

function PersonalizationButton({ chapterId, originalContent }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [personalizedContent, setPersonalizedContent] = useState(null);

  const handlePersonalize = async () => {
    setLoading(true);
    setError('');
    setPersonalizedContent(null);

    try {
      const response = await fetch('/api/v1/content/personalize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          // TODO: Add Authorization header with user's JWT token
        },
        body: JSON.stringify({
          chapterId: chapterId,
          originalContent: originalContent,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setPersonalizedContent(data.personalized_content);
    } catch (err) {
      console.error('Personalization API error:', err);
      setError('Failed to personalize content. Please ensure you are logged in.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.personalizationContainer}>
      <button
        className={styles.personalizeButton}
        onClick={handlePersonalize}
        disabled={loading}
      >
        {loading ? 'Personalizing...' : 'Personalize Chapter'}
      </button>
      {error && <p className={styles.errorMessage}>{error}</p>}
      {personalizedContent && (
        <div className={styles.personalizedContentPreview}>
          <h4>Personalized Content Preview:</h4>
          <div dangerouslySetInnerHTML={{ __html: personalizedContent }} />
          {/* In a real app, you'd likely integrate this into the main content display */}
        </div>
      )}
    </div>
  );
}

export default PersonalizationButton;
