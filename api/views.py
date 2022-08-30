from asyncio.windows_events import NULL
from smtplib import SMTP_SSL
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from api.models import CommAppLoginMaster,CommAppLogin
from api.serializers import CommAppLoginMasterSerializer
import math, random
from sms import send_sms
import json
from django.db import connection

from sms import send_sms
from django.core.mail import send_mail
import os
from twilio.rest import Client


@csrf_exempt
def sendsms(request):
    if request.method=='GET':
        # send_sms(
        # 'Here is the message',
        # '+917905142778',
        # ['+917905142778'],
        # fail_silently=False
        # )
        account_sid = 'ACa82297787eb4eee6b34fdac35b7efc22'
        auth_token = 'ac9c743a5d17d024d0811d454c2cf1a1'
        client = Client(account_sid, auth_token)
        message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+16075368930',
         to='+917905142778'
     )
        return HttpResponse("send sms executed")

@csrf_exempt
def sendemail(request):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        to=body['to']
        msg=body['msg']
        send_mail(
    'Mail From ambuj',
    msg,
    'realambuj@gmail.com',
    [to],
    fail_silently=False,
)
    obj={
        "message":"Email Successfully sent to",
        "email-id":to
    }
    return JsonResponse(obj,safe=False)

@csrf_exempt
def changepassword(request,userid):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select password from comm_app_login_master where ipasid = %s ",[userid])
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)
    elif (request.method=='POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        password = body['password']
        CommAppLoginMaster.objects.filter(ipasid=userid).update(password=password)
        obj={
            "message":"Successfull",
            }
        return JsonResponse(obj,safe=False)

@csrf_exempt
def getmenuid(request,id):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select menu_id from comm_role_priv where role_id= %s ",[id])
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)


@csrf_exempt
def update(request,user_id):
    if(request.method=='GET'):
        print(user_id)
        # print(request,query_params);
        # print(*args, **kwargs);
        commApp= CommAppLoginMaster.objects.raw("select * from comm_app_login_master where ipasid = %s ",[user_id])
        commApp_serializer = CommAppLoginMasterSerializer(commApp,many=True)
        return JsonResponse(commApp_serializer.data,safe=False)
    elif request.method=='PUT':
        commApp= CommAppLoginMaster.objects.get(ipasid=user_id)
        print(commApp)
        commApp_data = JSONParser().parse(request)
        print(commApp_data)
        commApp_serializer= CommAppLoginMasterSerializer(commApp,data = commApp_data)
        if(commApp_serializer.is_valid()):
            commApp_serializer.save()
            return JsonResponse("Edited successfully",safe=False)
        return JsonResponse("Failed to Edit",safe=False)
    return JsonResponse("Nothing",safe=False)
@csrf_exempt
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(6) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

@csrf_exempt
def generatepass() :
    digits = "0123456789qwertyuioplkjhgfdsazxcvbnm"
    password = ""
    for i in range(8) :
        password += digits[math.floor(random.random() * 32)]
    return password


