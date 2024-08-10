from django.shortcuts import render


# Create your views here.

def TestView(request):
    return render(request, 'index.html')

def accept_view(request):
    return render(request, 'accept.html')

def contacted_view(request):
    return render(request, 'contacted.html')

def extra_view(request):
    return render(request, 'extra.html')

def messages_view(request):
    return render(request, 'messages.html')

def received_view(request):
    return render(request, 'received.html')

def reject_view(request):
    return render(request, 'reject.html')

def sent_view(request):
    return render(request, 'sent.html')

def shortlist_view(request):
    return render(request, 'shortlist.html')

def shortlisted_view(request):
    return render(request, 'shortlisted.html')

def shortlistedby_view(request):
    return render(request, 'shortlistedby.html')

def viewedmyprofile_view(request):
    return render(request, 'viewedmyprofile.html')



