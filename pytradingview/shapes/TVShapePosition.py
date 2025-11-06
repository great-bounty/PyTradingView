class TVShapePosition:
    
    def __init__(self, x: float, y: float):
        
        self.x: float = x
        self.y: float = y
    
    def to_json(self) -> dict:
        """
        转换为字典格式，用于序列化传输到前端
        """
        return {
            'x': self.x,
            'y': self.y
        }
    
    def __repr__(self) -> str:
        """返回对象的字符串表示"""
        return f"TVShapePoint(time={self.x}, price={self.y})"