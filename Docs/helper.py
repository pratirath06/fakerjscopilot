def load_faker_helper_docs():
    docs = {
        "helper": {
            "array_functions": {
                "arrayElement": {
                    "description": "Returns random element from the given array",
                    "patterns": [
                        "random array element", "pick random",
                        "choose element"
                    ],
                    "examples": [
                        "faker.helpers.arrayElement(['cat', 'dog', 'mouse']) // 'dog'"
                    ],
                    "notes": "Throws error if array is empty"
                },
                "arrayElements": {
                    "description": "Returns a subset of random elements from the given array",
                    "patterns": [
                        "multiple elements", "random subset",
                        "pick multiple"
                    ],
                    "examples": [
                        "faker.helpers.arrayElements(['cat', 'dog', 'mouse']) // ['mouse', 'cat']",
                        "faker.helpers.arrayElements([1, 2, 3, 4, 5], 2) // [4, 2]",
                        "faker.helpers.arrayElements([1, 2, 3], { min: 1, max: 2 }) // [2, 3]"
                    ],
                    "parameters": {
                        "array": "array to pick from",
                        "count": "optional - number or { min, max } - how many elements to pick"
                    }
                },
                "weightedArrayElement": {
                    "description": "Returns a random element based on weight distribution",
                    "patterns": [
                        "weighted random", "probability pick",
                        "weighted choice"
                    ],
                    "examples": [
                        "faker.helpers.weightedArrayElement([",
                        "  { weight: 5, value: 'sunny' },",
                        "  { weight: 4, value: 'rainy' },",
                        "  { weight: 1, value: 'snowy' }",
                        "]) // 'sunny' (50% chance)"
                    ],
                    "parameters": {
                        "array": "array of { weight: number, value: any } objects"
                    }
                },
                "shuffle": {
                    "description": "Randomizes array elements in place or returns new shuffled array",
                    "patterns": [
                        "shuffle array", "randomize order",
                        "mix elements"
                    ],
                    "examples": [
                        "faker.helpers.shuffle(['a', 'b', 'c']) // ['b', 'c', 'a']",
                        "faker.helpers.shuffle(['a', 'b', 'c'], { inplace: true })"
                    ],
                    "parameters": {
                        "inplace": "optional - boolean - whether to modify original array"
                    }
                }
            },
            "object_functions": {
                "objectKey": {
                    "description": "Returns a random key from the given object",
                    "patterns": [
                        "random key", "pick key",
                        "object key"
                    ],
                    "examples": [
                        "faker.helpers.objectKey({ cat: 1, dog: 2 }) // 'dog'"
                    ]
                },
                "objectValue": {
                    "description": "Returns a random value from the given object",
                    "patterns": [
                        "random value", "pick value",
                        "object value"
                    ],
                    "examples": [
                        "faker.helpers.objectValue({ cat: 1, dog: 2 }) // 2"
                    ]
                },
                "objectEntry": {
                    "description": "Returns a random [key, value] pair from the object",
                    "patterns": [
                        "random entry", "key value pair",
                        "object entry"
                    ],
                    "examples": [
                        "faker.helpers.objectEntry({ cat: 1, dog: 2 }) // ['cat', 1]"
                    ]
                }
            },
            "string_functions": {
                "replaceSymbols": {
                    "description": "Replaces symbols in a string with random characters",
                    "patterns": [
                        "replace symbols", "symbol template",
                        "pattern string"
                    ],
                    "examples": [
                        "faker.helpers.replaceSymbols('?#*') // 'A2f'",
                        "faker.helpers.replaceSymbols('Your pin: ####') // 'Your pin: 1234'"
                    ],
                    "notes": [
                        "# - replaced with digit",
                        "? - replaced with letter",
                        "* - replaced with digit or letter"
                    ]
                },
                "replaceSymbolWithNumber": {
                    "description": "Replaces given symbol with random numbers",
                    "patterns": [
                        "number template", "digit pattern",
                        "number string"
                    ],
                    "examples": [
                        "faker.helpers.replaceSymbolWithNumber('!####') // '23789'",
                        "faker.helpers.replaceSymbolWithNumber('Your pin: ####') // 'Your pin: 1234'"
                    ],
                    "notes": "! generates numbers >= 2"
                },
                "fromRegExp": {
                    "description": "Generates string matching given RegExp-like pattern",
                    "patterns": [
                        "regex pattern", "string pattern",
                        "match pattern"
                    ],
                    "examples": [
                        "faker.helpers.fromRegExp('[A-Z]{5}') // 'PDKFH'",
                        "faker.helpers.fromRegExp(/[0-9]{3}-[A-Z]{2}/) // '123-PD'"
                    ],
                    "notes": "Supports limited RegExp features"
                }
            },
            "utility_functions": {
                "fake": {
                    "description": "Generates string by interpolating faker method placeholders",
                    "patterns": [
                        "template string", "faker template",
                        "interpolate template"
                    ],
                    "examples": [
                        "faker.helpers.fake('{{person.firstName}} {{person.lastName}}')",
                        "// 'John Smith'",
                        "faker.helpers.fake(['Hello {{person.firstName}}', 'Hi {{person.firstName}}'])"
                    ],
                    "notes": "Use string template literals instead when possible"
                },
                "maybe": {
                    "description": "Conditionally executes callback based on probability",
                    "patterns": [
                        "random execution", "probability call",
                        "maybe execute"
                    ],
                    "examples": [
                        "faker.helpers.maybe(() => 'Hello', { probability: 0.3 })"
                    ],
                    "parameters": {
                        "probability": "optional - number (0-1) - chance of execution"
                    }
                },
                "multiple": {
                    "description": "Generates array of values using given method",
                    "patterns": [
                        "repeat generation", "multiple values",
                        "generate array"
                    ],
                    "examples": [
                        "faker.helpers.multiple(() => faker.person.firstName(), { count: 3 })",
                        "// ['John', 'Jane', 'Bob']"
                    ],
                    "parameters": {
                        "count": "optional - number or { min, max } - how many values to generate"
                    }
                }
            }
        }
    }
    return docs