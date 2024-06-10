'use client'
import data from '../manga.json';
import './home.css'
import Link from 'next/link'

export default function Home() {
  let x = "manga-ny991307";

  return (
    <div>
      <h1>Look at me</h1>
      <Link href = {{
        pathname: `/manga/${x}`,
      }}> some link
      </Link>
    </div>
  )
}