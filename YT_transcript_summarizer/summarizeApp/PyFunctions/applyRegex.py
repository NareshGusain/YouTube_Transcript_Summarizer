import regex as re

def extract_youtube_id(url):

    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
    
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None

# eg: "https://youtu.be/HXqthPM-aOQ?si=2unkjpR3gQ914gBS" 
# id: --> "HXqthPM-aOQ"

