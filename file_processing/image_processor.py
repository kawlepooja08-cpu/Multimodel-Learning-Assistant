import easyocr


class ImageProcessor:

    @staticmethod
    def extract_text(image_path):
        """
        Extract text from image
        """

        try:
            reader = easyocr.Reader(['en'])

            result = reader.readtext(image_path)

            text = ""

            for item in result:
                text += item[1] + "\n"

            return text

        except Exception as e:
            print(f"Error: {e}")
            return ""