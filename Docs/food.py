def load_faker_food_docs():
    docs = {
        "food": {
            "adjective": {
                "description": "Generates a random dish adjective",
                "patterns": [
                    "food adjective", "dish adjective",
                    "food description", "generate food adjective"
                ],
                "examples": [
                    "faker.food.adjective() // 'crispy'"
                ],
                "notes": "Returns common adjectives used to describe food"
            },
            "description": {
                "description": "Generates a random detailed dish description",
                "patterns": [
                    "dish description", "food description",
                    "menu description", "generate food description"
                ],
                "examples": [
                    "faker.food.description() // 'An exquisite ostrich roast, infused with the essence of longan, slow-roasted to bring out its natural flavors and served with a side of creamy red cabbage'"
                ],
                "notes": "Generates complete, restaurant-style menu descriptions"
            },
            "dish": {
                "description": "Generates a random dish name",
                "patterns": [
                    "dish name", "food name",
                    "menu item", "generate dish name"
                ],
                "examples": [
                    "faker.food.dish() // 'Tagine-Rubbed Venison Salad'"
                ],
                "notes": "50% chance of returning a specific dish, 50% chance of generating a pattern-based dish name"
            },
            "ethnicCategory": {
                "description": "Generates a random food's ethnic category",
                "patterns": [
                    "cuisine type", "food origin",
                    "ethnic food", "generate cuisine type"
                ],
                "examples": [
                    "faker.food.ethnicCategory() // 'Italian'"
                ],
                "notes": "Returns common cuisine categories/origins"
            },
            "fruit": {
                "description": "Generates a random fruit name",
                "patterns": [
                    "fruit", "fruit name",
                    "fruit type", "generate fruit"
                ],
                "examples": [
                    "faker.food.fruit() // 'lemon'"
                ],
                "notes": "Returns common fruit names"
            },
            "ingredient": {
                "description": "Generates a random ingredient name",
                "patterns": [
                    "ingredient", "food ingredient",
                    "recipe ingredient", "generate ingredient"
                ],
                "examples": [
                    "faker.food.ingredient() // 'butter'"
                ],
                "notes": "Returns common cooking ingredients"
            },
            "meat": {
                "description": "Generates a random meat type",
                "patterns": [
                    "meat", "meat type",
                    "protein", "generate meat"
                ],
                "examples": [
                    "faker.food.meat() // 'venison'"
                ],
                "notes": "Returns various types of meat and protein"
            },
            "spice": {
                "description": "Generates a random spice name",
                "patterns": [
                    "spice", "seasoning",
                    "herb", "generate spice"
                ],
                "examples": [
                    "faker.food.spice() // 'chilli'"
                ],
                "notes": "Returns common spices and seasonings"
            },
            "vegetable": {
                "description": "Generates a random vegetable name",
                "patterns": [
                    "vegetable", "veggie",
                    "produce", "generate vegetable"
                ],
                "examples": [
                    "faker.food.vegetable() // 'broccoli'"
                ],
                "notes": "Returns common vegetable names"
            }
        },
        "usage_categories": {
            "menu_generation": {
                "description": "For generating restaurant menu content",
                "methods": [
                    "dish()",
                    "description()",
                    "adjective()"
                ]
            },
            "ingredients": {
                "description": "For generating recipe ingredients",
                "methods": [
                    "ingredient()",
                    "spice()",
                    "vegetable()",
                    "fruit()",
                    "meat()"
                ]
            },
            "categorization": {
                "description": "For food categorization",
                "methods": [
                    "ethnicCategory()"
                ]
            }
        }
    }
    return docs