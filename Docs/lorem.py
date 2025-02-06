def load_faker_lorem_docs():
    docs = {
        "lorem": {
            "basic_elements": {
                "word": {
                    "description": "Generates a single word with specified length",
                    "patterns": [
                        "single word", "lorem word",
                        "generate word"
                    ],
                    "examples": [
                        "faker.lorem.word() // 'temporibus'",
                        "faker.lorem.word(5) // 'velit'",
                        "faker.lorem.word({ length: { min: 5, max: 7 }, strategy: 'fail' })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } - Expected word length",
                        "strategy": "optional - 'fail'|'shortest'|'closest'|'longest'|'any-length' (default: 'any-length')"
                    }
                },
                "words": {
                    "description": "Generates multiple space-separated words",
                    "patterns": [
                        "multiple words", "word list",
                        "generate words"
                    ],
                    "examples": [
                        "faker.lorem.words() // 'qui praesentium pariatur'",
                        "faker.lorem.words(10)",
                        "faker.lorem.words({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "wordCount": "optional - number | { min, max } (default: 3)"
                    }
                }
            },
            "sentences": {
                "sentence": {
                    "description": "Generates single sentence with capital letter and period",
                    "patterns": [
                        "single sentence", "lorem sentence",
                        "generate sentence"
                    ],
                    "examples": [
                        "faker.lorem.sentence() // 'Voluptatum cupiditate suscipit autem.'",
                        "faker.lorem.sentence(5)",
                        "faker.lorem.sentence({ min: 3, max: 5 })"
                    ],
                    "parameters": {
                        "wordCount": "optional - number | { min: 3, max: 10 } - Words per sentence"
                    }
                },
                "sentences": {
                    "description": "Generates multiple sentences with separator",
                    "patterns": [
                        "multiple sentences", "sentence list",
                        "generate sentences"
                    ],
                    "examples": [
                        "faker.lorem.sentences()",
                        "faker.lorem.sentences(2)",
                        "faker.lorem.sentences(2, '\\n')",
                        "faker.lorem.sentences({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "sentenceCount": "optional - number | { min: 2, max: 6 }",
                        "separator": "optional - string (default: ' ')"
                    }
                }
            },
            "paragraphs": {
                "paragraph": {
                    "description": "Generates single paragraph with multiple sentences",
                    "patterns": [
                        "single paragraph", "lorem paragraph",
                        "generate paragraph"
                    ],
                    "examples": [
                        "faker.lorem.paragraph()",
                        "faker.lorem.paragraph(2)",
                        "faker.lorem.paragraph({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "sentenceCount": "optional - number | { min, max } (default: 3)"
                    }
                },
                "paragraphs": {
                    "description": "Generates multiple paragraphs with separator",
                    "patterns": [
                        "multiple paragraphs", "paragraph list",
                        "generate paragraphs"
                    ],
                    "examples": [
                        "faker.lorem.paragraphs()",
                        "faker.lorem.paragraphs(5)",
                        "faker.lorem.paragraphs(2, '<br/>\\n')",
                        "faker.lorem.paragraphs({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "paragraphCount": "optional - number | { min, max } (default: 3)",
                        "separator": "optional - string (default: '\\n')"
                    }
                }
            },
            "other_formats": {
                "lines": {
                    "description": "Generates newline-separated lines of text",
                    "patterns": [
                        "text lines", "line list",
                        "generate lines"
                    ],
                    "examples": [
                        "faker.lorem.lines()",
                        "faker.lorem.lines(2)",
                        "faker.lorem.lines({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "lineCount": "optional - number | { min: 1, max: 5 }"
                    }
                },
                "slug": {
                    "description": "Generates URL-friendly hyphenated text",
                    "patterns": [
                        "url slug", "hyphenated text",
                        "generate slug"
                    ],
                    "examples": [
                        "faker.lorem.slug() // 'dolores-illo-est'",
                        "faker.lorem.slug(5)",
                        "faker.lorem.slug({ min: 1, max: 3 })"
                    ],
                    "parameters": {
                        "wordCount": "optional - number | { min, max } (default: 3)"
                    }
                },
                "text": {
                    "description": "Generates random text using various lorem methods",
                    "patterns": [
                        "random text", "any text",
                        "generate text"
                    ],
                    "examples": [
                        "faker.lorem.text()"
                    ],
                    "notes": "Randomly uses one of: sentence, sentences, paragraph, paragraphs, lines"
                }
            }
        }
    }
    return docs