Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def hospital_access(request):
...     if request.method == "POST":
...         search = request.POST['search']
...         hospital = request.session['hospital']
... 
...         patients = Patient.objects.filter(problem_desc__icontains=search)
...         allowed = []
... 
...         for p in patients:
...             if hospital in p.access_data:
...                 p.revenue += 0.5
...                 p.save()
...                 allowed.append(p)
... 
...         return render(request, "ViewAccessData.html", {"data": allowed})
... 
