'use client'
import data from '../manga.json';
import React, { useState } from 'react';
// import { Link } from 'react-router-dom';
import Link from 'next/link';
import './home.css'

export default function Home() {
  const flattenedData = data.flat();
  let pairs: { id: string; cover: string }[] = [];

  const ids = new Set(); // Create a Set to store the ids

  flattenedData.forEach(item => {
    const parts = item.uid.split('-');
    const id = parts[1];
    const cover = item.cover;

    if (!ids.has(id)) { // If the id is not in the Set
      ids.add(id); // Add the id to the Set
      pairs.push({ id, cover }); // Add the pair to the pairs array
    }
  })

  return (
    <div>
      <h1>Look at me</h1>
  
      {pairs.map((pair, index) => (
        <Link href={`/manga/${pair.id}`} key={index} passHref> 
          <img 
            className="images"
            src={pair.cover} 
            alt={`Cover ${pair.id}`} 
          />
        </Link>
      ))}
    </div>
  )
}