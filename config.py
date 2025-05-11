from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# Data folders
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
EXTERNAL_DIR = DATA_DIR / "external"
METADATA_DIR = DATA_DIR / "metadata"

# Data files
SPEECHES_JSON = INTERIM_DIR / "speeches.json"
LEMMATIZED_JSON = INTERIM_DIR / "lemmatized_speeches.json"
WORD_FREQ_CSV = INTERIM_DIR / "word_frequencies.csv"
SPEECH_LENGTH_CSV = INTERIM_DIR / "speech_lengths.csv"
CLEANED_SPEECHES_CSV = INTERIM_DIR / "cleaned_speeches.csv"

# Resources
STOPWORDS_TXT = METADATA_DIR / "serbian_stopwords.txt"
PARTY_MAP_CSV = METADATA_DIR / "party_map.csv"
SENTIMENT_LATIN_CSV = EXTERNAL_DIR / "serbian_sentiment_latin.csv"

FIGURES_DIR = BASE_DIR / "figures"
