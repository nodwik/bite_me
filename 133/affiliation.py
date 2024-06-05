
def generate_affiliation_link(url):
    splitted_url = url.split('/')
    main_url = splitted_url[2].split('.')
    if main_url[0] == 'www':
        new_url = f'www.{main_url[1]}.com'
    else:
        new_url = f'www.{main_url[0]}.com'
    return f'http://{new_url}/{splitted_url[4]}/{splitted_url[5]}/?tag=pyb0f-20'
