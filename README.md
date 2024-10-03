# Python Simple Search Engine (PSSE)

PSSE is a simple light-weight search engine built in Python based on [Okapi BM25](https://en.wikipedia.org/wiki/Okapi_BM25) as the ranking function and an inverted index data structure to map keywords to documents.

## Installation

You can install it using `pip`.

```bash
pip install psse
```

## Usage

```python
# Search engine quick example

from psse.searchengine import SearchEngine

# Simple test documents dictionary. The documents could be scrapped or gathered in any datastructure you feel comfortable with.
test_docs = {
    "www.mayaangelou.com": "When I look back, I am so impressed again with the life-giving power of literature. If I were a young person today, trying to gain a sense of myself in the world, I would do that again by reading, just as I did when I was young.",
    "www.jhonwalters.com": "It wasn't until I started reading and found books they wouldn't let us read in school that I discovered you could be insane and happy and have a good life without being like everybody else.",
    "www.eudora.co": "Both reading and writing are experiences – lifelong – in the course of which we who encounter words used in certain ways are persuaded by them to be brought mind and heart within the presence, the power, of the imagination",
    "www.test.com": "A reader lives a thousand lives before he dies... The man who never reads lives only one",
}
documents_tuple_list = [
    (url, test_docs[url]) for url in test_docs
]  # SearchEngine indexing works with tuples like (url,content), that's why this conversion was necessary.

engine = SearchEngine()  # Create our Search Engine instance
engine.bulk_index(documents=documents_tuple_list)  # Indexing documents.
results = engine.search("reading books")  # Perform our query to our search engine.
print(
    results
)  # {'www.mayaangelou.com': 0.3200279965979123, 'www.jhonwalters.com': 1.5331273738104372, 'www.eudora.co': 0.32435134685528605}

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## TODO's
- Include diferent ranking functions.
- Include adapters for different Cloud providers.
- Launch PSSE as a Python Package.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact
For any type of contact please email me at sebastiang1493@gmail.com