# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

import os
import csv

from django.conf import settings
from django import forms

from .forms import initial_page
from .models import Document,Variable,Queryvar
from .parser_pdftabletocsv import pdftabletocsv

# Create your views here.

# takes in csv file and stores the entries in mysql monsoon database

def store_csv():
    #path of the csv file
    file_path = settings.BASE_DIR
    file_path=file_path+"/output.csv"

   #arrays needed for proper formatting as records are in different columns: i.e. one row has 2 records in this case
    years=[]
    years_index=[]
    variables=[]
    variables_index=[]
    
    with open(file_path,'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=str(u',')) 
        index=0
        for row in reader: 
            #get the indexes of years and Particulars
            if(index==0):
                print(row)
                for i in range(0,len(row)):
                    if(row[i].isdigit()):  # year is checked if its true for isdigit
                        years.append(row[i])
                        years_index.append(i)
                    elif (row[i]!=''):       # empty column header columns are not considered
                        variables.append(row[i])
                        variables_index.append(i)
                        
                index=1
            else:
                for i in range(0,len(variables)): # one variable at a time and its years are looped
                    for j in range(int(i*len(years)*0.5),int(i*len(years)*0.5)+int(len(years)*0.5)):
                        if( (row[int(variables_index[i])]!='' )& (row[int(years_index[j])]!='')):   
                            print(row[int(variables_index[i])],float(row[int(years_index[j])]))
                            p=Variable(var=row[int(variables_index[i])],year=int(years[j]),value=float(row[int(years_index[j])]))
                            p.save()  # saved into database
                    
                                    
    return
            
            
            
        
    
    


def index(request):
    if request.method == 'POST':  
        # Create a form instance and populate it with data from the request (binding):
        form = initial_page(request.POST,request.FILES)
        
        if form.is_valid():
            
            #query is loaded into here and saved into database. also file
            q1=Queryvar(var=form.cleaned_data['var'],year=int(form.cleaned_data['year']))
            q1.save()
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            
            #converts the pdf into csv file and stored in base_dir
            pdftabletocsv(newdoc.docfile.path)
            
            #stored as table in database
            #store_csv()
            
            
            return HttpResponseRedirect(reverse('result') )  # show the query result and also button to download csv
        
    else:
        form=initial_page()
        
    return render(request, 'parse_app/initial_page.html',{'form':form}) #displayes intial form for query



def result(request):
    form=forms.Form
    
    # extract query variable
    que = Queryvar.objects.all()
    
    #matched records are fetched here
    res=Variable.objects.filter(var__icontains=que[0].var,year=que[0].year)
    
    # delete the query variables
    
    
    
   
    if request.method == 'POST':
        que.delete() 
        return HttpResponseRedirect(reverse('final'))
                                   
        
    return render(request, 'parse_app/final_page.html',{'form':form,'Varlist':res,'Count':len(res)})



def final(request):
    file_path = settings.BASE_DIR
    file_path=file_path+"/output.csv"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename=CSV_output '
            return response
    raise Http404       
    
        
    