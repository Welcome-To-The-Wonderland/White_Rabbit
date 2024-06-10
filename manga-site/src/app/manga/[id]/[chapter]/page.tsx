'use client'
import React from "react";
import { usePathname } from 'next/navigation'

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
  const manga: MangaData = require("./../../../../manga.json");
  const pathname = usePathname();
  let splitPath = pathname.split('/');
  let id = splitPath[splitPath.length - 1];
  let out = id.split('-')[0] + '-' + id.split('-')[1];

  // Find the manga that matches the 'out' variable
  const mangaInfo = manga[out];

  const uidToFind = id;
  const chapterIndex = mangaInfo.chapters.findIndex(chapter => chapter.uid === uidToFind);
  
  return (
    <div>
      <h1>Chapter Info</h1>
      <h1>manga id: {out}</h1>
      <h1>chapter id: {id}</h1>

      {mangaInfo.chapters.map((chapter, index) => (
        // Only display images from the first chapter
        index === chapterIndex && (
          <div key={index}>
            {chapter.images.map((image, imageIndex) => (
              <img height="100px" width= "80px" key={imageIndex} src={image} alt={`Chapter image ${imageIndex + 1}`} />
            ))}
          </div>
        )
      ))}
    </div>
  )
}