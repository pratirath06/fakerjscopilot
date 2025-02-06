def load_faker_finance_docs():
    docs = {
        "finance": {
            "accountNumber": {
                "description": "Generates a random account number",
                "patterns": [
                    "account number", "bank account",
                    "generate account number"
                ],
                "examples": [
                    "faker.finance.accountNumber() // '92842238'",
                    "faker.finance.accountNumber(5) // '32564'",
                    "faker.finance.accountNumber({ length: 5 }) // '32564'"
                ],
                "parameters": {
                    "length": "optional - number (default: 8) - The length of the account number"
                }
            },
            "accountName": {
                "description": "Generates a random account name",
                "patterns": [
                    "account name", "bank account name",
                    "generate account name"
                ],
                "examples": [
                    "faker.finance.accountName() // 'Personal Loan Account'"
                ]
            },
            "routingNumber": {
                "description": "Generates a random routing number",
                "patterns": [
                    "routing number", "bank routing",
                    "generate routing number"
                ],
                "examples": [
                    "faker.finance.routingNumber() // '522814402'"
                ]
            },
            "amount": {
                "description": "Generates a random amount between the given bounds (inclusive)",
                "patterns": [
                    "amount", "money amount", "payment amount",
                    "generate amount"
                ],
                "examples": [
                    "faker.finance.amount() // '617.87'",
                    "faker.finance.amount({ min: 5, max: 10 }) // '5.53'",
                    "faker.finance.amount({ min: 5, max: 10, dec: 0 }) // '8'",
                    "faker.finance.amount({ min: 5, max: 10, dec: 2, symbol: '$' }) // '$5.85'"
                ],
                "parameters": {
                    "min": "optional - number (default: 0) - The lower bound",
                    "max": "optional - number (default: 1000) - The upper bound",
                    "dec": "optional - number (default: 2) - Number of decimal places",
                    "symbol": "optional - string (default: '') - Currency symbol",
                    "autoFormat": "optional - boolean (default: false) - Use Number.toLocaleString()"
                }
            },
            "transactionType": {
                "description": "Returns a random transaction type",
                "patterns": [
                    "transaction type", "payment type",
                    "generate transaction type"
                ],
                "examples": [
                    "faker.finance.transactionType() // 'payment'"
                ]
            },
            "currency": {
                "description": "Returns a random currency object with code, name and symbol",
                "patterns": [
                    "currency", "currency info",
                    "generate currency"
                ],
                "examples": [
                    "faker.finance.currency() // { code: 'USD', name: 'US Dollar', symbol: '$' }"
                ]
            },
            "bitcoinAddress": {
                "description": "Generates a random Bitcoin address",
                "patterns": [
                    "bitcoin address", "btc address",
                    "generate bitcoin address"
                ],
                "examples": [
                    "faker.finance.bitcoinAddress() // '1TeZEFLmGPLEQrSRdAcnZLoWwYeiHwmRog'",
                    "faker.finance.bitcoinAddress({ type: 'bech32' }) // 'bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4'"
                ],
                "parameters": {
                    "type": "optional - string ('legacy', 'sewgit', 'bech32', 'taproot')",
                    "network": "optional - string ('mainnet', 'testnet') (default: 'mainnet')"
                }
            },
            "creditCardNumber": {
                "description": "Generates a random credit card number",
                "patterns": [
                    "credit card", "credit card number", "cc number",
                    "generate credit card"
                ],
                "examples": [
                    "faker.finance.creditCardNumber() // '4427163488662'",
                    "faker.finance.creditCardNumber('visa') // '4882664999007'",
                    "faker.finance.creditCardNumber({ issuer: 'visa' }) // '4882664999007'"
                ],
                "parameters": {
                    "issuer": "optional - string (card issuer name or format pattern)"
                }
            },
            "creditCardCVV": {
                "description": "Generates a random credit card CVV",
                "patterns": [
                    "cvv", "card cvv", "security code",
                    "generate cvv"
                ],
                "examples": [
                    "faker.finance.creditCardCVV() // '506'"
                ]
            },
            "iban": {
                "description": "Generates a random IBAN (International Bank Account Number)",
                "patterns": [
                    "iban", "bank account number",
                    "generate iban"
                ],
                "examples": [
                    "faker.finance.iban() // 'TR736918640040966092800056'",
                    "faker.finance.iban({ formatted: true }) // 'FR20 8008 2330 8984 74S3 Z620 224'",
                    "faker.finance.iban({ formatted: true, countryCode: 'DE' }) // 'DE84 1022 7075 0900 1170 01'"
                ],
                "parameters": {
                    "formatted": "optional - boolean (default: false) - Format the IBAN with spaces",
                    "countryCode": "optional - string - Country code for the IBAN"
                }
            },
            "bic": {
                "description": "Generates a random SWIFT/BIC code based on ISO-9362 format",
                "patterns": [
                    "bic", "swift code", "bank identifier",
                    "generate bic"
                ],
                "examples": [
                    "faker.finance.bic() // 'WYAUPGX1'",
                    "faker.finance.bic({ includeBranchCode: true }) // 'KCAUPGR1432'"
                ],
                "parameters": {
                    "includeBranchCode": "optional - boolean (default: random) - Include branch code"
                }
            },
            "ethereumAddress": {
                "description": "Creates a random, non-checksum Ethereum address",
                "patterns": [
                    "ethereum address", "eth address",
                    "generate ethereum address"
                ],
                "examples": [
                    "faker.finance.ethereumAddress() // '0xf03dfeecbafc5147241cc4c4ca20b3c9dfd04c4a'"
                ]
            },
            "litecoinAddress": {
                "description": "Generates a random Litecoin address",
                "patterns": [
                    "litecoin address", "ltc address",
                    "generate litecoin address"
                ],
                "examples": [
                    "faker.finance.litecoinAddress() // 'MoQaSTGWBRXkWfyxKbNKuPrAWGELzcW'"
                ]
            },
            "pin": {
                "description": "Generates a random PIN number",
                "patterns": [
                    "pin", "pin number",
                    "generate pin"
                ],
                "examples": [
                    "faker.finance.pin() // '5067'",
                    "faker.finance.pin(6) // '213789'",
                    "faker.finance.pin({ length: 6 }) // '213789'"
                ],
                "parameters": {
                    "length": "optional - number (default: 4) - Length of the PIN"
                }
            },
            "transactionDescription": {
                "description": "Generates a random transaction description",
                "patterns": [
                    "transaction description", "payment description",
                    "generate transaction description"
                ],
                "examples": [
                    "faker.finance.transactionDescription() // 'payment transaction at Emard LLC using card ending with ****9187 for HNL 506.57 in account ***2584.'"
                ]
            }
        }
    }
    return docs