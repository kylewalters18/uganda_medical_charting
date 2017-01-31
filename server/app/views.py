from rest_framework import viewsets
from server.app.serializers import PatientSerializer, NoteSerializer
from server.app.models import Patient, Note


class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited
    """
    serializer_class = NoteSerializer

    def get_queryset(self):
      """
      This view should return all the notes for the specified patient
      """
      patient = self.kwargs['patient']
      return Note.objects.filter(patient=patient)
