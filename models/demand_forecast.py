import numpy as np

def forecast_demand():
    products = ["Widget A", "Widget B"]
    sales = np.random.randint(50, 150, size=len(products))
    return [{"product": product, "forecast": sale} for product, sale in zip(products, sales)]
