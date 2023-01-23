from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def reverse(request):
	text = request.GET["message"]
	reversetext = text[::-1]
	words = len(text.split())
	return render(request, 'reverse.html', {'text':text, 'reversetext':reversetext, 'words': words} )
