from django.urls import path

from . import views
from rest_framework import routers
from .views import EmployeeViewSet,TodoListApiView,TodoDetailApiView

router = routers.SimpleRouter()

router.register('employee',EmployeeViewSet,'employee')

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
    #   path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    #  path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),


    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('some_view/',views.some_view,name='some_view'),
    path('home',views.home),
    path('Todo', TodoListApiView.as_view()),
     path('Todo/<int:todo_id>/', TodoDetailApiView.as_view()),
     path('venue_pdf',views.venue_pdf),
     path('index',views.index,name='index')
   
    





# local imports


] + router.urls

