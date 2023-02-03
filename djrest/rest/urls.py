from django.urls import path
from .import views

urlpatterns = [
    path('snippets/', views.snippet_list),  #function based views 
    # path('snippets/', views. SnippetList.as_view()),  #class  based views,mixins,generics 
    path('snippets/<int:pk>/', views.snippet_detail), #function based views 
    # path('snippets/<int:pk>/', views. SnippetDetail.as_view()),   #class  based views,mixins,generics 
]