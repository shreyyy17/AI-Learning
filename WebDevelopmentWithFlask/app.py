from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

# Every flask app needs unique name

app = Flask(__name__)
posts = {
    0:{
        'post_id':0,
        'title':'Hwllo, Flask!!',
        'content':"THis is my first blog"
    },
    1:{
        'post_id':1,
        'title':'Hwllo, Flask 2!!',
        'content':"THis is my second blog"
    }
}

@app.route("/") #homepage
def home():
    return  render_template('home.jinja2',posts=posts)


@app.route("/about") #homepage
def about():
    return  'Hello, About page !!!!'

# This is how we can pass id in the route
@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.get(post_id)
    if not post: # if post not found then it will be None
        return render_template('404.jinja2',message=f"A Post with id {post_id} was not found")
    return render_template('post.jinja2',name=post['title'],content=post['content'])
    # return f'Post title {post['title']}, content:\n\n{post["content"]}'

@app.route("/post/form")
def form():
    return render_template('createForm.jinja2')


@app.route("/post/create" , methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'post_id':post_id,'title':title,'content':content}
        return redirect(url_for('post',post_id=post_id)) # this is how we can do redirect using url_for
    return render_template('createForm.jinja2')



if __name__ == '__main__':
    app.run(debug=True)