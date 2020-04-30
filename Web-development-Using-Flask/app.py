from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
posts={
    0: {
        'id': 0,
        'title': "Hello,World",
        'content': "This is my first blog post"
    }
}

#Defining a route/endpoint using the Decorator
'''
@app.route('/')
def home():
    return "Hello, World!"
'''
#The '/' endpoint will show all the blog posts
@app.route('/')
def home():
    return render_template('home.jinja2', posts=posts)

#Defining the /post/id endpoint
@app.route('/post/<int:post_id>') #/post/0
def post(post_id):
    post=posts.get(post_id)
    #post will be None if not found; not None => True
    if not post:
        return render_template('404.jinja2', message=f"A post with id {post_id} was not found")
    return render_template('post.jinja2',post=post)

    #return f"Post: {post['title']}, Content:\n\n{post['content']}"
    
    #rendering html contents in the file 'post.html' inside 'templates'r
    #return render_template('post.html')

    #rendering dynamic content
    #return render_template('post.html', post=posts.get(post_id))
#This route will just render another page with the form.
#HTML forms can then send data to another route... /post/create in this case.

#The below enpoint is not handled by the route '/post/create'
'''
@app.route('/post/form')
def form():
    return render_template('create.jinja2')
''' 
# This route will be arrived at looking like this:
# 127.0.0.1:5000/post/create?title=Hello&content=This%20is%20the%20post%20content.
#@app.route('/post/create')

#Getting the data from the FORM as hidden payload rather than Query string paramter
@app.route('/post/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title=request.form.get('title')
        content=request.form.get('content')
        post_id=len(posts)
        posts[post_id]={'id': post_id, 'title': title, 'content': content }
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.jinja2')

if __name__ == "__main__":
    app.run(debug=True)