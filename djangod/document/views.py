from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse


from .models import Article
from .models import Question,Choice,Employee
from django.template.loader import get_template
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
import reportlab
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework import mixins
from rest_framework import viewsets
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'document/year_archive.html', context)

# Create your views here.
def month_archive(request, month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {'month': month, 'article_list': a_list}
    return render(request, 'document/month_archive.html', context)


def article_detail(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'document/year_archive.html', context)    



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'document/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#             'latest_question_list': latest_question_list,
        
#     }
#     return render(request,'document/index.html',context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'document/detail.html', {'question': question})



# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'document/results.html', {'question': question})   


# class IndexView(generic.ListView):
#     template_name = 'document/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'document/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'document/results.html'


# def vote(request, question_id):
#     ... # same as above, no changes needed.     



import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# create automatic pdf
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


from .models import Fruits
def home(request):
    payload=[]
    db=None
    if cache.get('fruits'):
        payload=cache.get('fruits')
        db='redis'
        print(cache.ttl('fruits'))
    else:    
        objs=Fruits.objects.all()

    
        for obj in objs:
            payload.append(obj.fruit_name)
        db='sqllite'
        cache.set('fruits',payload)    

    return JsonResponse({'status':200,'db': db,' data':payload})


# class EmployeeList(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self,request):
#         employee=Employee.objects.all()
#         serializer=EmployeeSerializer(employee,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer=EmployeeSerializer(data=request.data)

#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         return Response("not valid ")   




from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django.core.exceptions import ValidationError
from django.contrib import messages
from rest_framework.decorators import action


# local imports

class  EmployeeViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
   
    
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    # permission_classes = [IsAuthenticated,]



    def list(self, request, *args, **kwargs):
        
        return Response(
            super().list(request, *args, **kwargs).data)

    def retrieve(self, request, *args, **kwargs):
        
        return Response(
            super().retrieve(request, *args, **kwargs).data
        )

    def create(self, request, *args, **kwargs):
        
        return Response(
            super().create(request, *args, **kwargs).data)

    def update(self, request, *args, **kwargs):
        
        return Response(
            super().update(request, *args, **kwargs).data)

    def destroy(self, request, *args, **kwargs):
        
        return Response(
            super().destroy(request, *args, **kwargs).data
        )


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
#Generate Pdf Dynamically.
def venue_pdf(request):
    bf=io.BytesIO()
    c=canvas.Canvas(bf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica" ,14)

    lines=[
         "my name is chirag",
         "what is your name",
         "please let me know",
    ]
    for line in lines:
            textob.textLine(line)


    c.drawText(textob)
    c.showPage()
    c.save()
    bf.seek(0)


    return FileResponse(bf,as_attachment=True,filename='venue.pdf')


class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



  
class TodoDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, todo_id, user_id):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Todo.objects.get(id=todo_id, user = user_id)
        except Todo.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, todo_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TodoSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, todo_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # 5. Delete
    def delete(self, request, todo_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(todo_id, request.user.id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )    



#file converter using celery
from django.core.files.storage import FileSystemStorage
import os 
from docx2pdf import convert


def index(request):
    if request.method=='POST':
        myfile=request.FILES['file']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        convert('/static/' +myfile.name)







    return render(request,'home.html')
