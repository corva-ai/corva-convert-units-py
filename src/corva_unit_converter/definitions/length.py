metric = {
    'mm': {
        'name': {
            'singular': 'Millimeter',
            'plural': 'Millimeters',
            'display': 'mm'
        },
        'to_anchor': 1 / 1000,
        'aliases': ['mm'],
    },
    'cm': {
        'name': {
            'singular': 'Centimeter',
            'plural': 'Centimeters',
            'display': 'cm'
        },
        'to_anchor': 1 / 100,
        'aliases': ['cm'],
    },
    'm': {
        'name': {
            'singular': 'Meter',
            'plural': 'Meters',
            'display': 'm'
        },
        'to_anchor': 1,
        'aliases': ['m', 'm.', 'meter', 'meters'],
    },
    'km': {
        'name': {
            'singular': 'Kilometer',
            'plural': 'Kilometers',
            'display': 'km'
        },
        'to_anchor': 1000,
        'aliases': ['km'],
    }
}

imperial = {
    'in': {
        'name': {
            'singular': 'Inch',
            'plural': 'Inches',
            'display': 'in'
        },
        'to_anchor': 1 / 12,
        'aliases': ['in', 'inch', 'inches', '"', 'ins', 'inus'],
    },
    'yd': {
        'name': {
            'singular': 'Yard',
            'plural': 'Yards',
            'display': 'yd'
        },
        'to_anchor': 3,
        'aliases': ['yd'],
    },
    'ft': {
        'name': {
            'singular': 'Foot',
            'plural': 'Feet',
            'display': 'ft'
        },
        'to_anchor': 1,
        'aliases': ['f', 'ft', "'", 'feet'],
    },
    'mi': {
        'name': {
            'singular': 'Mile',
            'plural': 'Miles',
            'display': 'mi'
        },
        'to_anchor': 5280,
        'aliases': ['mi'],
    }
}

rule = {
    "metric": metric,
    "imperial": imperial,
    "_anchors": {
        'metric': {
            'unit': 'm',
            'ratio': 3.28084
        },
        'imperial': {
            'unit': 'ft',
            'ratio': 1 / 3.28084
        }
    }
}
