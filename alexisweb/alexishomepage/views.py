from django.shortcuts import render

# Create your views here.
def main(request):
    contents = {}
    return render(request, 'alexishomepage/home.html', contents)