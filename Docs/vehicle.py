def load_faker_vehicle_docs():
    docs = {
        "vehicle": {
            "basic_info": {
                "vehicle": {
                    "description": "Returns random vehicle (manufacturer + model)",
                    "examples": [
                        "faker.vehicle.vehicle() // 'BMW Explorer'"
                    ]
                },
                "manufacturer": {
                    "description": "Returns random vehicle manufacturer",
                    "examples": [
                        "faker.vehicle.manufacturer() // 'Ford'"
                    ]
                },
                "model": {
                    "description": "Returns random vehicle model",
                    "examples": [
                        "faker.vehicle.model() // 'Explorer'"
                    ]
                }
            },
            "characteristics": {
                "type": {
                    "description": "Returns vehicle body type",
                    "examples": [
                        "faker.vehicle.type() // 'Coupe'"
                    ]
                },
                "fuel": {
                    "description": "Returns type of fuel",
                    "examples": [
                        "faker.vehicle.fuel() // 'Electric'"
                    ]
                },
                "color": {
                    "description": "Returns vehicle color",
                    "examples": [
                        "faker.vehicle.color() // 'red'"
                    ]
                }
            },
            "identifiers": {
                "vin": {
                    "description": "Generates Vehicle Identification Number (VIN)",
                    "examples": [
                        "faker.vehicle.vin() // 'YV1MH682762184654'"
                    ],
                    "notes": [
                        "17 characters long",
                        "Excludes potentially confusing characters (O,0,I,1,Q)",
                        "Follows standard VIN format"
                    ]
                },
                "vrm": {
                    "description": "Generates Vehicle Registration Mark (VRM)",
                    "examples": [
                        "faker.vehicle.vrm() // 'MF56UPA'"
                    ],
                    "notes": [
                        "UK format: 2 letters + 2 numbers + 3 letters",
                        "Follows DVLA format"
                    ]
                }
            },
            "other_vehicles": {
                "bicycle": {
                    "description": "Returns type of bicycle",
                    "examples": [
                        "faker.vehicle.bicycle() // 'Adventure Road Bicycle'"
                    ]
                }
            }
        }
    }
    return docs