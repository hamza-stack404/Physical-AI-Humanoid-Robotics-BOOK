import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/your-repo-name/__docusaurus/debug',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug', '663'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/config',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/config', '6b6'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/content',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/content', '71f'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/globalData',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/globalData', '01c'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/metadata',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/metadata', '83f'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/registry',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/registry', '122'),
    exact: true
  },
  {
    path: '/your-repo-name/__docusaurus/debug/routes',
    component: ComponentCreator('/your-repo-name/__docusaurus/debug/routes', '9c2'),
    exact: true
  },
  {
    path: '/your-repo-name/docs',
    component: ComponentCreator('/your-repo-name/docs', '7fb'),
    routes: [
      {
        path: '/your-repo-name/docs',
        component: ComponentCreator('/your-repo-name/docs', '756'),
        routes: [
          {
            path: '/your-repo-name/docs',
            component: ComponentCreator('/your-repo-name/docs', '4dd'),
            routes: [
              {
                path: '/your-repo-name/docs/Abstract',
                component: ComponentCreator('/your-repo-name/docs/Abstract', '6bf'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/AI Control',
                component: ComponentCreator('/your-repo-name/docs/AI Control', 'b74'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/AI for Embodied Intelligence',
                component: ComponentCreator('/your-repo-name/docs/AI for Embodied Intelligence', '32d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/APA References',
                component: ComponentCreator('/your-repo-name/docs/APA References', '8ed'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Case Studies',
                component: ComponentCreator('/your-repo-name/docs/Case Studies', '5e2'),
                exact: true
              },
              {
                path: '/your-repo-name/docs/Challenges',
                component: ComponentCreator('/your-repo-name/docs/Challenges', '598'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Conclusion',
                component: ComponentCreator('/your-repo-name/docs/Conclusion', '3ff'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Control Systems',
                component: ComponentCreator('/your-repo-name/docs/Control Systems', '7dc'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Embodiment',
                component: ComponentCreator('/your-repo-name/docs/Embodiment', 'db4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Foundations of Robotics',
                component: ComponentCreator('/your-repo-name/docs/Foundations of Robotics', '0c6'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Future',
                component: ComponentCreator('/your-repo-name/docs/Future', '638'),
                exact: true
              },
              {
                path: '/your-repo-name/docs/Future of Physical AI & Case Studies',
                component: ComponentCreator('/your-repo-name/docs/Future of Physical AI & Case Studies', 'b46'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Human-Robot Interaction',
                component: ComponentCreator('/your-repo-name/docs/Human-Robot Interaction', '807'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Humanoid Architecture',
                component: ComponentCreator('/your-repo-name/docs/Humanoid Architecture', '811'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Humanoid Kinematics & Dynamics',
                component: ComponentCreator('/your-repo-name/docs/Humanoid Kinematics & Dynamics', '4b0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Intro',
                component: ComponentCreator('/your-repo-name/docs/Intro', 'aae'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Perception Systems (Vision, Audio, Tactile)',
                component: ComponentCreator('/your-repo-name/docs/Perception Systems (Vision, Audio, Tactile)', '5aa'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Physical AI',
                component: ComponentCreator('/your-repo-name/docs/Physical AI', '997'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Robot Locomotion Mechanics',
                component: ComponentCreator('/your-repo-name/docs/Robot Locomotion Mechanics', 'c2e'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/your-repo-name/docs/Sensors & Actuators',
                component: ComponentCreator('/your-repo-name/docs/Sensors & Actuators', 'f61'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/your-repo-name/',
    component: ComponentCreator('/your-repo-name/', '8ba'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
