import React, { useState } from 'react';
import FormComponent from './FormComponent';
import CarouselComponent from './CarouselComponent';

const App = () => {
  const [tracks, setTracks] = useState([]);

  const fetchTracks = async ({ searchTerm, limit }) => {
    const url = `https://www.apitutor.org/spotify/simple/v1/search?q=${searchTerm}&type=track&limit=${limit}`;
    const response = await fetch(url);
    const data = await response.json();
    setTracks(data);
  };

  return (
    <div style={{ width: '640px', margin: 'auto', padding: '20px' }}>
      <h1>Spotify Search App</h1>
      <FormComponent onSearch={fetchTracks} />
      <CarouselComponent tracks={tracks} />
    </div>
  );
};

export default App;
