def load_faker_date_docs():
    docs = {
        "date": {
            "anytime": {
                "description": "Generates a random date that can be either in the past or future",
                "patterns": [
                    "random date", "any date",
                    "generate date"
                ],
                "examples": [
                    "faker.date.anytime() // '2022-07-31T01:33:29.567Z'"
                ],
                "parameters": {
                    "refDate": "optional - string | Date | number - Reference date (default: faker.defaultRefDate())"
                }
            },
            "past": {
                "description": "Generates a random date in the past",
                "patterns": [
                    "past date", "previous date",
                    "generate past date"
                ],
                "examples": [
                    "faker.date.past() // '2021-12-03T05:40:44.408Z'",
                    "faker.date.past({ years: 10 }) // '2017-10-25T21:34:19.488Z'",
                    "faker.date.past({ years: 10, refDate: '2020-01-01T00:00:00.000Z' })"
                ],
                "parameters": {
                    "years": "optional - number (default: 1) - Range of years in the past",
                    "refDate": "optional - string | Date | number - Reference date"
                }
            },
            "future": {
                "description": "Generates a random date in the future",
                "patterns": [
                    "future date", "upcoming date",
                    "generate future date"
                ],
                "examples": [
                    "faker.date.future() // '2022-11-19T05:52:49.100Z'",
                    "faker.date.future({ years: 10 }) // '2030-11-23T09:38:28.710Z'",
                    "faker.date.future({ years: 10, refDate: '2020-01-01T00:00:00.000Z' })"
                ],
                "parameters": {
                    "years": "optional - number (default: 1) - Range of years in the future",
                    "refDate": "optional - string | Date | number - Reference date"
                }
            },
            "between": {
                "description": "Generates a random date between two dates",
                "patterns": [
                    "date between", "date range",
                    "generate date between"
                ],
                "examples": [
                    "faker.date.between({ from: '2020-01-01T00:00:00.000Z', to: '2030-01-01T00:00:00.000Z' })"
                ],
                "parameters": {
                    "from": "required - string | Date | number - Start date",
                    "to": "required - string | Date | number - End date"
                },
                "notes": "Throws error if 'from' is after 'to'"
            },
            "betweens": {
                "description": "Generates multiple random dates between two dates, sorted chronologically",
                "patterns": [
                    "multiple dates", "date ranges",
                    "generate multiple dates"
                ],
                "examples": [
                    "faker.date.betweens({ from: '2020-01-01', to: '2030-01-01' })",
                    "faker.date.betweens({ from: '2020-01-01', to: '2030-01-01', count: 2 })",
                    "faker.date.betweens({ from: '2020-01-01', to: '2030-01-01', count: { min: 2, max: 5 }})"
                ],
                "parameters": {
                    "from": "required - string | Date | number - Start date",
                    "to": "required - string | Date | number - End date",
                    "count": "optional - number | { min: number, max: number } (default: 3) - Number of dates"
                }
            },
            "recent": {
                "description": "Generates a random date in the recent past (days)",
                "patterns": [
                    "recent date", "last few days",
                    "generate recent date"
                ],
                "examples": [
                    "faker.date.recent() // '2022-02-04T02:09:35.077Z'",
                    "faker.date.recent({ days: 10 }) // '2022-01-29T06:12:12.829Z'",
                    "faker.date.recent({ days: 10, refDate: '2020-01-01T00:00:00.000Z' })"
                ],
                "parameters": {
                    "days": "optional - number (default: 1) - Range of days in the past",
                    "refDate": "optional - string | Date | number - Reference date"
                }
            },
            "soon": {
                "description": "Generates a random date in the near future (days)",
                "patterns": [
                    "soon date", "coming days",
                    "generate soon date"
                ],
                "examples": [
                    "faker.date.soon() // '2022-02-05T09:55:39.216Z'",
                    "faker.date.soon({ days: 10 }) // '2022-02-11T05:14:39.138Z'",
                    "faker.date.soon({ days: 10, refDate: '2020-01-01T00:00:00.000Z' })"
                ],
                "parameters": {
                    "days": "optional - number (default: 1) - Range of days in the future",
                    "refDate": "optional - string | Date | number - Reference date"
                }
            },
            "birthdate": {
                "description": "Returns a random birthdate with customizable age/year ranges",
                "patterns": [
                    "birthdate", "date of birth",
                    "generate birthdate"
                ],
                "examples": [
                    "faker.date.birthdate() // '1977-07-10T01:37:30.719Z'",
                    "faker.date.birthdate({ mode: 'age', min: 18, max: 65 }) // '2003-11-02T20:03:20.116Z'",
                    "faker.date.birthdate({ mode: 'year', min: 1900, max: 2000 }) // '1940-08-20T08:53:07.538Z'"
                ],
                "parameters": {
                    "mode": "optional - 'age' | 'year' (default: 'age') - Generation mode",
                    "min": "optional - number (default: 18) - Minimum age/year",
                    "max": "optional - number (default: 80) - Maximum age/year",
                    "refDate": "optional - string | Date | number - Reference date (only for 'age' mode)"
                }
            },
            "month": {
                "description": "Returns a random month name",
                "patterns": [
                    "month name", "month",
                    "generate month"
                ],
                "examples": [
                    "faker.date.month() // 'October'",
                    "faker.date.month({ abbreviated: true }) // 'Feb'",
                    "faker.date.month({ context: true }) // 'June'"
                ],
                "parameters": {
                    "abbreviated": "optional - boolean (default: false) - Return abbreviated name",
                    "context": "optional - boolean (default: false) - Use contextual form (locale-specific)"
                }
            },
            "weekday": {
                "description": "Returns a random weekday name",
                "patterns": [
                    "weekday name", "day of week",
                    "generate weekday"
                ],
                "examples": [
                    "faker.date.weekday() // 'Monday'",
                    "faker.date.weekday({ abbreviated: true }) // 'Thu'",
                    "faker.date.weekday({ context: true }) // 'Thursday'"
                ],
                "parameters": {
                    "abbreviated": "optional - boolean (default: false) - Return abbreviated name",
                    "context": "optional - boolean (default: false) - Use contextual form (locale-specific)"
                }
            }
        }
    }
    return docs