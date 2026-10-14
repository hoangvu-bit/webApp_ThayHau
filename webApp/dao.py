import json

def load_categories():
    with open("data/cate.json",encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None,category_id=None):
    with open("data/products.json", encoding="utf-8") as f:
      prods = json.load(f)

      if q:
          prods = [p for p in prods if p["name"].find(q)>=0]

      if category_id:

          prods = [p for p in prods if p.get('category_id') == int(category_id)]

      return prods

def get_product_by_id(product_id):
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)

        for p in prods:
            if p['id'] == product_id:
                return p
    return None


if __name__=="__main__":
    print(load_products())