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