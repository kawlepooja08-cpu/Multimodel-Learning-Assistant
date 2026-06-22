class TextChunker:
    @staticmethod
    def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list:
        """
        Text ko chhote chunks mein divide karta hai.
        
        :param text: Clean kiya hua string text.
        :param chunk_size: Ek chunk mein maximum kitne characters hone chahiye.
        :param chunk_overlap: Do chunks ke beech mein kitne characters common (overlap) hone chahiye.
        :return: Chunks ki ek list.
        """
        if not text:
            return []
            
        chunks = []
        words = text.split()
        current_chunk = []
        current_length = 0
        
        for word in words:
            # Word ki length + space ki length add karein
            word_len = len(word) + 1 
            
            if current_length + word_len <= chunk_size:
                current_chunk.append(word)
                current_length += word_len
            else:
                # Naya chunk save karein
                chunks.append(" ".join(current_chunk))
                
                # Overlap create karne ke liye pichle chunk ke kuch words retain karein
                # (Simple approach: pichle chunk ke aakhri 3-4 words naye chunk mein le aana)
                overlap_words = current_chunk[-max(1, int(chunk_overlap/10)):] if current_chunk else []
                current_chunk = overlap_words + [word]
                current_length = sum(len(w) + 1 for w in current_chunk)
                
        # Aakhri bacha hua chunk add karein
        if current_chunk:
            chunks.append(" ".join(current_chunk))
            
        return chunks