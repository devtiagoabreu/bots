from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 70)
	session.set_do_like(enabled = True, percentage= 90)

	session.like_by_tags(['VarinhaDasVarinhas, LunaLovegood, HarryPotter'], amount=50)

	comentarios = ['Foto Legal! Malfeito feito!', 'Gostei do seu post! Malfeito feito!', 'O espírito sem limites é o maior tesouro do homem',  ]
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comments(comentarios, media= 'Photo')
	session.join_pods()