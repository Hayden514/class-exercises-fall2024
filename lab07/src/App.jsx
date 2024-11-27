import React from 'react';
import Profile from './Profile.jsx';
import ButtonCount from './ButtonCount.jsx';

export default function App() {
  // Define the array of people
  const people = [
    { name: 'Anita', image_url: 'https://picsum.photos/id/216/100/100' },
    { name: 'Ben', image_url: 'https://picsum.photos/id/217/100/100' },
    { name: 'Adwaina', image_url: 'https://picsum.photos/id/218/100/100' },
    { name: 'Laciesha', image_url: 'https://picsum.photos/id/219/100/100' },
  ];

  // JSX to render the page
  return (
    <>
      <header>
        <h1>My First App</h1>
      </header>
      <main>
        <p>Hello React!</p>

        {/* Dynamically render Profile components */}
        {people.map((person) => (
          <Profile
            key={person.name}
            name={person.name}
            picture={person.image_url}
          />
        ))}

        {/* Add multiple ButtonCount components */}
        <ButtonCount />
        <ButtonCount />
        <ButtonCount />
        <ButtonCount />
      </main>
    </>
  );
}
