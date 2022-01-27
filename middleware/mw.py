import re

from django.utils.deprecation import MiddlewareMixin

class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info

        times = self.visit_times.get(ip_address, 0)
        self.visit_times[ip_address] = times + 1
