from django.shortcuts import redirect, render
from . models import MovieInfo
from .forms import MovieForm
# Create your views here.

# def create(request):
#     # frm=MovieForm
#     if request.POST:
#         frm=MovieForm(request.POST,request.FILES)
#         print(request.FILES) 
#         if frm.is_valid():
#             frm.save()
#             return redirect('create')

#              else:
#                   frm = MovieForm()
#     return render(request, "create.html",{'frm':frm})

def create(request):
    frm = None  # Initialize with None
    if request.POST:
        frm = MovieForm(request.POST, request.FILES)
        print(request.FILES) 
        if frm.is_valid():
            frm.save()
            return redirect('create')
        else:
            frm = MovieForm()
    else:
        frm = MovieForm() 


    # print("fmr@#@#@#@#@#@#@#@#@#@#@#@#",frm)
    return render(request, "create.html", {'frm': frm})



'''def list(request):
    movie_data = {
        'movies': [
            {
                'title': 'Godfather',
                'summary': 'Story of an underworld King',
                'year': 1990,
                'success': True,
                'img': 'godfather.jpg'
            },
            {
                'title': 'Titanic',
                'summary': 'Unsuccessful Love',
                'year': 1997,
                'success': True,
                'img': 'titanic.jpg'
            },
            {
                'title': 'Into The Wild',
                'summary': 'Story of Travel',
                'year': 2009,
                'success': True,
                'img': 'intothewild.jpg'
            },
        ]
    }'''

def list(request):
    movie_set =MovieInfo.objects.all()
    print(movie_set)

    return render(request, 'list.html', {'movies': movie_set})

def edit(request,pk):
    edited= MovieInfo.objects.get(pk=pk)

    if request.POST:
        frm=MovieForm(request.POST,instance=edited)
        if frm.is_valid():
            edited.save()
    else:
        frm=MovieForm(instance=edited)

    ''' 
        title=request.POST.get('title')
        year=request.POST.get('year')
        description=request.POST.get('description')
        edited.title=title
        edited.year=year
        edited.description=description
        '''


    edited= MovieInfo.objects.get(pk=pk)
    frm=MovieForm(instance=edited)

    return render(request, "create.html",{'frm':frm})


def delete(request, pk):
    instance = MovieInfo.objects.get(pk=pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()

    return render(request, 'list.html', {'movies': movie_set})

'''
def delete(request, movie_id):
    movie = MovieInfo.objects.get(pk=movie_id)
    movie.delete()
    return render(request, 'list.html', {'movies': MovieInfo.objects.all()})
'''
# postman
