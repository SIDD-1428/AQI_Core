from database.engine import SessionLocal

from configuration.breakpoint_manager import BreakpointManager
from configuration.standard_manager import StandardManager

from aqi.engine import AQIEngine


class FakePacket:

    pm2_5 = 45


session = SessionLocal()

breakpoint_manager = BreakpointManager(session)
standard_manager = StandardManager(session)

engine = AQIEngine(
    breakpoint_manager,
    standard_manager
)
standard=standard_manager.get_active_standard()
print(standard)
print(standard.id)
result = engine.calculate(FakePacket())

print(result)

session.close()