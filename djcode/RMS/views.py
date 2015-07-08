from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from templates.models import *
from django.db.models import Q
import datetime
import os
from django.template import RequestContext, loader
notice_number = 6
resource_number = 5
homeworkfile_number = 0
homework_number = 100
one = 1
# #############################
add = course(num='122',student_id = '31200000',course_id='soften' )
add.save()
add = course(num='123',student_id = '31200000',course_id='soften1' )
add.save()
add = course(num='124',student_id = '31200000',course_id='soften2' )
add.save()
add = course(num='125',student_id = '31200000',course_id='soften3' )
add.save()
add = course(num='126',student_id = '31200000',course_id='soften4' )
add.save()
add = course(num='127',student_id = '31200000',course_id='soften5' )
add.save()
add = course(num='128',student_id = '31200000',course_id='soften6' )
add.save()
add = course(num='129',student_id = '31200000',course_id='soften7' )
add.save()
# add = course(num='142',manager_id = '31200002',course_id='soften' )
# add.save()
# add = course(num='143',manager_id = '31200002',course_id='soften1' )
# add.save()
# add = course(num='144',manager_id = '31200002',course_id='soften2' )
# add.save()
# add = course(num='145',manager_id = '31200002',course_id='soften3' )
# add.save()
# add = course(num='146',manager_id = '31200002',course_id='soften4' )
# add.save()
# add = course(num='147',manager_id = '31200002',course_id='soften5' )
# add.save()
# add = course(num='148',manager_id = '31200002',course_id='soften6' )
# add.save()
# add = course(num='149',manager_id = '31200002',course_id='soften7' )
# add.save()
# #############################
# add = Notice(notice_num='1',notice_title = 'h1',course_id='soften7',content='test1' )
# add.save()
# add = Notice(notice_num='2',notice_title = 'h2',course_id='soften7',content='test2' )
# add.save()
# add = Notice(notice_num='3',notice_title = 'h3',course_id='soften7',content='test3' )
# add.save()
# add = Notice(notice_num='4',notice_title = 'h4',course_id='soften7',content='test4' )
# add.save()
# add = Notice(notice_num='5',notice_title = 'h5',course_id='soften7',content='test5' )
# add.save()
# ##############################
# add = Homework(homework_num='1',course_id= 'soften7',title='homework1',content='testhomework1' )
# add.save()
# add = Homework(homework_num='2',course_id= 'soften7',title='homework2',content='testhomework2' )
# add.save()
# add = Homework(homework_num='3',course_id= 'soften7',title='homework3',content='testhomework3' )
# add.save()
# add = Homework(homework_num='4',course_id= 'soften7',title='homework4',content='testhomework4' )
# add.save()
# add = Homework(homework_num='5',course_id= 'soften7',title='homework5',content='testhomework5' )
# add.save()
# add = Homework(homework_num='6',course_id= 'soften7',title='homework6',content='testhomework6' )
# add.save()
# ##############################
# add = Resource(resource_id='1',course_id= 'soften7',resource_name='resource1',resource_add='address1' 
#     )
# add.save()
# add = Resource(resource_id='2',course_id= 'soften7',resource_name='resource2',resource_add='address2' 
#     )
# add.save()
# add = Resource(resource_id='3',course_id= 'soften7',resource_name='resource3',resource_add='address3' 
#     )
# add.save()
# add = Resource(resource_id='4',course_id= 'soften7',resource_name='resource4',resource_add='address4' 
#     )
# add.save()
# add = Resource(resource_id='5',course_id= 'soften7',resource_name='resource5',resource_add='address5' 
#     )
# add.save()

# ##############################
#handle_uploaded_file(request.FILES[''])



