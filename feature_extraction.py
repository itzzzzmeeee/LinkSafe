def basic_features(url):
    """
    Extract simple lexical features from a URL
    """
    return {
        "url_length": len(url),
        "num_dots": url.count("."),
        "has_at": 1 if "@" in url else 0,
        "has_hyphen": 1 if "-" in url else 0,
        "has_https": 1 if url.startswith("https") else 0
    }
