from flask import Flask, render_template, request
import requests
import datetime as dt
import smtplib
my_email = "blago82bt@gmail.com"
password = "123465Zxcvnb"


url = "https://api.npoint.io/c6d7da4fd960417460de"

app = Flask(__name__)


def send_mail(email, name, tel, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="naskoia7@gmail.com",
                            msg=f"Message from Kosmonavt ({email})"
                                "\n\n "
                                f"Name: {name}, phone {tel}, message: \n {message}"
                            )

@app.route('/')
def home():
    response = requests.get(url=url)
    data = response.json()
    return render_template("index.html", posts=data)


@app.route('/contact', methods=['GET', 'POST'])
def get_contact():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        tel = data['tel']
        message = data['message']
        send_mail(email, name, tel, message)
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)

@app.route('/posts')
def get_posts():
    response = requests.get(url=url)
    data = response.json()
    return render_template("posts.html", posts=data)


@app.route('/posts/<post_id>')
def post(post_id):
    response = requests.get(url=url)
    data = response.json()
    single_post = data[int(post_id)-1]
    return render_template("post.html", post=single_post)


@app.route('/about')
def get_about():
    return render_template("about.html")

@app.context_processor
def footer_date():
    now = dt.datetime.now().year
    return dict(now=now)




if __name__ == "__main__":
    app.run(debug=True)