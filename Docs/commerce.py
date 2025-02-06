def load_faker_commerce_docs():
    docs = {
        "commerce": {
            "department": {
                "description": "Returns a random department inside a shop",
                "patterns": [
                    "department", "shop department", "store department",
                    "generate department"
                ],
                "examples": [
                    "faker.commerce.department() // 'Garden'"
                ]
            },
            "productName": {
                "description": "Generates a random descriptive product name by combining adjective, material, and product",
                "patterns": [
                    "product name", "item name", "full product name",
                    "generate product name"
                ],
                "examples": [
                    "faker.commerce.productName() // 'Incredible Soft Gloves'"
                ],
                "notes": "Combines results from productAdjective(), productMaterial(), and product()"
            },
            "price": {
                "description": "Generates a price between min and max with realistic decimal values",
                "patterns": [
                    "price", "product price", "cost",
                    "generate price"
                ],
                "examples": [
                    "faker.commerce.price() // '828.07'",
                    "faker.commerce.price({ min: 100 }) // '904.19'",
                    "faker.commerce.price({ min: 100, max: 200 }) // '154.55'",
                    "faker.commerce.price({ min: 100, max: 200, dec: 0 }) // '133'",
                    "faker.commerce.price({ min: 100, max: 200, dec: 0, symbol: '$' }) // '$114'"
                ],
                "parameters": {
                    "min": "optional - number (default: 1) - Minimum price",
                    "max": "optional - number (default: 1000) - Maximum price",
                    "dec": "optional - number (default: 2) - Number of decimal places",
                    "symbol": "optional - string (default: '') - Currency symbol"
                },
                "notes": "For realistic pricing, last decimal is weighted: 50% chance of 9, 30% chance of 5, 10% chance of 0, 10% chance random"
            },
            "productAdjective": {
                "description": "Returns an adjective describing a product",
                "patterns": [
                    "product adjective", "item adjective",
                    "generate product adjective"
                ],
                "examples": [
                    "faker.commerce.productAdjective() // 'Handcrafted'"
                ]
            },
            "productMaterial": {
                "description": "Returns a material of a product",
                "patterns": [
                    "product material", "item material",
                    "generate material"
                ],
                "examples": [
                    "faker.commerce.productMaterial() // 'Rubber'"
                ]
            },
            "product": {
                "description": "Returns a short product name",
                "patterns": [
                    "product", "basic product", "item",
                    "generate basic product"
                ],
                "examples": [
                    "faker.commerce.product() // 'Computer'"
                ]
            },
            "productDescription": {
                "description": "Returns a product description",
                "patterns": [
                    "product description", "item description",
                    "generate description"
                ],
                "examples": [
                    "faker.commerce.productDescription() // 'Featuring Phosphorus-enhanced technology, our Fish offers unparalleled Modern performance'"
                ]
            },
            "isbn": {
                "description": "Returns a random ISBN (International Standard Book Number) identifier",
                "patterns": [
                    "isbn", "book number", "isbn code",
                    "generate isbn"
                ],
                "examples": [
                    "faker.commerce.isbn() // '978-0-692-82459-7'",
                    "faker.commerce.isbn(10) // '1-155-36404-X'",
                    "faker.commerce.isbn(13) // '978-1-60808-867-6'",
                    "faker.commerce.isbn({ separator: ' ' }) // '978 0 452 81498 1'",
                    "faker.commerce.isbn({ variant: 10, separator: ' ' }) // '0 940319 49 7'"
                ],
                "parameters": {
                    "variant": "optional - 10 | 13 (default: 13) - ISBN format variant",
                    "separator": "optional - string (default: '-') - Separator character"
                },
                "notes": "Generates valid ISBN-10 or ISBN-13 numbers with correct checksum"
            }
        }
    }
    return docs