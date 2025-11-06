
from pytradingview import TVEngine
from pathlib import Path
if __name__ == '__main__':
    engine = TVEngine()
    engine.get_instance().setup(str(Path(__file__).parent / 'indicators')).run();
