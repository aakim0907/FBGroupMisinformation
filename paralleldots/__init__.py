__all__= [ "config", "get_usage", "taxonomy", "ner", "similarity", "sentiment", "keywords", "emotion", "intent", "abuse", "custom_classifier", "phrase_extractor", "text_parser", "multilang_keywords", "nsfw", "popularity" ]

from paralleldots.similarity          import get_similarity          as similarity
from paralleldots.keywords            import get_keywords            as keywords
from paralleldots.phrase_extractor    import get_phrase_extractor    as phrase_extractor

from paralleldots.usage               import get_usage               as usage

from paralleldots.config              import set_api_key
from paralleldots.config              import get_api_key