from django.shortcuts import render

pokemon = [
  {'name': 'Pikachu', 'type': 'electric', 'description': 'pika pika type shit', 'age': 5},
  {'name': 'Oshawott', 'type': 'water', 'description': 'cute fr', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
   return render(request, 'about.html')

def pokemon_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'pokemon/index.html', {
    'pokemon': pokemon
  })