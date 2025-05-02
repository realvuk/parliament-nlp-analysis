# Serbian Parliament NLP Analysis

This project uses **Natural Language Processing (NLP)** to analyze speeches from the Serbian Parliament, exploring speaker behavior, linguistic trends, and patterns of sentiment, verbosity, and topics over time.

> **Goal:** Understand how Serbian parliamentary discourse is structured and what it reveals about communication patterns, sentiment, and focus areas in the legislature.

---

## Project Structure
parliament-nlp-analysis/  
├── data/  
│ ├── speeches.json # Parsed speech data  
│ └── stopwords_serbian.txt # Custom Serbian stopwords  
├── notebooks/  
│ └── 01_exploratory_analysis.ipynb  
├── scripts/  
│ └── parser.py # Script to extract data from .txt/.docx files  
├── cleaned_speeches.csv # Final output (optional)  
└── README.md
___
## Features

### Preprocessing
- **Lemmatization** and tokenization using `Stanza` (Serbian model)
- Custom **Serbian stopwords** for noise reduction
- Filtering of tokens shorter than 4 characters

### Basic Stats
- Speech length distribution
- Most active speakers
- Word frequency & word cloud

### Topic Modeling
- Applied **LDA** (Latent Dirichlet Allocation) using Gensim
- Extracted 5 dominant topics with top 15 keywords each

| Topic # | Interpretation |
|---------|----------------|
| 0       | General Discourse / Filler Words |
| 1       | Conversational Rhetoric |
| 2       | Economy and Industry |
| 3       | National Policy and Legal Framework |
| 4       | Legislative Procedures and Voting |

### Sentiment Analysis
- Simple sentiment score (positive - negative word count)
- Custom lexicons for Serbian
- Sentiment score distribution plotted

---

## Sample Visuals

-  **Word Cloud** of most common terms (after cleaning)
-  **Speech Length Distribution**
-  **Sentiment Score Distribution**
-  **Topic Breakdown** using top tokens

> Tip: Expand this with time-series, party-level summaries, or named entity recognition.

---

## Dependencies

- Python 3.10+
- `pandas`, `matplotlib`, `wordcloud`, `gensim`, `stanza`

```bash
pip install -r requirements.txt
python -m stanza.download sr
```
## How to Run

1. Add raw transcripts to `data/raw/docs/`
    
2. Run the parser (or use pre-parsed `speeches.json`)
    
3. Open and run `notebooks/01_exploratory_analysis.ipynb`
    

---

## Next Steps (Ideas)

- Add **NER (Named Entity Recognition)** using spaCy or regex
    
- Improve **sentiment** with a larger lexicon or pretrained classifier
    
- Create **party-level** summaries using metadata
    
- Visualize **topic/sentiment trends over time**
    

---

## License

MIT License

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
