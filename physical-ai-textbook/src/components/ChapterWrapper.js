import React from 'react';
import PersonalizationButton from './PersonalizationButton';
import TranslationButton from './TranslationButton';

function ChapterWrapper({ children, chapterId, originalContent }) {
  return (
    <div>
      {/* This button will appear at the top of each chapter that uses this wrapper */}
      <PersonalizationButton chapterId={chapterId} originalContent={originalContent} />
      <TranslationButton chapterId={chapterId} originalContent={originalContent} />
      
      {/* Render the actual chapter content */}
      {children}

      {/* Optionally, you could add another button at the bottom */}
      {/* <PersonalizationButton chapterId={chapterId} originalContent={originalContent} /> */}
    </div>
  );
}

export default ChapterWrapper;
