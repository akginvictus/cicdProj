# # """Route handlers for the main blueprint."""

# # from __future__ import annotations

# # from datetime import datetime

# # import psycopg2
# # import redis
# # from flask import current_app, render_template

# # from . import bp


# # @bp.route("/")
# # @bp.route("/home")
# # def home():
# #     return render_template(
# #         "index.html",
# #         title="Home Page",
# #         year=datetime.now().year,
# #     )


# # @bp.route("/contact")
# # def contact():
# #     return render_template(
# #         "contact.html",
# #         title="Contact",
# #         year=datetime.now().year,
# #         message="Your contact page.",
# #     )


# # @bp.route("/about")
# # def about():
# #     return render_template(
# #         "about.html",
# #         title="About",
# #         year=datetime.now().year,
# #         message="Your application description page.",
# #     )


# # @bp.route("/db-test")
# # def db_test():
# #     try:
# #         with _get_postgres_connection() as conn:
# #             cur = conn.cursor()
# #             cur.execute("SELECT NOW();")
# #             result = cur.fetchone()
# #         return f"Postgres Connected — Server Time: {result}"
# #     except Exception as exc:  # pragma: no cover - simple passthrough
# #         return f"Postgres {exc}"


# # @bp.route("/cache-test")
# # def cache_test():
# #     try:
# #         client = _get_redis_client()
# #         count = client.incr("visits")
# #         return f"Redis Connected - Visit Count: {count}"
# #     except Exception as exc:  # pragma: no cover - simple passthrough
# #         return f"Redis {exc}"


# # def _get_postgres_connection():
# #     config = current_app.config
# #     return psycopg2.connect(
# #         host=config["POSTGRES_HOST"],
# #         database=config["POSTGRES_DB"],
# #         user=config["POSTGRES_USER"],
# #         password=config["POSTGRES_PASSWORD"],
# #     )


# # def _get_redis_client():
# #     config = current_app.config
# #     return redis.StrictRedis(
# #         host=config["REDIS_HOST"],
# #         port=config["REDIS_PORT"],
# #         decode_responses=True,
# #     )



# from __future__ import annotations

# from datetime import datetime

# import psycopg2
# import redis
# from flask import current_app, render_template

# from . import bp


# @bp.route("/", endpoint="home")
# @bp.route("/home", endpoint="home")
# def home():
#     return render_template(
#         "index.html",
#         title="Home Page",
#         year=datetime.now().year,
#     )


# @bp.route("/contact", endpoint="contact")
# def contact():
#     return render_template(
#         "contact.html",
#         title="Contact",
#         year=datetime.now().year,
#         message="Your contact page.",
#     )


# @bp.route("/about", endpoint="about")
# def about():
#     return render_template(
#         "about.html",
#         title="About",
#         year=datetime.now().year,
#         message="Your application description page.",
#     )


# @bp.route("/db-test")
# def db_test():
#     try:
#         with _get_postgres_connection() as conn:
#             cur = conn.cursor()
#             cur.execute("SELECT NOW();")
#             result = cur.fetchone()
#         return f"Postgres Connected — Server Time: {result}"
#     except Exception as exc:  # pragma: no cover
#         return f"Postgres {exc}"


# @bp.route("/cache-test")
# def cache_test():
#     try:
#         client = _get_redis_client()
#         count = client.incr("visits")
#         return f"Redis Connected - Visit Count: {count}"
#     except Exception as exc:  # pragma: no cover
#         return f"Redis {exc}"


# def _get_postgres_connection():
#     config = current_app.config
#     return psycopg2.connect(
#         host=config["POSTGRES_HOST"],
#         database=config["POSTGRES_DB"],
#         user=config["POSTGRES_USER"],
#         password=config["POSTGRES_PASSWORD"],
#     )


# def _get_redis_client():
#     config = current_app.config
#     return redis.StrictRedis(
#         host=config["REDIS_HOST"],
#         port=config["REDIS_PORT"],
#         decode_responses=True,
#     )


from flask import render_template
from FlaskWebProject1.app.main import bp

@bp.route("/")
def home():
    return render_template("index.html", title="Home", year=2025)

@bp.route("/about")
def about():
    return render_template("about.html", title="About", year=2025)

@bp.route("/contact")
def contact():
    return render_template("contact.html", title="Contact", year=2025)

@bp.route("/info")
def info():
    return render_template("info.html", title="Contact", year=2025)

