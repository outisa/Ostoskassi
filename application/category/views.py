from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user
from flask_paginate import Pagination, get_page_args
from sqlalchemy import and_, or_

from application import app, db, login_required, login_manager
from application.category.models import Category
from application.category.forms import CategoryForm
from application.product.models import Product

@app.route("/category/list", methods=["GET", "POST"])
@login_required(role="ANY")
def category_index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    categories = Category.list_categories_for_user(current_user.id)
    total = len(categories)
    pagination_categories = categories[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template("category/listCategories.html", categories_list=pagination_categories,
                           page=page, per_page=per_page, pagination=pagination, form = CategoryForm())


@app.route("/category/edit/<category_id>/<category_category>")
@login_required(role="ANY")
def category_update_form(category_id, category_category):
    category = Category.query.get(category_id)
    # Avoiding error
    if not category:
        return login_manager.unauthorized()

    if category.account_id != current_user.id:
        return login_manager.unauthorized()

    return render_template("category/updateCategory.html", form = CategoryForm(), category_id = category_id, category_category=category_category)

@app.route("/category/delete/<category_id>/", methods=["POST"])
@login_required(role="ANY")
def category_delete(category_id):
    category =  Category.query.filter(Category.id==category_id).first()
    # Avoiding error
    if not category:
        return login_manager.unauthorized()

    if category.account_id != current_user.id:
        return login_manager.unauthorized()

    # Checking first, if some products need category
    products = Product.query.filter(Product.category_id==category_id).first()
    if not products:
        db.session().delete(category)
        db.session().commit()
        return redirect(url_for("category_index"))

    flash('Not able to delete! Some products use category ' + category.category +'.')
    return redirect(url_for("category_index"))


@app.route("/category/update/<category_id>/<category_category>", methods=["POST", "GET"])
@login_required(role="ANY")
def category_update(category_id, category_category):
    category = Category.query.get(category_id)
    # Avoiding error
    if not category:
        return login_manager.unauthorized()

    if category.account_id != current_user.id:
        return login_manager.unauthorized()

    form = CategoryForm(request.form)
    if not form.validate():
        return render_template("category/updateCategory.html", form = form, category_id = category_id, category_category=category_category)


    category = form.category.data
    check = Category.query.filter(and_(Category.category==category, or_(Category.id!=category_id, Category.account_id==0))).first()
    if check:
        return render_template("category/updateCategory.html", form = form, category_id = category_id, category_category=category_category,
                                                    error = "Category exists already.")
    update_category = Category.query.get(category_id)
    update_category.category = form.category.data
    db.session().commit()

    return redirect(url_for("category_index"))

@app.route("/category/", methods=["POST"])
@login_required(role="ANY")
def category_create():
    form = CategoryForm(request.form)
    if not form.validate():
        for error in form.category.errors:
            flash(error + ' Use characters: A-Z, a-z, 0-9, _ and spaces only between words. Category example: "Summer clothes2"')
            return redirect(url_for("category_index"))

    category = form.category.data
    check = Category.query.filter(and_(Category.category==category, or_(Category.account_id==current_user.id, Category.account_id==0))).first()
    if check:
        flash('Category exists already.')
        return redirect(url_for("category_index"))
    new_category = Category(form.category.data)
    new_category.account_id = current_user.id

    db.session().add(new_category)
    db.session().commit()

    return redirect(url_for("category_index"))


