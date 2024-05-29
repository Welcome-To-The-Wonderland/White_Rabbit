import data from '../manga.json'
import React from 'react'
import Link from 'next/link'

export default function Home() {
  return (
    <div>
      <h1>Look at me</h1>
      {data.map((manga, index) => (
        <Link href={`/manga/${manga}`} key={index}>
          <a>
            <img src={manga.cover} alt="manga_image" />
          </a>
        </Link>
      ))}
    </div>
  )
}