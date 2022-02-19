from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Chat
from django.http import HttpResponse, JsonResponse
from .forms import ChatForm
from .serializers import ChatSerializer



def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH", False) == "XMLHttpRequest"

class ChatMain(LoginRequiredMixin , View):

    login_url = "login"

    def get(self ,request): 

        if is_ajax(request) == False:
            if "last_message" not in request.session:
                request.session["last_message"] = 0

                if Chat.objects.all().exists():
                    request.session["last_message"] = Chat.objects.all().order_by("-pk")[0].pk
            else:
                if Chat.objects.all().exists():
                    request.session["last_message"] = Chat.objects.all().order_by("-pk")[0].pk
                    

        if is_ajax(request=request):
            
            if Chat.objects.filter(pk__gt = request.session["last_message"]).exists():
                query  = Chat.objects.filter(pk__gt = request.session["last_message"])
                request.session["last_message"] = query.order_by("-pk")[0].pk

                se_query = ChatSerializer(query , many=True)
                return JsonResponse(se_query.data , safe=False , status = 200)
            else:
                return JsonResponse({} , safe=False , status = 200)

        else:

            if Chat.objects.all().exists():
                request.session["last_message"] = Chat.objects.all().order_by("-pk")[0].pk
    
            form = ChatForm()            
            context = {
                        'form' : form,
                        'chats': Chat.objects.all()
                    }
            return render(request , "main.html" , context)

    def post(self , request):

        chat = Chat(text = request.POST["chat"] , user = request.user)
        chat.save()
        return HttpResponse("")
