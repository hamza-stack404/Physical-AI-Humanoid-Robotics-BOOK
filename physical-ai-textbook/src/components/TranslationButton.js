import React, { useState } from 'react';
import styles from './TranslationButton.module.css'; // Assuming you'll create this CSS module

function TranslationButton({ chapterId, originalContent, targetLanguage = 'ur' }) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [translatedContent, setTranslatedContent] = useState(null);

  const handleTranslate = async () => {
    setLoading(true);
    setError('');
    setTranslatedContent(null);

    try {
      const response = await fetch('/api/v1/content/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          chapterId: chapterId,
          originalContent: originalContent,
          targetLanguage: targetLanguage,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setTranslatedContent(data.translated_content);
    } catch (err) {
      console.error('Translation API error:', err);
      setError(`Failed to translate content to ${targetLanguage}.`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.translationContainer}>
      <button
        className={styles.translateButton}
        onClick={handleTranslate}
        disabled={loading}
      >
        {loading ? 'Translating...' : `Translate to ${targetLanguage.toUpperCase()}`}
      </button>
      {error && <p className={styles.errorMessage}>{error}</p>}
      {translatedContent && (
        <div className={styles.translatedContentPreview}>
          <h4>Translated Content Preview ({targetLanguage.toUpperCase()}):</h4>
          <div dangerouslySetInnerHTML={{ __html: translatedContent }} />
          {/* In a real app, you'd likely integrate this into the main content display */}
        </div>
      )}
    </div>
  );
}

export default TranslationButton;
