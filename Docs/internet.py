def load_faker_internet_docs():
    docs = {
        "internet": {
            "user_accounts": {
                "email": {
                    "description": "Generates email address using person's name",
                    "patterns": [
                        "email address", "generate email",
                        "user email"
                    ],
                    "examples": [
                        "faker.internet.email() // 'Kassandra4@hotmail.com'",
                        "faker.internet.email({ firstName: 'Jeanne' }) // 'Jeanne63@yahoo.com'",
                        "faker.internet.email({ firstName: 'John', lastName: 'Doe' }) // 'John.Doe@gmail.com'"
                    ],
                    "parameters": {
                        "firstName": "optional - string - First name to use",
                        "lastName": "optional - string - Last name to use",
                        "provider": "optional - string - Email provider domain",
                        "allowSpecialCharacters": "optional - boolean - Allow special characters in email"
                    }
                },
                "exampleEmail": {
                    "description": "Generates email using example domains (example.com)",
                    "patterns": [
                        "test email", "example email",
                        "safe email"
                    ],
                    "examples": [
                        "faker.internet.exampleEmail() // 'Helmer.Graham23@example.com'",
                        "faker.internet.exampleEmail({ firstName: 'John' }) // 'John96@example.net'"
                    ],
                    "parameters": {
                        "firstName": "optional - string - First name to use",
                        "lastName": "optional - string - Last name to use",
                        "allowSpecialCharacters": "optional - boolean - Allow special characters"
                    }
                },
                "username": {
                    "description": "Generates ASCII username from person's name",
                    "patterns": [
                        "username", "user name", "login name"
                    ],
                    "examples": [
                        "faker.internet.username() // 'Nettie_Zboncak40'",
                        "faker.internet.username({ firstName: 'John' }) // 'John98'",
                        "faker.internet.username({ firstName: 'John', lastName: 'Doe' }) // 'John.Doe'"
                    ],
                    "parameters": {
                        "firstName": "optional - string - First name to use",
                        "lastName": "optional - string - Last name to use"
                    }
                },
                "displayName": {
                    "description": "Generates Unicode display name (can include non-ASCII)",
                    "patterns": [
                        "display name", "profile name",
                        "visible name"
                    ],
                    "examples": [
                        "faker.internet.displayName() // 'Nettie_Zboncak40'",
                        "faker.internet.displayName({ firstName: 'Hélene' }) // 'Hélene98'"
                    ],
                    "parameters": {
                        "firstName": "optional - string - First name to use",
                        "lastName": "optional - string - Last name to use"
                    }
                },
                "password": {
                    "description": "Generates random password (not for actual use)",
                    "patterns": [
                        "password", "generate password",
                        "random password"
                    ],
                    "examples": [
                        "faker.internet.password() // '89G1wJuBLbGziIs'",
                        "faker.internet.password({ length: 20 }) // 'aF55c_8O9kZaPOrysFB_'"
                    ],
                    "parameters": {
                        "length": "optional - number (default: 15) - Password length",
                        "memorable": "optional - boolean (default: false) - Generate memorable password",
                        "pattern": "optional - RegExp - Pattern for chars to match",
                        "prefix": "optional - string - Prefix to use"
                    }
                }
            },
            "web": {
                "protocol": {
                    "description": "Returns random web protocol (http/https)",
                    "examples": [
                        "faker.internet.protocol() // 'http'"
                    ]
                },
                "url": {
                    "description": "Generates random URL",
                    "examples": [
                        "faker.internet.url() // 'https://remarkable-hackwork.info'",
                        "faker.internet.url({ protocol: 'http' }) // 'http://example.com'"
                    ],
                    "parameters": {
                        "protocol": "optional - 'http' | 'https' (default: 'https')",
                        "appendSlash": "optional - boolean - Add trailing slash"
                    }
                },
                "domainName": {
                    "description": "Generates random domain name",
                    "examples": [
                        "faker.internet.domainName() // 'slow-timer.info'"
                    ]
                },
                "domainSuffix": {
                    "description": "Returns random domain suffix",
                    "examples": [
                        "faker.internet.domainSuffix() // 'com'"
                    ]
                },
                "domainWord": {
                    "description": "Generates random domain word",
                    "examples": [
                        "faker.internet.domainWord() // 'close-reality'"
                    ]
                }
            },
            "networking": {
                "ip": {
                    "description": "Generates random IP (v4 or v6) address",
                    "examples": [
                        "faker.internet.ip() // '245.108.222.0'"
                    ]
                },
                "ipv4": {
                    "description": "Generates IPv4 address with optional network",
                    "examples": [
                        "faker.internet.ipv4() // '245.108.222.0'",
                        "faker.internet.ipv4({ network: 'private-a' }) // '10.199.154.205'"
                    ],
                    "parameters": {
                        "network": "optional - IPv4NetworkType - Network type",
                        "cidrBlock": "optional - string - CIDR block"
                    }
                },
                "ipv6": {
                    "description": "Generates IPv6 address",
                    "examples": [
                        "faker.internet.ipv6() // '269f:1230:73e3:318d:842b:daab:326d:897b'"
                    ]
                },
                "port": {
                    "description": "Generates random port number",
                    "examples": [
                        "faker.internet.port() // 9414"
                    ]
                },
                "mac": {
                    "description": "Generates random MAC address",
                    "examples": [
                        "faker.internet.mac() // '32:8e:2e:09:c6:05'"
                    ],
                    "parameters": {
                        "separator": "optional - string (default: ':') - Separator character"
                    }
                }
            },
            "web_content": {
                "color": {
                    "description": "Generates aesthetically pleasing hex color",
                    "examples": [
                        "faker.internet.color() // '#30686e'",
                        "faker.internet.color({ redBase: 100 }) // '#4e5f8b'"
                    ],
                    "parameters": {
                        "redBase": "optional - number - Base red (0-255)",
                        "greenBase": "optional - number - Base green (0-255)",
                        "blueBase": "optional - number - Base blue (0-255)"
                    }
                },
                "userAgent": {
                    "description": "Generates random user agent string",
                    "examples": [
                        "faker.internet.userAgent()"
                    ]
                },
                "emoji": {
                    "description": "Generates random emoji",
                    "examples": [
                        "faker.internet.emoji() // '🥰'",
                        "faker.internet.emoji({ types: ['food', 'nature'] }) // '🥐'"
                    ],
                    "parameters": {
                        "types": "optional - EmojiType[] - Types of emoji to use"
                    }
                }
            },
            "http": {
                "httpMethod": {
                    "description": "Returns random HTTP method",
                    "examples": [
                        "faker.internet.httpMethod() // 'PATCH'"
                    ]
                },
                "httpStatusCode": {
                    "description": "Generates random HTTP status code",
                    "examples": [
                        "faker.internet.httpStatusCode() // 200",
                        "faker.internet.httpStatusCode({ types: ['success'] }) // 200"
                    ],
                    "parameters": {
                        "types": "optional - HTTPStatusCodeType[] - Types of status codes"
                    }
                }
            },
            "jwt": {
                "jwt": {
                    "description": "Generates random JWT (JSON Web Token)",
                    "examples": [
                        "faker.internet.jwt()",
                        "faker.internet.jwt({ header: { alg: 'HS256' }})"
                    ],
                    "parameters": {
                        "header": "optional - object - JWT header fields",
                        "payload": "optional - object - JWT payload fields",
                        "refDate": "optional - Date - Reference date"
                    }
                },
                "jwtAlgorithm": {
                    "description": "Returns random JWT algorithm",
                    "examples": [
                        "faker.internet.jwtAlgorithm() // 'HS256'"
                    ]
                }
            }
        }
    }
    return docs