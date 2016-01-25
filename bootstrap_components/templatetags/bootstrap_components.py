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

@register.inclusion_tag('bootstrap/icon.html', takes_context=False)
def bootstrap_icon(icon):
    """ Render a simple icon on the page like <span class="glyphicon *icon" />.
    Please consider reading the usage notes as described on the Bootstrap 
    documentation: http://getbootstrap.com/components/#glyphicons-how-to-use 
    An aditional statement is important on Glyphicons, as the Bootstrap 
    documentation says:
    "Glyphicons Halflings are normally not available for free, but their creator 
    has made them available for Bootstrap free of cost. As a thank you, we only 
    ask that you include a link back to Glyphicons whenever possible." 
    Link here: http://glyphicons.com/
    """
    return {
        'icon': icon,
    }