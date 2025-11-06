
from pytradingview import TVEngine

if __name__ == '__main__':
    engine = TVEngine()
    engine.get_instance().setup('./indicators').run();
