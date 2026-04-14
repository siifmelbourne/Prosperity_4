from datamodel import OrderDepth, TradingState, Order
from typing import List
class trader:
    def run(self, state: TradingState):
        result = {}
        for product in state.order_depths:
            order_depth: OrderDepth = state.order_depths[product]
            orders: List[Order] = []
            if len(order_depth.buy_orders) == 0 or len(order_depth.sell_orders) == 0:
                continue
            best_bid = max(order_depth.buy_orders.keys())
            best_ask = min(order_depth.sell_orders.keys())
            mid = (best_bid + best_ask) / 2
            position = state.position.get(product, 0)
            limit = 20 #position limit

            if best_ask - best_bid < 2:
                continue

            buy_price = int(mid - 1)
            sell_price = int(mid + 1)
            #here the bid of +-1 from mid is arbitrary can be improved and adjusted to calculate better value
            if position > 10:
                buy_price -= 1 
            if position < -10:
                sell_price += 1  

            buy_volume = limit - position
            sell_volume = limit + position

            if buy_volume > 0:
                orders.append(Order(product, buy_price, buy_volume))

            if sell_volume > 0:
                orders.append(Order(product, sell_price, -sell_volume))

            result[product] = orders

        return result, 0, ""
