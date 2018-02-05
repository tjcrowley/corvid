from django.contrib.sessions.models import Session
from tracking.models import Visitor
from datetime import datetime

class UserRestrictMiddleware(object):
    """
    Prevents more than one user logging in at once from two different IPs
    """
    def process_request(self, request):
        ip_address = request.META.get('REMOTE_ADDR','')
        try:
            last_login = request.user.last_login
        except:
            last_login = 0
        if unicode(last_login)==unicode(datetime.now())[:19]:
            previous_visitors = Visitor.objects.filter(user=request.user).exclude(ip_address=ip_address)
            for visitor in previous_visitors:
                Session.objects.filter(session_key=visitor.session_key).delete()
                visitor.user = None
                visitor.save()
                
class SubdomainMiddleware:
    def process_request(self, request):
        host = request.META.get('HTTP_HOST', '')
        host_s = host.replace('www.', '').split('.')
        request.subdomain = None
        if len(host_s) > 2:
            request.subdomain = host_s[0]
            if request.path =="/accounts/signup/":
                request.subdomain = "www"
            if request.path =="/accounts/login/":
                request.subdomain = "www"