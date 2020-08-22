from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled=True, percentage=100)
	session.set_do_like(enabled=True, percentage=100)
	session.like_by_locations(['76674073/santa-barbara-doeste/'], amount=30)
	comentarios = ['Legal!', 'Gostei do seu post!']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comment(comentarios, media='Photo')
	session.join_pods()