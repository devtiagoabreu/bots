from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled=True, percentage=70)
	session.set_do_like(enabled=True, percentage=90)
	session.like_by_tags(['varinhadasvarinhas'], amount=99)
	comentarios = ['Por que aranhas? Por que não podia ser: sigam as borboletas?', 'Gostei do post!', 'O espírito sem limites é o maior tesouro do homem']
	session.set_do_comment(enabled = True, percentage=98)
	session.set_comment(comentarios, media='Photo')
	session.join_pods()