from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,ProfileUpdateForm,UserUpdateForm
from .serializer import ProfileSerializer
from .models import Profile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')

            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Your account has been updated!')

            return redirect('profile') 


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    ctx = {
        "u_form": u_form,
        "p_form": p_form
    }

    return render(request, 'users/profile.html',ctx)


class ProfileListApi(APIView):
    def get(self, request, format=None):
        all_profile = Profile.objects.all()

        serializers = ProfileSerializer(all_profile,many=True)

        return Response(serializers.data)



    def post(self, request, format=None):

        serializers = ProfileSerializer(data=request.data)
        # permission_classes = (IsAdminOrReadOnly)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


