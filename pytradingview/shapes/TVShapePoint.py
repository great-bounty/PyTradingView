class TVShapePoint:
    """
    图形点对象
    包含时间和价格信息
    """
    
    def __init__(self, time: int, price: float):
        """
        初始化图形点
        
        Args:
            time: UNIX 时间戳（秒）
            price: 价格值
        """
        self.time: int = time
        self.price: float = price
    
    def to_json(self) -> dict:
        """
        转换为字典格式，用于序列化传输到前端
        
        Returns:
            包含 time 和 price 的字典
        """
        return {
            'time': self.time,
            'price': self.price
        }
    
    def __repr__(self) -> str:
        """返回对象的字符串表示"""
        return f"TVShapePoint(time={self.time}, price={self.price})"