from app.services.user_service import UserService
from flask import render_template, redirect, url_for, flash, request, jsonify
from app.forms.user_form import UserForm

def show_form():
    form = UserForm()
    if form.validate_on_submit():
        # process form data
        name = form.name.data
        email = form.email.data
        flash(f"Received {name} <{email}>!", "success")
        return redirect(url_for('web.show_form'))

    return render_template('form.html', form=form)

def list_users():
    users = UserService.get_all_users()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    user = UserService.create_user(name, email)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email}), 201