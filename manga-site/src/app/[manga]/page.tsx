import react from 'react';
import data from '../../../../Manga Crawler/MangaReader/MangaReader/manga.json'

export default function manga() {
    return (
        <div>
          <h1>manga page</h1>
          <h3> {data[0]['manga-ny991307'].Title} </h3>
          <h3> Chapter: {data[0]['manga-ny991307'].Chapter} </h3>
          {data[0]['manga-ny991307'].Images.map((image, index) => (
            <img width="400px" height="50%" key={index} src={image} alt={`manga image ${index}`} />
          ))}
        </div>
    );
  }
  