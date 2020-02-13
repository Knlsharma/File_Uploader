from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import csv
import openpyxl

from collections import OrderedDict 
od = OrderedDict()
# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        list1 = []
        reader = csv.DictReader(decode_utf8(request.FILES['document']))

        print(type(reader))

        # data = {row["title"]: row["value"] for row in csv.DictReader(file_data, ("title", "value"))}
        """
        for row in reader:
            list1 += row
            print(row) 
        
        """
        for dct in map(dict, reader):
            list1.append(dct.get('id')) 

            
        
        
      #  print([dict(d) for d in reader if d == "id"])
        
        

    
          
        
 

        """
        decoded_file = uploaded_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            print(row)

        """    
        print(uploaded_file.name , uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url1 = fs.url(name)
        context['url1'] = url1
        print(url1)
        print(list1)
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', context)



def decode_utf8(input_iterator):
    for l in input_iterator:
        yield l.decode('utf-8')


     
