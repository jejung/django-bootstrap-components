=====       
Django Bootstrap Components
=====

Django Bootstrap Components is a simple Django app that introduce the component
oriented paradigm to your Django project, using the bootstrap project to render
fantanstic UIs.

For a complete guide read the documentation under the "docs" directory.

Quick start.

1. Add the bootstrap_components to your INSTALLED_APPS:

        INSTALLED_APPS = [
                ...
                'bootstrap_components',
       ]

   All the necessary static files will be included, you just need to execute 
   "python manage.py collectstatic" to serve the files.
   
2. Add the bootstrap_components context processor to your TEMPLATES setting:

    TEMPLATES = [
        ...
        {   
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'bootstrap_components.context_processors.commons',
                ],
            },
        },
        ...
    ]
    
    This way we get access to the django.conf.settings object from the settings
    context variable.

3. Configure your bootstrap_components options on the settings file:
    
    BOOTSTRAP = {
        'FROM': 'static',
    }
    
    This allows us to choose the origin of the static files, the options are 
    static (from the project server) and CDN (from maxcdn and google servers). 

4. In site pages extends bootstrap_components default template:

    {% extends "bootstrap/bootstrap_page.html" %}
    
   This template is a preconfigured version of the Bootstrap Basic template,that
   can be seen here: http://getbootstrap.com/getting-started/#template
   
   Alternatively, you can use the bootstrap_components template tag 
   bootstrap_page to create a base template for your site pages:
   
   On base.hmtl put
   {% load bootstrap_components %}
   {% bootstrap_page %}
   
   On other pages pu
   {% extends "base.html"}
   
   There are some sections on the page created over django templates block 
   system, so you can override the content. They are:
    - meta: To describe your own <meta> declarations.
    - title: To define the title of the page.
    - resources: In header declarations of css, javascript or any other resource 
    you need.
    - body: The content of the page itself.
    - scripts: The scripts that should be added to the end of the page, it's a 
    common pratice to place javascript there, because this way you enable the 
    browser to download and render the page in parallel. Check:
    https://developer.yahoo.com/performance/rules.html for a set of good reasons
    to do that.
    
5. Enjoy Bootstrap!