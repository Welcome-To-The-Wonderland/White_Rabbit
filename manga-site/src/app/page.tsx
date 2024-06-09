'use client'
import data from '../manga.json';
import './home.css'
import Link from 'next/link'

export default function Home() {
  let x = "random string order";
  let y = "string from home"

  const [id, setId] = useState('');
  return (
    <div>
      <h1>Look at me</h1>
      <Link href = {{
        pathname: `/manga/${x}`,
        query: {id: y},
      }}> some link
      </Link>
    </div>
  )
}