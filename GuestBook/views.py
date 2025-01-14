from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets

from .serializer import CommentSerializer, CommentCreateSerializer
from .models import Comment

@api_view(['GET', 'POST'])
def comment(request):
    if request.method == "GET":
        comment_list = Comment.objects.all().order_by('-create_date')
        
        if comment_list == False:
            return Response(status=404)
        
        else:
            serializer = CommentSerializer(comment_list, many = True)
            return Response(serializer.data, status=200)
    elif request.method == "POST":
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDelete(viewsets.ModelViewSet):
    serializer_class= CommentSerializer
    queryset=Comment.objects.all()