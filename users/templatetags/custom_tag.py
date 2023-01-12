from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css,"placeholder":" " })

@register.filter(name='place')
def place(field, text):
    return field.as_widget(attrs={"placeholder":text, "placeholder":" "})