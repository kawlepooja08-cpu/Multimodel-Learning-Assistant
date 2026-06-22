import re

class TextCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Text ko clean karta hai: extra spaces hatata hai, 
        newlines ko normalize karta hai aur text ko trim karta hai.
        """
        if not text:
            return ""
        
        # Multiple spaces aur tabs ko single space se replace karein
        text = re.sub(r'[ \t]+', ' ', text)
        
        # Do se zyada consecutive newlines ko double newline se replace karein (paragraphs manage karne ke liye)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        # Text ke aage aur peeche ke blank spaces ko remove karein
        return text.strip()