from django.shortcuts import render
import json, random, requests, os, inspect
from .models import Recipe, Update, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
# Create your views here.

path = "/path/to/folder" #!!!!!!!!!!!!!!!!!


base = """#!/bin/bash
clear

if [ $(tput colors) ]; then # Checks if terminal supports colors
	red="\e[31m"
	green="\e[32m"
	endcolor="\e[39m"
fi

echo ====================
echo "We are not responsible for any damages that may possibly occur while using Arrow"
echo ====================
echo "   "

sleep 2

sudo -s <<ARROW

# Update pacman
echo "Updating pacman (may take a while)"
(
pacman -Syy
) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor";
"""

def join(packages, update, tag):
	commit = """""" + base
	for i in packages:
		f = Recipe.objects.get(package_name = i)
		js = f.json
		if type(js["command"]) == list:
			commit += "echo 'Installing {}\n'".format(js["name"])
			for z in js["command"]:
				commit += "( \n"
				commit += z + " --needed --noconfirm" + "\n"
				commit *= """
					) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor";\n"""
		else:
			commit += "echo 'Installing {}'\n".format(js["name"])
			commit += """( \n{}\n) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor"; \n""".format(js["command"] + " --needed")

	if update:
		commit += """echo "Upgrading old packages"\n(\npacman -Syu \n) &> /dev/null && echo -e "$green OK $endcolor" || echo -e "$red FAILED $endcolor";\n"""
	commit += """ARROW\nexit 0"""

	print(path + "file.sh")
	with open(path + tag +".sh", "w") as f:
		f.write(commit)
		f.close

from dateutil import parser
import random
from django.template import RequestContext
def main(request):
	print path
	categories = Category.objects.all()
	objects = Recipe.objects.all()
	results = {}
	dic = "abcdefghijklmnopqrstuvwxyz123456890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	to_install = []
	if request.method=='POST':
		for i in request.POST:
			if request.POST[i] == "on":
				a,b,c,d,e,f = random.randint(0,60), random.randint(0,60), random.randint(0,60),random.randint(0,60), random.randint(0,60), random.randint(0,60)
				tag = dic[a] + dic[b] + dic[c] + dic[d] + dic[e] + dic[f]
				to_install.append(i)

				results["tag"] = tag

		join(to_install, True, tag)

	objects = Recipe.objects.all()
	results["apps"] = objects
	results["categories"] = categories
	return render_to_response("arrow/home.html", results, context_instance=RequestContext(request))

#http://stackoverflow.com/questions/2681338/django-serving-a-download-in-a-generic-view
def file_download(request, filename):
    #song = Song.objects.get(id=song_id)
	try:
		fsock = open(path + '%s.sh' % filename, 'r')
		response = HttpResponse(fsock, content_type='text')
		response['Content-Disposition'] = "attachment; filename= %s.sh" % filename
		return response
	except:
		return HttpResponse("File not found")
