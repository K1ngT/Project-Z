from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Asset, Locations
from .forms import AssetForm, LocationsForm

# Create your views here.

def inventory(request):
    inventory = Asset.objects.all()
    context = {'assets':inventory}
    return render(request, 'inventory/inventory.html', context)

def serverInfo(request,pk):
    assetObj = Asset.objects.get(id=pk)
    locations = assetObj.locationsInfo.all()
    return render(request, 'inventory/asset.html', {'assetObj':assetObj, 'locations':locations})

# View and Render location information.

def location(request):
    locations = Locations.objects.all()
    context = {'locations':locations}
    return render(request, 'inventory/locations.html', context)


#Create and Update Asset Models 
 
def createAsset(request):
    form = AssetForm()
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    context = {'form': form}
    return render (request, 'inventory/asset_form.html', context)


def updateAsset(request, pk):
    asset= Asset.objects.get(id=pk)
    form = AssetForm(instance=asset)

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('inventory')

    context = {'form': form}
    return render (request, 'inventory/asset_form.html', context)



# Create and Update  Location Models
def createLocation(request):
    lforms= LocationsForm()
    if request.method == 'POST':
        lforms = LocationsForm(request.POST)
        if lforms.is_valid():
            lforms.save()
            return redirect('inventory')



    context = {'lforms': lforms}
    return render (request,'inventory/locations_form.html', context )



# Delete Assets

def deleteAsset(request,pk):
    asset = Asset.objects.get(id=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('inventory')

    context={'object':asset}
    return render (request, 'inventory/delete_template.html', context)