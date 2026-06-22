import whisper


class AudioProcessor:

    model = whisper.load_model("base")

    @staticmethod
    def extract_text(audio_path):

        try:
            result = AudioProcessor.model.transcribe(audio_path)

            return result["text"]

        except Exception as e:
            print("Error:", e)
            return ""