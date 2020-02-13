from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from gassdjangoproject.gassdjangoapp.serializers import TestSerializer
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import os
import pymongo

from gassdjangodataexport import data_export

class HelloView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		return HttpResponse("Success! User is JWT Authenticated.", status=200)
		
class TestView(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		return HttpResponse("This Is Example Text For gassdjangoproject HTTP Response", status=200)
		
class TestViewINT(GenericAPIView): 
	serializer_class = TestSerializer 
	def post(self, request, test_userinput_int, format=None): 
		return HttpResponse("gassdjangoproject User Input INT: %s" % (test_userinput_int), status=200)
		
class TestViewSTR(GenericAPIView): 
	serializer_class = TestSerializer 
	def post(self, request, test_userinput_str, format=None): 
		return HttpResponse("gassdjangoproject User Input STR: %s" % (test_userinput_str), status=200)
		
class TestViewSLUG(GenericAPIView): 
	serializer_class = TestSerializer 
	def post(self, request, test_userinput_slug, format=None): 
		return HttpResponse("gassdjangoproject User Input SLUG: %s" % (test_userinput_slug), status=200)
		
class TestViewUUID(GenericAPIView): 
	serializer_class = TestSerializer 
	def post(self, request, test_userinput_uuid, format=None): 
		return HttpResponse("gassdjangoproject User Input UUID: %s" % (test_userinput_uuid), status=200)
		
class TestViewPATH(GenericAPIView): 
	serializer_class = TestSerializer 
	def post(self, request, test_userinput_path, format=None): 
		return HttpResponse("gassdjangoproject User Input PATH: %s" % (test_userinput_path), status=200)
		
class ExportODT(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadODT()
		return response

class ExportDOC(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadDOC()
		return response

class ExportDOCX(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadDOCX()
		return response

class ExportCSV(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadCSV()
		return response

class ExportODS(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadODS()
		return response

class ExportXLS(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadXLS()
		return response

class ExportXLSX(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadXLSX()
		return response

class ExportODP(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadODP()
		return response

class ExportPPT(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadPPT()
		return response

class ExportPPTX(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadPPTX()
		return response

class ExportPDF(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadPDF()
		return response

class ExportMP3(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadMP3()
		return response

class ExportHTML(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadHTML()
		return response

class ExportHTM(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadHTM()
		return response
	
class ExportJSON(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadJSON()
		return response

class ExportSQL(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadSQL()
		return response

class ExportTXT(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadTXT()
		return response

class ExportRTF(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadRTF()
		return response

class ExportJPG(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadJPG()
		return response

class ExportJPEG(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadJPEG()
		return response

class ExportPNG(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadPNG()
		return response

class ExportGIF(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadGIF()
		return response

class ExportQRCode(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadQRCode()
		return response

class ExportQRCodeUserInput(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, qrcode_text, format=None):
		response = data_export.downloadQRCodeUserInput(qrcode_text)
		return response

class ExportZIP(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, format=None):
		response = data_export.downloadZIP()
		return response
		
class MongoDB(GenericAPIView):
	serializer_class = TestSerializer
	def post(self, request, mDB_cluster_ConnectionStringOnly, mDB_cluster_database, mDB_cluster_database_collection, mDB_cluster_database_collection_item_id, mDB_cluster_database_collection_item_name, format=None):
		cluster = pymongo.MongoClient(mDB_cluster_ConnectionStringOnly)
		db = cluster[mDB_cluster_database]
		collection = db[mDB_cluster_database_collection]
		post1 = {"_id":mDB_cluster_database_collection_item_id,"name":mDB_cluster_database_collection_item_name}
		collection.insert_one(post1)
		return HttpResponse("mongoDB Cloud @ https://cloud.mongodb.com/", status=200)
