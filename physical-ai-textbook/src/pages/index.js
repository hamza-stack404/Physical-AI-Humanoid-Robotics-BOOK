import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';
import Chatbot from '../components/Chatbot';

function HomepageHeader() {
  return (
    <header className={styles.heroBanner}>
      <div className="container">
        <h1 className="hero__title">Physical AI & Humanoid Robotics</h1>
        <p className="hero__subtitle">An open-source textbook for the next generation of AI.</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/Intro">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title={`Hello from Docusaurus`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <Chatbot />
        {/* You can add more sections here. */}
      </main>
    </Layout>
  );
}