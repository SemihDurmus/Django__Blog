<h1 align="center">Making of Django Blog </h1>

1. Create environment and activate it
    `python3 -m venv benv` and `source benv/bin/activate`
2. Install django 
    `pip3 install django`
3. Create requirement.txt, .gitignore and .env files `pip freeze > requirements.txt` and start project `django-admin startproject cblog`
4. Install decouple
5. Move SECRET_KEY to .env and add the following to settings.py 
```
from decouple import config
``` 
and
```
SECRET_KEY = config('SECRET_KEY')
```
6. Change folder name to src and Start project
7. Create an app `python3 manage.py startapp blog` and add this line to settings>INSTALLED_APPS   `'blog.apps.BlogConfig'`
8. Migrate `python3 manage.py migrate`
9. Create superuser `python3 manage.py createsuperuser`
10. run server and check from browser `python3 manage.py runserver`
11. Create model (Category and Post)
12. Register the modelsin admin.py
13. Install pillow and edit requirement.txt
14. Make migrations + migrate
15. Run server and check, add items to models manually from admin panel
16. Add __str__ function to models to make them seen other than an object
17. Add MEDIA_URl and MEDIA_ROOT to seetings.py and edit urls.py. Create media_root folder
18. Edit models.py for uploading images (paths)
19. For generating slug create signals.py file, and add a function to apps.py
20. Edit signals.py
21. Create Comment, Like and View classes in models. Make migrations + migrate
22. Create forms.py. Add PostForm and CommentForm
23. Edit views -> post_list 
24. Edit settings.py ->TEMPLATES 
```
'DIRS': [BASE_DIR, "templates"]
```
25. Create folder templates under src folder and create file base.html
26. Create folders templates/blog under blog folder and create post_list.html
27. Create post_list function in views, edit both urls.py files
28. Create post_create function in views.(❗️ adding files, getting author info )
29. Create post_create.html and edit urls.py
30. uuid -> create file uyils.py. Inside create a 10 char-long unique id to improve slugify
31. Create post_details function in views, edit urls.py, create post_details.html file
32. Pace post titles in post_list page anchor to link user to post_detail page
33. Add update and delete posts as above
34. Apply bootstrap starter template to base.html
35. Create navbar.html under src/templates
36. Include navbar in base.html
37. Create folders static/blog under application (blog) and create main.css file. (This is sth django wants)
38. Add main.css file's link to head section of base.html and add `{% load static %}` on top
39. Edit settings.py as 
```
STATICFILES_DIRS = [BASE_DIR / "static"]
```
40. Apply a card style to post_list page with bootstrap.
41. Get a kit script from fontawesome and apply to base.html to icons for comment, like and view
42. Add functions to Post class in models.py to retrieve count of comments, likes and views
43. Import CommentForm to views and add comment to post_detail function
44. Add a method to Post class to retrieve all the comments of a post
45. Display all the comments of a post using a for loop in post_detail page, and add a form to the same page to get comments from the user 
46. Import Like to views + add a like function + add like func to urls + create a form in post_detail.html (❗️ Note the action url)
47. Add an if statement to post_detail.html do display delete and update buttons. If the user is the author, he should see update & delete buttons for his own post
48. Now the problem is that a user can reach delete & update pages to any post by typing the url path to address bar. A temporary solution below. After using authentication we will change the way we do it.
49. Install HttpResponse from django.http in views and add an if statement to post_update and post_delete as 
```python
if request.user.id != obj.author.id
    return HttpResponse("You are not authorized")
```
We will change this to a more advanced method soon.

50. Install django-crispy-forms with pip and add crispy_forms to INSTALLED_APPS in settings.py. This third party app is for styling forms w bootstrap.
51. Edit the detail, create, update and delete pages as follows: 
    * add `{% load crispy_forms_tags %}`
    * and change previously `form.as_p` to `form|crispy`
