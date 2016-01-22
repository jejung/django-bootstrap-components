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
   
2. Include the bootstrap_components URLConf in your project urls.py. It is
   required because some components make AJAX requests to update data and
   handle events.

       url(r'^bootstrap_components/', include('bootstrap_componets.urls')),

3. Enjoy the new components on your site!
