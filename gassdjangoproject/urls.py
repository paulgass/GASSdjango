from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework import permissions
from rest_framework.decorators import api_view
from gassdjangoproject.gassdjangoapp import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

swagger_info = openapi.Info(
    title="API",
    default_version='v1',
    description="Here Are The gassdjangoproject API Endpoints"
)

SchemaView = get_schema_view(
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>.json|.yaml)$', SchemaView.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', SchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', SchemaView.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/', TemplateView.as_view(template_name='api.html'), name='api'),
    path('database/', TemplateView.as_view(template_name='database.html'), name='database'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('signin/', TemplateView.as_view(template_name='signin.html'), name='signin'),
    path('api/v1/_test', views.TestView.as_view(), name="1"),
    path('api/v1/_test-int/<int:test_userinput_int>', views.TestViewINT.as_view(), name="2"), 
    path('api/v1/_test-str/<str:test_userinput_str>', views.TestViewSTR.as_view(), name="3"), 
    path('api/v1/_test-slug/<slug:test_userinput_slug>', views.TestViewSLUG.as_view(), name="4"), 
    path('api/v1/_test-uuid/<uuid:test_userinput_uuid>', views.TestViewUUID.as_view(), name="5"), 
    path('api/v1/_test-path/<path:test_userinput_path>', views.TestViewPATH.as_view(), name="6"),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/v1/odt', views.ExportODT.as_view(), name="8"),
    path('api/v1/doc', views.ExportDOC.as_view(), name="9"),
    path('api/v1/docx', views.ExportDOCX.as_view(), name="10"),
    path('api/v1/csv', views.ExportCSV.as_view(), name="11"),
    path('api/v1/ods', views.ExportODS.as_view(), name="12"),
    path('api/v1/xls', views.ExportXLS.as_view(), name="13"),
    path('api/v1/xlsx', views.ExportXLSX.as_view(), name="14"),
    path('api/v1/odp', views.ExportODP.as_view(), name="15"),
    path('api/v1/ppt', views.ExportPPT.as_view(), name="16"),
    path('api/v1/pptx', views.ExportPPTX.as_view(), name="17"),
    path('api/v1/pdf', views.ExportPDF.as_view(), name="18"),
    path('api/v1/html', views.ExportHTML.as_view(), name="19"),
    path('api/v1/htm', views.ExportHTM.as_view(), name="20"),
    path('api/v1/json', views.ExportJSON.as_view(), name="21"),
    path('api/v1/sql', views.ExportSQL.as_view(), name="22"),
    path('api/v1/txt', views.ExportTXT.as_view(), name="23"),
    path('api/v1/rtf', views.ExportRTF.as_view(), name="24"),
    path('api/v1/jpg', views.ExportJPG.as_view(), name="25"),
    path('api/v1/jpeg', views.ExportJPEG.as_view(), name="26"),
    path('api/v1/png', views.ExportPNG.as_view(), name="27"),
    path('api/v1/mp3', views.ExportMP3.as_view(), name="28"),
    path('api/v1/gif', views.ExportGIF.as_view(), name="29"),
    path('api/v1/qrcode', views.ExportQRCode.as_view(), name="30"),
    path('api/v1/qrcodeUserInput/<path:qrcode_text>', views.ExportQRCodeUserInput.as_view(), name="31"),
    path('api/v1/zip', views.ExportZIP.as_view(), name="32"),
    path('api/v1/mongoDB/<path:mDB_cluster_ConnectionStringOnly>/<str:mDB_cluster_database>/<str:mDB_cluster_database_collection>/<str:mDB_cluster_database_collection_item_id>/<str:mDB_cluster_database_collection_item_name>', views.MongoDB.as_view(), name='mongodbdjango')
]
