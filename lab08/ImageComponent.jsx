import React from 'react';
import { Image } from 'antd';

const ImageComponent = ({ src, alt, width = 200, style }) => {
  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      style={{ margin: '10px', ...style }}
    />
  );
};

export default ImageComponent;
