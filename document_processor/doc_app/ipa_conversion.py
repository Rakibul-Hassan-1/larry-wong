import re

# Dictionary mapping abbreviations to their IPA equivalents
abbreviations_to_ipa = {
    'NASA': 'ˈnæsə',
    'UN': 'juːˈɛn',
    'US': 'jʊˈɛs',
    'WLAN' : 'dAbᵊljuː-LAN',
    'AP' : 'eɪ-pi',
    # Add more abbreviations as needed
}

def replace_abbreviations_with_ipa(text):
    """Replaces recognized abbreviations in the given text with their IPA notations highlighted."""
    pattern = r'\b(' + '|'.join(re.escape(key) for key in abbreviations_to_ipa.keys()) + r')\b'
    # Replace each found abbreviation with its IPA notation wrapped in span tags for highlighting
    return re.sub(pattern, lambda match: f'<span class="highlight">{abbreviations_to_ipa[match.group()]}</span>', text)
