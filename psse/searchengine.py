from collections import defaultdict
from math import log
from psse.helpers import normalize_string, url_scores_update


class SearchEngine:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self._index: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self._documents: dict[str, str] = {}
        self._avgdl: float = 0.0
        self.k1 = k1
        self.b = b

    @property
    def posts(self) -> list[str]:
        return list(self._documents.keys())

    @property
    def number_of_documents(self) -> int:
        return len(self._documents)

    @property
    def avgdl(self) -> float:
        """Average Document Length - avdl"""
        if self._avgdl == 0.0:
            # Needs to be computed once.
            self._avgdl = sum(len(d) for d in self._documents.values()) / len(
                self._documents
            )
        return self._avgdl

    def index(self, url: str, content: str) -> None:
        """Method which receives an -url- and its -content- and adds it to the set of documents while normalizing
        its words into the inverted index dictionary.
        """
        self._documents[url] = content
        words = normalize_string(content).split(" ")
        for word in words:
            self._index[word][url] += 1

    def bulk_index(self, documents: list[tuple[str, str]]):
        """Method which implements index() over a list of (url,content) tuples."""
        for url, content in documents:
            self.index(url, content)

    def idf(self, kw: str) -> float:
        """Method which calculates the inverse document frequency, calculating the importance of a word -kw- within a document."""
        N: int = self.number_of_documents
        n_kw: int = len(self.get_urls(kw))
        return log((N - n_kw + 0.5) / (n_kw + 0.5) + 1)

    def rank(self, kw: str) -> dict[str, float]:
        """Method which ranks the results based on the keyword -kw- focusing on the query terms regardless of the proximity of the content results. This ranking function is based on Okapi BM25"""
        result: dict[str, float] = {}
        idf_score: float = self.idf(kw)
        avgdl: float = self.avgdl
        for url, freq in self.get_urls(kw).items():
            numerator = freq * (self.k1 + 1)
            denominator = freq + self.k1 * (
                1 - self.b + self.b * len(self._documents[url]) / avgdl
            )
            result[url] = idf_score * numerator / denominator
        return result

    def search(self, query: str) -> dict[str, float]:
        """Method which performs a search using -query- to the search engine."""
        keywords: list[str] = normalize_string(query).split(" ")
        url_scores: dict[str, float] = {}
        for kw in keywords:
            kw_urls_score = self.rank(kw)
            url_scores = url_scores_update(url_scores, kw_urls_score)
        return url_scores

    def get_urls(self, keyword: str) -> dict[str, int]:
        """Method which retrieves -urls- based on the provided -keyword-."""
        normalized_keyword: str = normalize_string(keyword)
        return self._index[normalized_keyword]
