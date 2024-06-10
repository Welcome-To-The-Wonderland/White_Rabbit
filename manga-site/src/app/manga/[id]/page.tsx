'use client'
import React from "react";
import { usePathname } from 'next/navigation'
import manga from "./../../../manga.json"

interface MangaInfo {
  title : string;
  cover : string;
  chapters : Chapter[];
}

interface MangaData {
  [key: string]: MangaInfo;
}

interface Chapter {
  number: number;
  images: string[];
  uid : string
}

export default function Manga() {
  const manga: MangaData = require("./../../../manga.json");
  const pathname = usePathname();
  let splitPath = pathname.split('/');
  let out = splitPath[splitPath.length - 1];

  // Find the manga that matches the 'out' variable
  const mangaInfo = manga[out];
  
  return (
    <div>
      <h1>Manga info</h1>
      <h1>here: {out}</h1>

      <h1>Title: {mangaInfo.title}</h1>

      {mangaInfo && (
        <div>
          <h2>Chapters</h2>
          <ul>
            {mangaInfo.chapters.map((chapter, index) => (
              <li key={index}> 
                <p>{chapter.number}</p>
                <p>{chapter.uid}</p>
                
                {chapter.images.map((image, index) => (
                  <img height="100px" width= "80px" key={index} src={image} alt={`Chapter image ${index + 1}`} />
                ))}

              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}