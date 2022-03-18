from django import template

register = template.Library()

@register.filter
def persian_int(number):
    persian_numbers = u'۱۲۳۴۵۶۷۸۹۰'
    english_numbers = u'1234567890'

    list = [int(x) for x in str(number)]
   
    dic = { 
        0:"۰",
        1:'١', 
        2:'٢', 
        3:'۳', 
        4:'۴', 
        5:'۵', 
        6:'۶', 
        7:'۷', 
        8:'۸', 
        9:'۹', 
        }

    S = ''.join(str(dic[e]) for e in list)
           
    try:
         return S
    except KeyError:
         return list