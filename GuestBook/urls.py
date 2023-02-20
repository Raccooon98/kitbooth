from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('all/', views.get_comment_list),
    path('create/', views.create_comment)
]

##전체 정보 조회(req: {} -> res : {clubList : {...}})
#방명록 작성(req : {comment : "ddddd"} -> res : {name : dd, ddd: sss, ...})
urlpatterns = format_suffix_patterns(urlpatterns)