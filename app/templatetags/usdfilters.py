from django import template

register=template.Library()


@register.filter(name='swapcase')
def swap(value):
    return value.swapcase()

@register.filter()
def remove(value,char):
    return value.replace(char,'')

#register.filter('remove',remove)

#register.filter('swapcase',swap)