from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from bos.models import BOS
from .forms import BOSForm

def index(request):
    return render(request, 'bos/index.html')

@login_required
def bos(request):
    """ Shows BOS's"""
    bos = BOS.objects.order_by('-date_added')
    context = {'bos':bos}
    return render(request, 'bos/bos.html', context)

def showbos(request, bos_id):
    """Shows the details for the specific BOS"""
    bos = BOS.objects.get(id=bos_id)
    area = BOS.objects.get(id=bos_id).Area
    topic = BOS.objects.get(id=bos_id).Topic
    comments = BOS.objects.get(id=bos_id).Comments
    date = BOS.objects.get(id=bos_id).date_added
    owner = BOS.objects.get(id=bos_id).owner
    context = {'bos_id':bos, 'area':area, 'topic':topic, 'comments':comments, 'date':date, 'owner':owner}
    return render(request, 'bos/showbos.html', context)

@login_required
def new_bos(request):
    """Submit a BOS"""
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = BOSForm()
    else:
        # POST data submitted; process the info
        form = BOSForm(data=request.POST)
        if form.is_valid():
            BOS = form.save(commit=False)
            BOS.owner = request.user
            BOS.save()    
            return redirect('bos:bos')
    
    # Display a blank or invalid form
    context = {'form':form}
    return render(request, 'bos/new_bos.html', context)