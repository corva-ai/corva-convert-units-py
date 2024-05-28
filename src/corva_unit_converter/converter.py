import logging
from typing import Dict, Union

from . import definitions

measures = {
    "acoustic_slowness": definitions.acoustic_slowness.rule,
    "angle": definitions.angle.rule,
    "angle_per_length": definitions.angle_per_length.rule,
    "angular_velocity": definitions.angular_velocity.rule,
    "area": definitions.area.rule,
    "density": definitions.density.rule,
    "energy": definitions.torque.rule,
    "force": definitions.force.rule,
    "gas_concentration": definitions.gas_concentration.rule,
    "gas_volume": definitions.inverse_pressure.rule,
    "inverse_pressure": definitions.gas_volume.rule,
    "length": definitions.length.rule,
    "length_per_angle": definitions.length_per_angle.rule,
    "mass": definitions.mass.rule,
    "mass_flow_rate": definitions.mass_flow_rate.rule,
    "mpl": definitions.mpl.rule,
    "porosity": definitions.porosity.rule,
    "power": definitions.power.rule,
    "pressure": definitions.pressure.rule,
    "pressure_gradient": definitions.pressure_gradient.rule,
    "proportion": definitions.proportion.rule,
    "revolution_per_volume": definitions.revolution_per_volume.rule,
    "speed": definitions.speed.rule,
    "strokes_rate": definitions.strokes_rate.rule,
    "temperature": definitions.temperature.rule,
    "time": definitions.time.rule,
    "torque": definitions.torque.rule,
    "volume_concentration": definitions.volume_concentration.rule,
    "volume_flow_rate": definitions.volume_flow_rate.rule,
}


def map_aliases_to_unit(measure, excluded_units):
    return [{alias: unit} for unit in measure if unit not in excluded_units
            for alias in measure[unit].get('aliases') or [unit]]


def get_unit_for_alias(alias, measure):
    mapping = map_aliases_to_unit(measure, [])
    new_unit = [unit for item in mapping for key, unit in item.items() if key == alias]
    return new_unit[0] if new_unit else None


class Converter:
    def __init__(self):
        self.origin = {}
        self.destination = {}

    def get_unit_definition(self, source, unit):
        definition = source.get(unit)
        if not definition:
            definition = self.get_unit(unit)
            if not definition:
                logging.info(f"{unit=} not found")
                return
        return definition

    def convert(self, unit_from: str, unit_to: str,  # noqa: CCR001, CFQ004
                value: Union[int, float]):
        """Main function"""
        origin = self.get_unit_definition(source=self.origin, unit=unit_from)
        destination = self.get_unit_definition(source=self.destination, unit=unit_to)

        if not origin or not destination:
            return

        # Don't change the value if origin and destination are the same
        if origin["abbr"] == destination["abbr"]:
            return value

        # Convert from the source value to its anchor inside the system
        result = value * origin["unit"]["to_anchor"]

        # for some units it's a simple shift (e.g. C to K)
        if "anchor_shift" in origin["unit"]:
            result -= origin["unit"]["anchor_shift"]

        # Convert from one system to another
        if origin["system"] != destination["system"]:
            # Convert through transformation
            transform = measures[origin["measure"]]["_anchors"][origin["system"]].get("transform")
            if transform and callable(transform):
                result = transform(result)

            # Convert through the anchor ratio
            result *= measures[origin["measure"]]["_anchors"][origin["system"]]["ratio"]

        # Apply shift after transformation for F to K
        if "anchor_shift" in destination["unit"]:
            result += destination["unit"]["anchor_shift"]

        # Convert to another unit inside the destination system
        return result / destination["unit"]["to_anchor"]

    @staticmethod
    def get_unit(abbr) -> Dict:  # noqa: CCR001
        for measure, systems in measures.items():
            for system, units in systems.items():
                if system == "_anchors":
                    break
                new_abbr = get_unit_for_alias(abbr, units) or abbr
                for test_abbr, unit in units.items():
                    if test_abbr == new_abbr:
                        return {
                            "abbr": new_abbr,
                            "measure": measure,
                            "system": system,
                            "unit": unit
                        }
        return {}
