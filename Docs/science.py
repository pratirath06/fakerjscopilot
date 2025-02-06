def load_faker_science_docs():
    docs = {
        "science": {
            "chemicalElement": {
                "description": "Returns random periodic table element object",
                "patterns": [
                    "chemical element", "periodic element",
                    "element data"
                ],
                "examples": [
                    "faker.science.chemicalElement() // { symbol: 'H', name: 'Hydrogen', atomicNumber: 1 }",
                    "faker.science.chemicalElement() // { symbol: 'Xe', name: 'Xenon', atomicNumber: 54 }"
                ],
                "returns": {
                    "symbol": "string - Element symbol (e.g. 'He')",
                    "name": "string - Full element name (e.g. 'Helium')",
                    "atomicNumber": "number - Atomic number (e.g. 2)"
                }
            },
            "unit": {
                "description": "Returns random scientific unit object",
                "patterns": [
                    "scientific unit", "measurement unit",
                    "physics unit"
                ],
                "examples": [
                    "faker.science.unit() // { name: 'meter', symbol: 'm' }",
                    "faker.science.unit() // { name: 'second', symbol: 's' }"
                ],
                "returns": {
                    "name": "string - Full unit name (e.g. 'meter')",
                    "symbol": "string - Unit symbol (e.g. 'm')"
                }
            }
        }
    }
    return docs