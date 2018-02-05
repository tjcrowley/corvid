from django.contrib.sessions.models import Session

class OnlyOneUserMiddleware(object):
    """
    Middleware to ensure that a logged-in user only has one session active.
    Will kick out any previous session. 
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            cur_session_key = request.user.get_profile().session_key
            if cur_session_key and cur_session_key != request.session.session_key:
                # Default handling... kick the old session...
                try:
                    s = Session.objects.get(session_key=cur_session_key)
                    s.delete()
                except ObjectDoesNotExist:
                    pass
            if not cur_session_key or cur_session_key != request.session.session_key:
                p = request.user.get_profile()
                p.session_key = request.session.session_key
                p.save()
                                
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