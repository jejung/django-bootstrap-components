from django import template

register = template.Library()

@register.inclusion_tag('bootstrap/bootstrap_page.html', takes_context=True)
def bootstrap_page(context):
    """ A useful tag to transform your page on an extension of bootstrap basic
    template. Ceckout bootstrap site for more details: 
    http://getbootstrap.com/getting-started/#template.
    
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
    """
    return context
