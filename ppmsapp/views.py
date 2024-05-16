import email
import os
import secrets
import string
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from ppmsapp.models import *
from django.contrib import messages
from django.core.mail import EmailMessage
import sweetify
# Create your views here.
def home(request): 
    # prd = Report.objects.all()
    return render(request,"home.html")

def Eadmin(request):
    return render(request,"admin.html")

def Euser(request):
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    apt=Leave.objects.filter(l_users=user)
    bpt=Attendance.objects.filter(a_users=user)
    return render(request,'employee.html',{'usr':user,'apt':apt,'bpt':bpt})

def loginpage(request):
    return render(request,'login.html')

def signup(request):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    paswd = ''.join(secrets.choice(alphabet) for i in range(16))
    return render(request,'signup.html',{'passwd':paswd})

def add_report(request):
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    catg = Category.objects.all()
    return render(request,'admin/areport.html',{'usr':user,'catg':catg})

def showreport(request):
    scatg =Category.objects.all()
    sprd = Report.objects.all()
    return render(request,'admin/sreport.html',{'cat':scatg,'prod':sprd})

def edit_report(request,od):
    ecatg = Category.objects.all()
    prd = Report.objects.get(id=od)
    return render(request,'admin/ereport.html',{'ecatg':ecatg,'prod':prd})

def a_report(request):
    if request.method == 'POST':
        pname = request.POST['prname']
        pdes = request.POST['prdesc']
        date= request.POST['prdate']
        pstock = request.POST['prstock']
        catg = request.POST['adcatg']
        cat = Category.objects.get(id=catg)
        add = Report(r_name=pname,r_details=pdes,r_DOB=date,r_quantity=pstock,r_category=cat)
        add.save()
        sweetify.success(request,'Report added',button='Ok',timer=5000)
        return redirect('add_report')

def e_report(request,od):
    if request.method == 'POST':
        prod = Report.objects.get(id=od)
        prod.r_name = request.POST['nprname']
        prod.r_details = request.POST['nprdesc']
        prod.r_DOB = request.POST['nprdate']
        prod.r_quantity = request.POST['nprquanity']
        catg = request.POST['nadcatg']
        cat = Category.objects.get(id=catg)
        prod.r_category = cat
        prod.save()
        sweetify.success(request,'Report Updated',button='Ok',timer=5000)
        return redirect('showreport')
    

def add_category(request):
    return render(request,'admin/acategory.html')

def show_category(request):
    catgry = Category.objects.all()
    return render(request,'admin/showcateg.html',{'catg':catgry})

def edit_category(request,od):
    catgry = Category.objects.get(id=od)
    return render(request,'admin/ecategory.html',{'catg':catgry})

def show_user(request): #admin.....
    usr = Employee.objects.all()
    return render(request,'admin/showusers.html',{'user':usr})

def feed(request):
    feds=Feedback.objects.all()
    return render(request,'employee/feedback.html',{'feeds':feds})

def show_feed(request):
    fed=Feedback.objects.all()
    return render(request,'admin/showfeed.html',{'sfeed':fed})

def tfeed(request):
        if request.method == 'POST':
            fn=request.POST['fname']
            fe=request.POST['feed']
            fi=request.POST['email']
            addfeed=Feedback(f_name=fn,f_feed=fe,f_status=fi)
            addfeed.save()
            sweetify.success(request,"Feedback has beign send")
            return redirect('feed')    
     
def efeed(request):
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    efeed= Review.objects.all()
    return render(request,'employee/efeedback.html',{'usr':user,'efeeds':efeed})

def show_efeed(request):
    efeeds = Review.objects.all()
    return render(request,'admin/showefeed.html',{'esfeed':efeeds})

def etfeed(request):
        if request.method == 'POST':
            usr = User.objects.get(username=u_name)
            atten = Employee.objects.get(e_user=usr)
            edob=request.POST['edate']
            efe=request.POST['efeed']  
            addefeed=Review(re_DOB=edob,re_feed=efe,re_users=atten)
            addefeed.save()
            atten.save()
            sweetify.success(request,"Employee feedback has beign send")
            return redirect('efeed') 
        
