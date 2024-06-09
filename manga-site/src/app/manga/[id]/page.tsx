import React from "react";
interface MangaProps {
    id: string;
} 

export default function Manga({ id }: MangaProps) {

  return (
    <div>
      <h1>Manga info</h1>
      <h1> {id} </h1>
    </div>
  )
}