def index(request):
    print request
    templates=loader.get_template('templates/index.html')
    context = RequestContext(request, {
    	'user': '1',
    	})
    response =  HttpResponse(templates.render(context))
    response.set_cookie('uid','31200000')
    response.set_cookie('type','student')
    response.set_cookie('username','sadad')
    response.set_cookie('uid','31200001')
    response.set_cookie('type','teacher')
    response.set_cookie('username','teacher1')
    # response.set_cookie('uid','31200002')
    # response.set_cookie('type','manager')
    # response.set_cookie('username','manager1')
    return response
def getcourselist(request):
    if request.COOKIES['type'] == 'student':
        return course.objects.filter(student_id=request.COOKIES['uid'])
    elif request.COOKIES['type'] == 'teacher':
        return course.objects.filter(teacher_id=request.COOKIES['uid'])
    else:
        return course.objects.filter(manager_id=request.COOKIES['uid'])

def resource(request):
    print 'sb'
    print request
    templates=loader.get_template('templates/Resource.html')
    #course_list = getcourselist(request)
    course_list = getcourselist(request)
    context = RequestContext(request, {
        'course_list': course_list,
        })
    print request.COOKIES['uid']
    return HttpResponse(templates.render(context))
def resourcecourse(request):
    print request.GET['course_id']
    course_name = request.GET['course_id']
    templates=loader.get_template('templates/ResourceCourse.html')
    course_list = getcourselist(request)
    notice_list = Notice.objects.filter(course_id=course_name).order_by('-date')
    homework_list = Homework.objects.filter(Q(course_id=course_name)&Q(end_date__gt=datetime.datetime.now())).order_by('-end_date')
    
    resource_list = Resource.objects.filter(Q(course_id=course_name)&Q(resource_top='1'))
    view_list = {}
    if request.COOKIES['type'] == 'student':
        sid = request.COOKIES['uid']
        view_l = Ex.objects.filter(student_id=sid)
        print view_l
        for i in view_l:
            view_list[i.homework_num] = 1;
    else:
        for i in homework_list:
            view_list[i.homework_num] = 1; 
    NewHomework = False
    for i in homework_list:
        if i.homework_num not in view_list:
            NewHomework = True
    if len(homework_list) > 5:
        homework_list = homework_list[0:5]
    if len(notice_list) > 5:
        notice_list = notice_list[0:5]     
    context = RequestContext(request, {
        'course_list': course_list,
        'Notice_list': notice_list,
        'course_id': course_name,
        'homework_list': homework_list,
        'resource_list': resource_list,
        'current_time': datetime.datetime.now(),
        'view_list': view_list,
        'NewHomework': NewHomework,
        })
    return HttpResponse(templates.render(context))
def resourcelist(request):
    print request.GET['course_id']
    course_name = request.GET['course_id']
    templates=loader.get_template('templates/ResourceList.html')
    course_list = getcourselist(request)
    resource_list = Resource.objects.filter(course_id=course_name)
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'resource_list': resource_list,
        })
    return HttpResponse(templates.render(context))

def noticelist(request):
    print request.GET['course_id']
    course_name = request.GET['course_id']
    templates=loader.get_template('templates/NoticeList.html')
    course_list = getcourselist(request)
    notice_list = Notice.objects.filter(course_id=course_name)
    context = RequestContext(request, {
        'course_list': course_list,
        'Notice_list': notice_list,
        'course_id': course_name,
        })
    return HttpResponse(templates.render(context))
def homeworklist(request):
    print request.GET['course_id']
    course_name = request.GET['course_id']
    templates=loader.get_template('templates/HomeworkList.html')
    course_list = getcourselist(request)
    if request.COOKIES['type'] == 'student':
        homework_list = Homework.objects.filter(Q(course_id=course_name)&Q(end_date__gt=datetime.datetime.now())).order_by('end_date')
    else:
        homework_list = Homework.objects.filter(course_id=course_name)
    
    view_list = {}
    if request.COOKIES['type'] == 'student':
        sid = request.COOKIES['uid']
        view_l = Ex.objects.filter(student_id=sid)
        print view_l
        for i in view_l:
            view_list[i.homework_num] = 1;
    else:
        for i in homework_list:
            view_list[i.homework_num] = 1; 

    NewHomework = False
    for i in homework_list:
        if i.homework_num not in view_list:
            NewHomework = True

    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'current_time': datetime.datetime.now(),
        'homework_list': homework_list,
        'view_list':view_list,
        'NewHomework': NewHomework,
        })
    return HttpResponse(templates.render(context))
