def load_faker_company_docs():
    docs = {
        "company": {
            "name": {
                "description": "Generates a random company name",
                "patterns": [
                    "company name", "business name",
                    "corporation name", "generate company"
                ],
                "examples": [
                    "faker.company.name() // 'Zieme, Hauck and McClure'"
                ],
                "notes": "Localized in many locales for region-specific company names"
            },
            "catchPhrase": {
                "description": "Generates a random catch phrase by combining adjective, descriptor, and noun",
                "patterns": [
                    "catch phrase", "company slogan",
                    "business motto", "generate catch phrase"
                ],
                "examples": [
                    "faker.company.catchPhrase() // 'Upgradable systematic flexibility'"
                ],
                "notes": "Combines results from catchPhraseAdjective(), catchPhraseDescriptor(), and catchPhraseNoun()"
            },
            "buzzPhrase": {
                "description": "Generates a random business buzz phrase by combining verb, adjective, and noun",
                "patterns": [
                    "buzz phrase", "business jargon",
                    "corporate speak", "generate buzz phrase"
                ],
                "examples": [
                    "faker.company.buzzPhrase() // 'cultivate synergistic e-markets'"
                ],
                "notes": "Combines results from buzzVerb(), buzzAdjective(), and buzzNoun()"
            },
            "catchPhraseAdjective": {
                "description": "Returns a random catch phrase adjective",
                "patterns": [
                    "catch phrase adjective",
                    "company adjective",
                    "generate catch phrase adjective"
                ],
                "examples": [
                    "faker.company.catchPhraseAdjective() // 'Multi-tiered'"
                ]
            },
            "catchPhraseDescriptor": {
                "description": "Returns a random catch phrase descriptor",
                "patterns": [
                    "catch phrase descriptor",
                    "company descriptor",
                    "generate catch phrase descriptor"
                ],
                "examples": [
                    "faker.company.catchPhraseDescriptor() // 'composite'"
                ]
            },
            "catchPhraseNoun": {
                "description": "Returns a random catch phrase noun",
                "patterns": [
                    "catch phrase noun",
                    "company noun",
                    "generate catch phrase noun"
                ],
                "examples": [
                    "faker.company.catchPhraseNoun() // 'leverage'"
                ]
            },
            "buzzAdjective": {
                "description": "Returns a random business buzz adjective",
                "patterns": [
                    "buzz adjective",
                    "business adjective",
                    "generate buzz adjective"
                ],
                "examples": [
                    "faker.company.buzzAdjective() // 'one-to-one'"
                ]
            },
            "buzzVerb": {
                "description": "Returns a random business buzz verb",
                "patterns": [
                    "buzz verb",
                    "business verb",
                    "generate buzz verb"
                ],
                "examples": [
                    "faker.company.buzzVerb() // 'empower'"
                ]
            },
            "buzzNoun": {
                "description": "Returns a random business buzz noun",
                "patterns": [
                    "buzz noun",
                    "business noun",
                    "generate buzz noun"
                ],
                "examples": [
                    "faker.company.buzzNoun() // 'paradigms'"
                ]
            }
        },
        "related_modules": {
            "commerce": {
                "description": "For products and commerce-related data",
                "module": "commerce",
                "usage": "faker.commerce.*"
            },
            "finance": {
                "description": "For finance-related entries",
                "module": "finance",
                "usage": "faker.finance.*"
            }
        }
    }
    return docs