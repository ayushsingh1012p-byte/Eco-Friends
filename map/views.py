# from django.shortcuts import render, redirect
# from .models import Bin
# from django.contrib.auth.decorators import login_required

# @login_required
# def bins_map(request):
#     bins = Bin.objects.all()
#     return render(request, 'map.html', {'bins': bins})


# @login_required
# def add_bin(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         lat = request.POST.get('lat')
#         lon = request.POST.get('lon')
#         image = request.FILES.get('image')

#         Bin.objects.create(
#             user=request.user,
#             name=name,
#             description=description,
#             latitude=lat,
#             longitude=lon,
#             image=image
#         )
#         return redirect('map')
#     return render(request, 'add_bin.html')
