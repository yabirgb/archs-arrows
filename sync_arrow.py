import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()

import json, random, requests
from archi.models import Recipe, Update, Category

def main():
	#?client_id=xxxx&client_secret=yyyy'
	auth = "#?client_id=xxxx&client_secret=yyyy'"
	url = "https://api.github.com/repos/{}/{}/contents/recipes".format("yabirgb", "archs-arrows", "recipes") + auth

	commits_url = "https://api.github.com/repos/{}/{}/commits".format("yabirgb", "archs-arrows", "recipes")
	r = requests.get(commits_url)
	last = r.json()[0]["commit"]["committer"]["date"]

	if Update.objects.count() == 0 or last != Update.objects.last().last_update:

		r = requests.get(url)
		files = [i for i in r.json()]

		for i in files:
			r = requests.get(i["download_url"])
			package_name = r.json()["name"]
			try:
				cat, created = Category.objects.get_or_create(name = r.json()["category"])
				cat.save()
			except:
				print("no category")
			a, created = Recipe.objects.get_or_create(package_name = package_name)
			a.json = r.json()
			try:
				a.category = cat
				print("assigned")
			except:
				print("Can't asign")
			a.package_name = package_name
			a.save()
		Update(last_update = last).save()
		print ("Updated")

	else:
		print("no")

main()