def downloadhomework(request):
    templates=loader.get_template('templates/DownloadHomework.html')
    return HttpResponse(templates.render('fjoejf'))
def assignnotice(request):
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    templates=loader.get_template('templates/AssignNotice.html')
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        })
    return HttpResponse(templates.render(context))
def assignhomework(request):
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    templates=loader.get_template('templates/AssignHomework.html')
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        })
    return HttpResponse(templates.render(context))
def homework_display(request):
    homework_id = request.GET['homework_id']
    course_name = request.GET['course_id']
    homework_list = Homework.objects.filter(homework_num=homework_id)
    templates=loader.get_template('templates/Homework.html')
    course_list = getcourselist(request)
    if request.COOKIES['type'] == 'student':
        sid = request.COOKIES['uid']
        print ':'
        print Ex.objects.filter(Q(student_id=sid) & Q(homework_num=homework_id))
        
        if  len(Ex.objects.filter(Q(student_id=sid) & Q(homework_num=homework_id))) == 0:  
            print 'sb'
            add = Ex(student_id=sid,homework_num=homework_id,is_view=True,is_done=False)
            add.save()
            print 'aaaaaaa'
    context = RequestContext(request, {
        'homework': homework_list[0],
        'course_id': course_name,
        'course_list':course_list,
        })
    return HttpResponse(templates.render(context))

def notice_display(request):
    templates=loader.get_template('templates/Notice.html')
    notice_num = request.GET['notice_id']
    course_name = request.GET['course_id']
    notice = Notice.objects.filter(notice_num=notice_num)
    course_list = getcourselist(request)
    print course_list[0].course_id
    context = RequestContext(request, {
        'Notice': notice[0],
        'course_id': course_name,
        'course_list': course_list,
        })
    return HttpResponse(templates.render(context))

def delete_notice(request):
    templates=loader.get_template('templates/NoticeList.html')
    notice_num = request.GET['notice_id']
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    notice_list = Notice.objects.filter(course_id=course_name)
    try:
        Notice.objects.filter(notice_num=notice_num).delete()
        context = RequestContext(request, {
            'succ': 'yes',
            'course_id': course_name,
            'course_list':course_list,
            'Notice_list': notice_list,
            })
    except:
        context = RequestContext(request, {
            'succ': 'no',
            'course_id': course_name,
            'course_list':course_list,
            'Notice_list': notice_list,
            })
    return HttpResponse(templates.render(context))

def notice_assign(request):
    templates=loader.get_template('templates/AssignNotice.html')
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    try:
        global notice_number
        print '1'
        print notice_number 
        notice_number = notice_number + one
        print '2'
        class_id = request.GET['course_id']
       
        print '4'
        title = request.POST['title']
        print '5'
        content = request.POST['content']
        print '6'
        add = Notice(notice_num=str(notice_number),
            notice_title = title,
            course_id=class_id,
            content=content )
        print '7'
        add.save()
        print '8'
        print 'sssss'
        context = {
        'title': title,
        'content':content,
        'result': True,
        'course_list': course_list,
        'course_id': course_name,
        }
        return render_to_response('templates/AssignNotice.html',context)
    except:
        print 'sssd'
        context = {
        'title': request.POST['title'],
        'content':request.POST['content'],
        'result': False,
        'course_list': course_list,
        'course_id': course_name,
        }
        return render_to_response('templates/AssignNotice.html',context)

