def load_faker_hacker_docs():
    docs = {
        "hacker": {
            "abbreviation": {
                "description": "Returns a random hacker/IT abbreviation",
                "patterns": [
                    "tech abbreviation", "IT acronym",
                    "hacker abbreviation", "generate abbreviation"
                ],
                "examples": [
                    "faker.hacker.abbreviation() // 'THX'"
                ],
                "notes": "Returns common technical abbreviations and acronyms"
            },
            "adjective": {
                "description": "Returns a random hacker/IT adjective",
                "patterns": [
                    "tech adjective", "IT adjective",
                    "hacker adjective", "generate tech adjective"
                ],
                "examples": [
                    "faker.hacker.adjective() // 'cross-platform'"
                ],
                "notes": "Returns descriptive words commonly used in tech contexts"
            },
            "noun": {
                "description": "Returns a random hacker/IT noun",
                "patterns": [
                    "tech noun", "IT noun",
                    "hacker noun", "generate tech noun"
                ],
                "examples": [
                    "faker.hacker.noun() // 'system'"
                ],
                "notes": "Returns technical terms and concepts used in IT"
            },
            "verb": {
                "description": "Returns a random hacker/IT verb",
                "patterns": [
                    "tech verb", "IT verb",
                    "hacker verb", "generate tech verb"
                ],
                "examples": [
                    "faker.hacker.verb() // 'copy'"
                ],
                "notes": "Returns action words commonly used in technical contexts"
            },
            "ingverb": {
                "description": "Returns a random hacker/IT verb with -ing suffix",
                "patterns": [
                    "continuous verb", "ing verb",
                    "tech action", "generate tech action"
                ],
                "examples": [
                    "faker.hacker.ingverb() // 'navigating'"
                ],
                "notes": "Returns continuous action verbs (e.g., backing up, programming)"
            },
            "phrase": {
                "description": "Generates a random hacker/IT phrase by combining various elements",
                "patterns": [
                    "tech phrase", "IT sentence",
                    "hacker speak", "generate tech phrase"
                ],
                "examples": [
                    "faker.hacker.phrase() // 'If we override the card, we can get to the HDD feed through the back-end HDD sensor!'"
                ],
                "notes": "Combines abbreviations, adjectives, nouns, and verbs into coherent technical phrases"
            }
        },
        "related_modules": {
            "word": {
                "description": "For general vocabulary instead of tech-specific terms",
                "module": "word",
                "usage": "faker.word.*"
            },
            "lorem": {
                "description": "For generating lorem ipsum text",
                "module": "lorem",
                "usage": "faker.lorem.*"
            },
            "company": {
                "description": "For corporate buzzwords and catchphrases",
                "module": "company",
                "usage": "faker.company.*"
            }
        },
        "usage_examples": {
            "technical_description": {
                "description": "Generate technical description",
                "code": [
                    "const adj = faker.hacker.adjective()",
                    "const noun = faker.hacker.noun()",
                    "`The ${adj} ${noun}` // 'The neural interface'"
                ]
            },
            "action_description": {
                "description": "Generate action description",
                "code": [
                    "const verb = faker.hacker.ingverb()",
                    "const noun = faker.hacker.noun()",
                    "`Currently ${verb} the ${noun}` // 'Currently synthesizing the protocol'"
                ]
            }
        }
    }
    return docs