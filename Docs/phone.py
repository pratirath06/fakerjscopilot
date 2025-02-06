def load_faker_phone_docs():
    docs = {
        "phone": {
            "number": {
                "description": "Generates random phone number in various formats",
                "patterns": [
                    "phone number", "telephone",
                    "generate phone"
                ],
                "examples": [
                    "faker.phone.number() // '961-770-7727'",
                    "faker.phone.number({ style: 'human' }) // '555.770.7727 x1234'",
                    "faker.phone.number({ style: 'national' }) // '(961) 770-7727'",
                    "faker.phone.number({ style: 'international' }) // '+15551234567'"
                ],
                "parameters": {
                    "style": "optional - 'human'|'national'|'international' (default: 'human')"
                },
                "notes": [
                    "Supports country-specific formats based on locale",
                    "Can generate extensions with 'human' style",
                    "'human' style simulates common manual input formats",
                    "'national' style follows standardized format",
                    "'international' style follows E.123 format"
                ],
                "related": [
                    "faker.string.numeric() - For generating numeric strings",
                    "faker.helpers.fromRegExp() - For regex pattern matching"
                ]
            },
            "imei": {
                "description": "Generates IMEI (International Mobile Equipment Identity) number",
                "patterns": [
                    "imei number", "device id",
                    "mobile identifier"
                ],
                "examples": [
                    "faker.phone.imei() // '13-850175-913761-7'"
                ],
                "notes": [
                    "Generates valid format with check digit",
                    "Format: XX-XXXXXX-XXXXXX-L where L is Luhn check digit"
                ]
            }
        }
    }
    return docs