52. Style these pages with bootstrap
53. 🚩 Create users app + add the new app to INSTALLED_APPS in settings.py
54. Create a Profile class in users > models add fields. Add a function to point the path to save the uploaded profile pictures of the user
55. pip freeze > requiremets.txt
56. makemigrations & migrate
57. Register Profile in users > admin.py
58. In order to automatically create a userf profile just after adding a user create a signals.py file (see the code)
59. Add a ready method in users > apps.py to make signals.py take effect
60. Add users path to main urls
61. Create users > urls + import views from django.contrib.auth to use built-in views of django
62. Create users > forms.py + create a registration form + add a method to prevent email repetation
63. Import registration to views + create a registration func
64. Create users > templates/users/register.html + import register func and add path to urls 
65. Give a link to register.html from navbar.html
66. To make email a required field add the following code to registration class in forms.py 
```python
email = forms.EmailField()
#default value is True, otherwise EmailField(required = False)
# models => blank=True
# forms => required=False
```
67. Import Profile to forms and create ProfileUpdateForm and UserUpdateForm. We will update two forms in one page.
68. Import ProfileUpdateForm and UserUpdateForm to views + create a profile function to handle both forms.
69. Create profil.html + arrahne urls + give a link in navbar.html
70. By default django structures login page is created at "registration/login.html". To change this path we overwrite a new template name as 
```python
path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login")
```
71. Add a link from navbar to login and add another link to register page.
72. Do the same for logout just like login
73. By default after logging in Django redirects to "accounts/profile". To change the path add `LOGIN_REDIRECT_URL = "blog:list"` to settings.py
74. In blog > views import login_required from django.contrib.auth.decorators and add `@login_required()` on top of post_create func. The purpose is to prevent getting an error when a user writes /create path to address bar. But first we need to add `LOGIN_URL="login"` because the link is diverted by default to another path which we do not want.
75. Add `@login_required()` on top of post_delete, post_update and like functions accordingly.
76. Import messages from django.contrib in blog > views and add `messages.success(request, "Post successfully created")` after `post.save()` and before redirect in post_create func.
77. Do the same for post_update and post delete
78. Add also a warning message to post_delete and post_update like the one below
```python
if request.user.id != obj.author.id:
    messages.warning(request, "You are not the author")
    return redirect("blog:list")
``` 
79. Add an if statement and a for loop to base.html to display warning messages on the pages.
```html
 <div class="container">
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
</div>
```
80. User can be redirected to register page by writing users/register path to address bar even if the user is already logged in. To fix this add the folowing to register func in users > views
```python
if request.user.is_authenticated:
    messages.warning(request, "You already have an account")
    return redirect("blog:list")
```
81. Add success messages for register and profile functions
82. For handling the issues regarding password forgetting,resetting etc we use django's defaults. 
83. For password resetting add `path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset_email.html', name='password_reset'),` to urls + create password_reset_email.html page and add link from forgot passsword in login page to password_reset_email.html
84. Add path and create password_reset_done. This is for giving information that a recovery email has been sent. We will handle email issue soon.
85. Add path and create password_reset_confirmation. This is for confirmation of the new password.
86. For sending email for password reset add the following to settings.py. Note that these settings are for gmail. For other services find relevant information.
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # this mail will send emails to users
EMAIL_PORT = 587  # post for gmail
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_PASSWORD")
```
for email and the password we use .env file like
```
EMAIL_USER = example@gmail.com
EMAIL_PASSWORD = examplepassword
```
87. To check if this system for gmail works => go to google account settings > security. Switch the security level to "Less secure app access". This method is not the best practice, only for trying.
88. When the user clicks Forgot password he is redirected to password reset request page. Here the user writes his own email. But the app does not control if the email is registered before. To fix this import PasswordResetForm to users > forms and add the following class 
```python
class PasswordResetEmailCheck(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("There is no such email")
        return email
```
Then import PasswordResetEmailCheck to urls and overwrite the form class in the password_reset path to change the default form django uses:
```python
path(
    'password-reset/', 
    auth_views.PasswordResetView.as_view(
        template_name='users/password_reset_email.html', 
        form_class=PasswordResetEmailCheck
    ), 
    name='password_reset'
)
```
