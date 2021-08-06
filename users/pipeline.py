import requests

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'google-oauth2':
        return

    api_url = f'https://www.googleapis.com/oauth2/v1/userinfo?access_token={response["access_token"]}'

    response = requests.get(api_url)

    if response.status_code != 200:
        return

    data = response.json()
    print(data)

    if 'picture' in data:
        picture_url = data['picture']
        picture = requests.get(picture_url, stream=True)
        picture.raw.decode_content = True
        user.image.save(f'{user.username}.jpg', picture.raw)
