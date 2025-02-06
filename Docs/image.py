def load_faker_image_docs():
    docs = {
        "image": {
            "avatar": {
                "description": "Generates a random avatar image URL",
                "patterns": [
                    "avatar", "profile picture",
                    "user avatar", "generate avatar"
                ],
                "examples": [
                    "faker.image.avatar() // 'https://avatars.githubusercontent.com/u/97165289'"
                ],
                "notes": "Currently uses GitHub avatars"
            },
            "avatarGitHub": {
                "description": "Generates a random avatar from GitHub",
                "patterns": [
                    "github avatar", "github profile",
                    "github picture"
                ],
                "examples": [
                    "faker.image.avatarGitHub() // 'https://avatars.githubusercontent.com/u/97165289'"
                ]
            },
            "url": {
                "description": "Generates a random image URL from various providers",
                "patterns": [
                    "image url", "random image",
                    "generate image url"
                ],
                "examples": [
                    "faker.image.url() // 'https://loremflickr.com/640/480?lock=1234'"
                ],
                "parameters": {
                    "width": "optional - number - Image width (default: random 1-3999)",
                    "height": "optional - number - Image height (default: random 1-3999)"
                },
                "notes": "Randomly uses either LoremFlickr or Picsum Photos"
            },
            "urlLoremFlickr": {
                "description": "Generates a random image URL from LoremFlickr",
                "patterns": [
                    "lorem flickr", "flickr image",
                    "category image"
                ],
                "examples": [
                    "faker.image.urlLoremFlickr() // 'https://loremflickr.com/640/480?lock=1234'",
                    "faker.image.urlLoremFlickr({ category: 'nature' }) // 'https://loremflickr.com/640/480/nature?lock=1234'"
                ],
                "parameters": {
                    "width": "optional - number - Image width (default: random 1-3999)",
                    "height": "optional - number - Image height (default: random 1-3999)",
                    "category": "optional - string - Image category"
                }
            },
            "urlPicsumPhotos": {
                "description": "Generates a random image URL from Picsum Photos",
                "patterns": [
                    "picsum", "lorem picsum",
                    "random photo"
                ],
                "examples": [
                    "faker.image.urlPicsumPhotos() // 'https://picsum.photos/seed/NWbJM2B/640/480'",
                    "faker.image.urlPicsumPhotos({ grayscale: true }) // '...?grayscale'",
                    "faker.image.urlPicsumPhotos({ blur: 4 }) // '...?blur=4'"
                ],
                "parameters": {
                    "width": "optional - number - Image width (default: random 1-3999)",
                    "height": "optional - number - Image height (default: random 1-3999)",
                    "grayscale": "optional - boolean - Convert to grayscale",
                    "blur": "optional - number (0-10) - Blur amount"
                }
            },
            "dataUri": {
                "description": "Generates a data URI containing an SVG image",
                "patterns": [
                    "data uri", "svg image",
                    "embedded image"
                ],
                "examples": [
                    "faker.image.dataUri() // 'data:image/svg+xml;charset=UTF-8,...'",
                    "faker.image.dataUri({ type: 'svg-base64' }) // 'data:image/svg+xml;base64,...'"
                ],
                "parameters": {
                    "width": "optional - number - Image width (default: random 1-3999)",
                    "height": "optional - number - Image height (default: random 1-3999)",
                    "color": "optional - string - Background color (default: random)",
                    "type": "optional - 'svg-uri' | 'svg-base64' - Encoding type"
                },
                "notes": "Generates actual image data, not just a URL"
            }
        },
        "usage_categories": {
            "avatars": {
                "description": "For generating user profile pictures",
                "methods": [
                    "avatar()",
                    "avatarGitHub()"
                ]
            },
            "random_images": {
                "description": "For generating random image URLs",
                "methods": [
                    "url()",
                    "urlLoremFlickr()",
                    "urlPicsumPhotos()"
                ]
            },
            "embedded_images": {
                "description": "For generating embedded image data",
                "methods": [
                    "dataUri()"
                ]
            }
        }
    }
    return docs