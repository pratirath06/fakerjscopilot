def load_faker_airline_docs():
    docs = {
        "airline": {
            "airport": {
                "description": "Generates a random airport object with name and IATA code",
                "patterns": [
                    "airport", "airport info", "airport data",
                    "generate airport"
                ],
                "examples": [
                    "faker.airline.airport() // { name: 'Dallas Fort Worth International Airport', iataCode: 'DFW' }"
                ],
                "returns": {
                    "name": "string - The full airport name",
                    "iataCode": "string - The 3-letter IATA airport code"
                }
            },
            "airline": {
                "description": "Generates a random airline object with name and IATA code",
                "patterns": [
                    "airline", "airline company", "carrier",
                    "generate airline"
                ],
                "examples": [
                    "faker.airline.airline() // { name: 'American Airlines', iataCode: 'AA' }"
                ],
                "returns": {
                    "name": "string - The airline company name",
                    "iataCode": "string - The 2-letter IATA airline code"
                }
            },
            "airplane": {
                "description": "Generates a random airplane object with name and IATA type code",
                "patterns": [
                    "airplane", "aircraft", "plane model",
                    "generate airplane"
                ],
                "examples": [
                    "faker.airline.airplane() // { name: 'Airbus A321neo', iataTypeCode: '32Q' }"
                ],
                "returns": {
                    "name": "string - The airplane model name",
                    "iataTypeCode": "string - The IATA type code for the aircraft"
                }
            },
            "recordLocator": {
                "description": "Generates a random record locator (booking reference/confirmation code)",
                "patterns": [
                    "record locator", "booking reference", "confirmation code",
                    "reservation code", "generate record locator"
                ],
                "examples": [
                    "faker.airline.recordLocator() // 'KIFRWE'",
                    "faker.airline.recordLocator({ allowNumerics: true }) // 'E5TYEM'",
                    "faker.airline.recordLocator({ allowVisuallySimilarCharacters: true }) // 'ANZNEI'",
                    "faker.airline.recordLocator({ allowNumerics: true, allowVisuallySimilarCharacters: true }) // '1Z2Z3E'"
                ],
                "parameters": {
                    "allowNumerics": "optional - boolean (default: false) - Allow numeric characters",
                    "allowVisuallySimilarCharacters": "optional - boolean (default: false) - Allow visually similar characters (0/O, 1/I/L)"
                }
            },
            "seat": {
                "description": "Generates a random airplane seat designation",
                "patterns": [
                    "seat", "seat number", "airplane seat",
                    "generate seat"
                ],
                "examples": [
                    "faker.airline.seat() // '22C'",
                    "faker.airline.seat({ aircraftType: 'regional' }) // '7A'",
                    "faker.airline.seat({ aircraftType: 'widebody' }) // '42K'"
                ],
                "parameters": {
                    "aircraftType": "optional - string ('narrowbody'|'regional'|'widebody') (default: 'narrowbody') - Type of aircraft"
                }
            },
            "aircraftType": {
                "description": "Returns a random aircraft type",
                "patterns": [
                    "aircraft type", "plane type",
                    "generate aircraft type"
                ],
                "examples": [
                    "faker.airline.aircraftType() // 'narrowbody'"
                ]
            },
            "flightNumber": {
                "description": "Generates a random flight number (1-4 digits)",
                "patterns": [
                    "flight number", "flight",
                    "generate flight number"
                ],
                "examples": [
                    "faker.airline.flightNumber() // '2405'",
                    "faker.airline.flightNumber({ addLeadingZeros: true }) // '0249'",
                    "faker.airline.flightNumber({ length: 3 }) // '425'",
                    "faker.airline.flightNumber({ length: { min: 2, max: 3 } }) // '84'",
                    "// With airline code",
                    "`${faker.airline.airline().iataCode}${faker.airline.flightNumber({ addLeadingZeros: true })}` // 'AA0798'"
                ],
                "parameters": {
                    "length": "optional - number or {min: number, max: number} (default: {min: 1, max: 4}) - Number of digits",
                    "addLeadingZeros": "optional - boolean (default: false) - Pad with leading zeros up to 4 digits"
                }
            }
        }
    }
    return docs
