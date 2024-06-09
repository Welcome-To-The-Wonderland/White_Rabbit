import { createContext } from 'react';

interface ContextProps {
  id: string;
  setId: React.Dispatch<React.SetStateAction<string>>;
}

export const MangaContext = createContext<ContextProps | undefined>(undefined);