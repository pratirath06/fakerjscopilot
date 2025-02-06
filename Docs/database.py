def load_faker_database_docs():
    docs = {
        "database": {
            "column": {
                "description": "Returns a random database column name",
                "patterns": [
                    "column name", "database column", "field name",
                    "generate column"
                ],
                "examples": [
                    "faker.database.column() // 'createdAt'"
                ],
                "notes": "Returns common column names used in relational databases"
            },
            "type": {
                "description": "Returns a random database column type",
                "patterns": [
                    "data type", "column type", "field type",
                    "generate type"
                ],
                "examples": [
                    "faker.database.type() // 'timestamp'"
                ],
                "notes": "Returns standard SQL data types used in relational databases"
            },
            "collation": {
                "description": "Returns a random database collation",
                "patterns": [
                    "collation", "character set", "sorting rules",
                    "generate collation"
                ],
                "examples": [
                    "faker.database.collation() // 'utf8_unicode_ci'"
                ],
                "notes": "Returns common database collations used for string comparison and sorting"
            },
            "engine": {
                "description": "Returns a random database engine",
                "patterns": [
                    "database engine", "storage engine",
                    "db engine", "generate engine"
                ],
                "examples": [
                    "faker.database.engine() // 'ARCHIVE'"
                ],
                "notes": "Returns names of database storage engines (e.g., InnoDB, MyISAM, ARCHIVE)"
            },
            "mongodbObjectId": {
                "description": "Returns a MongoDB ObjectId string",
                "patterns": [
                    "mongodb id", "object id", "mongo id",
                    "generate mongodb id"
                ],
                "examples": [
                    "faker.database.mongodbObjectId() // 'e175cac316a79afdd0ad3afb'"
                ],
                "notes": "Generates a 24-character hexadecimal string representing a MongoDB ObjectId"
            }
        },
        "usage_categories": {
            "relational": {
                "description": "For traditional relational database needs",
                "methods": [
                    "column()",
                    "type()",
                    "collation()",
                    "engine()"
                ]
            },
            "nosql": {
                "description": "For NoSQL database needs",
                "methods": [
                    "mongodbObjectId()"
                ]
            }
        }
    }
    return docs