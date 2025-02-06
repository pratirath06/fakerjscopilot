def load_faker_datatype_docs():
    docs = {
        "datatype": {
            "boolean": {
                "description": "Returns a boolean value (true or false) with configurable probability",
                "patterns": [
                    "boolean", "random boolean", "true/false",
                    "generate boolean"
                ],
                "examples": [
                    "faker.datatype.boolean() // false",
                    "faker.datatype.boolean(0.9) // true",
                    "faker.datatype.boolean({ probability: 0.1 }) // false"
                ],
                "parameters": {
                    "probability": "optional - number | { probability: number } (default: 0.5) - Probability of returning true (0.00 to 1.00)"
                },
                "notes": [
                    "Probability of 0.75 means true will be returned 75% of the time",
                    "Probability <= 0.0 always returns false",
                    "Probability >= 1.0 always returns true",
                    "Probability is limited to two decimal places",
                    "Can be called with either a number or an options object"
                ]
            }
        },
        "usage_examples": {
            "default": {
                "description": "50/50 chance of true/false",
                "code": "faker.datatype.boolean()"
            },
            "mostly_true": {
                "description": "90% chance of true",
                "code": "faker.datatype.boolean(0.9)"
            },
            "mostly_false": {
                "description": "10% chance of true",
                "code": "faker.datatype.boolean({ probability: 0.1 })"
            },
            "always_true": {
                "description": "Always returns true",
                "code": "faker.datatype.boolean(1)"
            },
            "always_false": {
                "description": "Always returns false",
                "code": "faker.datatype.boolean(0)"
            }
        }
    }
    return docs