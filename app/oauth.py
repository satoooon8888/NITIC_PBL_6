from flask import flash, current_app
from flask_login import current_user, login_user, logout_user
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound
from .models import db, User, OAuth

import re

blueprint = make_google_blueprint(
    scope=["profile", "email"],
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user),
    redirect_url="/check"
)

# create/login local user on successful OAuth login
@oauth_authorized.connect_via(blueprint)
def google_logged_in(blueprint, token):
    logout_user()
    if not token:
        return False

    resp = blueprint.session.get("/oauth2/v1/userinfo")
    if not resp.ok:
        return False

    info = resp.json()
    user_id = info["id"]

    # Find this OAuth token in the database, or create it
    query = OAuth.query.filter_by(provider=blueprint.name, provider_user_id=user_id)
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = OAuth(provider=blueprint.name, provider_user_id=user_id, token=token)

    # print(oauth)

    if oauth.user:
        login_user(oauth.user)

    else:
        # Create a new local user account for this user
        name = f"{info['family_name']} {info['given_name']}"
        email = info["email"]

        if current_app.config["ENABLE_EMAIL_VALIDATION"] == True:
            # 茨城高専のメールアドレス以外は弾く
            if not re.match("^.*@gm.ibaraki-ct.ac.jp$", email):
                return False
            # 生徒用のメールアドレスは弾く
            if re.match("^st[0-9]{5}[a-z]{2}@gm.ibaraki-ct.ac.jp$", email):
                return False

        user = User(name=name, email=email, location_id=None)
        # Associate the new local user account with the OAuth token
        oauth.user = user
        # Save and commit our database models
        db.session.add_all([user, oauth])
        db.session.commit()
        # Log in the new local user account
        login_user(user)

    # Disable Flask-Dance's default behavior for saving the OAuth token
    return False


# notify on OAuth provider error
@oauth_error.connect_via(blueprint)
def google_error(blueprint, message, response):
    msg = ("OAuth error from {name}! " "message={message} response={response}").format(
        name=blueprint.name, message=message, response=response
    )
    flash(msg, category="error")
