def load_faker_system_docs():
    docs = {
        "system": {
            "file_operations": {
                "fileName": {
                    "description": "Generates random file name with extensions",
                    "examples": [
                        "faker.system.fileName() // 'faithfully_calculating.u8mdn'",
                        "faker.system.fileName({ extensionCount: 2 }) // 'times_after.swf.ntf'"
                    ],
                    "parameters": {
                        "extensionCount": "optional - number | { min, max } (default: 1)"
                    }
                },
                "commonFileName": {
                    "description": "Generates file name with common extension",
                    "examples": [
                        "faker.system.commonFileName() // 'dollar.jpg'",
                        "faker.system.commonFileName('txt') // 'global_borders_wyoming.txt'"
                    ],
                    "parameters": {
                        "extension": "optional - string - Specific extension to use"
                    }
                },
                "fileExt": {
                    "description": "Returns file extension for given mime-type",
                    "examples": [
                        "faker.system.fileExt() // 'emf'",
                        "faker.system.fileExt('application/json') // 'json'"
                    ],
                    "parameters": {
                        "mimeType": "optional - string - MIME type to get extension for"
                    }
                }
            },
            "mime_types": {
                "mimeType": {
                    "description": "Returns random MIME type",
                    "examples": [
                        "faker.system.mimeType() // 'video/vnd.vivo'"
                    ]
                },
                "commonFileType": {
                    "description": "Returns common file type (video, audio, etc)",
                    "examples": [
                        "faker.system.commonFileType() // 'audio'"
                    ]
                },
                "fileType": {
                    "description": "Returns random file type",
                    "examples": [
                        "faker.system.fileType() // 'message'"
                    ]
                }
            },
            "paths": {
                "directoryPath": {
                    "description": "Returns random directory path",
                    "examples": [
                        "faker.system.directoryPath() // '/etc/mail'"
                    ]
                },
                "filePath": {
                    "description": "Returns full file path",
                    "examples": [
                        "faker.system.filePath() // '/usr/local/src/money.dotx'"
                    ]
                }
            },
            "network": {
                "networkInterface": {
                    "description": "Returns random network interface name",
                    "examples": [
                        "faker.system.networkInterface() // 'enp0s3'",
                        "faker.system.networkInterface({ interfaceType: 'wl' }) // 'wlo1'",
                        "faker.system.networkInterface({ interfaceSchema: 'mac' })"
                    ],
                    "parameters": {
                        "interfaceType": "optional - 'en'|'wl'|'ww'",
                        "interfaceSchema": "optional - 'index'|'slot'|'mac'|'pci'"
                    }
                }
            },
            "versions": {
                "semver": {
                    "description": "Returns semantic version number",
                    "examples": [
                        "faker.system.semver() // '1.15.2'"
                    ]
                }
            },
            "scheduling": {
                "cron": {
                    "description": "Returns cron expression",
                    "examples": [
                        "faker.system.cron() // '45 23 * * 6'",
                        "faker.system.cron({ includeYear: true }) // '45 23 * * 6 2067'",
                        "faker.system.cron({ includeNonStandard: true }) // '@yearly'"
                    ],
                    "parameters": {
                        "includeYear": "optional - boolean (default: false)",
                        "includeNonStandard": "optional - boolean (default: false)"
                    }
                }
            }
        }
    }
    return docs