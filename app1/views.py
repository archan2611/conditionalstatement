from django.shortcuts import render

# Create your views here.
def operation(request):
    d={'a':123, 'b':456, 'c':234}
    return render(request, 'operation.html', d)