@csrf_exempt
def generateotp(request,user_id):
    if(request.method=='GET'):
        #print(user_id)
        if(len(user_id)==11):
            strotp=generateOTP()
            print(strotp)
            if not (CommAppLoginMaster.objects.filter(ipasid=user_id).exists()):
                obj={
                "error":True,
                "success":False,
                "message":"USER NOT FOUND",
                "OTP":"0"
            }
                return JsonResponse(obj,safe=False)
            elif(CommAppLoginMaster.objects.filter(ipasid=user_id).exists()):
                emp=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('emp_status', flat=True)
                emp=list(emp)
                status=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('status', flat=True)
                status=list(status)
                flag=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('active_flag', flat=True)
                flag=list(flag)
                print(emp[0],status[0],flag[0])
                if(emp[0]=='w' and status[0]=='v' and flag[0]=='y'):
                    CommAppLoginMaster.objects.filter(ipasid=user_id).update(otp=strotp)
                    #return HttpResponse("ok vai")
                    obj={
                    "error":False,
                    "success":True,
                    "message":"Successfull",
                    "OTP":strotp
                }
                    return JsonResponse(obj,safe=False)
                else:
                    obj={
                    "error":True,
                    "success":False,
                    "message":"ACCOUNT EXPIRED",
                    "OTP":"0"
                }
                    return JsonResponse(obj,safe=False)
        elif (len(user_id)==12 or len(user_id)==10 ):
            strotp=generateOTP()
            print(strotp)
            if not (CommAppLoginMaster.objects.filter(aadhar_no=user_id).exists()):
                obj={
                    "error":True,
                    "success":False,
                    "message":"USER NOT FOUND",
                    "OTP":"0"
                }
                return JsonResponse(obj,safe=False)
            elif(CommAppLoginMaster.objects.filter(aadhar_no=user_id).exists()):
                emp=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('emp_status', flat=True)
                emp=list(emp)
                status=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('status', flat=True)
                status=list(status)
                flag=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('active_flag', flat=True)
                flag=list(flag)
                print(emp[0],status[0],flag[0])
                if(emp[0]=='w' and status[0]=='v' and flag[0]=='y'):
                    CommAppLoginMaster.objects.filter(aadhar_no=user_id).update(otp=strotp)
                        #return HttpResponse("ok vai")
                    obj={
                        "error":False,
                        "success":True,
                        "message":"Successfull",
                        "OTP":strotp,
                    }
                    return JsonResponse(obj,safe=False)
                else:
                    obj={
                        "error":True,
                        "success":False,
                        "message":"ACCOUNT EXPIRED",
                        "OTP":"0"
                    }
                    return JsonResponse(obj,safe=False)
        else:
            obj={
                        "error":True,
                        "success":False,
                        "message":"USER NOT FOUND",
                        "OTP":"0"
                    }
            return JsonResponse(obj,safe=False)

@csrf_exempt
def updates(request, user_id):
    if(request.method=='POST'):
        emp = CommAppLoginMaster.objects.filter(ipasid=user_id)
   #you can do this for as many fields as you like
   #here I asume you had a form with input like <input type="text" name="name"/>
   #so it's basically like that for all form fields
        
        for object in emp:
            emp.password = request.POST.get('password')
            object.save()
        return HttpResponse('updated')

@csrf_exempt   
def getbldg(request):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select bldg_desc from comm_bldg_master")
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)

@csrf_exempt   
def directorate(request):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select * from comm_dte_master")
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)

@csrf_exempt   
def basic(request,levelname):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        s="select "+levelname+" from viicpc_fixation_matrix";
        cursor.execute(s)
        print(levelname)
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)

@csrf_exempt   
def paylevel(request):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select * from comm_pay_level")
        r=cursor.fetchall()
        return JsonResponse(r,safe=False)  



@csrf_exempt        
def getempdetail(request,login_id):
    if(request.method=='GET'):
        cursor  = connection.cursor()
        cursor.execute("select * from empdetail where login_id=%s",[login_id])
        r=cursor.fetchall()

        return JsonResponse(r[0],safe=False)     

@csrf_exempt
def getotp(request,user_id):
    if(request.method=='GET'):
        #print(user_id)
        if(len(user_id)==11):
            #strotp=generateOTP()
            #print(strotp)
            if not (CommAppLoginMaster.objects.filter(ipasid=user_id).exists()):
                obj={
                "error":True,
                "success":False,
                "message":"USER NOT FOUND",
                "OTP":NULL
            }
                return JsonResponse(obj,safe=False)
            elif(CommAppLoginMaster.objects.filter(ipasid=user_id).exists()):
                emp=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('emp_status', flat=True)
                emp=list(emp)
                status=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('status', flat=True)
                status=list(status)
                flag=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('active_flag', flat=True)
                flag=list(flag)
                otp=CommAppLoginMaster.objects.filter(ipasid=user_id).values_list('otp', flat=True)
                otp=list(otp)
                print(otp)
                print(emp[0],status[0],flag[0])
                if(emp[0]=='w' and status[0]=='v' and flag[0]=='y'):
                    #CommAppLoginMaster.objects.filter(ipasid=user_id).update(otp=strotp)
                    #return HttpResponse("ok vai")
                    obj={
                    "error":False,
                    "success":True,
                    "message":"Successfull",
                    "OTP":otp[0],
                }
                    return JsonResponse(obj,safe=False)
                else:
                    obj={
                    "error":True,
                    "success":False,
                    "message":"ACCOUNT EXPIRED",
                    "OTP":NULL
                }
                    return JsonResponse(obj,safe=False)
        elif (len(user_id)==12 or len(user_id)==10):
            #strotp=generateOTP()
            #print(strotp)
            if not (CommAppLoginMaster.objects.filter(aadhar_no=user_id).exists()):
                obj={
                    "error":True,
                    "success":False,
                    "message":"USER NOT FOUND",
                    "OTP":NULL
                }
                return JsonResponse(obj,safe=False)
            elif(CommAppLoginMaster.objects.filter(aadhar_no=user_id).exists()):
                emp=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('emp_status', flat=True)
                emp=list(emp)
                status=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('status', flat=True)
                status=list(status)
                flag=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('active_flag', flat=True)
                flag=list(flag)
                otp=CommAppLoginMaster.objects.filter(aadhar_no=user_id).values_list('otp', flat=True)
                otp=list(otp)
                print(emp[0],status[0],flag[0])
                if(emp[0]=='w' and status[0]=='v' and flag[0]=='y'):
                    obj={
                        "error":False,
                        "success":True,
                        "message":"Successfull",
                        "OTP":otp[0],
                    }
                    return JsonResponse(obj,safe=False)
                else:
                    obj={
                        "error":True,
                        "success":False,
                        "message":"ACCOUNT EXPIRED",
                        "OTP":NULL
                    }
                    return JsonResponse(obj,safe=False)