def register(request):
     usr = User.objects.get(username=u_name)
     user= Employee.objects.get(e_user=usr)
     rreg=Attendance.objects.all()
     return render(request,'admin/register.html',{'usr':user,'ratten':rreg})
 
def show_register(request):
    reg=Attendance.objects.all() 
    return render(request,'admin/showregister.html',{'sreg':reg})

def show_astatus(request):
    usr = User.objects.get(username=u_name)
    atten = Employee.objects.get(e_user=usr)
    astat = Attendance.objects.filter(a_users=atten)
    return render(request,'employee/astatus.html',{'usr':atten,'alev':astat})

def tregister(request):
        if request.method == 'POST':
            usr = User.objects.get(username=u_name)
            atten = Employee.objects.get(e_user=usr)
            lrdob=request.POST['date']
            lshift=request.POST['shift']
            try:
                 attend = Employee.objects.get(e_user=usr)
            except:
                sweetify.warning(request,'Employee name not matching')
                return redirect('Eadmin')
            if attend != None:
                Attendance(a_DOB =lrdob, a_shift=lshift,a_users=attend).save()
                attend.a_DOB = lrdob
                attend.a_shift = lshift
                attend.a_status=None
                atten.save()
                sweetify.success(request,"Attendance has beign recorded")
                return redirect('register')
            else:
                sweetify.success(request,'wrong Employee number')
                return redirect('Euser')
                
def accpts(request,of,od):
        aps = Attendance.objects.get(id=od,a_users=of)
        if aps:
            if aps.a_status == None:
                aps.a_status = 'Present'
                aps.save()
                a_users = Employee.objects.get(id=of)
                a_users.a_status = 'Present'
                a_users.save()
                return redirect('show_register')
            elif aps.a_status == 'Present' :
                return redirect('show_register')
            else:
                if aps.a_status != 'Present':
                    aps.a_status = 'Present'
                    aps.save()
                    a_users = Employee.objects.get(id=of)
                    a_users.a_status = 'Present'
                    a_users.save()
                    return redirect('show_register')
                else:
                    sweetify.error(request,'error')
        return redirect('show_register')

def rejects(request,od,of):
    aps = Attendance.objects.get(id=od,a_users=of)
    if aps:
            if aps.a_status == None:
                aps.a_status = 'Absent'
                aps.save()
                a_users = Employee.objects.get(id=of)
                a_users.a_status = 'Absent'
                a_users.save()
                return redirect('show_register')
            elif aps.a_status == 'Absent':
                return redirect('show_register')
            else:
                if aps.a_status!= 'Absent':
                    aps.a_status = 'Absent'
                    aps.save()
                    a_users = Employee.objects.get(id=of)
                    a_users.a_status = 'Absent'
                    a_users.save()
                    return redirect('show_register')
    else:
        sweetify.error(request,'error')
        return redirect('show_register')
            
def aleave(request):
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    rleave = Leave.objects.all()
    return render(request,'admin/leave.html',{'usr':user,'rleave':rleave})

def show_status(request):
    usr = User.objects.get(username=u_name)
    atten = Employee.objects.get(e_user=usr)
    stat = Leave.objects.filter(l_users=atten)
    return render(request,'employee/status.html',{'usr':atten,'lev':stat})
       
def show_leave(request):
    leav=Leave.objects.all()
    return render(request,'admin/showleave.html',{'sleave':leav}) 
     
def tleave(request):
        if request.method == 'POST':
            usr = User.objects.get(username=u_name)
            atten = Employee.objects.get(e_user=usr)
            lreas = request.POST['reas']
            lldob = request.POST['ldate']
            try:
                emp = Employee.objects.get(e_user=usr)
            except:
                sweetify.warning(request,'Employee id not matching')
                return redirect('aleave')
            if emp != None:
                Leave(l_DOB=lldob,l_reason=lreas,l_users=emp).save()
                emp.l_reason = lreas
                emp.l_DOB = lldob
                emp.l_status=None
                emp.save()
                atten.save()
                sweetify.success(request,'Leave request has been recorded. Please wait for confirmation',button='Ok',timer=5000)
                return redirect('aleave')
            else:
                sweetify.success(request,'wrong Employee number')
                return redirect('aleave')
        
