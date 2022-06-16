from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from estateapp.forms import createProperty
from estateapp.models import Property

def Homepage(request):

    Items = Property.objects.all()
    data = {"Props": Items }
    return render(request, 'index.html', data )


def HomeDescription(request, pk):

    House = Property.objects.filter(id = pk)[0]
    priceWithComma = '{:,}'.format(House.price) 

    data2 = { "Name" : House.name,
              "Price": priceWithComma  ,
              "Address" : House.address,
              "Rooms" : House.Rooms,
              "Picture" : House.imgg
            }
    return render(request, 'home.html' , data2 )


def createProp(request):
    if request.method == "POST":
        formContent = createProperty(request.POST, request.FILES)

        if formContent.is_valid():

            print (formContent.cleaned_data)
            formContent.save()

    data3 = {"form":createProperty}

    return render(request, 'createproperty.html' , data3 )


def DeleteProp(request, ind):
    
    ToDelete = Property.objects.filter(id = ind)[0]
    print(ToDelete, "deleted fam")
    ToDelete.delete()

    return HttpResponseRedirect('/' )


def UpdateProp(request, priKey):
    itemToUpdate = Property.objects.filter(id=priKey)[0]

# form with the selected model prefilled in it as an instance for editing/ updating
    formMan = createProperty(instance=itemToUpdate)

    if request.method == "POST":
        formContent = createProperty(request.POST, instance=itemToUpdate , files=request.FILES)

        if formContent.is_valid():

            print (formContent.cleaned_data)
            formContent.save()

    data4 = {"form":formMan}

    return render(request, 'updateproperty.html' , data4 )

