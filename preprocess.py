import spacy
from keybert import KeyBERT

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

def analyze_text(text):
    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        top_n=5
    )

    return {
        "clean_text": text,
        "entities": entities,
        "keywords": [k[0] for k in keywords]
    }