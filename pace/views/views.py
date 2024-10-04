import json

from django.http import JsonResponse
from django.shortcuts import render, redirect

from pace.models import Profile


def index(request):
    if request.user.is_authenticated:
        return render(request, "pace/index.html")
    else:
        return redirect('login')



def setup(request):
    if request.method == "POST":
        # Assuming the user is already authenticated
        user = request.user
        user_profile = user.profile

        # Parse the JSON data from the request body
        data = json.loads(request.body)

        # Update the user profile with the data received
        user_profile.first_name = data.get("fullName", "")
        user_profile.email = data.get("email", "")
        user_profile.age = data.get("age", "")  # Assuming you have an age field in the user_profile
        user_profile.learning_style = data.get("learningStyle", "")
        user_profile.education_level = data.get("educationLevel", "")
        user_profile.interests = data.get("interests", [])
        user_profile.goals = data.get("goals", [])
        user_profile.is_setup = True

        # Save the updated user_profile
        user_profile.save()

        # Return a JSON response indicating success
        return JsonResponse({"message": "Profile updated successfully."}, status=200)

    # If not a POST request, return a method not allowed response

    return render(request, "pace/user/setup.html", {
        "profile": Profile.objects.filter(user=request.user).first(),
        "edu_list": ["Primary", "Secondary", "High School", "Undergraduate", "Graduate", "Professional"],
        "style_list": ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"],

    })

def profile(request):
    return render(request, "pace/user/profile.html", {
        "profile": Profile.objects.filter(user=request.user).first(),
        "edu_list": ["Primary", "Secondary", "High School", "Undergraduate", "Graduate", "Professional"],
        "style_list": ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"],
    })