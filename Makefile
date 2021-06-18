run:
	docker-compose run toxogos_api $(c)

manage:
	docker-compose run toxogos_api python manage.py $(c)

chown:
	sudo chown `whoami` -R .

shell:
	docker-compose run toxogos_api python manage.py shell_plus

loadgames:
	docker-compose run toxogos_api python manage.py loaddata games/fixtures/designers

test:
	docker-compose run toxogos_api pytest -c pytest.ini
