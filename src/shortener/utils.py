import random
import string

# def code_generator(size=6, chars='abcdefghijklmnopqrstuvwyxz1234567890'):
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    '''
    new_code = 'dasdsdsd'
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    '''
    # Instead 4 lines above
    return ''.join(random.choice(chars) for _ in range(size))   # temp var

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    #print(instance)                                     # http://pavelstyt5.com/
    #print(instance.__class__)                     # <class 'shortener.models.KirrURL'>
    #print(instance.__class__.__name__)   # KirrURL
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code