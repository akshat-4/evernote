from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.
def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def userlogin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['pass']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['adminuser']
        p = request.POST['adminpass']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login_admin.html', d)


def signup(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        branch = request.POST['branch']
        password = request.POST['pass1']
        uname = request.POST['uname']
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=fname, last_name=lname)
            Signup.objects.create(user=user, contact=mobile, branch=branch, role=role)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'signup.html', d)


def admin_home(request):
    if not request.user.is_staff:
        redirect('login_admin')
    pn = Notes.objects.filter(status="pending").count()
    an = Notes.objects.filter(status="approved").count()
    rn = Notes.objects.filter(status="rejected").count()
    alln = Notes.objects.all().count()
    d = {'pn': pn, 'an': an, 'rn': rn, 'alln': alln}
    return render(request, 'admin_home.html', d)


def Logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    d = {'data': data, 'user': user}
    return render(request, 'profile.html', d)


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method == 'POST':
        old = request.POST['oldpass']
        new = request.POST['newpass1']
        confirm = request.POST['newpass2']
        if new == confirm:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(new)
            u.save()
            error = "no"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'changepassword.html', d)


def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        cont = request.POST['contact']
        branch = request.POST['branch']
        user.first_name = fname
        user.last_name = lname
        data.contact = cont
        data.branch = branch
        user.save()
        data.save()
        error = True
    d = {'data': data, 'user': user, 'error': error}
    return render(request, 'editprofile.html', d)


def uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method == 'POST':
        branch = request.POST['branch']
        subject = request.POST['subject']
        ftype = request.POST['filetype']
        desc = request.POST['desc']
        notesfile = request.FILES['notesfile']
        currentuser = User.objects.filter(username=request.user.username).first()
        try:
            Notes.objects.create(user=currentuser, uploadingdate=date.today(), branch=branch, subject=subject, description=desc, filetype=ftype, notesfile=notesfile, status='pending')
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'uploadnotes.html', d)


def view_mynotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    notes = Notes.objects.filter(user=user)
    pn = Notes.objects.filter(user=user).count()
    d = {'notes': notes, 'user': user, 'pn': pn}
    return render(request, 'view_mynotes.html', d)


def delete_mynotes(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_mynotes')


def viewusers(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    users = Signup.objects.all()
    d = {'users': users}
    return render(request, 'viewusers.html', d)


def delete_users(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('viewusers')


def pending_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="pending")
    d = {'notes': notes}
    return render(request, 'pending_notes.html', d)


def approved_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="approved")
    d = {'notes': notes}
    return render(request, 'approved_notes.html', d)


def all_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.all()
    d = {'notes': notes}
    return render(request, 'all_notes.html', d)


def rejected_notes(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.filter(status="rejected")
    d = {'notes': notes}
    return render(request, 'rejected_notes.html', d)


def assign_status(request, pid):
    if not request.user.is_staff:
        return redirect('login_admin')
    notes = Notes.objects.get(id=pid)
    error = ""
    if request.method == 'POST':
        s = request.POST['status']
        try:
            notes.status = s
            notes.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'notes': notes}
    return render(request, 'assign_status.html', d)


def delete_notes(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('all_notes')


def user_viewallnotes(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    notes = Notes.objects.filter(status="approved")
    d = {'notes': notes}
    return render(request, 'user_viewallnotes.html', d)


def contact(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        desc = request.POST['desc']
        try:
            Feedback.objects.create(uploadingdate=date.today(), name=uname, contact=mobile, email=email, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'contact.html', d)


def user_personal(request):
    return render(request, 'user_personal.html')


def personal_upload(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method == 'POST':
        myfile = request.FILES['file1']
        desc = request.POST['desc']
        currentuser = User.objects.filter(username=request.user.username).first()
        try:
            Personal.objects.create(user=currentuser, uploadingdate=date.today(), file=myfile, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'personal_upload.html', d)


def personal_fav(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Personal.objects.filter(user=user, fav='yes')
    pn = Notes.objects.filter(user=user).count()
    d = {'data': data, 'user': user, 'pn': pn}
    return render(request, 'personal_fav.html', d)


def personal_myfiles(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Personal.objects.filter(user=user)
    pn = Notes.objects.filter(user=user).count()
    d = {'data': data, 'user': user, 'pn': pn}
    return render(request, 'personal_myfiles.html', d)


def personal_notepad(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method == 'POST':
        filename = request.POST['filename']
        content = request.POST['content']
        currentuser = User.objects.filter(username=request.user.username).first()
        try:
            Notepad.objects.create(user=currentuser, uploadingdate=date.today(), filename=filename, content=content)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'personal_notepad.html')

def personal_deletenotes(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    file = Personal.objects.get(id=pid)
    file.delete()
    return redirect('personal_myfiles')

def personal_addfav(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    file = Personal.objects.get(id=pid)
    file.fav = 'yes'
    file.save()
    return redirect('personal_myfiles')


def personal_removefav(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    file = Personal.objects.get(id=pid)
    file.fav = 'no'
    file.save()
    return redirect('personal_fav')

def personal_notepadfiles(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    user = User.objects.get(id=request.user.id)
    data = Notepad.objects.filter(user=user)
    d = {'data': data, 'user': user}
    return render(request, 'personal_notepadfiles.html', d)


def personal_notepaddelete(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    file = Notepad.objects.get(id=pid)
    file.delete()
    return redirect('personal_notepadfiles')

def personal_notepadview(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ''
    if request.method == 'POST':
        newfilename = request.POST['filename']
        newfilecontent = request.POST['content']
        fileid = int(request.POST['id'])
        try:
            user = User.objects.get(id=request.user.id)
            file = Notepad.objects.get(user=user, id=fileid)
            file.content = newfilecontent
            file.filename = newfilename
            file.save()
            error = 'no'
        except:
            error = "yes"
    file = Notepad.objects.get(id=pid)
    d = {'file': file}
    return render(request, 'personal_notepadview.html', d)