def resource_upload(request):
    global resource_number
    templates=loader.get_template('templates/ResourceList.html')
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    try:
        f = request.FILES['file']
        address = r'resource/'+f.name
        print address
        f = handle_uploaded_file(f,address)
        print address
        add = Resource(resource_id=str(resource_number+1),
            course_id=course_name,
            resource_name = f.name,
            resource_add = address,
            )
        resource_number += 1
        print address
        add.save()
        print address
        resource_list = Resource.objects.filter(course_id=course_name)
        context = RequestContext(request, {
        'succ': 'yes',
        'course_id':course_name,
        'course_list':course_list,
        'resource_list':resource_list,
        })
        return HttpResponse(templates.render(context))
    except:
        resource_list = Resource.objects.filter(course_id=course_name)
        context = RequestContext(request, {
        'succ': 'no',
        'course_id':course_name,
        'course_list':course_list,
        'resource_list':resource_list,
        })
        return HttpResponse(templates.render(context))

def handle_uploaded_file(f,address):
    with open(address, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
        info.close()
    return f
def read_file(filename, buf_size=8192):
    with open(filename, "rb") as f:
        while True:
            content = f.read(buf_size)
            if content:
                yield content
            else:
                break
def file_download(request):
    resource_b = request.GET['type']
    if resource_b == '1':
        resource_id = request.GET['resource_id']
        fre = Resource.objects.filter(resource_id=resource_id)[0].frequency
        Resource.objects.filter(resource_id=resource_id).update(frequency=(fre +1))
    filename = request.GET['address']
    f = read_file(filename)
    response = HttpResponse(f)
    response['Content-Disposition'] = 'attachment; filename=%s'  % filename.split('/')[-1]
    #response['Content-Length'] = len(f)
    return response

def delete_resource(request):
    templates=loader.get_template('templates/ResourceList.html')
    resource_id = request.GET['resource_id']
    a = Resource.objects.filter(resource_id=resource_id)

    os.remove(a[0].resource_add)
    Resource.objects.filter(resource_id=resource_id).delete()
    try:
        resource_name = request.GET['title']
    except:
        resource_name = ''
    course_name = request.GET['course_id']
    resource_list = Resource.objects.filter(course_id=course_name)
    course_list = getcourselist(request)
    result_list = Resource.objects.filter(Q(resource_name__contains=resource_name) & Q(course_id=course_name))
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'resource_list': resource_list,
        'result_list': result_list,
        'title':resource_name,
        })
    return HttpResponse(templates.render(context))

def stick_resource(request):
    templates=loader.get_template('templates/ResourceList.html')
    resource_id = request.GET['resource_id']
    try:
        resource_name = request.GET['title']
    except:
        resource_name = ''
    Resource.objects.filter(resource_id=resource_id).update(resource_top= '1')
    course_name = request.GET['course_id']
    result_list = Resource.objects.filter(Q(resource_name__contains=resource_name) & Q(course_id=course_name))
    resource_list = Resource.objects.filter(course_id=course_name)
    course_list = getcourselist(request)
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'resource_list': resource_list,
        'result_list': result_list,
        'title':resource_name,
        })
    return HttpResponse(templates.render(context))


def cancal_stick_resource(request):
    templates=loader.get_template('templates/ResourceList.html')
    resource_id = request.GET['resource_id']
    try:
        resource_name = request.GET['title']
    except:
        resource_name = ''
    course_name = request.GET['course_id']
    Resource.objects.filter(resource_id=resource_id).update(resource_top= '0')
    
    result_list = Resource.objects.filter(Q(resource_name__contains=resource_name) & Q(course_id=course_name))
    resource_list = Resource.objects.filter(course_id=course_name)
    course_list = getcourselist(request)
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'resource_list': resource_list,
        'result_list': result_list,
        'title':resource_name,
        })
    return HttpResponse(templates.render(context))

