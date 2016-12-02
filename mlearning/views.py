from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Term, Assessment, Glossary
from .serializers import TermSerializer, AssessmentSerializer, GlossarySerializer


# Create your views here.
class TermList(APIView):
    def get(self, request):
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data)


class AssessmentList(APIView):
    def get(self, request):
        assessments = Assessment.objects.all()
        serializer = AssessmentSerializer(assessments, many=True)
        return Response(serializer.data)


class GlossaryList(APIView):
    def get(self, request):
        glossary_list = Glossary.objects.all()
        serializer = GlossarySerializer(glossary_list, many=True)
        return Response(serializer.data)
