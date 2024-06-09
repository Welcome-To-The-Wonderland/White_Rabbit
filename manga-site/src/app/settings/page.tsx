import { useRouter } from 'next/router'
import React from 'react'

export default function Home() {
  const router = useRouter()

  const navigateToManga = (id) => {
    router.push(`/manga/${id}`)
  }

  return (
    <div>
      
    </div>
  )
}