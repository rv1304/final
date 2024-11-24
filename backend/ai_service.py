import numpy as np

def predict_demand():
    products = ["Widget A", "Widget B"]
    predicted_sales = np.random.randint(20, 100, size=len(products))
    return [{"product": product, "predicted_demand": demand} for product, demand in zip(products, predicted_sales)]
