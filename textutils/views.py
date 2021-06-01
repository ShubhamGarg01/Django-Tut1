from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
    #return HttpResponse ("<h1>Home </h1>")
def analyze(request):
    ditext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','offc')
    upcase = request.POST.get('uppercase','offc')
    lowcase = request.POST.get('lowercase','offc') 
    #analyzed = ditext
    if removepunc == "on" or upcase=="on" or lowcase=="on":  
         if upcase == "on": 
             ditext = ditext.upper()
         if lowcase == "on":
             ditext = ditext.lower()  
         analyzed = ditext      
         if removepunc == "on" :   
            punctuations= '''!()-[]{};:'",<>./?@;'''
            analyzed= ""
            for char in ditext:
                if char not in punctuations:
                    analyzed= analyzed + char
         params= {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    
         return render(request,'analyze.html',params)
         
    else:
         return HttpResponse("No mode selected")     

