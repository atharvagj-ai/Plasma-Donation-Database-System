from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Donor, dnumber, blooddetail, hospitalUser, plasmabankUser, hospital_feedback, donor_feedback, available, donation_plasma_bank
from datetime import date
import json, requests
import urllib3

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['search1']

        http = urllib3.PoolManager()

        heroes = http.request('GET', 'https://api.covid19india.org/state_district_wise.json')

        state_dict = json.loads(heroes.data.decode('UTF-8'))

        # print(hero_dict)
        # print(state_dict['Delhi']['districtData']['Central Delhi']['active'])
        for i in state_dict['Delhi']['districtData']:
            print(i)
        temp = 0
        active = 0
        for i in state_dict:
            for j in state_dict[i]['districtData']:
                if city == j:
                    temp = 1
                    active = (state_dict[i]['districtData'][j]['active'])
                    confirmed = state_dict[i]['districtData'][j]['confirmed']
                    # decreased = ("Active: ", state_dict[i]['districtData'][j]['decreased'])
                    recovered = state_dict[i]['districtData'][j]['recovered']
                    break
        if temp == 0:
            a = "District not found"
            return render(request, "home/index.html", {'city':city, 'a':a, 'active':"Not Found", 'confirmed':"Not Found", 'recovered':"Not Found"})
        else:
            return render(request, "home/index.html", {'city':city, 'temp': temp, 'active':active, 'confirmed':confirmed, 'recovered':recovered })
            

    return render(request, "home/index.html")

def donate(request):
    return render(request, "home/form.html")