def accpt(request,od,oa):
    apt = Leave.objects.get(id=oa,l_users=od)
    if apt:
            if apt.l_status == None:
                apt.l_status = 'Approved'
                apt.save()
                l_users = Employee.objects.get(id=od)
                l_users.l_status = 'Approved'
                l_users.save()
                return redirect('show_leave')
            elif apt.l_status == 'Approved' :
                return redirect('show_leave')
            else:
                if apt.l_status != 'Approved':
                    apt.l_status = 'Approved'
                    apt.save()
                    l_users = Employee.objects.get(id=od)
                    l_users.l_status = 'Approved'
                    l_users.save()
                    return redirect('show_leave')
    else:
        sweetify.error(request,'error')
        return redirect('show_leave')

def rejctd(request,oa,od):
    apt = Leave.objects.get(id=oa,l_users=od)
    if apt:
            if apt.l_status == None:
                apt.l_status = 'Rejected'
                apt.save()
                l_users = Employee.objects.get(id=od)
                l_users.l_status = 'Rejected'
                l_users.save()
                return redirect('show_leave')
            elif apt.l_status == 'Rejected':
                return redirect('show_leave')
            else:
                if apt.l_status!= 'Rejected':
                    apt.l_status = 'Rejected'
                    apt.save()
                    l_users = Employee.objects.get(id=od)
                    l_users.l_status = 'Rejected'
                    l_users.save()
                    return redirect('show_leave')
    else:
        sweetify.error(request,'error')
        return redirect('show_leave')
        
def new_passwd(request):  #user password change
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    return render(request,'employee/newpass.html',{'usr':user})


def Login(request):
    if request.method== 'POST':
        global u_name
        u_name = request.POST['logname']
        pawd = request.POST['passw']
        log= auth.authenticate(username = u_name, password = pawd)
        if log is not None:
            if log.is_staff:
                auth.login(request,log)
                sweetify.success(request,'Login successful')
                return redirect('Eadmin')
            else:
                auth.login(request,log)
                sweetify.success(request,'Login successful')
                return redirect('Euser')
        else:
            sweetify.error(request,"User name or password does not match. Try again.")
            return redirect('loginpage')
        
def Signup(request):
    try:
        if request.method == 'POST':
            Fname = request.POST['fname']
            Lname= request.POST['lname']
            usernam= request.POST['uname']
            Email = request.POST['E-mail']
            Address=request.POST['adds']
            Age=request.POST['Age']
            paswd = request.POST['pswd']
        try:
            pht = request.FILES['photo']
        except:
            pht = None
        if paswd:
            if User.objects.filter(password = paswd).exists():
                print("This user name already exists")
                sweetify.error(request,"User name already exist")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=usernam,first_name=Fname,
                            last_name=Lname,email=Email,password=paswd)
                user.save()
                mail = EmailMessage ("Account Registered",
                                "Thanks for registering with us. Your account is created , username="+"  "+ usernam +"  "+ " Password=" + "  " + paswd +"  " + ". Please log in with this credentials in future use. Warning:please dont share your password with anyother or any third party applications",
                                "GNG@gmail.com","yourmailid_@gmail.com",
                                [Email]) mail.send()
                    
                employee=User.objects.get(username=usernam) # for adding id in foriegn key column
                custm = Employee(e_fname=Fname,e_lname=Lname,e_address=Address,
                                               e_age=Age,e_photo=pht,
                                               e_email=Email,e_user=employee)
                custm.save()
                sweetify.success(request,"Your account has been registered successfully. An E-mail with password have send. Please use the Login credetianls to login ")
                return redirect('signup')
          
    except:
            sweetify.error(request,"Some details seems to be missing or wrong. Please check again that all detials are entered correctly")
            return redirect('signup')
        
