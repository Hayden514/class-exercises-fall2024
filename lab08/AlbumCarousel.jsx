import React from 'react';
import { Carousel } from 'antd';

const albums = [
  {
    id: '6BzxX6zkDsYKFJ04ziU5xQ',
    name: 'COWBOY CARTER',
    image_url:
      'https://i.scdn.co/image/ab67616d0000b2731572698fff8a1db257a53599',
    spotify_url: 'https://open.spotify.com/album/6BzxX6zkDsYKFJ04ziU5xQ',
  },
  // 更多专辑数据...
];

const AlbumCarousel = () => {
  return (
    <Carousel autoplay dotPosition="top">
      {albums.map((album) => (
        <div key={album.id} style={{ textAlign: 'center' }}>
          <img
            src={album.image_url}
            alt={album.name}
            style={{ maxWidth: '100%', borderRadius: '8px' }}
          />
          <h3>{album.name}</h3>
        </div>
      ))}
    </Carousel>
  );
};

export default AlbumCarousel;
