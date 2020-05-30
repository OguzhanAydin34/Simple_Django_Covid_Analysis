from django.shortcuts import render
from django.http import HttpResponse
import first_app.deneme as deneme
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")
my_dict = {'insert_me': "Hello I am from views.py!"}
country_hidden="hidden"
world_hidden="hidden"
table_hidden="hidden"
pie_hidden="hidden"
def index(request):
    countryName=request.GET.get('CountryName')
    dateData = request.GET.get('dataDate')
    world0=request.GET.get('world')
    country0=request.GET.get('country')
    table=0
    global country_hidden
    global world_hidden
    global table_hidden
    global pie_hidden
    if(world0):
        country_hidden="hidden"
        table_hidden="hidden"
        world_hidden="visible"
    if(country0):
        world_hidden="hidden"
        pie_hidden="hidden"
        country_hidden="visible"
    countriesAsOption=deneme.countriesAsOption()
    dateAsOption=deneme.dateAsOption()
    if(countryName):
        table_hidden="visible"
        deneme.countryData(countryName)
        deneme.countryDailyData(countryName)
        table = deneme.countryTable(countryName)
        my_dict['table'] = table
        countryInfo = deneme.countryInformation(countryName)
        my_dict['countryInfo'] = countryInfo
        my_dict['image1'] = "first_app/images/" + str(countryName) + "Total.png"
        my_dict['image2'] = "first_app/images/" + str(countryName) + "Daily.png"
    my_dict['table_hidden'] = table_hidden


    if(dateData):
        pie_hidden="visible"
        deneme.pieChart(str(dateData))
        my_dict['pie'] = "first_app/images/pie(" + str(dateData) + ").png"

    my_dict['pie_hidden'] = pie_hidden
    my_dict['country_hidden']=country_hidden
    my_dict['world_hidden'] = world_hidden
    my_dict['countriesAsOption']=countriesAsOption
    my_dict['dateAsOption'] = dateAsOption
    return render(request,'first_app/index.html',context=my_dict)