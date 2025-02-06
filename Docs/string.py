def load_faker_string_docs():
    docs = {
        "string": {
            "basic_generators": {
                "fromCharacters": {
                    "description": "Generates string from given characters",
                    "examples": [
                        "faker.string.fromCharacters('abc') // 'c'",
                        "faker.string.fromCharacters(['a', 'b', 'c']) // 'a'",
                        "faker.string.fromCharacters('abc', 10) // 'cbbbacbacb'"
                    ],
                    "parameters": {
                        "characters": "string | string[] - Characters to use",
                        "length": "optional - number | { min, max } (default: 1)"
                    }
                },
                "alpha": {
                    "description": "Generates string of letters",
                    "examples": [
                        "faker.string.alpha() // 'b'",
                        "faker.string.alpha(10) // 'fEcAaCVbaR'",
                        "faker.string.alpha({ casing: 'lower', exclude: ['a'] })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "casing": "optional - 'upper'|'lower'|'mixed' (default: 'mixed')",
                        "exclude": "optional - string[] - Characters to exclude"
                    }
                },
                "alphanumeric": {
                    "description": "Generates string of letters and numbers",
                    "examples": [
                        "faker.string.alphanumeric() // '2'",
                        "faker.string.alphanumeric(5) // '3e5V7'",
                        "faker.string.alphanumeric({ casing: 'upper' })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "casing": "optional - 'upper'|'lower'|'mixed' (default: 'mixed')",
                        "exclude": "optional - string[] - Characters to exclude"
                    }
                }
            },
            "numeric_strings": {
                "numeric": {
                    "description": "Generates string of digits",
                    "examples": [
                        "faker.string.numeric() // '2'",
                        "faker.string.numeric(5) // '31507'",
                        "faker.string.numeric({ allowLeadingZeros: false })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "allowLeadingZeros": "optional - boolean (default: true)",
                        "exclude": "optional - string[] - Digits to exclude"
                    }
                },
                "binary": {
                    "description": "Generates binary number string",
                    "examples": [
                        "faker.string.binary() // '0b1'",
                        "faker.string.binary({ length: 10 }) // '0b1101011011'",
                        "faker.string.binary({ prefix: 'bin_' })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "prefix": "optional - string (default: '0b')"
                    }
                },
                "octal": {
                    "description": "Generates octal number string",
                    "examples": [
                        "faker.string.octal() // '0o3'",
                        "faker.string.octal({ length: 10 }) // '0o1526216210'",
                        "faker.string.octal({ prefix: 'oct_' })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "prefix": "optional - string (default: '0o')"
                    }
                },
                "hexadecimal": {
                    "description": "Generates hexadecimal number string",
                    "examples": [
                        "faker.string.hexadecimal() // '0xB'",
                        "faker.string.hexadecimal({ length: 10 }) // '0xaE13d044cB'",
                        "faker.string.hexadecimal({ casing: 'upper', prefix: '#' })"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)",
                        "casing": "optional - 'upper'|'lower'|'mixed' (default: 'mixed')",
                        "prefix": "optional - string (default: '0x')"
                    }
                }
            },
            "identifiers": {
                "uuid": {
                    "description": "Generates UUID v4",
                    "examples": [
                        "faker.string.uuid() // '4136cd0b-d90b-4af7-b485-5d1ded8db252'"
                    ]
                },
                "ulid": {
                    "description": "Generates ULID (Universally Unique Lexicographically Sortable Identifier)",
                    "examples": [
                        "faker.string.ulid() // '01ARZ3NDEKTSV4RRFFQ69G5FAV'",
                        "faker.string.ulid({ refDate: '2020-01-01T00:00:00.000Z' })"
                    ],
                    "parameters": {
                        "refDate": "optional - Date - Reference date for timestamp"
                    }
                },
                "nanoid": {
                    "description": "Generates Nano ID",
                    "examples": [
                        "faker.string.nanoid() // 'ptL0KpX_yRMI98JFr6B3n'",
                        "faker.string.nanoid(10) // 'VsvwSdm_Am'"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 21)"
                    }
                }
            },
            "special": {
                "sample": {
                    "description": "Generates string of UTF-16 chars between 33-125",
                    "examples": [
                        "faker.string.sample() // 'Zo!.:*e>wR'",
                        "faker.string.sample(5) // '6Bye8'"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 10)"
                    }
                },
                "symbol": {
                    "description": "Generates string of special characters",
                    "examples": [
                        "faker.string.symbol() // '$'",
                        "faker.string.symbol(5) // '#*!.~'"
                    ],
                    "parameters": {
                        "length": "optional - number | { min, max } (default: 1)"
                    }
                }
            }
        }
    }
    return docs