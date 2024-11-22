from flask import Blueprint, request, session, g, render_template, url_for, redirect, flash
from flask_login import LoginManager, login_user, current_user, logout_user
from app.models.database_SEDELT import db, UserBase, Admin
from sqlalchemy.exc import NoResultFound

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return UserBase.query.get(int(user_id))

@bp_auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        try:
            user = db.session.execute(db.select(UserBase).filter_by(username=username)).scalar_one()

            if not user.check_password(password):
                error = "Usuário ou senha incorreta!"
            else:
                login_user(user)
                return redirect(url_for('home.home',))

        except NoResultFound:
            error = 'Usuário não encontrado na base de dados'
        except Exception as er:
            error = f"Erro inesperado: {er}" 
            print(er)

        flash(error)
        
    return render_template('auth/login.html')


@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        nickname = request.form['nickname']
        email = request.form['email']
        password = request.form['password']
        is_admin = request.form.get('is_admin', False)

        error = None

        if not username:
            error = 'O nome de usuario é obrigatório'
        elif not nickname:
            error = 'O apelido é obrigatório'
        elif not email:
            error = 'O e-mail é obrigatório'
        elif not password:
            error = 'A senha é obrigatória'
        
        if error is None:
            try:
                if is_admin:
                    user = Admin(username, nickname, email, password)
                else:
                    user = UserBase(username, nickname, email, password)
                
                db.session.add(user)
                db.session.commit()
                flash('Cadastro realizado com sucesso!')

                return redirect(url_for('auth.login'))
            
            except Exception as e:
                flash(f'Erro ao cadastrar  o usuário')
                print(e)
        
        else:
            flash(error)
        
    return render_template('auth/register.html')


@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.home'))
