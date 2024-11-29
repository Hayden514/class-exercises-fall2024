import React from 'react';
import { Carousel } from 'antd';

const CarouselComponent = ({ tracks }) => {
  if (tracks.length === 0) {
    return (
      <p style={{ textAlign: 'center' }}>No tracks to display. Search above!</p>
    );
  }

  return (
    <Carousel autoplay dotPosition="bottom">
      {tracks.map((track) => (
        <div key={track.id} style={{ textAlign: 'center' }}>
          <iframe
            src={`https://open.spotify.com/embed/track/${track.id}?utm_source=generator`}
            width="100%"
            height="352"
            frameBorder="0"
            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
            loading="lazy"
            style={{ borderRadius: '8px' }}
          ></iframe>
        </div>
      ))}
    </Carousel>
  );
};

export default CarouselComponent;
