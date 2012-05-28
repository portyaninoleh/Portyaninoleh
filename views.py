# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
import datetime
from mysite.books.models import Book
from django.core.mail import send_mail
from mysite.forms import ContactForm
from django.shortcuts import render_to_response

def currentTimeTemplate(request):
    nowTemp = datetime.datetime.now()
    temp = get_template('currentDatetime.html')
    con = Context({'currentDate': nowTemp})
    html = temp.render(con)
    return HttpResponse(html)

def currentTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



def hoursAhead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('nextTime.html', {'nextTime': dt})

def hello(request):
    host = request.get_host()
    path = request.path
    full_path = request.get_full_path()
    user_agent = request.META['HTTP_USER_AGENT']
    return render_to_response("hello.html", {'host': host, 'path': path, 'full_path': full_path, 'user_agent': user_agent})


def timeRender(request):
    nowRender = datetime.datetime.now()
    return render_to_response('currentDatetime.html', {'currentDate': nowRender})

def get_request(request):
    n = request.META.items()
    n.sort()
    html = []
    for k, m in n:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, m))
    return HttpResponse('<table>%s</table>' % '\n'. join(html))

def athlets(request):
    t = get_template('test.html')
    athlet_list = ['Oleh']
    con = Context(athlet_list)
    html = t.render(con)
    return HttpResponse(html)
#def search_form(request):
#    return render_to_response("search_form.html")

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term')
        elif len(q) > 20:
            errors.append('Enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

#def contact(request):
#    errors = []
#    if request.method == "post":
#        if not request.POST.get('subject', ''):
#            errors.append('Enter a subject')
#        if not request.POST.get('message', ''):
#            errors.append('Enter the message')
#        if request.POST.get('email') and '@' not in request.POST['email']:
#            errors.append('enter a valid mailbox')
#        if not errors:
#            send_mail(
#                request.POST['subject'],
#                request.POST['message'],
#                request.POST.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
#            return HttpResponseRedirect('/contact/thanks')
#    return render_to_response('contact_form.html', {'errors': errors})

def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        import ipdb; ipdb.set_trace()
        if not form. is_valid():
#            cd = form.cleaned_data

#            send_mail(
#                cd['subject'],
#                cd['message'],
#                cd.get('email', 'noreply@example.com'),
#                ['siteowner@example.com'],
#            )
            return HttpResponseRedirect('/contact_us/')
        else:
            return render_to_response('contact_form.html', {'error': 'fuck ye)))'})
    else:
        form = ContactForm(
            initial = {'subject': 'I love your site'}
        )
        return render_to_response('contact_form.html', {'form': form})