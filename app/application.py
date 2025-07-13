from flask import Flask, render_template, request, session, redirect, url_for
from app.components.retriever import create_qa_chain
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Converts the new line characters of the answer into html <br> tags
from markupsafe import Markup
<<<<<<< HEAD


def nl2br(value):
    return Markup(value.replace("\n", "<br>\n"))


app.jinja_env.filters["nl2br"] = nl2br
=======
def nl2br(value):
    return Markup(value.replace("\n", "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br
>>>>>>> 16a58f6 (Final changes)


@app.route("/", methods=["GET", "POST"])
def index():
    if "messages" not in session:
        session["messages"] = []
<<<<<<< HEAD

    if request.method == "POST":
        user_input = request.form.get("prompt")

        if user_input:
            messages = session["messages"]
            messages.append({"role": "user", "content": user_input})
            session["messages"] = messages

=======
        
    if request.method == "POST":
        user_input = request.form.get("prompt")
        
        if user_input:
            messages = session["messages"]
            messages.append({'role':'user', 'content': user_input})
            session['messages'] = messages
            
>>>>>>> 16a58f6 (Final changes)
            try:
                qa_chain = create_qa_chain()
                response = qa_chain.invoke({"query": user_input})
                result = response.get("result", "No response")
<<<<<<< HEAD

                messages.append({"role": "assistant", "content": result})
                session["messages"] = messages

            except Exception as e:
                error_message = CustomException("Something went wrong", e)
                logger.error(str(error_message))
                return render_template(
                    "index.html", messages=session["messages"], error=error_message
                )

        return redirect(url_for("index"))

=======
                
                messages.append({"role": "assistant", "content": result})
                session["messages"] = messages
                
            except Exception as e:
                error_message = CustomException("Something went wrong", e)
                logger.error(str(error_message))                
                return render_template("index.html", messages=session["messages"], error = error_message)
        
        return redirect(url_for("index"))
    
>>>>>>> 16a58f6 (Final changes)
    return render_template("index.html", messages=session.get("messages", []))


@app.route("/clear", methods=["GET", "POST"])
def clear():
    session.pop("messages", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
=======
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
>>>>>>> 16a58f6 (Final changes)
