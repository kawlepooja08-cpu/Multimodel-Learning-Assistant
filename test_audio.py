import os
import sys

# Enable UTF-8 for emoji support
sys.stdout.reconfigure(encoding="utf-8")

from file_processing.audio_processor import AudioProcessor

audio_file = "sample.mp3"

print("🎵 Checking Audio File...")

print("✅ File Exists:", os.path.exists(audio_file))

if os.path.exists(audio_file):

    print("📄 File Size:", os.path.getsize(audio_file), "bytes")

    print("\n🎙️ Converting Audio to Text...\n")

    text = AudioProcessor.extract_text(audio_file)

    print("📝 ===== TRANSCRIBED TEXT =====\n")
    print(text)

    print("\n🔤 Extracted Characters:", len(text))

    print("\n✅ Audio Processing Successful 🚀")

else:
    print("❌ Audio File Not Found!")