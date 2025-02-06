def load_faker_animal_docs():
    docs = {
        "animal": {
            "dog": {
                "description": "Returns a random dog breed",
                "patterns": [
                    "dog", "dog breed", "canine",
                    "generate dog breed"
                ],
                "examples": [
                    "faker.animal.dog() // 'Irish Water Spaniel'"
                ]
            },
            "cat": {
                "description": "Returns a random cat breed",
                "patterns": [
                    "cat", "cat breed", "feline",
                    "generate cat breed"
                ],
                "examples": [
                    "faker.animal.cat() // 'Singapura'"
                ]
            },
            "snake": {
                "description": "Returns a random snake species",
                "patterns": [
                    "snake", "snake species", "serpent",
                    "generate snake"
                ],
                "examples": [
                    "faker.animal.snake() // 'Eyelash viper'"
                ]
            },
            "bear": {
                "description": "Returns a random bear species",
                "patterns": [
                    "bear", "bear species", "ursine",
                    "generate bear"
                ],
                "examples": [
                    "faker.animal.bear() // 'Asian black bear'"
                ]
            },
            "lion": {
                "description": "Returns a random lion species",
                "patterns": [
                    "lion", "lion species", "big cat",
                    "generate lion"
                ],
                "examples": [
                    "faker.animal.lion() // 'Northeast Congo Lion'"
                ]
            },
            "cetacean": {
                "description": "Returns a random cetacean species (whales, dolphins, porpoises)",
                "patterns": [
                    "cetacean", "whale", "dolphin", "porpoise",
                    "generate cetacean"
                ],
                "examples": [
                    "faker.animal.cetacean() // 'Spinner Dolphin'"
                ]
            },
            "horse": {
                "description": "Returns a random horse breed",
                "patterns": [
                    "horse", "horse breed", "equine",
                    "generate horse"
                ],
                "examples": [
                    "faker.animal.horse() // 'Swedish Warmblood'"
                ]
            },
            "bird": {
                "description": "Returns a random bird species",
                "patterns": [
                    "bird", "bird species", "avian",
                    "generate bird"
                ],
                "examples": [
                    "faker.animal.bird() // 'Buller's Shearwater'"
                ]
            },
            "cow": {
                "description": "Returns a random cow species",
                "patterns": [
                    "cow", "cow species", "cattle",
                    "generate cow"
                ],
                "examples": [
                    "faker.animal.cow() // 'Brava'"
                ]
            },
            "fish": {
                "description": "Returns a random fish species",
                "patterns": [
                    "fish", "fish species", "aquatic",
                    "generate fish"
                ],
                "examples": [
                    "faker.animal.fish() // 'Mandarin fish'"
                ]
            },
            "crocodilia": {
                "description": "Returns a random crocodilian species",
                "patterns": [
                    "crocodile", "alligator", "crocodilian",
                    "generate crocodilia"
                ],
                "examples": [
                    "faker.animal.crocodilia() // 'Philippine Crocodile'"
                ]
            },
            "insect": {
                "description": "Returns a random insect species",
                "patterns": [
                    "insect", "bug", "arthropod",
                    "generate insect"
                ],
                "examples": [
                    "faker.animal.insect() // 'Pyramid ant'"
                ]
            },
            "rabbit": {
                "description": "Returns a random rabbit species",
                "patterns": [
                    "rabbit", "bunny", "hare",
                    "generate rabbit"
                ],
                "examples": [
                    "faker.animal.rabbit() // 'Florida White'"
                ]
            },
            "rodent": {
                "description": "Returns a random rodent breed",
                "patterns": [
                    "rodent", "mouse", "rat",
                    "generate rodent"
                ],
                "examples": [
                    "faker.animal.rodent() // 'Cuscomys ashanika'"
                ]
            },
            "type": {
                "description": "Returns a random animal type",
                "patterns": [
                    "animal type", "animal category",
                    "generate animal type"
                ],
                "examples": [
                    "faker.animal.type() // 'crocodile'"
                ]
            },
            "petName": {
                "description": "Returns a random pet name",
                "patterns": [
                    "pet name", "animal name",
                    "generate pet name"
                ],
                "examples": [
                    "faker.animal.petName() // 'Coco'"
                ]
            }
        }
    }
    return docs