## Airline Boarding Ticket pdf file to mail
## Step
#requirement install package
#pip3.7 install xhtml2pdf html5lib pypdf
#
#1. 구간 및 날짜 선택
#2. 조회
#3. 예약
#4. 결제
#5. 예약내역 pdf 파일 변환 및 이메일 발송
#"""

from django.shortcuts import render
import reportlab
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from io import BytesIO
from io import StringIO
#import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
#from cgi import escape
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView
#from weasyprint import HTML
from django.core.files.storage import FileSystemStorage
from django.views.generic import View
from airline_cousrse_search.models import *
from .render import Render


# 예약 티켓 다운로드 및 PDF 출력기능 model_name e.g) GmptoCju======

#path('b_gmp2cju_dl/', b_gmp2cju_dl.as_view(), name="b_gmp2cju_dl"),
#path('b_gmp2pus_dl/', b_gmp2pus_dl.as_view(), name="b_gmp2pus_dl"),
#path('b_cju2pus_dl/', b_cju2pus_dl.as_view(), name="b_cju2pus_dl"),
#path('b_cju2gmp_dl/', b_cju2gmp_dl.as_view(), name="b_cju2gmp_dl"),
#path('b_pus2cju_dl/', b_pus2cju_dl.as_view(), name="b_pus2cju_dl"),
#path('b_pus2gmp_dl/', b_pus2gmp_dl.as_view(), name="b_pus2gmp_dl"),



# 전체구간 조회
class boarding_ticket_download(View):
    def get(self, request):
        object_list = CargoAll.objects.all()
        params = {
            'object_list': object_list,
            'request': request
        }
        return Render.render('airline_course_search/airline_full_time.html', params)


#김포 - 제주구간 pdf 파일 출력
class b_gmp2cju_dl(View):
    def get(self, request):
        object_list = GmptoCju.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_gmp2cju.html', params)


#김포 - 부신구간 pdf 파일 출력
class b_gmp2pus_dl(View):
    def get(self, request):
        object_list = GmptoPus.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_gmp2pus.html', params)


#제주 - 부신구간 pdf 파일 출력
class b_cju2pus_dl(View):
    def get(self, request):
        object_list = CjutoPus.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_cju2pus.html', params)


#제주 - 김포구간 pdf 파일 출력
class b_cju2gmp_dl(View):
    def get(self, request):
        object_list = CjutoGmp.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_cju2gmp.html', params)


#부산 - 제주구간 pdf 파일 출력
class b_pus2cju_dl(View):
    def get(self, request):
        object_list = PustoCju.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_pus2cju.html', params)


#부산 - 김포구간 pdf 파일 출력
class b_pus2gmp_dl(View):
    def get(self, request):
        object_list = PustoGmp.objects.all()
        params = {
            'object_list' : object_list,
            'request' : request
        }
        return Render.render('airline_course_search/flight_list_pus2gmp.html', params)



# 예약 티켓 다운로드 및 PDF 출력기능 ======

# TEST ======
def boarding(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="boarding_ticket.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 100, "Airline Boarding Ticket.")
    p.showPage()
    p.save()
    return response
    return render(request, 'Ticketing/ticket_list.html')
# TEST ======


#==== Code Search ====#

#class PDFTemplateResponse(TemplateResponse):

#    def generate_pdf(self, retval):

#        html = self.content
#        result = StringIO,StringIO()
#        rendering = pisa.pisaDocument(StringIO,StringIO(html.encode("ISO-8859-1")), result)

#        if not rendering.err:
#            return HttpResponse('customer boarding ticket not found<pre>%s</pre>' % escape(html))
#        else:
#            self.content = result.getvalue()

#    def __init__(self, *args, **kwargs):
#        super(PDFTemplateResponse, self).__init__(*args, content_type="application/pdf", **kwargs) ##orig:mimetype
#        self.add_post_render_callback(self.generate_pdf)


## pdf file export
#class PDFTemplateView(TemplateView):
#    response_class = PDFTemplateResponse

#class Boarding_Ticket_View(PDFTemplateView):
#    template_name = './test.html'


#def ticket_view(request):
#    response = HttpResponse(content_type='application/pdf')
#    response['Content-Disposition'] = 'attachment; filename="boarding_ticket.pdf"'

#    buffer = BytesIO()

#    p = canvas.Canvas(response)
#    p.drawString(100,100, "Hello world")
#    p.showPage()
#    p.save()

#    pdf = buffer.getvalue()
#    buffer.close()
#    response.write(pdf)
#    return response
