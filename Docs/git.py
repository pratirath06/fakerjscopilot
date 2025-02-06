def load_faker_git_docs():
    docs = {
        "git": {
            "branch": {
                "description": "Generates a random git branch name",
                "patterns": [
                    "branch name", "git branch",
                    "generate branch"
                ],
                "examples": [
                    "faker.git.branch() // 'feed-parse'"
                ],
                "notes": "Combines hacker nouns and verbs to create branch names"
            },
            "commitEntry": {
                "description": "Generates a random commit entry as printed by git log",
                "patterns": [
                    "commit entry", "git log",
                    "commit details", "generate commit entry"
                ],
                "examples": [
                    "faker.git.commitEntry()",
                    "// commit fe8c38a965d13d9794eb36918cb24cebe49a45c2",
                    "// Author: Marion Becker <Marion_Becker49@gmail.com>",
                    "// Date: Mon Nov 7 05:38:37 2022 -0600",
                    "//",
                    "//     generate open-source system"
                ],
                "parameters": {
                    "merge": "optional - boolean (default: 20% true) - Include merge message line",
                    "eol": "optional - 'LF' | 'CRLF' (default: 'CRLF') - End of line character",
                    "refDate": "optional - string | Date | number - Reference date for commit"
                },
                "notes": "Generates complete git log entries including hash, author, date, and message"
            },
            "commitMessage": {
                "description": "Generates a random commit message",
                "patterns": [
                    "commit message", "git message",
                    "generate message"
                ],
                "examples": [
                    "faker.git.commitMessage() // 'reboot cross-platform driver'"
                ],
                "notes": "Creates messages using hacker verb + adjective + noun pattern"
            },
            "commitDate": {
                "description": "Generates a date string formatted like git log output",
                "patterns": [
                    "commit date", "git date",
                    "generate commit date"
                ],
                "examples": [
                    "faker.git.commitDate() // 'Mon Nov 7 14:40:58 2022 +0600'",
                    "faker.git.commitDate({ refDate: '2020-01-01' }) // 'Tue Dec 31 05:40:59 2019 -0400'"
                ],
                "parameters": {
                    "refDate": "optional - string | Date | number - Reference date for commit"
                },
                "notes": "Uses git's standard date format: Day Month DD HH:MM:SS YYYY +ZZZZ"
            },
            "commitSha": {
                "description": "Generates a random commit SHA hash",
                "patterns": [
                    "commit sha", "git hash",
                    "commit hash", "generate sha"
                ],
                "examples": [
                    "faker.git.commitSha() // '2c6e3880fd94ddb7ef72d34e683cdc0c47bec6e6'",
                    "faker.git.commitSha({ length: 7 }) // 'dbee57b'",
                    "faker.git.commitSha({ length: 8 }) // '0e52376a'"
                ],
                "parameters": {
                    "length": "optional - number (default: 40) - Length of the SHA hash"
                },
                "notes": [
                    "Default length is 40 characters (full SHA-1)",
                    "Common short lengths: 7 (GitHub), 8 (GitLab)"
                ]
            }
        },
        "usage_examples": {
            "complete_log": {
                "description": "Generate a complete git log entry",
                "code": "faker.git.commitEntry({ merge: true })"
            },
            "short_hash": {
                "description": "Generate GitHub-style short hash",
                "code": "faker.git.commitSha({ length: 7 })"
            },
            "branch_name": {
                "description": "Generate feature branch name",
                "code": "faker.git.branch()"
            }
        }
    }
    return docs