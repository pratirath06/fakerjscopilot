def load_faker_book_docs():
    docs = {
        "book": {
            "author": {
                "description": "Returns a random author name from a list of famous authors",
                "patterns": [
                    "author", "book author", "writer",
                    "generate author"
                ],
                "examples": [
                    "faker.book.author() // 'William Shakespeare'"
                ],
                "notes": "Returns existing author names. For fictional authors, use faker.person.fullName()"
            },
            "format": {
                "description": "Returns a random book format",
                "patterns": [
                    "book format", "publication format",
                    "format type", "binding type",
                    "generate book format"
                ],
                "examples": [
                    "faker.book.format() // 'Hardcover'"
                ],
                "notes": "Returns common book formats like Hardcover, Paperback, etc."
            },
            "genre": {
                "description": "Returns a random book genre",
                "patterns": [
                    "genre", "book genre", "literary genre",
                    "book category", "generate genre"
                ],
                "examples": [
                    "faker.book.genre() // 'Fantasy'"
                ],
                "notes": "Returns common literary genres like Fantasy, Mystery, Romance, etc."
            },
            "publisher": {
                "description": "Returns a random book publisher",
                "patterns": [
                    "publisher", "publishing house",
                    "book publisher", "generate publisher"
                ],
                "examples": [
                    "faker.book.publisher() // 'Addison-Wesley'"
                ],
                "notes": "Returns names of well-known publishing companies"
            },
            "series": {
                "description": "Returns a random book series name",
                "patterns": [
                    "series", "book series",
                    "novel series", "generate series"
                ],
                "examples": [
                    "faker.book.series() // 'Harry Potter'"
                ],
                "notes": "Returns names of popular book series"
            },
            "title": {
                "description": "Returns a random book title",
                "patterns": [
                    "title", "book title",
                    "book name", "generate title"
                ],
                "examples": [
                    "faker.book.title() // 'Romeo and Juliet'"
                ],
                "notes": "Returns titles of well-known books"
            }
        }
    }

    # Add related methods from other modules
    docs["related_methods"] = {
        "isbn": {
            "description": "Generate an ISBN (International Standard Book Number)",
            "module": "commerce",
            "usage": "faker.commerce.isbn()",
            "note": "Use this method to generate valid ISBN numbers for books"
        },
        "fictional_author": {
            "description": "Generate a fictional author name",
            "module": "person",
            "usage": "faker.person.fullName()",
            "note": "Use this method when you need a non-existing author name"
        }
    }

    return docs