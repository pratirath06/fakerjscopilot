def load_faker_location_docs():
    docs = {
        "location": {
            "address_components": {
                "zipCode": {
                    "description": "Generates random zip code with specified format",
                    "patterns": [
                        "zip code", "postal code",
                        "generate zip"
                    ],
                    "examples": [
                        "faker.location.zipCode() // '17839'",
                        "faker.location.zipCode('####') // '6925'",
                        "faker.location.zipCode({ state: 'CA' })"
                    ],
                    "parameters": {
                        "format": "optional - string - Format pattern to use",
                        "state": "optional - string - State to generate zip for"
                    }
                },
                "city": {
                    "description": "Generates random localized city name",
                    "patterns": [
                        "city name", "municipality",
                        "generate city"
                    ],
                    "examples": [
                        "faker.location.city() // 'East Jarretmouth'",
                        "fakerDE.location.city() // 'Bad Lilianadorf'"
                    ]
                },
                "street": {
                    "description": "Generates random street name",
                    "patterns": [
                        "street name", "road name",
                        "generate street"
                    ],
                    "examples": [
                        "faker.location.street() // 'Schroeder Isle'"
                    ]
                },
                "streetAddress": {
                    "description": "Generates complete street address",
                    "patterns": [
                        "street address", "full address",
                        "generate address"
                    ],
                    "examples": [
                        "faker.location.streetAddress() // '0917 O'Conner Estates'",
                        "faker.location.streetAddress(true) // '3393 Ronny Way Apt. 742'"
                    ],
                    "parameters": {
                        "useFullAddress": "optional - boolean - Include secondary address"
                    }
                },
                "secondaryAddress": {
                    "description": "Generates secondary address (apt/suite number)",
                    "patterns": [
                        "apartment number", "suite number",
                        "unit number"
                    ],
                    "examples": [
                        "faker.location.secondaryAddress() // 'Apt. 861'"
                    ]
                },
                "buildingNumber": {
                    "description": "Generates random building number",
                    "patterns": [
                        "building number", "house number",
                        "address number"
                    ],
                    "examples": [
                        "faker.location.buildingNumber() // '379'"
                    ]
                }
            },
            "administrative_areas": {
                "state": {
                    "description": "Returns random state or administrative division",
                    "patterns": [
                        "state name", "province", "region",
                        "administrative division"
                    ],
                    "examples": [
                        "faker.location.state() // 'Mississippi'",
                        "faker.location.state({ abbreviated: true }) // 'LA'"
                    ],
                    "parameters": {
                        "abbreviated": "optional - boolean - Return abbreviation"
                    }
                },
                "county": {
                    "description": "Returns random county or second-level division",
                    "patterns": [
                        "county", "district", "department"
                    ],
                    "examples": [
                        "faker.location.county() // 'Monroe County'",
                        "fakerGB.location.county() // 'Cambridgeshire'"
                    ]
                }
            },
            "countries": {
                "country": {
                    "description": "Returns random country name",
                    "patterns": [
                        "country name", "nation",
                        "generate country"
                    ],
                    "examples": [
                        "faker.location.country() // 'Greece'"
                    ]
                },
                "countryCode": {
                    "description": "Returns random country code (ISO 3166-1)",
                    "patterns": [
                        "country code", "ISO code",
                        "nation code"
                    ],
                    "examples": [
                        "faker.location.countryCode() // 'SJ'",
                        "faker.location.countryCode('alpha-3') // 'TJK'",
                        "faker.location.countryCode('numeric') // '528'"
                    ],
                    "parameters": {
                        "variant": "optional - 'alpha-2'|'alpha-3'|'numeric' (default: 'alpha-2')"
                    }
                },
                "continent": {
                    "description": "Returns random continent name",
                    "patterns": [
                        "continent", "landmass"
                    ],
                    "examples": [
                        "faker.location.continent() // 'Asia'"
                    ]
                }
            },
            "coordinates": {
                "latitude": {
                    "description": "Generates random latitude coordinate",
                    "patterns": [
                        "latitude", "lat coordinate",
                        "generate latitude"
                    ],
                    "examples": [
                        "faker.location.latitude() // -30.9501",
                        "faker.location.latitude({ max: 10, min: -10, precision: 5 }) // 2.68452"
                    ],
                    "parameters": {
                        "max": "optional - number (default: 90) - Maximum value",
                        "min": "optional - number (default: -90) - Minimum value",
                        "precision": "optional - number (default: 4) - Decimal precision"
                    }
                },
                "longitude": {
                    "description": "Generates random longitude coordinate",
                    "patterns": [
                        "longitude", "long coordinate",
                        "generate longitude"
                    ],
                    "examples": [
                        "faker.location.longitude() // -30.9501",
                        "faker.location.longitude({ max: 10, min: -10, precision: 5 }) // 2.68452"
                    ],
                    "parameters": {
                        "max": "optional - number (default: 180) - Maximum value",
                        "min": "optional - number (default: -180) - Minimum value",
                        "precision": "optional - number (default: 4) - Decimal precision"
                    }
                },
                "nearbyGPSCoordinate": {
                    "description": "Generates GPS coordinate near given location",
                    "patterns": [
                        "nearby coordinate", "location near",
                        "close coordinate"
                    ],
                    "examples": [
                        "faker.location.nearbyGPSCoordinate() // [33.8475, -170.5953]",
                        "faker.location.nearbyGPSCoordinate({ origin: [33, -170], radius: 1000, isMetric: true })"
                    ],
                    "parameters": {
                        "origin": "optional - [lat, long] - Center coordinate",
                        "radius": "optional - number (default: 10) - Maximum distance",
                        "isMetric": "optional - boolean (default: false) - Use kilometers"
                    }
                }
            },
            "other": {
                "direction": {
                    "description": "Returns random cardinal or ordinal direction",
                    "patterns": [
                        "direction", "compass direction"
                    ],
                    "examples": [
                        "faker.location.direction() // 'Northeast'",
                        "faker.location.direction({ abbreviated: true }) // 'SW'"
                    ],
                    "parameters": {
                        "abbreviated": "optional - boolean - Use abbreviation"
                    }
                },
                "timeZone": {
                    "description": "Returns random IANA timezone for locale",
                    "patterns": [
                        "timezone", "time zone"
                    ],
                    "examples": [
                        "faker.location.timeZone() // 'Pacific/Guam'"
                    ]
                },
                "language": {
                    "description": "Returns random spoken language with codes",
                    "patterns": [
                        "language", "spoken language",
                        "language code"
                    ],
                    "examples": [
                        "faker.location.language() // { alpha2: 'de', alpha3: 'deu', name: 'German' }"
                    ],
                    "returns": {
                        "name": "string - Full language name",
                        "alpha2": "string - ISO 639-1 code",
                        "alpha3": "string - ISO 639-2 code"
                    }
                }
            }
        }
    }
    return docs