def search_resource(request):
    templates=loader.get_template('templates/ResourceList.html')
    try:
        resource_name = request.POST['title']
    except:
        resource_name = ''
    course_name = request.GET['course_id']
    order = request.POST['order']
    result_list = Resource.objects.filter(Q(resource_name__contains=resource_name) & Q(course_id=course_name))
    if order == 'time':
        result_list=result_list.order_by('-date')
    elif order == 'frequency':
        result_list=result_list.order_by('-frequency')   
    
    resource_list = Resource.objects.filter(course_id=course_name)
    course_list = getcourselist(request)
    context = RequestContext(request, {
        'course_list': course_list,
        'course_id': course_name,
        'resource_list': resource_list,
        'result_list': result_list,
        'title':resource_name,
        })
    return HttpResponse(templates.render(context))

def homework_upload(request):
    global homeworkfile_number
    templates=loader.get_template('templates/Homework.html')
    course_name = request.GET['course_id']
    homework_num = request.GET['homework_num']
    course_list = getcourselist(request)
    if request.COOKIES['type'] == 'student':
            sid = request.COOKIES['uid']
    try:
        f = request.FILES['file']
        address = r'homework/'+f.name
        f = handle_uploaded_file(f,address)
        add = HomeworkFile(homework_id=str(homeworkfile_number+1),
            homework_num=homework_num,
            course_id=course_name,
            student_id = sid,
            homework_add = address,
            )
        homeworkfile_number += 1
        add.save()
        print 'yyy'
        homeworkfile_list = HomeworkFile.objects.filter(course_id=course_name)
        context = RequestContext(request, {
        'succ': 'yes',
        'course_id':course_name,
        'course_list':course_list,
        'homeworkfile_list':homeworkfile_list,
        })
        
        Ex.objects.filter(Q(student_id=sid) & Q(homework_num=homework_id)).update(is_done=True)
        return HttpResponse(templates.render(context))
    except:
        homeworkfile_list = HomeworkFile.objects.filter(course_id=course_name)
        context = RequestContext(request, {
        'succ': 'no',
        'course_id':course_name,
        'course_list':course_list,
        'homeworkfile_list':homeworkfile_list,
        })
        return HttpResponse(templates.render(context))

def gethomework_list(request):
    templates=loader.get_template('templates/DownloadHomework.html')
    course_name = request.GET['course_id']
    homework_num = request.GET['homework_num']
    course_list = getcourselist(request)
    homeworkfile_list = HomeworkFile.objects.filter(Q(homework_num=homework_num)
        & Q(course_id=course_name))

    context = RequestContext(request, {
        'course_id':course_name,
        'course_list':course_list,
        'homeworkfile_list':homeworkfile_list,
        })
    return HttpResponse(templates.render(context))

def delete_homework(request):
    templates=loader.get_template('templates/HomeworkList.html')
    course_name = request.GET['course_id']
    homework_num = request.GET['homework_num']
    course_list = getcourselist(request)
    Homework.objects.filter(homework_num=homework_num).delete()
    homework_list = Homework.objects.filter(course_id=course_name)
    context = RequestContext(request, {
        'course_id':course_name,
        'course_list':course_list,
        'homework_list':homework_list,
        })
    return HttpResponse(templates.render(context))

def homework_assign(request):
    course_name = request.GET['course_id']
    course_list = getcourselist(request)
    try:
        global homework_number
        print '1'
        homework_number = homework_number + one
        print '2'
        class_id = request.GET['course_id']
        
        print '4'
        title = request.POST['title']
        print '5'
        deadline = request.POST['deadline']
        content = request.POST['content']
        print '6'
        add = Homework(homework_num=str(homework_number),
            course_id = class_id,
            title = title,
            end_date = deadline,
            content=content )
        print '7'
        add.save()
        print '8'
        print 'sssss'
        context = {
        'title': title,
        'course_list':course_list,
        'content':content,
        'course_id':course_name,
        'result': True,
        }
        return render_to_response('templates/AssignHomework.html',context)
    except:
        print 'sssd'
        context = {
        'title': request.POST['title'],
        'course_list':course_list,
        'course_id':course_name,
        'content':request.POST['content'],
        'result': False,
        }
        return render_to_response('templates/AssignHomework.html',context)


