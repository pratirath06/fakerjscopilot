def load_faker_person_docs():
    docs = {
        "person": {
            "name_components": {
                "firstName": {
                    "description": "Returns random first name, optionally by sex",
                    "patterns": [
                        "first name", "given name",
                        "generate first name"
                    ],
                    "examples": [
                        "faker.person.firstName() // 'Antwan'",
                        "faker.person.firstName('female') // 'Victoria'",
                        "faker.person.firstName('male') // 'Tom'"
                    ],
                    "parameters": {
                        "sex": "optional - 'female' | 'male' - Specific sex for name"
                    }
                },
                "lastName": {
                    "description": "Returns random last name, optionally by sex",
                    "patterns": [
                        "last name", "surname",
                        "family name"
                    ],
                    "examples": [
                        "faker.person.lastName() // 'Hauck'",
                        "faker.person.lastName('female') // 'Grady'",
                        "faker.person.lastName('male') // 'Barton'"
                    ],
                    "parameters": {
                        "sex": "optional - 'female' | 'male' - Specific sex for name"
                    }
                },
                "middleName": {
                    "description": "Returns random middle name, optionally by sex",
                    "patterns": [
                        "middle name", "second name",
                        "generate middle name"
                    ],
                    "examples": [
                        "faker.person.middleName() // 'James'",
                        "faker.person.middleName('female') // 'Eloise'",
                        "faker.person.middleName('male') // 'Asher'"
                    ],
                    "parameters": {
                        "sex": "optional - 'female' | 'male' - Specific sex for name"
                    }
                },
                "prefix": {
                    "description": "Returns random name prefix (Mr., Mrs., etc)",
                    "patterns": [
                        "name prefix", "title prefix",
                        "generate prefix"
                    ],
                    "examples": [
                        "faker.person.prefix() // 'Miss'",
                        "faker.person.prefix('female') // 'Ms.'",
                        "faker.person.prefix('male') // 'Mr.'"
                    ],
                    "parameters": {
                        "sex": "optional - 'female' | 'male' - Specific sex for prefix"
                    }
                },
                "suffix": {
                    "description": "Returns random name suffix (Jr., Sr., etc)",
                    "patterns": [
                        "name suffix", "title suffix",
                        "generate suffix"
                    ],
                    "examples": [
                        "faker.person.suffix() // 'DDS'"
                    ]
                }
            },
            "full_name": {
                "fullName": {
                    "description": "Generates complete name with optional components",
                    "patterns": [
                        "full name", "complete name",
                        "generate name"
                    ],
                    "examples": [
                        "faker.person.fullName() // 'Allen Brown'",
                        "faker.person.fullName({ firstName: 'Joann' }) // 'Joann Osinski'",
                        "faker.person.fullName({ sex: 'female' }) // 'Mrs. Marcella Huels'"
                    ],
                    "parameters": {
                        "firstName": "optional - string - Specific first name to use",
                        "lastName": "optional - string - Specific last name to use",
                        "sex": "optional - 'female' | 'male' - Sex for name components"
                    }
                }
            },
            "personal_info": {
                "gender": {
                    "description": "Returns random gender identity",
                    "patterns": [
                        "gender", "gender identity",
                        "generate gender"
                    ],
                    "examples": [
                        "faker.person.gender() // 'Trans*Man'"
                    ]
                },
                "sex": {
                    "description": "Returns random binary sex designation",
                    "patterns": [
                        "sex", "biological sex",
                        "generate sex"
                    ],
                    "examples": [
                        "faker.person.sex() // 'female'"
                    ]
                },
                "sexType": {
                    "description": "Returns random sex type for parameter use",
                    "patterns": [
                        "sex type", "sex parameter",
                        "generate sex type"
                    ],
                    "examples": [
                        "faker.person.sexType() // Sex.Female"
                    ]
                },
                "bio": {
                    "description": "Returns random short biography",
                    "patterns": [
                        "biography", "profile bio",
                        "generate bio"
                    ],
                    "examples": [
                        "faker.person.bio() // 'oatmeal advocate, veteran 🐠'"
                    ]
                },
                "zodiacSign": {
                    "description": "Returns random zodiac sign",
                    "patterns": [
                        "zodiac", "star sign",
                        "astrological sign"
                    ],
                    "examples": [
                        "faker.person.zodiacSign() // 'Pisces'"
                    ]
                }
            },
            "job_info": {
                "jobTitle": {
                    "description": "Generates random job title",
                    "patterns": [
                        "job title", "position title",
                        "occupation title"
                    ],
                    "examples": [
                        "faker.person.jobTitle() // 'Global Accounts Engineer'"
                    ]
                },
                "jobDescriptor": {
                    "description": "Returns random job descriptor",
                    "patterns": [
                        "job descriptor", "role descriptor",
                        "position descriptor"
                    ],
                    "examples": [
                        "faker.person.jobDescriptor() // 'Customer'"
                    ]
                },
                "jobArea": {
                    "description": "Returns random job area/department",
                    "patterns": [
                        "job area", "department",
                        "work area"
                    ],
                    "examples": [
                        "faker.person.jobArea() // 'Brand'"
                    ]
                },
                "jobType": {
                    "description": "Returns random job type/level",
                    "patterns": [
                        "job type", "position level",
                        "role type"
                    ],
                    "examples": [
                        "faker.person.jobType() // 'Assistant'"
                    ]
                }
            }
        }
    }
    return docs