def uprofile(request):
    global u_name
    usr = User.objects.get(username=u_name)
    user= Employee.objects.get(e_user=usr)
    print(user)
    global data1
    data1= Employee.objects.get(e_user=usr)
    print(data1)
    return render(request,'employee/profile.html',{'usr':user, 'data1':data1})  

        
def eprofile(request):
    if request.method=='POST':
        us = User.objects.get(username=u_name)
        us.first_name=request.POST['pfname']
        us.last_name=request.POST['plname']
        us.save()
        
        data1.e_fname = request.POST['pfname']
        data1.e_lname = request.POST['plname']
        data1.e_phone_numbr = request.POST['phnmbr']
        data1.e_address = request.POST['adds']
        data1.e_post = request.POST['post']
        data1.e_age = request.POST['age']
        try:
            if len(request.FILES)!=0:
                try:
                    if len(data1.e_photo)>0:
                        os.remove(data1.e_photo.path)
                    data1.e_photo= request.FILES['photo']
                except:
                    None
                data1.e_photo = request.FILES['photo']
        except:
            data1.e_photo = request.FILES['photo']
        data1.save()
        sweetify.success(request,"Data successfully Updated")
        return redirect('Euser')
    
@login_required(login_url='Login')   
def change_password(request):
    if request.method == 'POST':
        passwd = request.POST['paswrd']
        cpasswd = request.POST['cpaswrd']
        if passwd == cpasswd:
            pasd = User.objects.get(username=u_name)
            pasd.set_password(passwd)
            pasd.save()
            sweetify.success(request,'Password changed successfully')
            return redirect('Euser')
        else:
            sweetify.error(request,'Password is not matching.')
            return redirect('new_passwd')
    
def a_category(request):
    if request.method == 'POST':
        pcatg = request.POST['pcatgr']
        pri = request.POST['pric']
        st = request.POST['stoc']
        catg = Category(product_category= pcatg, product_price = pri,product_stock = st)
        catg.save()
        sweetify.success(request,'Category added',button='Ok',timer=5000)
        return redirect('show_category')

def e_category(request,od):
    if request.method == 'POST':
        catg = Category.objects.get(id=od)
        catg.product_category = request.POST['npcatgr']
        catg.product_price = request.POST['npri']
        catg.product_stock = request.POST['nst']
        catg.save()
        sweetify.success(request,'Category Updated',button='Ok',timer=5000)
        return redirect('show_category')
 

def delete_cat(request,od):
    cat=Category.objects.get(id=od) 
    cat.delete()
    sweetify.success(request,"Category deleted")
    return redirect('show_category')
    
def delete_report(request,od):
    prod=Report.objects.get(id=od) 
    prod.delete()
    sweetify.success(request,"customer report deleted")
    return redirect('showreport')

def delete_leave(request,od):
    sleave=Leave.objects.get(id=od)
    sleave.delete()
    sweetify.success(request,"Employee leave details deleted",button='Ok',timer=5000)
    return redirect('show_leave')

def delete_register(request,od):
    sreg=Attendance.objects.get(id=od)
    sreg.delete()
    sweetify.success(request,"Attendance record deleted",button='Ok',timer=5000)
    return redirect('show_register')

def delete_feed(request,od):
    sfeed=Feedback.objects.get(id=od)
    sfeed.delete()
    sweetify.success(request,"Feedback  deleted",button='Ok',timer=5000)
    return redirect('show_feed')

def delete_efeed(request,od):
    esfed=Review.objects.get(id=od)
    esfed.delete()
    sweetify.success(request,"Employee feedback  deleted",button='Ok',timer=5000)
    return redirect('show_efeed')

def deletecust(request,od):
    cust = Employee.objects.get(id=od)
    catm = cust.e_user.id
    usr = User.objects.get(id=catm)
    usr.delete()
    cust.delete()
    sweetify.success(request,"Employee account permanently deleted",button='Ok',timer=5000)
    return redirect("show_user")

@login_required(login_url='loginpage')
def Logout(request):
    auth.logout(request)
    # sweetify.success(request,"You have being logged out")
    return redirect('home')

