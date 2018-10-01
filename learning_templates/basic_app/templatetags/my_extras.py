from django import template

register = template.Library()

def slash(value,arg):
    """
    tHIS CUTS OUT ALL VALUES OF "arg" fr om the string
    """
    return value.replace(arg,'')

register.filter('slash',slash)

