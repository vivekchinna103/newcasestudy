from django.urls import re_path,path
from CaseStudyApp import viewss,views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('allCases/',viewss.get_all_cases,name="getallcasesapi"),
    re_path(r'^case/([0-9]+)$',views.casestudyApi),
    path('case/<int:id>/', viewss.get_case_id, name='getcasewithid'),
    path('filter/', viewss.filter_endpoint, name='filter'),
    re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)