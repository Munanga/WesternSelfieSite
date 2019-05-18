from django.shortcuts import render
from WestApp.models import ImageModel
from WestApp.forms import ImageForm
from django.http import HttpResponseRedirect

# Create your views here.
def homepage(request):
    query_get_images = ImageModel.objects.order_by('-caption')
    context = {"images":query_get_images}
    return render(request,'index.html',context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = ImageForm()
    context = {"form":form}
    return render(request,'upload.html',context)





