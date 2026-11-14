import unittest
from types import SimpleNamespace

from aqi.engine import AQIEngine
from aqi.rounding import round_aqi_index


class FakeStandardManager:
    def get_active_standard(self):
        return SimpleNamespace(id=1)


class FakeBreakpointManager:
    def __init__(self, breakpoints=None):
        self.breakpoints = breakpoints or {}

    def get_breakpoints(self, pollutant, standard_id):
        return self.breakpoints.get(pollutant, [])


class AQIEngineTests(unittest.TestCase):
    def setUp(self):
        self.breakpoint = SimpleNamespace(
            conc_low=0.0,
            conc_high=20.0,
            aqi_low=0,
            aqi_high=20,
            category="Good",
            color="#00aa00",
        )

    def packet(self, **overrides):
        values = {
            "pm2_5": 12.5,
            "pm10": None,
            "no2": None,
            "so2": None,
            "co": None,
            "o3": None,
            "nh3": None,
        }
        values.update(overrides)
        return SimpleNamespace(**values)

    def test_subindex_is_rounded_half_up_before_result_is_returned(self):
        engine = AQIEngine(
            FakeBreakpointManager({"PM2_5": [self.breakpoint]}),
            FakeStandardManager(),
        )

        result = engine.calculate(self.packet())

        self.assertIsNotNone(result)
        self.assertEqual(result.aqi, 13)
        self.assertEqual(result.subindices, {"PM2_5": 13})

    def test_no_matching_breakpoints_returns_no_result(self):
        engine = AQIEngine(
            FakeBreakpointManager(),
            FakeStandardManager(),
        )

        self.assertIsNone(engine.calculate(self.packet()))

    def test_rounding_helper_uses_half_up(self):
        self.assertEqual(round_aqi_index(21.5), 22)
        self.assertEqual(round_aqi_index(21.49), 21)

    def test_non_finite_concentrations_are_ignored(self):
        engine = AQIEngine(
            FakeBreakpointManager({"PM2_5": [self.breakpoint]}),
            FakeStandardManager(),
        )

        result = engine.calculate(self.packet(pm2_5=float("nan")))

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
