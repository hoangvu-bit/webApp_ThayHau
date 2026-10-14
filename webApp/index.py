from flask import Flask, render_template,request
import dao
app = Flask(__name__)


@app.route("/")
def index():
    # 1. Lấy từ khóa tìm kiếm (nếu có)
    q = request.args.get('q')

    # 2. Lấy ID danh mục khi người dùng bấm vào thanh điều hướng (nếu có)
    cate_id = request.args.get('category_id')

    cates = dao.load_categories()

    # 3. Truyền cả 2 tham số lọc vào hàm load_products
    products = dao.load_products(q=q, category_id=cate_id)

    return render_template("index.html", cates=cates, prods=products)


@app.route("/product/<int:id>")
def details(id):
    return render_template("productsDetail.html")


if __name__=="__main__":
    app.run(debug=True)