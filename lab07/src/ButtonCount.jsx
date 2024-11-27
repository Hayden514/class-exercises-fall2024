import React, { useState } from 'react';

export default function ButtonCount() {
  const [count, setCount] = useState(0);

  function addOne() {
    setCount(count + 1);
  }

  function resetCounter() {
    setCount(0);
  }

  return (
    <div>
      <button onClick={addOne}>You have clicked {count} times</button>
      <button onClick={resetCounter}>Reset</button>
    </div>
  );
}