@csrf_exempt
def setdetail(request,login_id):
    if(request.method=='POST'):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        #login_id = body['login_id']
        name = body['name']
        desg_id = body['desg_id']
        dte_id = body['dte_id']
        bldg_id=body['bldg_id']
        address=body['address']
        email=body['email']
        rly_ph_off=body['rly_ph_off']
        rly_ph_home=body['rly_ph_home']
        gaz_nongz=body['gaz_nongz']
        emp_sex=body['emp_sex']
        pay_level=body['pay_level']
        cur_basic=body['cur_basic']
        mobno=body['mobno']
        
        CommAppLogin.objects.filter(login_id=login_id).update(name=name)
        CommAppLogin.objects.filter(login_id=login_id).update(desig_id=desg_id)
        CommAppLogin.objects.filter(login_id=login_id).update(dte_id=dte_id)
        CommAppLogin.objects.filter(login_id=login_id).update(bldg_id=bldg_id)
        CommAppLogin.objects.filter(login_id=login_id).update(address=address)
        CommAppLogin.objects.filter(login_id=login_id).update(bldg_id=bldg_id)
        CommAppLogin.objects.filter(login_id=login_id).update(email=email)
        CommAppLogin.objects.filter(login_id=login_id).update(rly_ph_off=rly_ph_off)
        CommAppLogin.objects.filter(login_id=login_id).update(rly_ph_home=rly_ph_home)
        CommAppLogin.objects.filter(login_id=login_id).update(gaz_nongz=gaz_nongz)
        CommAppLogin.objects.filter(login_id=login_id).update(emp_sex=emp_sex)
        CommAppLogin.objects.filter(login_id=login_id).update(pay_level=pay_level)
        CommAppLogin.objects.filter(login_id=login_id).update(cur_basic=cur_basic)
        CommAppLogin.objects.filter(login_id=login_id).update(mobno=mobno)
        obj={
                    "message":"Successfull",
                }
        return JsonResponse(obj,safe=False)
    return HttpResponse("Testing API Call ambuj")



def resetpassword(request,user_id):
    if(request.method=='GET'):
        #print(user_id)
        if(len(user_id)==11):
            strp=generatepass()
            print(strp)
            CommAppLoginMaster.objects.filter(ipasid=user_id).update(password=strp)
            obj={
                    "error":False,
                    "success":True,
                    "message":"Successfull",
                    "Password":strp
                }
            return JsonResponse(obj,safe=False)
        elif (len(user_id)==12 or len(user_id)==10):
            strp=generatepass()
            print(strp)
            CommAppLoginMaster.objects.filter(aadhar_no=user_id).update(password=strp)
            obj={
                    "error":False,
                    "success":True,
                    "message":"Successfull",
                    "Password":strp
                }
            return JsonResponse(obj,safe=False)

def index(request):
    obj={
        'name':'Ambuj',
        'college':'IIITN'
    }
    return JsonResponse(obj,safe=False)


def home(request):
#     send_mail(
#     'Subject here',
#     'Here is the message.',
#     'realambuj@gmail.com',
#     ['bt20cse054@iiitn.ac.in'],
#     fail_silently=False,
# )
    return HttpResponse("Testing API Call ambuj")