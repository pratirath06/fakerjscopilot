def load_faker_number_docs():
    docs = {
        "number": {
            "basic": {
                "int": {
                    "description": "Returns random integer between bounds (inclusive)",
                    "patterns": [
                        "integer", "whole number",
                        "generate integer"
                    ],
                    "examples": [
                        "faker.number.int() // 2900970162509863",
                        "faker.number.int(100) // 52",
                        "faker.number.int({ min: 10, max: 100 }) // 57",
                        "faker.number.int({ min: 10, max: 100, multipleOf: 10 }) // 50"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 0) - Lower bound",
                        "max": "optional - number (default: Number.MAX_SAFE_INTEGER) - Upper bound",
                        "multipleOf": "optional - number (default: 1) - Result will be multiple of this"
                    },
                    "throws": [
                        "When min > max",
                        "When no suitable integers between min and max",
                        "When multipleOf is not positive integer"
                    ]
                },
                "float": {
                    "description": "Returns random floating-point number",
                    "patterns": [
                        "float", "decimal number",
                        "generate decimal"
                    ],
                    "examples": [
                        "faker.number.float() // 0.5688541042618454",
                        "faker.number.float(3) // 2.367973240558058",
                        "faker.number.float({ min: 20, max: 30 }) // 23.94764115102589",
                        "faker.number.float({ fractionDigits: 2 }) // 0.57",
                        "faker.number.float({ multipleOf: 0.25 }) // 7.75"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 0.0) - Lower bound",
                        "max": "optional - number (default: 1.0) - Upper bound",
                        "fractionDigits": "optional - number - Max decimal places",
                        "multipleOf": "optional - number - Result will be multiple of this"
                    },
                    "throws": [
                        "When min > max",
                        "When multipleOf is negative",
                        "When fractionDigits is negative",
                        "When both fractionDigits and multipleOf provided"
                    ]
                }
            },
            "different_bases": {
                "binary": {
                    "description": "Returns binary number as string",
                    "patterns": [
                        "binary number", "base-2",
                        "generate binary"
                    ],
                    "examples": [
                        "faker.number.binary() // '1'",
                        "faker.number.binary(255) // '110101'",
                        "faker.number.binary({ min: 0, max: 65535 })"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 0) - Lower bound",
                        "max": "optional - number (default: 1) - Upper bound"
                    }
                },
                "octal": {
                    "description": "Returns octal number as string",
                    "patterns": [
                        "octal number", "base-8",
                        "generate octal"
                    ],
                    "examples": [
                        "faker.number.octal() // '5'",
                        "faker.number.octal(255) // '377'",
                        "faker.number.octal({ min: 0, max: 65535 })"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 0) - Lower bound",
                        "max": "optional - number (default: 7) - Upper bound"
                    }
                },
                "hex": {
                    "description": "Returns hexadecimal number as lowercase string",
                    "patterns": [
                        "hex number", "base-16",
                        "generate hex"
                    ],
                    "examples": [
                        "faker.number.hex() // 'b'",
                        "faker.number.hex(255) // '9d'",
                        "faker.number.hex({ min: 0, max: 65535 })"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 0) - Lower bound",
                        "max": "optional - number (default: 15) - Upper bound"
                    }
                }
            },
            "special_types": {
                "bigInt": {
                    "description": "Returns random BigInt number",
                    "patterns": [
                        "big integer", "bigint",
                        "generate bigint"
                    ],
                    "examples": [
                        "faker.number.bigInt() // 55422n",
                        "faker.number.bigInt(100n) // 52n",
                        "faker.number.bigInt({ min: 10n, max: 100n }) // 36n"
                    ],
                    "parameters": {
                        "min": "optional - bigint (default: 0n) - Lower bound",
                        "max": "optional - bigint (default: min + 999999999999999n) - Upper bound"
                    }
                },
                "romanNumeral": {
                    "description": "Returns roman numeral string",
                    "patterns": [
                        "roman numeral", "roman number",
                        "generate roman"
                    ],
                    "examples": [
                        "faker.number.romanNumeral() // 'CMXCIII'",
                        "faker.number.romanNumeral(5) // 'III'",
                        "faker.number.romanNumeral({ min: 5, max: 10 }) // 'VII'"
                    ],
                    "parameters": {
                        "min": "optional - number (default: 1) - Lower bound",
                        "max": "optional - number (default: 3999) - Upper bound"
                    },
                    "throws": [
                        "When min < 1",
                        "When max > 3999",
                        "When min > max"
                    ]
                }
            }
        }
    }
    return docs