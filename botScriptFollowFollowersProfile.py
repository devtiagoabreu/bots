from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage= 100)
	session.follow_user_followers(['olivarasdr'], amount=40, randomize=False)
	session.follow_user_following(['olivarasdr'], amount=30, randomize=False)
	comentarios = ['Por que aranhas? Por que não podia ser: sigam as borboletas?', 'Gostei do post!', 'O espírito sem limites é o maior tesouro do homem']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comment(comentarios, media= 'Photo')
	session.join_pods()