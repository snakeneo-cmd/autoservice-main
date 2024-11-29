from django.shortcuts import render

def index(request):
    return render(request, 'autoservice/index.html')

def statistics(request):
    context = {
        'paslaugu_kiekis': 10,  # Replace with actual data
        'uzsakymu_kiekis': 5,   # Replace with actual data
        'automobiliu_kiekis': 3 # Replace with actual data
    }
    return render(request, 'autoservice/statistics.html', context)