def donorhome(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        mobile = request.POST['mobile']
        blood = request.POST['blood']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['state']
        # address = request.POST['address']
        query1 = request.POST['query1']
        query2 = request.POST['query2']
        query3 = request.POST['query3']
        query4 = request.POST['query4']
        query5 = request.POST['query5']
        query6 = request.POST['query6']
        query7 = request.POST['query7']

        donor = Donor(fname=fname, lname = lname, mobile= mobile, blood = blood , email = email, age= age, gender= gender,city=city,
        state = state, query1=query1, query2=query2, query3=query3, query4= query4, query5=query5,
        query6=query6 , query7=query7
        )
        
        donor.save()
        available_ = available(donor=donor, available=True)
        available_.save()
        # blood1 = blooddetail(donor=donor, blood_group=blood)
        # blood1.save()
        return render(request, "home/donorhome.html", {'donor':donor})
    else:
        return HttpResponse("Ooops!!")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        reg = request.POST['reg']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        city = request.POST['city']
        state = request.POST['state']
        usertype = request.POST['usertype']
        usertype = int(usertype)
        if pass1 != pass2:
            return HttpResponse("Password didn't match")
        user = User.objects.create_user(username = reg, email = email, password = pass1, first_name = name, last_name = usertype)
        user.save()
        if usertype == 0:
            hu = hospitalUser(user= user ,city=city, state=state)
            hu.save()
            messages.success(request,"You have successfully registered as a Hospital User")
        elif usertype == 1:
            pbu = plasmabankUser(user = user, city=city, state=state)
            pbu.save()
            messages.success(request,"You have successfully registered as Plasma Bank User")

        return render(request, "home/index.html")
    else:
        messages.error(request, "Invalid")
        return render(request, 'home/index.html')

# def showthis(request):
#     obj = donors.objects.all()
#     context = {'obj' : obj}
#     return render(request, "home/")
name1 = ''

def handlelogin(request):
    obj = Donor.objects.all()
    hosuser = hospitalUser.objects.all()
    plasmauser = plasmabankUser.objects.all()
    don = dnumber.objects.all()
    don1 = donation_plasma_bank.objects.all()
    donor_feed = donor_feedback.objects.all()
    hos_feed = hospital_feedback.objects.all()

    available_ = available.objects.all()
    temp = obj[0]
    # don = dnumber.objects.all()
    if request.method == "POST":
        name = request.POST['loginreg']
        pass1 = request.POST['loginpassword']

        user = authenticate(username = name, password = pass1)

        if user is not None:
            login(request, user)
            for i in hosuser:
                if user.id == i.user_id:
                    temp = i
                    return render(request, "home/hospitalhome.html",{'obj':obj, 'status':available_, 'don1':don1,
                     'don':don, 'hosuser': i, 'hos_feed':hos_feed, 'donor_feed':donor_feed})
            
        else:
            messages.error(request, "Invalid User")
            return redirect('home')
    
    return render(request, "home/hospitalhome.html",{'obj':obj, 'status':available_, 'don1':don1, 'don':don,
     'hosuser':hosuser,'hosuser':temp})

# def instance(name):
#     return name
#  name = instance(name)

def hoshome(request):
    obj = Donor.objects.all()
    don = dnumber.objects.all()
    don1 = donation_plasma_bank.objects.all()
    available_ = available.objects.all()
    hosuser = hospitalUser.objects.all()

    temp = obj[0]

    if request.method == "POST":
        dname = request.POST['dname']
        donorno = request.POST['donorno']
        passhome = request.POST['passhome']

        user1 = authenticate(username = dname, password = passhome)
        if user1 is not None:
            lname = int(user1.last_name)
            if lname == 0:
                messages.success(request, "You can edit the number")
                dnum = dnumber(user=user1, number = donorno)
                dnum.save()
            elif lname == 1:
                messages.success(request, "You can edit the number")
                dnum = donation_plasma_bank(user=user1, number = donorno)
                dnum.save()
            for i in hosuser:
                if user.id == i.user_id:
                    temp = i
                    return render(request, "home/hospitalhome.html",{'obj':obj, 'status':available_, 'don1':don1,
                     'don':don, 'hosuser': i})
        else:
            messages.error(request, "Incorrect Password")
        # dnum = dnumber(user = user.id, number=donorno)
        # dnum.save()
    return render(request, "home/hospitalhome.html",{'obj':obj, 'don':don, 'don1':don1, 'status':available_, 'hosuser':temp})

def profile(request):
    hosuser = hospitalUser.objects.all()
    plasmauser = plasmabankUser.objects.all()
    return render(request, "home/profile.html", {'plasmauser':plasmauser, 'hosuser':hosuser})

def requests(request, donor_pk, u_id):
    donor = Donor.objects.all()
    available_ = available.objects.all()
    dnum = dnumber.objects.all()
    for i in donor:
        if i.id == donor_pk:
            for j in available_:
                if j.donor_id == donor_pk:
                    if j.available == True:
                        j.available = False
                        j.save()
                        for k in dnum:
                            if k.user_id == u_id:
                                k.number = k.number - 1
                                k.save()
                        return render(request, "home/request.html", {'donor_pk':donor_pk, 'donor':i,'dnum':dnum})
                    else:
                        return render(request, "home/request_no.html", {'donor':i})
def donorprofile(request, donor_pk):
    obj = Donor.objects.all()
    blood_det = blooddetail.objects.all()
    available_ = available.objects.all()
    # donor = get_object_or_404(Donor, donor_pk)
    # if request.method == 'GET':
        # id = request.GET['donor_id']
    temp = 0
    temp1= 0
    temp2 = -1
    for i in range(0, len(available_)):
        if available_[i].donor_id == donor_pk:
            temp2 = i
    for i in range(0, len(blood_det)):
        if blood_det[i].donor_id == donor_pk:
            temp = i
            temp1 = 1
            break
    if temp1 == 1:
        return render(request, "home/donorprofile.html", {'obj':obj, 'pk':donor_pk, 'temp':blood_det[temp], 'status':available_[temp2]})
    else:
        return render(request, "home/donorprofile.html", {'obj':obj, 'pk':donor_pk, 'status':available_[temp2]})

def hosfeed(request, donor_pk):
    obj = Donor.objects.all()
    user = User.objects.all()
    if request.method == "POST":
        plasma = request.POST['pbno']
        ftitle = request.POST['ftitle']
        review = request.POST['review']
        feedback = request.POST['hosfeed']
        to_date = date.today()
        filled_by = request.POST['hos']
        # filled_by = int(filled_by)
        for i in range(0, len(user)):
            if user[i].username == filled_by:
                for j in range(0, len(user)):
                    if user[j].username == plasma:
                        hosfeedback = hospital_feedback(ftitle=ftitle, review=review, feedback=feedback,
                        submission_date= to_date,hospital= user[i], plasma_bank=user[j])
                        hosfeedback.save()
                        return render(request, "home/submit.html")
        
    return render(request, "home/hosfeed.html", {'donor_pk':donor_pk, 'donor':obj})

def bloodform(request, donor_pk):
    obj = Donor.objects.all()
    temp = 0
    for i in range(0, len(obj)):
        if obj[i].id == donor_pk:
            temp = i
    if request.method == "POST":
        rhtype = request.POST['rhtype']
        plate = request.POST['platelets']
        wbc = request.POST['wbc']
        antibody = request.POST['antibody']
        bld = blooddetail(donor=obj[temp], blood_group=obj[temp].blood, rhtype=rhtype, plate= plate, wbc=wbc, antibody=antibody)
        bld.save()
        return render(request, "home/submit.html")
    return render(request, "home/bloodform.html",{"donor_pk":donor_pk, "donor":obj, "obj1":obj[temp].fname})


def submit(request):
    return render(request, "home/submit.html")
def submit_feedback(request):
    donor = Donor.objects.all()
    if request.method == "POST":
        idno = request.POST['idno']
        ftitle = request.POST['ftitle']
        review = request.POST['review']
        feedback = request.POST['feedback']
        idno = int(idno)
        submission_date = date.today()
        d_feed = donor_feedback(ftitle=ftitle, review=review, feedback=feedback, submission_date=submission_date,
        donor_id=donor[idno])
        d_feed.save()
        return HttpResponse("Submitted Successfully")
    # return render(request, "home/feedback.html", {'id':idno, 'fname':donor[idno-1].fname, 'temp':temp})
    
    # donor = Donor.objects.all()
    # if request.method == "GET":
    #     idno = request.GET['feedbackno']
    #     idno = int(idno)
    #     temp = 0
    #     for i in donor:
    #         if idno == i.id:
    #             temp = i.id
    #     if temp > 0:
    #         if request.method == "POST":
    #             ftitle = request.POST['ftitle']
    #             review = request.POST['review']
    #             feedback = request.POST['feedback']
    #             submission_date = date.today()
    #             d_feed = donor_feedback(ftitle=ftitle, review=review, feedback=feedback, submission_date=submission_date, donor_id=donor[idno-1])
    #             d_feed.save()
    #             return HttpResponse("Submitted Successfully")
    #         return render(request, "home/feedback.html", {'id':idno, 'fname':donor[idno-1].fname, 'temp':temp})
    #     else:
    #         return HttpResponse("Not Found")

def feedback(request):
    donor = Donor.objects.all()
    user = User.objects.all()
    if request.method == "GET":
        idno = request.GET['feedbackno']
        idno = int(idno)
        idn = idno
        temp = 0
        for i in donor:
            if idno == i.id:
                temp = i.id
        if temp > 0:
            return render(request, "home/feedback.html", {'id':idno, 'fname':donor[idno-1].fname, 'temp':temp})
        else:
            return HttpResponse("Not Found")
    if request.method == "POST":
                # idno = request.POST['IDNO']
                pln = request.POST['pbno']
                ftitle = request.POST['ftitle']
                review = request.POST['review']
                feedback = request.POST['feedback']
                submission_date = date.today()
                # pln = int(pln)
                d_feed = donor_feedback(ftitle=ftitle, review=review, feedback=feedback,
                        submission_date=submission_date, plasma_bank=pln)
                d_feed.save()
                return render(request, "home/submit.html")
    return HttpResponse(request, "hi")
    
# def delete(request, delete_no):
#     return HttpResponse("Deleted", {'delete_no':delete_no})

def handlelogout(request):
    logout(request)
    messages.success(request, "You have successfully logout")
    return redirect('home')