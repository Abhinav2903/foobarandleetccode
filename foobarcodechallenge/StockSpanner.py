class StockSpanner:
    def __init__(self):
        self.Stock=[]
        
    def next(self, price: int) -> int:
        stack=self.Stock
        stacksum=1
        # curvalue=price
        while stack and stack[-1][0]<=price:
            wt=stack.pop()[1]
            stacksum+=wt
            
        stack.append((price,stacksum))
        return stacksum

# price=[100, 80, 60, 70, 60, 75, 85],
# obj = StockSpanner()
# param_1 = obj.next(price)

