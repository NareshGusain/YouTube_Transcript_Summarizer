import regex as re
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def extract_youtube_id(url):
    """Extracts the YouTube video ID from a given URL."""
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def generate_transcript(video_id):
    """Fetches the transcript for a given YouTube video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        no_of_words = sum(len(item['text'].split()) for item in transcript)
        return transcript, no_of_words
    except (TranscriptsDisabled, NoTranscriptFound):
        return None, 0
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None, 0

def clean_transcript(transcript):
    """
    Cleans the transcript list of dicts into a readable string.
    Removes music cues, joins lines, and skips empty/irrelevant text.
    """
    if not transcript:
        return ""
    lines = []
    for item in transcript:
        text = item.get('text', '').strip()
        # Skip music cues or empty lines
        if not text or '[Music]' in text or '[Applause]' in text or '[Laughter]' in text:
            continue
        lines.append(text)
    # Join lines, fix double spaces, etc.
    cleaned = ' '.join(lines)
    cleaned = re.sub(r'\s{2,}', ' ', cleaned)
    return cleaned.strip()

# Example usage:
if __name__ == "__main__":
    url = "https://youtu.be/HXqthPM-aOQ?si=2unkjpR3gQ914gBS"
    video_id = extract_youtube_id(url)
    if video_id:
        transcript, word_count = generate_transcript(video_id)
        readable = clean_transcript(transcript)
        print(f"Transcript ({word_count} words):\n")
        print(readable)
    else:
        print("Invalid YouTube URL.")