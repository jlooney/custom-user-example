from django.shortcuts import render
from blog.models import MyUser
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView

class HomePageView(ListView):
    model = MyUser



class UserProfileView(View):
    def get(self, request, user_id):

        try:
            user = MyUser.objects.get(id=user_id)
        except:
            user = None

        context = {
            "viewed_user": user
        }

        return render(request, "user_profile.html", context)