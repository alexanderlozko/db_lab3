from flask import render_template, request, redirect
from app import app
from app import db
from app.models import Brand, Product
import random
import time

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    message = ''

    brand_posts = Brand.query.all()
    product_posts = Product.query.all()

    if request.method == 'POST':
        brand = request.form.get('name_brand')
        year = request.form.get('year_brand')
        #проверки на год нет
        if brand and year != '':
            add = Brand(name=brand, year=year)
            db.session.add(add)
            db.session.commit()
            #message = 'brand was added'
            return redirect('index')


        # try:
        #     db.session.add(add)
        #     db.session.commit()
        # except Exception:
        #     message = 'Error'


        product = request.form.get('name_product')
        price = request.form.get('price_product')
        brand_prod = request.form.get('brand_product')

        add = Product(name=product, price=price, brand=brand_prod)

        # try:
        #     db.session.add(add)
        #     db.session.commit()
        # except Exception:
        #     message = 'Error'

        list_br = []
        all = Brand.query.all()
        for br in all:
            list_br.append(br.name)

        if product and price != '':
            if str(brand_prod) in list_br:
                db.session.add(add)
                db.session.commit()
                #message = 'product was added'
                return redirect('index')
            message = 'brand not exist! create brand!'

    return render_template('index.html', message=message, brand_posts=brand_posts, product_posts=product_posts)


@app.route('/delete_product/<id>')
def delete_product(id):
    dl = db.session.query(Product).get(id)
    db.session.delete(dl)
    db.session.commit()
    return redirect('/index')

@app.route('/delete_brand/<name>')
def delete_brand(name):
    dl = db.session.query(Brand).get(name)
    db.session.delete(dl)
    db.session.commit()

    dl_list = Product.query.filter_by(brand=name).all()
    for dl1 in dl_list:
        db.session.query(Product).get(dl1.id)
        db.session.delete(dl1)
        db.session.commit()
    return redirect('/index')