from unittest.mock import patch

from src.corva_unit_converter.converter import Converter


def test_get_measures_returns_correct_keys():
    """Should return a list of available measures."""
    converter = Converter()
    result = converter.get_measures()

    expected_keys = [
        "acoustic_slowness", "angle", "angle_per_length", "angular_velocity",
        "area", "density", "energy", "force", "gas_concentration",
        "gas_volume", "gamma_radiation", "inverse_pressure", "length", "length_per_angle",
        "mass", "mass_flow_rate", "mpl", "porosity", "power", "pressure",
        "pressure_gradient", "proportion", "revolution_per_volume", "speed",
        "strokes_rate", "temperature", "time", "torque",
        "volume_concentration", "volume_flow_rate", "viscosity", "voltage"
    ]

    assert sorted(result) == sorted(expected_keys)


def test_convert_with_invalid_measure():
    """Should return None because 'proportions' measure doesn't exist."""
    with patch('logging.info') as mocked_info:
        converter = Converter()
        result = converter.convert('%', 'Fraction', 1, 'proportios')

        assert result is None
        assert mocked_info.called
        expected_invalid_measure_msg = (
            f"Invalid measure: proportios. "
            f"Available measures are: {converter.get_measures()}"
        )
        mocked_info.assert_called_with(expected_invalid_measure_msg)
