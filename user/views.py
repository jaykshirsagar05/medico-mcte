from django.core.management import call_command
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import User,Analyze
from django.db.models import Q
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from fastai import *
from fastai.vision import *
from fastai.vision.models import efficientnet
import numpy as np

# Create your views here.
def dashboard(request):
    return render(request, "dashboard.html")

def user(request):
    if request.method == 'POST' and "save" in request.POST:
        armyno = request.POST['armyno']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        posttype = request.POST['posttype']
        relation = request.POST['relation']
        sex = request.POST['sex']
        age = request.POST['age']
        rank = request.POST['rank']
        healthproblem = request.POST['healthproblem']
        problemhistory = request.POST['problemhistory']
        
        patient = User(armyno=armyno,firstname=firstname,lastname=lastname,posttype=posttype,relation=relation,sex=sex,age=age,rank=rank,healthproblem=healthproblem,problemhistory=problemhistory)
        patient.save()
        print("Done")
        return redirect('/dashboard/user')
    if request.method == 'POST' and "analyze" in request.POST:
        armyno = request.POST['armyno']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        posttype = request.POST['posttype']
        relation = request.POST['relation']
        sex = request.POST['sex']
        age = request.POST['age']
        rank = request.POST['rank']
        healthproblem = request.POST['healthproblem']
        problemhistory = request.POST['problemhistory']
        
        patient = User(armyno=armyno,firstname=firstname,lastname=lastname,posttype=posttype,relation=relation,sex=sex,age=age,rank=rank,healthproblem=healthproblem,problemhistory=problemhistory)
        patient.save()
        print("Done")
        return redirect('/dashboard/analyze')
    else:
        count= User.objects.all().count()
        context= {'count': count}
        return render(request, "user.html", context)

def analyze(request):
    #patientinfo = User.objects.all()
    #print(patientinfo)
    context = {}
    if request.method == 'POST':
        uploaded_image = request.FILES['img']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        context['url'] = fs.url(name)
        label = predict('jay')
        pic = Analyze(images=uploaded_image)
        pic.save()
        return redirect('/dashboard/analyze')
    return render(request, "analyze.html", context)

def visualize(request):
    return render(request, "visualize.html")

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        
        if search:
            match = User.objects.filter(Q(id__icontains=search) |
                                        Q(armyno__icontains=search)                                       
                                        )
            if match:
                return render(request,'search.html',{'sr':match})
            else:
                messages.error(request,'No result found!')
        else:
            return redirect('/dashboard/search')
 
    return render(request, "search.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def predict(img):
    learn = load_learner('/home/jay/MCTE/medical/medical/assets/models/','odr-EffNetB3-stage2a.pkl')
    print('learner loaded...')
    tfms = get_transforms(max_rotate=360,max_zoom=0.9,max_lighting=0.1,p_lighting=0.5)
    img = open_image('/home/jay/MCTE/medical/medical/assets/models/1088_right.jpg')
    img.apply_tfms(tfms[0],size=224)
    pred=learn.predict(img)[2]
    print('transformations applied...')
    pred = to_np(pred)
    pred = np.argmax(pred)
    # indices = [i for i, x in enumerate(pred) if x == 1]
    label = learn.data.classes[pred]
    print("label:{}".format(label))
    return label

# if __name__ == "__main__":
#     predict('jay')