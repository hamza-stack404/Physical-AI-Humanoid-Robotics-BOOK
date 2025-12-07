import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/__docusaurus/debug',
    component: ComponentCreator('/__docusaurus/debug', '5ff'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/config',
    component: ComponentCreator('/__docusaurus/debug/config', '5ba'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/content',
    component: ComponentCreator('/__docusaurus/debug/content', 'a2b'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/globalData',
    component: ComponentCreator('/__docusaurus/debug/globalData', 'c3c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/metadata',
    component: ComponentCreator('/__docusaurus/debug/metadata', '156'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/registry',
    component: ComponentCreator('/__docusaurus/debug/registry', '88c'),
    exact: true
  },
  {
    path: '/__docusaurus/debug/routes',
    component: ComponentCreator('/__docusaurus/debug/routes', '000'),
    exact: true
  },
  {
    path: '/docs',
    component: ComponentCreator('/docs', '9f1'),
    routes: [
      {
        path: '/docs',
        component: ComponentCreator('/docs', '721'),
        routes: [
          {
            path: '/docs',
            component: ComponentCreator('/docs', '327'),
            routes: [
              {
                path: '/docs/Abstract',
                component: ComponentCreator('/docs/Abstract', '363'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/AI Control',
                component: ComponentCreator('/docs/AI Control', 'a5f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/AI for Embodied Intelligence',
                component: ComponentCreator('/docs/AI for Embodied Intelligence', '432'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/APA References',
                component: ComponentCreator('/docs/APA References', '3ee'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Case Studies',
                component: ComponentCreator('/docs/Case Studies', '851'),
                exact: true
              },
              {
                path: '/docs/Challenges',
                component: ComponentCreator('/docs/Challenges', 'd5d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Conclusion',
                component: ComponentCreator('/docs/Conclusion', '0c4'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Control Systems',
                component: ComponentCreator('/docs/Control Systems', '4d8'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Embodiment',
                component: ComponentCreator('/docs/Embodiment', 'bcb'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Foundations of Robotics',
                component: ComponentCreator('/docs/Foundations of Robotics', 'c62'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Future',
                component: ComponentCreator('/docs/Future', 'd02'),
                exact: true
              },
              {
                path: '/docs/Future of Physical AI & Case Studies',
                component: ComponentCreator('/docs/Future of Physical AI & Case Studies', '9bd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Human-Robot Interaction',
                component: ComponentCreator('/docs/Human-Robot Interaction', '4fd'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Humanoid Architecture',
                component: ComponentCreator('/docs/Humanoid Architecture', '46b'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Humanoid Kinematics & Dynamics',
                component: ComponentCreator('/docs/Humanoid Kinematics & Dynamics', '9c3'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Intro',
                component: ComponentCreator('/docs/Intro', '586'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Perception Systems (Vision, Audio, Tactile)',
                component: ComponentCreator('/docs/Perception Systems (Vision, Audio, Tactile)', '132'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Physical AI',
                component: ComponentCreator('/docs/Physical AI', '911'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Robot Locomotion Mechanics',
                component: ComponentCreator('/docs/Robot Locomotion Mechanics', '020'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/docs/Sensors & Actuators',
                component: ComponentCreator('/docs/Sensors & Actuators', '35e'),
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
    path: '/',
    component: ComponentCreator('/', '2e1'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
