from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
from .models import Profile
from .models import BlogAdmin

@csrf_exempt
def profile(request, encoded):
    """Gets the team profile"""
    if request.method == 'GET':
        try:
            decode_data = base64.b64decode(encoded).decode('utf-8')
            get_name = decode_data.split('-')[1]
            get_firstName = get_name.split('_')[0]
            personal_data = Profile.objects.get(first_name=get_firstName)
            data = {
                'first_name': personal_data.first_name,
                'last_name': personal_data.last_name,
                'roles': personal_data.roles,
                'intro': personal_data.intro,
                'image': personal_data.image.url,
                'twitter': personal_data.twitter_handle,
                'facebook': personal_data.facebook_handle,
                'instagram': personal_data.instagram_handle
            }
            # return render(request, 'data/data.html', {'data': data})
            return JsonResponse({'Information': data}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)
        
# @csrf_exempt
# def create_profile(request):
#     """Creates a team profile"""
#     if request.method == 'POST':
#         try:
#             data = request.POST
#             image_file = request.FILES.get('image')
#             # read_image = image_file.read()
#             Profile.objects.create(
#                 first_name=data['first_name'],
#                 last_name=data['last_name'],
#                 roles=data['roles'],
#                 intro = data['intro'],
#                 image=image_file
#             )
#             return JsonResponse({'message': 'Profile created successfully'}, status=201)
#         except Exception as e:
#             return JsonResponse({'error': f'Profile not created {e}'}, status=401)

@csrf_exempt
def create_post(request):
    """Creates a post"""
    if request.method == 'POST':
        data = {
            'title': request.POST.get('title'),
            'body': request.POST.get('body')
        }

        if not all(data.values()):
            return JsonResponse({'error': 'Some Fields are missing'}, status=400)
        BlogAdmin.objects.create(title=data['title'], body=data['body'])
        return JsonResponse({'message': 'Added successfully'}, status=201)
    
@csrf_exempt
def get_post(request):
    """Gets new blog data after ever update"""
    if request.method == 'GET':
        blog = BlogAdmin.objects.all()
        blog_count = []
        for count in blog:
            define_all = {
                'title': count.title,
                'categories': count.categories,
                'subheading': count.subheading,
                'image': count.image.url,
                'body': count.body,
                'time': count.created_at.strftime("%d-%m-%Y")
            }
            blog_count.append(define_all)
        return JsonResponse({'blog_post': blog_count}, status=201)
    
