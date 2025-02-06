def load_faker_color_docs():
    docs = {
        "color": {
            "human": {
                "description": "Returns a random human-readable color name",
                "patterns": [
                    "color name", "named color",
                    "human readable color"
                ],
                "examples": [
                    "faker.color.human() // 'red'"
                ]
            },
            "rgb": {
                "description": "Returns an RGB color in various formats",
                "patterns": [
                    "rgb color", "rgb", "hex color",
                    "generate rgb"
                ],
                "examples": [
                    "faker.color.rgb() // '#0d7f26'",
                    "faker.color.rgb({ prefix: '0x' }) // '0x9ddc8b'",
                    "faker.color.rgb({ casing: 'upper' }) // '#B8A51E'",
                    "faker.color.rgb({ format: 'css' }) // 'rgb(216, 17, 192)'",
                    "faker.color.rgb({ format: 'decimal' }) // [64, 192, 174]",
                    "faker.color.rgb({ includeAlpha: true }) // '#f96efb5e'",
                    "faker.color.rgb({ format: 'css', includeAlpha: true }) // 'rgba(180, 158, 24, 0.75)'"
                ],
                "parameters": {
                    "prefix": "optional - string (default: '#') - Prefix for hex format",
                    "casing": "optional - 'lower' | 'upper' | 'mixed' (default: 'lower') - Case for hex format",
                    "format": "optional - 'hex' | 'css' | 'binary' | 'decimal' (default: 'hex') - Output format",
                    "includeAlpha": "optional - boolean (default: false) - Include alpha channel"
                }
            },
            "cmyk": {
                "description": "Returns a CMYK color",
                "patterns": [
                    "cmyk color", "cmyk",
                    "generate cmyk"
                ],
                "examples": [
                    "faker.color.cmyk() // [0.31, 0.52, 0.32, 0.43]",
                    "faker.color.cmyk({ format: 'css' }) // 'cmyk(35%, 39%, 68%, 60%)'",
                    "faker.color.cmyk({ format: 'binary' }) // '00110010 00001000 01110110 00110010'"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format"
                }
            },
            "hsl": {
                "description": "Returns an HSL color",
                "patterns": [
                    "hsl color", "hsl",
                    "generate hsl"
                ],
                "examples": [
                    "faker.color.hsl() // [201, 0.23, 0.32]",
                    "faker.color.hsl({ format: 'css' }) // 'hsl(0deg 100% 80%)'",
                    "faker.color.hsl({ includeAlpha: true }) // [300, 0.21, 0.52, 0.28]",
                    "faker.color.hsl({ format: 'css', includeAlpha: true }) // 'hsl(0deg 100% 50% / 0.5)'"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format",
                    "includeAlpha": "optional - boolean (default: false) - Include alpha channel"
                }
            },
            "hwb": {
                "description": "Returns an HWB (Hue, Whiteness, Blackness) color",
                "patterns": [
                    "hwb color", "hwb",
                    "generate hwb"
                ],
                "examples": [
                    "faker.color.hwb() // [201, 0.21, 0.31]",
                    "faker.color.hwb({ format: 'css' }) // 'hwb(354 72% 41%)'",
                    "faker.color.hwb({ format: 'binary' }) // (8-32 bits x 3)"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format"
                }
            },
            "lab": {
                "description": "Returns a LAB (CIELAB) color",
                "patterns": [
                    "lab color", "cielab", "lab",
                    "generate lab"
                ],
                "examples": [
                    "faker.color.lab() // [0.832133, -80.3245, 100.1234]",
                    "faker.color.lab({ format: 'css' }) // 'lab(29.2345% 39.3825 20.0664)'",
                    "faker.color.lab({ format: 'binary' }) // (8-32 bits x 3)"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format"
                }
            },
            "lch": {
                "description": "Returns an LCH color (Lightness, Chroma, Hue)",
                "patterns": [
                    "lch color", "lch",
                    "generate lch"
                ],
                "examples": [
                    "faker.color.lch() // [0.522345, 72.2, 56.2]",
                    "faker.color.lch({ format: 'css' }) // 'lch(52.2345% 72.2 56.2)'",
                    "faker.color.lch({ format: 'binary' }) // (8-32 bits x 3)"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format"
                },
                "notes": "Chroma is bounded to 230 as anything above won't make a noticeable difference in browsers"
            },
            "colorByCSSColorSpace": {
                "description": "Returns a random color in specified CSS color space",
                "patterns": [
                    "css color space", "color space",
                    "generate color space"
                ],
                "examples": [
                    "faker.color.colorByCSSColorSpace() // [0.93, 1, 0.82]",
                    "faker.color.colorByCSSColorSpace({ format: 'css', space: 'display-p3' }) // 'color(display-p3 0.12 1 0.23)'",
                    "faker.color.colorByCSSColorSpace({ format: 'binary' }) // (8-32 bits x 3)"
                ],
                "parameters": {
                    "format": "optional - 'decimal' | 'css' | 'binary' (default: 'decimal') - Output format",
                    "space": "optional - 'sRGB' | 'display-p3' | 'rec2020' | 'a98-rgb' | 'prophoto-rgb' (default: 'sRGB') - Color space"
                }
            },
            "space": {
                "description": "Returns a random color space name",
                "patterns": [
                    "color space name", "space name",
                    "generate space"
                ],
                "examples": [
                    "faker.color.space() // 'sRGB'"
                ]
            },
            "cssSupportedFunction": {
                "description": "Returns a random CSS-supported color function name",
                "patterns": [
                    "css function", "color function",
                    "generate css function"
                ],
                "examples": [
                    "faker.color.cssSupportedFunction() // 'rgb'"
                ]
            },
            "cssSupportedSpace": {
                "description": "Returns a random CSS-supported color space name",
                "patterns": [
                    "css space", "supported space",
                    "generate css space"
                ],
                "examples": [
                    "faker.color.cssSupportedSpace() // 'display-p3'"
                ]
            }
        }
    }
    return docs