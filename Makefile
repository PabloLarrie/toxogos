run:
	docker-compose run toxogos_api $(c)

manage:
	docker-compose run toxogos_api python manage.py $(c)

chown:
	sudo chown `whoami` -R .