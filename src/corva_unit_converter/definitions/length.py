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
        'aliases': ['f', 'ft', "'", 'feet', "ftUS"],
    },
    'mi': {
        'name': {
            'singular': 'Mile',
            'plural': 'Miles',
            'display': 'mi'
        },
        'to_anchor': 5280,
        'aliases': ['mi'],
    },
    '32nd': {
        'name': {
            'singular': '1/32 part of an Inch',
            'plural': '32 parts of an Inch',
            'display': '¹/₃₂ part of an Inch'
        },
        'to_anchor': 1 / 384,
        'aliases': ['32nd', "32nd in", "in/32"],
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
