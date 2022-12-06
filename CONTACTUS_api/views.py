from rest_framework import filters, status, viewsets, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

class contact_usView(CreateAPIView):
    queryset = models.contact_us.objects.all()
    serializer_class = serializers.contact_usSerializer
    search_fields = ("phone_number", "your_message")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
