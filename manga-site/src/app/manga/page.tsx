import React from 'react';
import data from '../../manga.json'

export default function Chapters(props) {
  const id = props.id;
  return (
    <div>
      <h1>chapters page</h1>
      <h1> {id} </h1>
    </div>
  );
}